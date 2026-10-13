"""Arma mockup.html (v1) o mockup-vN.html: copia precios.html real y reemplaza sólo el hero (.pr-hero).
Uso: python build.py [v2|v3]
"""
import io
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
VER = sys.argv[1] if len(sys.argv) > 1 else ""

src = io.open(ROOT / "precios.html", encoding="utf-8").read()
sec = io.open(HERE / (f"hero-section-{VER}.html" if VER else "hero-section.html"), encoding="utf-8").read().rstrip("\n")
start = src.index('    <section class="pr-hero"')
end = src.index("</section>", start) + len("</section>")
out = src[:start] + sec + src[end:]
out = re.sub(r'\s*<link rel="preload" as="image"[^>]+>', "", out)
out = re.sub(r'(href|src)="(?!https?:|#|data:|\.\./)([^"]+)"', lambda m: f'{m.group(1)}="../../{m.group(2)}"', out)
out = out.replace("<title>Precios | Órbita</title>", "<title>[Mockup S] Hero de Precios — Órbita</title>")
css = '  <link rel="stylesheet" href="hero.css">\n' + (f'  <link rel="stylesheet" href="hero-{VER}.css">\n' if VER else "")
out = out.replace("</head>", css + "</head>", 1)
name = f"mockup-{VER}.html" if VER else "mockup.html"
io.open(HERE / name, "w", encoding="utf-8", newline="\n").write(out)
print(name, len(out))
