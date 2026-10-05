"""Restricted, auto-refreshing preview for a temporary Cloudflare Tunnel."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from html import escape
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import hashlib
import json

from auto_publish import MEDIA_EXTENSIONS, public_files, worktrees


ROOT = Path(__file__).resolve().parent
ACTIVE_SOURCE = ROOT / ".preview-sync" / "active_source.json"
PAGES = {
    "index.html",
    "marketing.html",
    "software.html",
    "automatizaciones.html",
    "precios.html",
    "iniciar-sesion.html",
}
MOCKUP_FILES = {
    "mockups/marketing-contact-v1-a.html",
    "mockups/marketing-contact-proposal.css",
    "mockups/marketing-contact-proposal.js",
}
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


def is_allowed(path: str, root: Path) -> bool:
    if not path.startswith("/"):
        return False
    segments = path[1:].split("/")
    if any(segment in {"", ".", ".."} or segment.startswith(".") for segment in segments):
        return False
    relative = Path(*segments)
    if relative.as_posix() in MOCKUP_FILES:
        return True
    if len(segments) == 1:
        return segments[0] in PAGES or segments[0] == "favicon.svg"
    if len(segments) == 2 and segments[0] == "css":
        return relative.suffix == ".css"
    if len(segments) == 2 and segments[0] == "js":
        return relative.suffix == ".js"
    if len(segments) >= 3 and segments[0] == "assets" and relative.suffix.lower() in MEDIA_EXTENSIONS:
        return (root / relative).resolve() in public_files(root)
    return False


def active_root() -> Path:
    try:
        selected = Path(json.loads(ACTIVE_SOURCE.read_text(encoding="utf-8"))["root"]).resolve()
        if selected.is_dir():
            return selected
    except (OSError, ValueError, KeyError, TypeError):
        pass
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
    paths = public_files(root)
    paths.extend(root / name for name in MOCKUP_FILES)
    # A fingerprint also notices removals and changes to less recent files.
    version = hashlib.sha256(str(root).encode("utf-8"))
    for path in sorted(paths):
        try:
            stat = path.stat()
        except FileNotFoundError:
            continue
        version.update(f"{path.relative_to(root).as_posix()}:{stat.st_mtime_ns}:{stat.st_size}\n".encode())
    return version.hexdigest()


class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
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
        path = unquote(urlsplit(self.path).path)
        if path in {"/branches", "/branches/"}:
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
        if target.suffix == ".html":
            html = target.read_text(encoding="utf-8")
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
    server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(PreviewHandler, directory=str(ROOT)))
    print(f"Preview running at http://127.0.0.1:{args.port}", flush=True)
    server.serve_forever()
