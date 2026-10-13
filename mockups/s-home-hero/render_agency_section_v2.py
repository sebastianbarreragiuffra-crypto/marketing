"""Propuesta de la sección siguiente al hero, exportada sólo como imagen."""
from PIL import Image, ImageDraw
from render_mockups import ROOT, PAPER, DARK, PANEL, LIME, SOFT, MUTED, f, text, rr

GREEN = (72, 98, 46)
GRAY = (89, 97, 82)
LINE = (204, 205, 191)


def icon(d, x, y, kind):
    rr(d, (x, y, x+48, y+48), 12, (235, 238, 221))
    if kind == 0:
        rr(d, (x+13, y+10, x+36, y+38), 3, None, GREEN, 2)
        for yy, length in [(18, 14), (25, 14), (32, 8)]:
            d.line((x+17, y+yy, x+17+length, y+yy), fill=GREEN, width=2)
    elif kind == 1:
        for xx, height in [(13, 12), (23, 23), (33, 17)]:
            d.rectangle((x+xx, y+36-height, x+xx+4, y+36), fill=GREEN)
    else:
        for yy, xx in [(15, 19), (24, 32), (33, 23)]:
            d.line((x+11, y+yy, x+38, y+yy), fill=GREEN, width=2)
            d.ellipse((x+xx-3, y+yy-3, x+xx+3, y+yy+3), fill=PAPER, outline=GREEN, width=2)


items = [
    ("01", "Preparamos tus anuncios", "Mensajes y piezas para los canales que acordemos."),
    ("02", "Gestionamos tus campañas", "Google, Meta o TikTok, según la propuesta contratada."),
    ("03", "Revisamos y ajustamos", "Analizamos resultados y decidimos los próximos cambios."),
]

im = Image.new("RGB", (1440, 810), PAPER)
d = ImageDraw.Draw(im)
text(d, (48, 100), "EL TRABAJO DE ÓRBITA", 12, GREEN, 800)
for y, label in [(175, "Así trabajamos"), (239, "en tus campañas.")]:
    text(d, (48, y), label, 55, DARK if y == 175 else GREEN, 800, "manrope")
text(d, (49, 389), "Definimos contigo el alcance.", 21, DARK, 600)
text(d, (49, 425), "Nos encargamos del trabajo publicitario", 19, GRAY)
text(d, (49, 455), "y revisamos contigo cómo continuar.", 19, GRAY)
for index, (num, title, detail) in enumerate(items):
    y = 118 + index*165
    d.line((624, y-15, 1391, y-15), fill=LINE, width=1)
    text(d, (626, y+6), num, 21, GREEN, 800, "manrope")
    icon(d, 704, y, index)
    text(d, (784, y+2), title, 28, DARK, 800, "manrope")
    text(d, (784, y+50), detail, 17, GRAY)
rr(d, (48, 657, 1391, 760), 20, PANEL)
text(d, (77, 684), "Los ajustes los decide el equipo de Órbita.", 24, PAPER, 800, "manrope")
text(d, (77, 725), "GISBA aporta información para el análisis y facilita la coordinación contigo.", 17, SOFT)
im.save(ROOT / "seccion-02-agencia-desktop-1440.png", optimize=True)

im = Image.new("RGB", (390, 1030), PAPER)
d = ImageDraw.Draw(im)
text(d, (20, 47), "EL TRABAJO DE ÓRBITA", 11, GREEN, 800)
for y, label in [(108, "Así trabajamos"), (155, "en tus campañas.")]:
    text(d, (18, y), label, 39, DARK if y == 108 else GREEN, 800, "manrope")
text(d, (20, 256), "Definimos contigo el alcance.", 17, DARK, 600)
text(d, (20, 285), "Nos encargamos de la publicidad", 16, GRAY)
text(d, (20, 309), "y revisamos cómo continuar.", 16, GRAY)
mobile_details = [
    ["Mensajes y piezas para los", "canales que acordemos."],
    ["Google, Meta o TikTok, según", "la propuesta contratada."],
    ["Analizamos resultados y decidimos", "los próximos cambios."],
]
for index, (num, title, detail) in enumerate(items):
    y = 383 + index*151
    d.line((20, y-15, 370, y-15), fill=LINE, width=1)
    icon(d, 20, y, index)
    text(d, (87, y), title, 20, DARK, 800, "manrope")
    for n, line in enumerate(mobile_details[index]):
        text(d, (87, y+40+n*24), line, 15, GRAY)
rr(d, (18, 857, 372, 1007), 16, PANEL)
text(d, (36, 877), "Los ajustes los decide", 21, PAPER, 800, "manrope")
text(d, (36, 906), "el equipo de Órbita.", 21, PAPER, 800, "manrope")
text(d, (36, 944), "GISBA aporta información para el análisis", 13, SOFT)
text(d, (36, 968), "y facilita la coordinación contigo.", 13, SOFT)
im.save(ROOT / "seccion-02-agencia-mobile-390.png", optimize=True)
for path in sorted(ROOT.glob("seccion-02-agencia-*.png")):
    print(path.name, Image.open(path).size, path.stat().st_size)
