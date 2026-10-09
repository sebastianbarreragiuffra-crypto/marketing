"""Restricted, auto-refreshing preview for a temporary Cloudflare Tunnel."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from html import escape
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import json
import re

from auto_publish import worktrees
from site_state import (EXTRA_ROOT, PAGES, content_version, public_files,
                        public_status, status)


ROOT = Path(__file__).resolve().parent
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".avif"}
LIVE_SCRIPT = """(() => {
  let previous;
  async function check() {
    try {
      const response = await fetch('./__version', {cache: 'no-store'});
      if (!response.ok) return;
      const current = await response.text();
      if (previous !== undefined && current !== previous) location.reload();
      previous = current;
    } catch (_) { /* Tunnel may be temporarily unavailable. */ }
  }
  check();
  setInterval(check, 1500);
})();"""


STYLESHEET = re.compile(r'<link\s+rel="stylesheet"\s+href="(css/[^"?]+\.css)(?:\?[^\"]*)?"\s*>')


def inline_preview_styles(html: str, root: Path) -> str:
    """Avoid partial styles when a tunnel drops parallel stylesheet requests.

    This changes only the temporary preview response; source HTML keeps its
    normal stylesheet links for static hosting and CSS files stay editable.
    """
    def replace(match: re.Match[str]) -> str:
        relative = match.group(1)
        if not is_allowed('/' + relative, root):
            return match.group(0)
        source = (root / relative).resolve()
        if not source.is_relative_to(root) or not source.is_file():
            return match.group(0)
        css = source.read_text(encoding="utf-8")
        css = css.replace('../assets/', 'assets/')
        return f'<style data-preview-source="{escape(relative)}">\n{css}\n</style>'

    return STYLESHEET.sub(replace, html)


def is_allowed(path: str, root: Path) -> bool:
    if not path.startswith("/"):
        return False
    segments = path[1:].split("/")
    if any(segment in {"", ".", ".."} or segment.startswith(".") for segment in segments):
        return False
    relative = Path(*segments)
    if len(segments) == 1:
        return segments[0] in PAGES or segments[0] in EXTRA_ROOT
    return (root / relative).resolve() in public_files(root)


def active_root() -> Path:
    # A worktree edit or a state file from another PC must never switch this URL.
    # Alternate sources are selected only through the explicit /b/<branch>/ URL.
    return ROOT


def branch_roots() -> dict[str, Path]:
    roots: dict[str, Path] = {}
    for root, branch in worktrees().items():
        if branch != "detached":
            alias = "".join(char.lower() if char.isalnum() and char.isascii() else "-" for char in branch)
            if alias and alias not in roots:
                roots[alias] = root
    return roots


def latest_version(root: Path) -> str:
    return content_version(root)


class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        if getattr(self, "_image_etag", None):
            # Reuse image bytes while checking every request for local changes.
            self.send_header("Cache-Control", "public, max-age=0, must-revalidate")
            self.send_header("ETag", self._image_etag)
        else:
            self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()

    def respond(self, content: bytes, content_type: str, body: bool = True):
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        if body:
            self.wfile.write(content)

    def serve(self, body: bool):
        self._image_etag = None
        path = unquote(urlsplit(self.path).path)
        if path in {"/branches", "/branches/"}:
            branches = branch_roots()
            preferred = "main" if "main" in branches else next(iter(branches), None)
            if preferred is None:
                self.send_error(404)
                return
            self.send_response(302)
            self.send_header("Location", f"/b/{preferred}/")
            self.end_headers()
            return
        if path in {"/branch-list", "/branch-list/"}:
            entries = sorted(branch_roots().items())
            links = "".join(
                f'<li><a href="/b/{escape(alias)}/">{escape(alias)}</a></li>'
                for alias, _ in entries
            )
            page = (
                '<!doctype html><html lang="es"><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1">'
                '<title>Vistas en vivo de Órbita</title>'
                '<style>body{font:18px system-ui;max-width:720px;margin:4rem auto;padding:0 1rem}'
                'li{margin:.7rem 0}a{color:#246244}</style>'
                '<h1>Ramas en vivo</h1><p>Los cambios escritos en este computador '
                'aparecen al refrescar cada vista.</p><ul>' + links + '</ul></html>'
            )
            self.respond(page.encode("utf-8"), "text/html; charset=utf-8", body)
            return
        root = active_root()
        if path.startswith("/b/"):
            pieces = path.split("/", 3)
            alias = pieces[2]
            selected = branch_roots().get(alias)
            if selected is None:
                self.send_error(404)
                return
            if len(pieces) == 3:
                self.send_response(302)
                self.send_header("Location", path + "/")
                self.end_headers()
                return
            root = selected
            path = "/" + pieces[3]
        if path == "/__version":
            self.respond(latest_version(root).encode(), "text/plain; charset=utf-8", body)
            return
        if path == "/__site.json":
            self.respond(json.dumps(public_status(root), ensure_ascii=False).encode("utf-8"),
                         "application/json; charset=utf-8", body)
            return
        if path == "/__live.js":
            self.respond(LIVE_SCRIPT.encode(), "application/javascript; charset=utf-8", body)
            return
        if path == "/":
            path = "/index.html"
        elif path.lstrip("/") + ".html" in PAGES:
            path += ".html"
        if not is_allowed(path, root):
            self.send_error(404)
            return
        target = (root / path.lstrip("/")).resolve()
        if not target.is_relative_to(root) or not target.is_file():
            self.send_error(404)
            return
        if target.suffix.lower() in IMAGE_EXTENSIONS:
            stat = target.stat()
            self._image_etag = f'"{stat.st_mtime_ns:x}-{stat.st_size:x}"'
            requested_tags = self.headers.get("If-None-Match", "").split(",")
            if any(tag.strip() in {self._image_etag, "*"} for tag in requested_tags):
                self.send_response(304)
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-Type", self.guess_type(str(target)))
            self.send_header("Content-Length", str(stat.st_size))
            self.end_headers()
            if body:
                self.wfile.write(target.read_bytes())
            return
        if target.suffix == ".html":
            html = target.read_text(encoding="utf-8")
            html = inline_preview_styles(html, root)
            html = html.replace("</body>", '<script src="./__live.js"></script>\n</body>')
            self.respond(html.encode("utf-8"), "text/html; charset=utf-8", body)
            return
        self.path = path
        self.directory = str(root)
        if body:
            super().do_GET()
        else:
            super().do_HEAD()

    def do_GET(self):
        self.serve(True)

    def do_HEAD(self):
        self.serve(False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8766)
    args = parser.parse_args()
    current = status(ROOT)
    print(f"Site version: {current['version']}", flush=True)
    if not current['difference']['matches'] or current['missing'] or current['blocked']:
        print("VERSION NO VERIFICADA: ejecutar python site_state.py --check; "
              "no sustituir recursos desde copias antiguas.", flush=True)
    if current['active_uncommitted'] or current['active_untracked']:
        print("Hay cambios locales activos: F5 los muestra, pero un pull en otro PC no los recibe.", flush=True)
    server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(PreviewHandler, directory=str(ROOT)))
    print(f"Preview running at http://127.0.0.1:{args.port}", flush=True)
    server.serve_forever()
