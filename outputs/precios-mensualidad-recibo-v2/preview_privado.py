"""Vista local de la propuesta. Solo escucha en 127.0.0.1; no usa Cloudflare."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from live_preview import is_allowed

PREFIX = "/outputs/precios-mensualidad-recibo-v2/"
OWN_FILES = {"precios-propuesta.html", "mensualidad.html", "mensualidad-recibo-v2.css"}


class PrivatePreview(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        path = unquote(urlsplit(self.path).path)
        target = (ROOT / path.lstrip("/")).resolve()
        own = path.startswith(PREFIX) and path[len(PREFIX):] in OWN_FILES
        if not target.is_relative_to(ROOT) or not (own or is_allowed(path, ROOT)):
            self.send_error(404)
            return
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def list_directory(self, path):
        self.send_error(404)


if __name__ == "__main__":
    print("Propuesta privada: http://127.0.0.1:8771" + PREFIX + "precios-propuesta.html#mensualidad", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8771), PrivatePreview).serve_forever()
