"""Keep the single Cloudflare Pages preview on the most recently edited Git worktree.

Usage: python auto_publish.py --once | --watch | --dry-run
This intentionally publishes uncommitted changes. Only public site assets are staged.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote


REPO = Path(__file__).resolve().parent
DATA = REPO / ".preview-sync"
STAGE = DATA / "stage"
ACTIVE = DATA / "active_source.json"
LAST_DEPLOYED = DATA / "last_deployed.json"
PROJECT = "orbita-marketing"
PRODUCTION_URL = f"https://{PROJECT}.pages.dev"
PAGES = (
    "index.html",
    "marketing.html",
    "software.html",
    "automatizaciones.html",
    "precios.html",
    "iniciar-sesion.html",
)
EXTRA_ROOT = ("favicon.svg", "404.html", "robots.txt", "_headers", "_redirects")
MEDIA_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".avif", ".woff", ".woff2", ".ttf", ".mp4"}
ASSET_REFERENCE = re.compile(r"assets/[a-zA-Z0-9_./%+\-]+")
POLL_SECONDS = 1.5
DEBOUNCE_SECONDS = 4.0


def worktrees() -> dict[Path, str]:
    result = subprocess.run(
        ["git", "worktree", "list", "--porcelain"],
        cwd=REPO, capture_output=True, text=True, check=True,
    )
    found: dict[Path, str] = {}
    path: Path | None = None
    branch = "detached"
    for line in (*result.stdout.splitlines(), ""):
        if line.startswith("worktree "):
            path = Path(line[9:]).resolve()
            branch = "detached"
        elif line.startswith("branch refs/heads/"):
            branch = line[len("branch refs/heads/"):]
        elif not line and path is not None:
            if path.is_dir():
                found[path] = branch
            path = None
    return found


def public_files(root: Path) -> list[Path]:
    paths = {root / name for name in (*PAGES, *EXTRA_ROOT) if (root / name).is_file()}
    for folder_name, extension in (("css", ".css"), ("js", ".js")):
        folder = root / folder_name
        if folder.is_dir():
            paths.update(path for path in folder.iterdir() if path.is_file() and path.suffix == extension)

    # Keep the existing site imagery. Additional assets are included only when
    # they are referenced by an HTML, CSS, or JS file.
    hero = root / "assets" / "hero"
    if hero.is_dir():
        paths.update(path for path in hero.rglob("*") if path.is_file() and path.suffix.lower() in MEDIA_EXTENSIONS)
    for source in tuple(paths):
        if source.suffix not in {".html", ".css", ".js"}:
            continue
        try:
            content = source.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        for match in ASSET_REFERENCE.findall(content):
            candidate = (root / unquote(match)).resolve()
            if candidate.is_relative_to(root) and candidate.is_file() and candidate.suffix.lower() in MEDIA_EXTENSIONS:
                paths.add(candidate)
    return sorted(paths)


def fingerprint(root: Path, branch: str) -> str:
    digest = hashlib.sha256(branch.encode("utf-8"))
    for path in public_files(root):
        try:
            stat = path.stat()
        except FileNotFoundError:
            continue
        relative = path.relative_to(root).as_posix()
        digest.update(f"{relative}:{stat.st_size}:{stat.st_mtime_ns}\n".encode("utf-8"))
    return digest.hexdigest()


def atomic_json(path: Path, data: dict) -> None:
    DATA.mkdir(exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, path)


def source_label(root: Path, branch: str) -> str:
    return branch if branch != "detached" else f"detached-{root.name}"


def select_live_source(root: Path, branch: str) -> None:
    atomic_json(ACTIVE, {"root": str(root), "branch": source_label(root, branch)})
    print(f"Live tunnel now serves {source_label(root, branch)}", flush=True)


def prepare_stage(root: Path, branch: str, version: str) -> int:
    # STAGE is a fixed directory beneath DATA. Verify before any recursive delete.
    DATA.mkdir(exist_ok=True)
    resolved_stage = STAGE.resolve()
    if not resolved_stage.is_relative_to(DATA.resolve()) or resolved_stage == DATA.resolve():
        raise RuntimeError("Invalid deployment staging path")
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir()
    count = 0
    for source in public_files(root):
        relative = source.relative_to(root)
        destination = STAGE / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        count += 1
    missing = [name for name in PAGES if not (STAGE / name).is_file()]
    if missing:
        raise RuntimeError(f"Missing public pages: {', '.join(missing)}")
    marker = {
        "source_branch": source_label(root, branch),
        "version": version,
        "deployed_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    (STAGE / "__preview.json").write_text(json.dumps(marker, ensure_ascii=False), encoding="utf-8")
    return count


def verify_remote(version: str) -> bool:
    for attempt in range(10):
        try:
            request = urllib.request.Request(
                f"{PRODUCTION_URL}/__preview.json?check={time.time_ns()}",
                headers={"Cache-Control": "no-cache", "User-Agent": "OrbitaPreviewVerifier/1.0"},
            )
            with urllib.request.urlopen(request, timeout=10) as response:
                marker = json.load(response)
            if marker.get("version") == version:
                return True
        except (OSError, ValueError):
            pass
        time.sleep(min(attempt + 1, 4))
    return False


def deploy(root: Path, branch: str, version: str, dry_run: bool = False) -> bool:
    count = prepare_stage(root, branch, version)
    label = source_label(root, branch)
    print(f"Staged {count} public files from {label} ({version[:12]})", flush=True)
    if dry_run:
        return True
    npx = shutil.which("npx.cmd" if os.name == "nt" else "npx")
    if not npx:
        raise RuntimeError("npx is unavailable")
    command = [
        npx, "--yes", "wrangler", "pages", "deploy", str(STAGE),
        "--project-name", PROJECT, "--branch", "main",
        "--commit-message", f"Live preview: {label}", "--commit-dirty=true",
    ]
    result = subprocess.run(
        command, cwd=REPO, text=True, encoding="utf-8", errors="replace",
        capture_output=True, timeout=180,
    )
    print(result.stdout[-3000:].encode("ascii", "backslashreplace").decode("ascii"), flush=True)
    if result.returncode:
        print(result.stderr[-3000:].encode("ascii", "backslashreplace").decode("ascii"), file=sys.stderr, flush=True)
        return False
    if not verify_remote(version):
        print("Deployment finished, but the stable URL has not shown the new version yet.", file=sys.stderr, flush=True)
        return False
    atomic_json(LAST_DEPLOYED, {"root": str(root), "branch": label, "version": version})
    print(f"Verified {PRODUCTION_URL} at {version[:12]} from {label}", flush=True)
    return True


def last_deployment() -> dict:
    try:
        return json.loads(LAST_DEPLOYED.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def watch() -> None:
    known: dict[Path, tuple[str, str]] = {}
    pending: tuple[Path, str, str] | None = None
    last_change = 0.0
    retry_after = 0.0
    first_poll = True
    print(f"Watching all Git worktrees; one URL: {PRODUCTION_URL}", flush=True)
    while True:
        current = worktrees()
        for root, branch in current.items():
            version = fingerprint(root, branch)
            previous = known.get(root)
            known[root] = (branch, version)
            # New worktrees discovered after startup are also new editing sources.
            changed = not first_poll and (previous is None or previous != (branch, version))
            if changed:
                pending = (root, branch, version)
                last_change = time.monotonic()
                select_live_source(root, branch)
        for missing in set(known) - set(current):
            known.pop(missing)
            if pending and pending[0] == missing:
                pending = None
                fallback = next(iter(current), None)
                if fallback is not None:
                    select_live_source(fallback, current[fallback])
        if first_poll and known:
            deployed = last_deployment()
            deployed_root = Path(deployed.get("root", str(REPO))).resolve()
            source = deployed_root if deployed_root in known else REPO
            if source not in known:
                source = next(iter(known))
            branch, version = known[source]
            select_live_source(source, branch)
            if deployed.get("version") != version:
                pending = (source, branch, version)
                last_change = time.monotonic() - DEBOUNCE_SECONDS
            first_poll = False
        if pending and time.monotonic() >= max(last_change + DEBOUNCE_SECONDS, retry_after):
            root, branch, version = pending
            latest = fingerprint(root, branch) if root.is_dir() else ""
            if latest != version:
                pending = (root, branch, latest)
                last_change = time.monotonic()
            elif last_deployment().get("version") == version:
                pending = None
            else:
                try:
                    if deploy(root, branch, version):
                        pending = None
                        retry_after = 0.0
                    else:
                        retry_after = time.monotonic() + 20
                except (OSError, RuntimeError, subprocess.TimeoutExpired) as error:
                    print(f"Deploy failed: {error}", file=sys.stderr, flush=True)
                    retry_after = time.monotonic() + 20
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--once", action="store_true", help="Deploy current checkout once")
    mode.add_argument("--watch", action="store_true", help="Watch all worktrees and deploy latest edit")
    mode.add_argument("--dry-run", action="store_true", help="Stage current checkout without deploying")
    args = parser.parse_args()
    if args.watch:
        watch()
    else:
        branches = worktrees()
        branch = branches.get(REPO, "detached")
        version = fingerprint(REPO, branch)
        select_live_source(REPO, branch)
        if not deploy(REPO, branch, version, dry_run=args.dry_run):
            sys.exit(1)
