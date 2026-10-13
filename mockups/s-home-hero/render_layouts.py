"""Wireframes de layout para el hero de Inicio; no son assets del sitio."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONT = Path(r"C:\Windows\Fonts\arial.ttf")
BOLD = Path(r"C:\Windows\Fonts\arialbd.ttf")
BG = "#eeeeee"
INK = "#262626"
MUTED = "#626262"
LINE = "#a5a5a5"
PANEL = "#d4d4d4"
WHITE = "#f8f8f8"


def font(size, bold=False):
    return ImageFont.truetype(str(BOLD if bold else FONT), size)


def txt(draw, xy, value, size=18, color=INK, bold=False):
    draw.text(xy, value, fill=color, font=font(size, bold))


def box(draw, xy, fill=WHITE, outline=LINE, radius=12, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def lines(draw, x, y, items, size, gap, color=INK, bold=False):
    for n, item in enumerate(items):
        txt(draw, (x, y + n * gap), item, size, color, bold)


def header(draw, w, mobile=False):
    h = 72 if mobile else 82
    draw.rectangle((0, 0, w, h), fill="#383838")
    txt(draw, (24 if mobile else 48, 23), "ORBITA", 22, "#ffffff", True)
    if mobile:
        txt(draw, (w - 65, 22), "MENU", 12, "#ffffff", True)
    else:
        txt(draw, (760, 30), "Inicio   Marketing   Software   Precios   Iniciar sesión", 14, "#ffffff")
        box(draw, (1235, 20, 1390, 62), fill="#f1f1f1", outline="#f1f1f1", radius=21)
        txt(draw, (1268, 32), "Hablemos", 15, INK, True)
    return h


def copy(draw, mobile=False, top=160, x=48, variant=1):
    eyebrow = "PUBLICIDAD PARA ECOMMERCE Y B2B"
    if mobile:
        txt(draw, (x, top), eyebrow, 13, MUTED, True)
        lines(draw, x, top + 43, ["Un equipo para", "crear y gestionar", "tu publicidad."], 35, 45, INK, True)
        lines(draw, x, top + 200, ["Creamos tus anuncios y gestionamos", "tus campañas. GISBA ayuda a", "mostrarte qué se hizo y qué sigue."], 16, 24)
        box(draw, (x, top + 293, 390 - x, top + 347), fill="#8e8e8e", outline="#8e8e8e", radius=26)
        txt(draw, (x + 45, top + 309), "Agenda una reunión  >", 17, "#ffffff", True)
        txt(draw, (x, top + 370), "1 usuario GISBA incluido", 14, MUTED)
        txt(draw, (x, top + 392), "Pauta publicitaria aparte", 14, MUTED)
    else:
        txt(draw, (x, top), eyebrow, 16, MUTED, True)
        lines(draw, x, top + 49, ["Un equipo para", "crear y gestionar", "tu publicidad."], 52, 60, INK, True)
        lines(draw, x, top + 250, ["Creamos tus anuncios y gestionamos tus", "campañas. GISBA ayuda a mostrarte lo", "que se hizo y qué sigue."], 21, 31)
        box(draw, (x, top + 380, x + 316, top + 440), fill="#858585", outline="#858585", radius=30)
        txt(draw, (x + 31, top + 397), "Agenda una reunión   >", 20, "#ffffff", True)
        txt(draw, (x, top + 465), "1 usuario GISBA incluido  ·  Pauta aparte", 16, MUTED)


def base(title, note, mobile=False):
    w, h = (390, 844) if mobile else (1440, 810)
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    header(d, w, mobile)
    if not mobile:
        txt(d, (48, 765), f"{title}  |  {note}  |  WIREFRAME - NO PUBLICADO", 14, MUTED)
    return im, d


def layout_1(mobile=False):
    im, d = base("01 · Hero actual refinado", "Mantiene anuncios y composicion", mobile)
    if mobile:
        copy(d, True, 100, 22)
        txt(d, (22, 559), "EJEMPLO ILUSTRATIVO", 12, MUTED, True)
        box(d, (22, 584, 368, 824), PANEL)
        txt(d, (38, 604), "Anuncio de un negocio", 17, INK, True)
        box(d, (38, 644, 352, 805), "#bababa", outline="#bababa")
    else:
        copy(d, False, 174)
        txt(d, (800, 130), "UN NEGOCIO · ANUNCIOS POR CANAL", 16, MUTED, True)
        box(d, (730, 323, 885, 560), PANEL)
        txt(d, (747, 341), "Google", 18, INK, True)
        box(d, (890, 170, 1190, 637), WHITE)
        txt(d, (914, 192), "Meta · anuncio", 19, INK, True)
        box(d, (914, 242, 1166, 573), PANEL)
        txt(d, (945, 385), "Pieza creativa", 21, INK, True)
        box(d, (1196, 265, 1362, 573), PANEL)
        txt(d, (1213, 286), "TikTok", 18, INK, True)
        txt(d, (780, 665), "Estrategia  >  Creacion  >  Gestion  >  Ajustes", 18, MUTED)
        txt(d, (913, 700), "Ejemplos ilustrativos", 14, MUTED)
    return im


def layout_2(mobile=False):
    im, d = base("02 · Promesa + proceso", "Menos protagonismo de anuncios", mobile)
    if mobile:
        copy(d, True, 100, 22)
        txt(d, (22, 559), "CÓMO TRABAJAMOS", 13, MUTED, True)
        for i, label in enumerate(["01 Estrategia", "02 Anuncios", "03 Gestión"]):
            y = 584 + i * 62
            box(d, (22, y, 368, y + 48), PANEL)
            txt(d, (40, y + 14), label, 17, INK, True)
    else:
        txt(d, (48, 132), "PUBLICIDAD PARA ECOMMERCE Y B2B", 16, MUTED, True)
        lines(d, 48, 178, ["Un equipo para crear y gestionar", "tu publicidad."], 58, 67, INK, True)
        lines(d, 49, 341, ["Creamos tus anuncios, gestionamos tus campañas y compartimos", "contigo qué se hizo y qué sigue, con apoyo de GISBA."], 21, 32)
        box(d, (48, 435, 365, 496), fill="#858585", outline="#858585", radius=30)
        txt(d, (80, 453), "Agenda una reunión   >", 20, "#ffffff", True)
        txt(d, (400, 456), "1 usuario GISBA incluido · Pauta aparte", 16, MUTED)
        for i, label in enumerate(["Estrategia", "Anuncios", "Gestión", "Información GISBA"]):
            x = 48 + i * 347
            box(d, (x, 563, x + 315, 705), PANEL)
            txt(d, (x + 22, 585), f"0{i+1}", 18, MUTED, True)
            txt(d, (x + 22, 635), label, 22, INK, True)
    return im


def layout_3(mobile=False):
    im, d = base("03 · Responsabilidades", "Muestra agencia y visibilidad", mobile)
    if mobile:
        copy(d, True, 100, 22)
        txt(d, (22, 559), "QUIÉN HACE QUÉ", 13, MUTED, True)
        box(d, (22, 584, 368, 679), PANEL)
        txt(d, (38, 604), "ÓRBITA GESTIONA", 16, INK, True)
        txt(d, (38, 635), "Anuncios y campañas", 15, INK)
        box(d, (22, 689, 368, 784), WHITE)
        txt(d, (38, 709), "TÚ VES CON GISBA", 16, INK, True)
        txt(d, (38, 740), "Información y pendientes", 15, INK)
    else:
        copy(d, False, 174)
        txt(d, (810, 138), "DEL TRABAJO A LA VISIBILIDAD", 16, MUTED, True)
        box(d, (744, 183, 1304, 381), PANEL)
        txt(d, (778, 213), "ÓRBITA CREA Y GESTIONA", 22, INK, True)
        box(d, (778, 260, 950, 351), WHITE)
        box(d, (964, 260, 1136, 351), WHITE)
        box(d, (1150, 260, 1270, 351), WHITE)
        txt(d, (802, 290), "Anuncio", 16, MUTED)
        txt(d, (988, 290), "Campaña", 16, MUTED)
        txt(d, (1162, 290), "Ajuste", 16, MUTED)
        txt(d, (1005, 395), "v", 28, MUTED, True)
        box(d, (814, 443, 1362, 645), WHITE)
        txt(d, (846, 472), "EL CLIENTE REVISA CON GISBA", 22, INK, True)
        txt(d, (846, 528), "Información · pendientes · coordinación", 19, MUTED)
        txt(d, (846, 590), "Vista conceptual, no captura del producto", 14, MUTED)
    return im


for number, renderer in enumerate((layout_1, layout_2, layout_3), 1):
    for mode in ("desktop", "mobile"):
        output = ROOT / f"hero-layout-{number:02d}-{mode}.png"
        renderer(mode == "mobile").save(output, optimize=True)
        print(output.name, Image.open(output).size)

sheet = Image.new("RGB", (1440, 1790), "#f7f7f7")
sd = ImageDraw.Draw(sheet)
txt(sd, (28, 16), "Hero Inicio · tres direcciones de layout", 28, INK, True)
txt(sd, (28, 52), "Wireframes grises: comparación de jerarquía, no diseño final ni publicación.", 16, MUTED)
for index in range(1, 4):
    y = 95 + (index - 1) * 560
    desktop = Image.open(ROOT / f"hero-layout-{index:02d}-desktop.png")
    mobile = Image.open(ROOT / f"hero-layout-{index:02d}-mobile.png")
    desktop.thumbnail((950, 534))
    mobile.thumbnail((245, 530))
    sheet.paste(desktop, (20, y + 30))
    sheet.paste(mobile, (1010, y + 8))
    txt(sd, (20, y), f"0{index} · {['Actual refinado', 'Promesa + proceso', 'Responsabilidades'][index - 1]}", 21, INK, True)
sheet.save(ROOT / "hero-layout-comparativo.png", optimize=True)
print("hero-layout-comparativo.png", sheet.size)
