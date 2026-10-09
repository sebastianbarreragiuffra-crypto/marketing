"""Inventory and content identity of the current root pages, without Git writes.

Public API for the preview server:
    public_files(root, strict=False) -> sorted list[Path]
    content_version(root) -> SHA256 str (independent of machine path and mtime)
    file_digest(path) -> SHA256 of normalized UTF-8 runtime text or intact bytes
    load_manifest(root) -> manifest dict | None
    status(root) -> local diagnostic dict (includes relative Git file names)
    preview_metadata(root) -> compact public dict (no machine/file paths or PII)
    public_status(root) -> version, Git branch/HEAD and active-change counts

Only dependencies reachable from PAGES and existing EXTRA_ROOT files count.
Static HTML URLs, CSS imports/URLs and literal assets/... references in scripts
are supported. Constructed JavaScript URLs require an explicit literal reference.
Identity describes normalized content, not byte-for-byte equality: UTF-8 BOM and
LF/CRLF/CR differences in runtime text are ignored to survive Git autocrlf across
PCs. Media binaries retain their exact bytes; actual text edits change identity.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import posixpath
import re
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent
MANIFEST_NAME = "site-manifest.json"
SCHEMA = 1
PAGES = (
    "index.html", "marketing.html", "software.html", "automatizaciones.html",
    "precios.html", "iniciar-sesion.html", "hablemos.html",
)
EXTRA_ROOT = ("favicon.svg", "404.html", "robots.txt", "_headers", "_redirects")
TEXT_EXTENSIONS = {".html", ".css", ".js", ".svg", ".txt"}
TEXT_ROOT_FILES = {"_headers", "_redirects"}
MEDIA_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".avif",
    ".woff", ".woff2", ".ttf", ".otf", ".mp4", ".webm", ".ico",
}
PRIVATE_DIRECTORIES = {"outputs", "mockups", "dist", "node_modules", "tests", "__pycache__"}
CSS_URL = re.compile(r"url\(\s*(?:\"([^\"]*)\"|'([^']*)'|([^)]*))\s*\)", re.I)
CSS_IMPORT = re.compile(r"@import\s+(?:\"([^\"]*)\"|'([^']*)')", re.I)
CSS_COMMENT = re.compile(r"/\*.*?\*/", re.S)
JS_ASSET = re.compile(r"(?P<quote>['\"`])(?P<url>(?:\.?\.?/|/)?assets/[^'\"`\r\n]*)(?P=quote)")
INLINE_SCRIPT = re.compile(r"<script\b[^>]*>(.*?)</script\s*>", re.I | re.S)


class SiteStateError(ValueError):
    """A current page references an unavailable or nonpublic resource."""


@dataclass(frozen=True)
class Inventory:
    files: tuple[Path, ...]
    missing: tuple[str, ...]
    blocked: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.missing and not self.blocked


def _srcset_urls(value: str):
    # Preserve commas inside a data URL and percent-encoded spaces in file names.
    cursor = 0
    while cursor < len(value):
        while cursor < len(value) and (value[cursor].isspace() or value[cursor] == ","):
            cursor += 1
        start = cursor
        while cursor < len(value) and not value[cursor].isspace():
            cursor += 1
        url = value[start:cursor]
        if not url:
            break
        if url.endswith(","):
            yield url.rstrip(",")
            continue
        yield url
        depth = 0
        while cursor < len(value):
            char = value[cursor]
            cursor += 1
            if char == "(":
                depth += 1
            elif char == ")":
                depth = max(0, depth - 1)
            elif char == "," and depth == 0:
                break


class _HTMLReferences(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.urls: list[str] = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if not value:
                continue
            if name in {"href", "src", "poster"}:
                self.urls.append(value)
            elif name in {"srcset", "imagesrcset"}:
                self.urls.extend(_srcset_urls(value))

    handle_startendtag = handle_starttag


def _css_references(text: str):
    text = CSS_COMMENT.sub("", text)
    for pattern in (CSS_URL, CSS_IMPORT):
        for match in pattern.finditer(text):
            value = next(group for group in match.groups() if group is not None)
            # CSS escapes for spaces are common in hand-authored file names.
            yield value.replace("\\ ", " ").strip()


def _references(source: Path):
    if source.suffix.lower() not in {".html", ".css", ".js", ".svg"}:
        return
    text = source.read_text(encoding="utf-8-sig")
    if source.suffix.lower() in {".html", ".svg"}:
        parser = _HTMLReferences()
        parser.feed(text)
        yield from parser.urls
    if source.suffix.lower() in {".css", ".html", ".svg"}:
        yield from _css_references(text)
    if source.suffix.lower() in {".js", ".html"}:
        scripts = [text] if source.suffix.lower() == ".js" else INLINE_SCRIPT.findall(text)
        for script in scripts:
            for match in JS_ASSET.finditer(script):
                value = match.group("url")
                if "${" not in value:
                    # Browser-created assets/... paths resolve against the root page.
                    yield "/" + value.removeprefix("./").removeprefix("/")


def _resolve_reference(reference: str, source: str) -> tuple[str | None, bool]:
    reference = reference.strip()
    if not reference or reference.startswith("#"):
        return None, False
    try:
        parsed = urlsplit(reference)
    except ValueError:
        return reference, True
    if parsed.scheme or parsed.netloc:
        return None, False
    path = unquote(parsed.path)
    if not path:
        return None, False
    if "\\" in path or "\x00" in path:
        return path, True
    relative = posixpath.normpath(path.lstrip("/") if path.startswith("/")
                                 else posixpath.join(posixpath.dirname(source), path))
    if relative in {".", ""}:
        relative = "index.html"
    segments = relative.split("/")
    if any(segment.startswith(".") or segment in PRIVATE_DIRECTORIES for segment in segments):
        return relative, True
    suffix = Path(relative).suffix.lower()
    allowed = (
        relative in PAGES or relative in EXTRA_ROOT
        or (segments[0] == "css" and suffix == ".css")
        or (segments[0] == "js" and suffix == ".js")
        or (segments[0] == "assets" and suffix in MEDIA_EXTENSIONS)
    )
    return relative, not allowed


def scan_site(root: Path | str) -> Inventory:
    """Return reachable files plus relative missing/blocked diagnostics.

    Missing root pages are errors; EXTRA_ROOT files are optional unless linked.
    Hidden and archival directories never enter the public dependency closure.
    """
    root = Path(root).resolve()
    pending = list(PAGES) + [name for name in EXTRA_ROOT if (root / name).is_file()]
    visited: set[str] = set()
    paths: dict[str, Path] = {}
    missing: set[str] = set()
    blocked: set[str] = set()
    while pending:
        relative = pending.pop()
        if relative in visited:
            continue
        visited.add(relative)
        path = root / relative
        resolved = path.resolve()
        if not resolved.is_relative_to(root):
            blocked.add(relative)
            continue
        if any(part.startswith(".") or part in PRIVATE_DIRECTORIES
               for part in resolved.relative_to(root).parts):
            blocked.add(relative)
            continue
        if not path.is_file():
            missing.add(relative)
            continue
        paths[relative] = path
        try:
            references = list(_references(path))
        except (OSError, UnicodeError) as error:
            raise SiteStateError(f"No se pudo leer el recurso activo: {relative}") from error
        for reference in references:
            dependency, forbidden = _resolve_reference(reference, relative)
            if dependency is None:
                continue
            if forbidden:
                blocked.add(f"{relative} -> {dependency}")
            else:
                pending.append(dependency)
    return Inventory(tuple(paths[name] for name in sorted(paths)), tuple(sorted(missing)), tuple(sorted(blocked)))


def public_files(root: Path | str, strict: bool = False) -> list[Path]:
    inventory = scan_site(root)
    if strict and not inventory.valid:
        details = [*inventory.missing, *inventory.blocked]
        raise SiteStateError("Recursos activos faltantes o no públicos: " + "; ".join(details))
    return list(inventory.files)


def file_digest(path: Path | str) -> str:
    """Hash normalized runtime text, but preserve every byte of binary assets.

    Normalization removes only an initial UTF-8 BOM and unifies line endings;
    whitespace, wording, CSS/JS code, SVG data and all other content stay intact.
    """
    path = Path(path)
    content = path.read_bytes()
    if path.suffix.lower() in TEXT_EXTENSIONS or path.name in TEXT_ROOT_FILES:
        try:
            text = content.decode("utf-8-sig")
        except UnicodeError as error:
            raise SiteStateError(f"El recurso de texto activo no es UTF-8: {path.name}") from error
        content = text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    return hashlib.sha256(content).hexdigest()


def _state(root: Path | str) -> tuple[dict, Inventory]:
    root = Path(root).resolve()
    inventory = scan_site(root)
    files = {path.relative_to(root).as_posix(): file_digest(path)
             for path in inventory.files}
    payload = {"schema": SCHEMA, "files": files}
    # An invalid live preview has its own identity and cannot match a valid manifest.
    if not inventory.valid:
        payload["missing"] = inventory.missing
        payload["blocked"] = inventory.blocked
    version = hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False,
                                        separators=(",", ":")).encode("utf-8")).hexdigest()
    return {"schema": SCHEMA, "version": version, "files": files}, inventory


def content_version(root: Path | str) -> str:
    return _state(root)[0]["version"]


def load_manifest(root: Path | str) -> dict | None:
    path = Path(root) / MANIFEST_NAME
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise SiteStateError("site-manifest.json no es un manifiesto válido") from error
    if (not isinstance(data, dict) or set(data) != {"schema", "version", "files"}
            or data["schema"] != SCHEMA or not isinstance(data["files"], dict)
            or not isinstance(data["version"], str) or not re.fullmatch(r"[0-9a-f]{64}", data["version"])):
        raise SiteStateError("Esquema de site-manifest.json no válido")
    for name, digest in data["files"].items():
        resolved, forbidden = _resolve_reference(name, "index.html")
        if forbidden or resolved != name or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise SiteStateError("Ruta o hash no válido en site-manifest.json")
    payload = {"schema": SCHEMA, "files": data["files"]}
    expected = hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False,
                                         separators=(",", ":")).encode("utf-8")).hexdigest()
    if data["version"] != expected:
        raise SiteStateError("La versión del manifiesto no corresponde a sus hashes")
    return data


def manifest_difference(current: dict, manifest: dict | None) -> dict:
    if manifest is None:
        return {"added": [], "removed": [], "changed": [], "matches": False}
    old, new = manifest["files"], current["files"]
    return {
        "added": sorted(new.keys() - old.keys()),
        "removed": sorted(old.keys() - new.keys()),
        "changed": sorted(name for name in old.keys() & new.keys() if old[name] != new[name]),
        "matches": current["version"] == manifest["version"],
    }


def _git(root: Path, *arguments: str) -> str | None:
    try:
        result = subprocess.run(["git", "-C", str(root), *arguments], capture_output=True,
                                encoding="utf-8", errors="replace", check=False)
    except OSError:
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def status(root: Path | str) -> dict:
    """Local state, including branch/HEAD and changes restricted to active files."""
    root = Path(root).resolve()
    current, inventory = _state(root)
    manifest_error = None
    try:
        manifest = load_manifest(root)
    except SiteStateError as error:
        manifest, manifest_error = None, str(error)
    active = set(current["files"]) | set(inventory.missing)
    changed = _git(root, "diff", "HEAD", "--name-only", "-z", "--relative")
    untracked = _git(root, "ls-files", "--others", "--exclude-standard", "-z")
    return {
        "version": current["version"], "files": current["files"],
        "missing": list(inventory.missing), "blocked": list(inventory.blocked),
        "manifest_version": manifest["version"] if manifest else None,
        "manifest_error": manifest_error,
        "difference": manifest_difference(current, manifest),
        "branch": _git(root, "branch", "--show-current"),
        "head": _git(root, "rev-parse", "HEAD"),
        "active_uncommitted": sorted(active.intersection(changed.split("\0"))) if changed is not None else None,
        "active_untracked": sorted(active.intersection(untracked.split("\0"))) if untracked is not None else None,
    }


def preview_metadata(root: Path | str) -> dict:
    """Public health/version only; intentionally omit Git names, paths and PII."""
    current, inventory = _state(root)
    try:
        manifest = load_manifest(root)
        manifest_valid = manifest is not None
    except SiteStateError:
        manifest, manifest_valid = None, False
    return {
        "schema": SCHEMA, "version": current["version"], "file_count": len(current["files"]),
        "manifest_version": manifest["version"] if manifest else None,
        "manifest_matches": bool(manifest and current["version"] == manifest["version"]),
        "manifest_valid": manifest_valid, "missing_count": len(inventory.missing),
        "blocked_count": len(inventory.blocked), "resources_complete": inventory.valid,
    }


def public_status(root: Path | str) -> dict:
    """Compact handoff diagnostics; Git identity and counts, never file lists."""
    data = status(root)
    return {
        "schema": SCHEMA, "version": data["version"], "file_count": len(data["files"]),
        "manifest_version": data["manifest_version"],
        "manifest_matches": data["difference"]["matches"],
        "manifest_valid": data["manifest_version"] is not None and data["manifest_error"] is None,
        "branch": data["branch"], "head": data["head"],
        "dirty_active": len(data["active_uncommitted"]) if data["active_uncommitted"] is not None else None,
        "untracked_active": len(data["active_untracked"]) if data["active_untracked"] is not None else None,
        "missing_count": len(data["missing"]), "blocked_count": len(data["blocked"]),
        "resources_complete": not data["missing"] and not data["blocked"],
    }


def write_manifest(root: Path | str) -> dict:
    root = Path(root).resolve()
    current, inventory = _state(root)
    if not inventory.valid:
        raise SiteStateError("No se guarda una versión incompleta: " + "; ".join([*inventory.missing, *inventory.blocked]))
    path = root / MANIFEST_NAME
    temporary = path.with_name(MANIFEST_NAME + ".tmp")
    temporary.write_text(json.dumps(current, sort_keys=True, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)
    return current


def _print_status(data: dict):
    print("Versión activa:", data["version"])
    print("Rama:", data["branch"] or "NO VERIFICADA / detached")
    print("HEAD:", data["head"] or "NO VERIFICADO")
    print("Recursos activos:", len(data["files"]))
    print("Manifiesto:", "COINCIDE" if data["difference"]["matches"] else "PENDIENTE / DIFERENTE")
    for label, field in (("Faltantes", "missing"), ("Referencias no públicas", "blocked"),
                         ("Cambios activos sin commit", "active_uncommitted"),
                         ("Recursos activos sin seguimiento Git", "active_untracked")):
        values = data[field]
        print(f"{label}: " + (", ".join(values) if values else "ninguno" if values is not None else "NO VERIFICADO"))
    if data["manifest_error"]:
        print(data["manifest_error"])
    for label, field in (("Agregados", "added"), ("Retirados", "removed"), ("Modificados", "changed")):
        if data["difference"][field]:
            print(f"{label} respecto del manifiesto: " + ", ".join(data["difference"][field]))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Comprueba la versión de las páginas vigentes sin modificar Git.")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--write", action="store_true", help="Guardar la versión actual en site-manifest.json.")
    modes.add_argument("--check", action="store_true", help="Comprobar que la carpeta coincide con el manifiesto.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Raíz de la carpeta del sitio.")
    args = parser.parse_args(argv)
    try:
        if args.write:
            written = write_manifest(args.root)
            print("Manifiesto guardado:", written["version"])
        data = status(args.root)
        _print_status(data)
    except (SiteStateError, OSError) as error:
        print("BLOQUEADO:", error)
        return 2
    valid = not data["missing"] and not data["blocked"] and not data["manifest_error"]
    return 0 if valid and (not args.check or data["difference"]["matches"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
