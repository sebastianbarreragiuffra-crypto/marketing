"""Integration checks for the served source and the portable deployment inventory."""

import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import urlopen
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import auto_publish
import live_preview
import site_state


class LiveSourceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'current'
        self.root.mkdir()
        for page in site_state.PAGES:
            self.put(page, '<!doctype html><title>Actual</title><body>Actual</body>')
        self.put('index.html', '<link rel="stylesheet" href="css/current.css">'
                 '<script src="js/current.js"></script><body><img src="assets/hero/current.webp">Actual</body>')
        self.put('css/current.css', 'body{color:#0b0d0b}')
        self.put('js/current.js', 'console.log("current")')
        self.put('assets/hero/current.webp', 'illustrative image bytes')
        self.put('css/old.css', 'body{color:red}')
        self.put('archive/old.html', '<body>Anterior</body>')
        self.put('mockups/marketing-contact-v1-a.html', '<body>Propuesta</body>')
        self.put('.preview-sync/active_source.json', json.dumps({'root': str(self.root / 'archive')}))
        site_state.write_manifest(self.root)

    def put(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def server(self):
        root_patch = patch.object(live_preview, 'ROOT', self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        server = live_preview.ThreadingHTTPServer(('127.0.0.1', 0), live_preview.PreviewHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        return f'http://127.0.0.1:{server.server_port}'

    def test_root_is_fixed_and_archival_resources_are_not_served(self):
        base = self.server()
        self.assertEqual(self.root, live_preview.active_root())
        with urlopen(base + '/') as response:
            text = response.read().decode()
            self.assertIn('data-preview-source="css/current.css"', text)
            self.assertIn('Actual', text)
            self.assertIn('no-store', response.headers['Cache-Control'])
        for path in ('/css/old.css', '/archive/old.html', '/mockups/marketing-contact-v1-a.html', '/outputs/old.html'):
            with self.subTest(path=path), self.assertRaises(HTTPError) as error:
                urlopen(base + path)
            self.assertEqual(404, error.exception.code)
            error.exception.close()

    def test_source_changes_have_a_content_identity_and_no_cached_html(self):
        base = self.server()
        before = urlopen(base + '/__version').read().decode()
        self.put('precios.html', '<body>Cierre nuevo</body>')
        after = urlopen(base + '/__version').read().decode()
        self.assertNotEqual(before, after)
        with urlopen(base + '/precios.html') as response:
            self.assertIn('Cierre nuevo', response.read().decode())
            self.assertIn('no-store', response.headers['Cache-Control'])
        metadata = json.load(urlopen(base + '/__site.json'))
        self.assertFalse(metadata['manifest_matches'])
        self.assertEqual(after, metadata['version'])
        self.assertNotIn(str(self.root), json.dumps(metadata))
        self.assertNotIn('files', metadata)

    def test_another_worktree_requires_an_explicit_branch_path(self):
        other = Path(self.temporary.name) / 'other'
        other.mkdir()
        for page in site_state.PAGES:
            (other / page).write_text('<body>Otra rama</body>', encoding='utf-8')
        base = self.server()
        with patch.object(live_preview, 'branch_roots', return_value={'other': other}):
            self.assertIn(b'Actual', urlopen(base + '/').read())
            self.assertIn(b'Otra rama', urlopen(base + '/b/other/').read())
            self.assertIn(b'Actual', urlopen(base + '/').read())

    def test_staging_uses_only_current_files_and_preserves_a_previous_stage_on_missing_assets(self):
        data = Path(self.temporary.name) / 'staging-state'
        stage = data / 'stage'
        version = auto_publish.fingerprint(self.root, 'main')
        with patch.object(auto_publish, 'DATA', data), patch.object(auto_publish, 'STAGE', stage):
            auto_publish.prepare_stage(self.root, 'main', version)
            self.assertTrue((stage / 'css/current.css').exists())
            self.assertFalse((stage / 'css/old.css').exists())
            self.assertFalse((stage / 'archive').exists())
            self.assertFalse((stage / 'mockups').exists())
            marker = (stage / '__preview.json').read_bytes()
            (self.root / 'assets/hero/current.webp').unlink()
            with self.assertRaises(site_state.SiteStateError):
                auto_publish.prepare_stage(self.root, 'main', version)
            self.assertEqual(marker, (stage / '__preview.json').read_bytes())


if __name__ == '__main__':
    unittest.main()
