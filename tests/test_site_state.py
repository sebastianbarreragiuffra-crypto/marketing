"""Focused regression checks for cross-PC current-site identity."""

import importlib.util
import contextlib
import io
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location("site_state", Path(__file__).resolve().parents[1] / "site_state.py")
state = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = state
SPEC.loader.exec_module(state)


class SiteStateTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "pc2"
        self.root.mkdir()
        for name in state.PAGES:
            self.put(name, "<!doctype html><title>Órbita</title>")
        self.put("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg"/>')

    def put(self, name, content="image bytes"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def relative_files(self):
        return {path.relative_to(self.root).as_posix() for path in state.public_files(self.root)}

    def test_identity_survives_other_pc_root_and_modified_times(self):
        self.put("index.html", '<link href="css/current.css"><img src="assets/hero/current.webp">')
        self.put("css/current.css", "body { color: #0b0d0b; }")
        self.put("assets/hero/current.webp")
        other = self.root.parent / "different-pc-folder"
        shutil.copytree(self.root, other)
        for path in other.rglob("*"):
            if path.is_file():
                os.utime(path, (12345, 12345))
        self.assertEqual(state.content_version(self.root), state.content_version(other))
        self.assertEqual(state.write_manifest(self.root), state.write_manifest(other))
        manifest_text = (self.root / state.MANIFEST_NAME).read_text(encoding="utf-8")
        self.assertNotIn(str(self.root), manifest_text)
        self.assertNotIn("mtime", manifest_text)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(0, state.main(["--root", str(self.root), "--check"]))

    def test_modification_and_removal_produce_diagnostics(self):
        self.put("index.html", '<img src="assets/hero/current.webp">')
        image = self.put("assets/hero/current.webp", "first image")
        original = state.write_manifest(self.root)
        image.write_text("updated image", encoding="utf-8")
        status = state.status(self.root)
        self.assertNotEqual(original["version"], status["version"])
        self.assertEqual(["assets/hero/current.webp"], status["difference"]["changed"])
        image.unlink()
        status = state.status(self.root)
        self.assertEqual(["assets/hero/current.webp"], status["missing"])
        self.assertEqual(["assets/hero/current.webp"], status["difference"]["removed"])
        self.assertFalse(state.preview_metadata(self.root)["resources_complete"])
        with self.assertRaises(state.SiteStateError):
            state.write_manifest(self.root)
        self.assertEqual(original, state.load_manifest(self.root))

    def test_identity_normalizes_runtime_bom_and_line_endings_only(self):
        self.put("index.html", '<!doctype html>\n<link href="css/current.css">\n<script src="js/current.js"></script>\n'
                                '<img src="assets/hero/current.webp">\n')
        self.put("css/current.css", "body {\n  color: black;\n}\n")
        self.put("js/current.js", "const current = true;\nconsole.log(current);\n")
        self.put("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg">\n</svg>\n')
        self.put("robots.txt", "User-agent: *\nDisallow: /private\n")
        self.put("_headers", "/*\n  Cache-Control: no-cache\n")
        self.put("_redirects", "/old / 302\n")
        image = self.put("assets/hero/current.webp")
        binary_bytes = b"\xef\xbb\xbfmedia\r\nintact\rbytes\n"
        image.write_bytes(binary_bytes)
        other = self.root.parent / "pc1-crlf"
        shutil.copytree(self.root, other)
        for path in other.rglob("*"):
            if path.is_file() and (path.suffix.lower() in state.TEXT_EXTENSIONS or path.name in state.TEXT_ROOT_FILES):
                text = path.read_bytes().decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
                line_ending = "\r" if path.suffix == ".js" else "\r\n"
                path.write_bytes(b"\xef\xbb\xbf" + text.replace("\n", line_ending).encode("utf-8"))
        self.assertEqual(state.content_version(self.root), state.content_version(other))
        self.assertEqual(state.write_manifest(self.root), state.write_manifest(other))
        self.assertEqual(hashlib.sha256(binary_bytes).hexdigest(), state.file_digest(image))
        self.assertEqual(binary_bytes, (other / "assets/hero/current.webp").read_bytes())
        version = state.content_version(other)
        (other / "css/current.css").write_text("body { color: blue; }\n", encoding="utf-8")
        self.assertNotEqual(version, state.content_version(other))
        version = state.content_version(self.root)
        image.write_bytes(binary_bytes.replace(b"\r\n", b"\n"))
        self.assertNotEqual(version, state.content_version(self.root))

    def test_unreachable_old_styles_scripts_and_hero_are_excluded(self):
        self.put("index.html", '<link href="css/current.css"><script src="js/current.js"></script>')
        self.put("css/current.css", "body { color: black }")
        self.put("js/current.js", "console.log('current')")
        self.put("css/old.css", "body { color: red }")
        self.put("js/old.js", "const url='assets/hero/old.webp'")
        old = self.put("assets/hero/old.webp")
        before = state.content_version(self.root)
        old.write_text("other unused image", encoding="utf-8")
        self.assertEqual(before, state.content_version(self.root))
        self.assertNotIn("css/old.css", self.relative_files())
        self.assertNotIn("js/old.js", self.relative_files())
        self.assertNotIn("assets/hero/old.webp", self.relative_files())

    def test_dependency_closure_srcset_css_and_js_literal_assets(self):
        self.put("index.html", '''<link href="css/current.css?v=4"><script src="js/current.js"></script>
<picture><source srcset="assets/hero/image%20small.webp 1x, assets/hero/image-large.webp 2x">
<img src="assets/hero/image%20small.webp" srcset="data:image/svg+xml,%3Csvg%3E 1x, assets/hero/image-large.webp 2x"></picture>
<a href="hablemos.html#contacto">Contactar</a><a href="https://example.com/privacy">Externo</a>
<a href="mailto:info@example.com">Email</a><use href="#logo"/><img src="//example.com/external.webp">''')
        self.put("css/current.css", '@import "nested/part.css"; .pic {background:url("../assets/hero/one+two.webp?v=2")}')
        self.put("css/nested/part.css", '@font-face {src:url("../../assets/fonts/current.woff2")}')
        self.put("js/current.js", "const photo = 'assets/hero/script.webp?v=2';")
        for name in ("assets/hero/image small.webp", "assets/hero/image-large.webp", "assets/hero/one+two.webp",
                     "assets/fonts/current.woff2", "assets/hero/script.webp"):
            self.put(name)
        inventory = state.scan_site(self.root)
        self.assertEqual((), inventory.missing)
        self.assertEqual((), inventory.blocked)
        actual = self.relative_files()
        for name in ("css/nested/part.css", "assets/fonts/current.woff2", "assets/hero/image small.webp",
                     "assets/hero/image-large.webp", "assets/hero/one+two.webp", "assets/hero/script.webp"):
            self.assertIn(name, actual)

    def test_private_paths_are_excluded_even_when_linked(self):
        self.put("index.html", '<script src=".preview-sync/service.js"></script><img src="outputs/old.png">'
                                '<link href="mockups/proposal.css"><img src="assets/.private/image.webp">'
                                '<img src="assets/hero/../../.env"><img src="dist/image.webp">')
        for name in (".preview-sync/service.js", "outputs/old.png", "mockups/proposal.css",
                     "assets/.private/image.webp", ".env", "dist/image.webp"):
            self.put(name)
        inventory = state.scan_site(self.root)
        self.assertEqual(6, len(inventory.blocked))
        self.assertEqual(set(state.PAGES) | {"favicon.svg"}, self.relative_files())
        with self.assertRaises(state.SiteStateError):
            state.public_files(self.root, strict=True)
        metadata = state.preview_metadata(self.root)
        self.assertNotIn("files", metadata)
        self.assertNotIn("branch", metadata)
        self.assertNotIn("root", metadata)
        self.assertNotIn(str(self.root), json.dumps(metadata))
        public = state.public_status(self.root)
        self.assertNotIn("files", public)
        self.assertNotIn("active_untracked", public)
        self.assertNotIn(str(self.root), json.dumps(public))

    def test_extras_are_retained_but_not_operational_files(self):
        self.put("robots.txt", "User-agent: *")
        self.put("_headers", "/*\n  Cache-Control: no-cache")
        self.put("README.md", "private documentation")
        self.put("live_preview.py", "private operational code")
        self.assertIn("robots.txt", self.relative_files())
        self.assertIn("_headers", self.relative_files())
        self.assertNotIn("README.md", self.relative_files())
        self.assertNotIn("live_preview.py", self.relative_files())

    def test_tampered_manifest_is_rejected(self):
        manifest = state.write_manifest(self.root)
        manifest["files"]["index.html"] = "0" * 64
        (self.root / state.MANIFEST_NAME).write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaises(state.SiteStateError):
            state.load_manifest(self.root)

    def test_asset_symlink_cannot_publish_a_private_target(self):
        self.put("index.html", '<img src="assets/hero/link.webp">')
        private = self.put(".preview-sync/private.webp", "not public")
        link = self.root / "assets/hero/link.webp"
        link.parent.mkdir(parents=True)
        try:
            link.symlink_to(private)
        except (OSError, NotImplementedError):
            self.skipTest("This host does not permit temporary symbolic links")
        inventory = state.scan_site(self.root)
        self.assertEqual(("assets/hero/link.webp",), inventory.blocked)
        self.assertNotIn("assets/hero/link.webp", self.relative_files())


if __name__ == "__main__":
    unittest.main()
