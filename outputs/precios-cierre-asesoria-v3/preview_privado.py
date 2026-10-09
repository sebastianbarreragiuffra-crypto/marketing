"""Vista local de Precios v3, sin publicación y sin modificar la vista v2."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from live_preview import is_allowed

PREFIX = "/outputs/precios-cierre-asesoria-v3/"
OWN_PATHS = {
    PREFIX + "precios-propuesta.html",
    PREFIX + "cierre-asesoria-v3.css",
    PREFIX + "cierre.html",
    "/outputs/precios-mensualidad-recibo-v2/mensualidad-recibo-v2.css",
}


class PrivatePreview(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        path = unquote(urlsplit(self.path).path)
        target = (ROOT / path.lstrip("/")).resolve()
        if not target.is_relative_to(ROOT) or not (path in OWN_PATHS or is_allowed(path, ROOT)):
            self.send_error(404)
            return
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def list_directory(self, path):
        self.send_error(404)


if __name__ == "__main__":
    print("Propuesta privada: http://127.0.0.1:8772" + PREFIX + "precios-propuesta.html#asesoria", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8772), PrivatePreview).serve_forever()
