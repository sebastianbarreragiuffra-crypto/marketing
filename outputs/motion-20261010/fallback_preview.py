"""Local-only public-asset fixtures; never a source or deployment directory."""
import json
import re
import shutil
import time
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

root = Path(__file__).resolve().parents[2]
fixture = Path(__file__).resolve().parent / 'fallback-fixture'
fixture.mkdir(exist_ok=True)
manifest = json.loads((root / 'site-manifest.json').read_text(encoding='utf-8'))
for filename in manifest['files']:
    target = fixture / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / filename, target)
for page in ['index', 'marketing', 'software', 'precios', 'hablemos', 'iniciar-sesion']:
    html = (root / f'{page}.html').read_text(encoding='utf-8')
    no_js = re.sub(r'<script\b[^>]*>.*?</script>', '', html, flags=re.S | re.I)
    (fixture / f'nojs-{page}.html').write_text(no_js, encoding='utf-8')
    delayed = html.replace('js/experience-motion.js?v=20261010-m1', 'js/experience-motion.js?v=20261010-m1&qa-delay=1')
    (fixture / f'delayed-{page}.html').write_text(delayed, encoding='utf-8')

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlsplit(self.path).query)
        if query.get('qa-delay') == ['1']:
            time.sleep(3)
        super().do_GET()

print('Local fallback fixtures: http://127.0.0.1:8873', flush=True)
ThreadingHTTPServer(('127.0.0.1', 8873), partial(Handler, directory=str(fixture))).serve_forever()
