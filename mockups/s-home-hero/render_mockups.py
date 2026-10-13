"""Exporta imágenes estáticas del hero propuesto, sin modificar el sitio."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT.parent.parent / "assets" / "hero"
MANROPE = ROOT / "Manrope.ttf"
DM = ROOT / "DMSans.ttf"

DARK = (11, 13, 11)
DEEP = (11, 13, 11)
PANEL = (23, 29, 23)
LIME = (199, 244, 91)
PAPER = (246, 243, 235)
SOFT = (209, 220, 204)
MUTED = (176, 194, 169)


def f(size, weight=400, family="dm"):
    font = ImageFont.truetype(str(MANROPE if family == "manrope" else DM), size)
    if family == "manrope":
        font.set_variation_by_axes([weight])
    else:
        font.set_variation_by_axes([14, weight])
    return font


def text(d, xy, value, size, color=PAPER, weight=400, family="dm"):
    d.text(xy, value, font=f(size, weight, family), fill=color)


def rr(d, box, radius, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def background(w, h):
    im = Image.new("RGB", (w, h), DEEP)
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((int(w * .58), -80, int(w * 1.22), int(h * .86)), fill=(89, 162, 38, 95))
    gd.ellipse((-300, int(h * .45), 280, int(h * 1.18)), fill=(75, 130, 35, 60))
    glow = glow.filter(ImageFilter.GaussianBlur(110 if w > 500 else 65))
    im = Image.alpha_composite(im.convert("RGBA"), glow)
    d = ImageDraw.Draw(im)
    if w > 500:
        d.arc((1240, -260, 1840, 340), 85, 260, fill=(148, 205, 74, 75), width=2)
    else:
        d.arc((225, -230, 690, 235), 75, 265, fill=(122, 184, 70, 75), width=2)
    return im


def brand(d, x, y, mobile=False):
    cx, cy, r = x + 13, y + 14, 12
    for dx, dy in ((1, 0), (0, 1), (1, 1), (1, -1)):
        d.line((cx-r*dx, cy-r*dy, cx+r*dx, cy+r*dy), fill=LIME, width=3)
    text(d, (x+36, y-1), "ÓRBITA", 23 if not mobile else 21, PAPER, 800, "manrope")
    dotx = x+138 if not mobile else x+131
    d.ellipse((dotx, y+21, dotx+5, y+26), fill=LIME)


def arrow(d, x, y, color=DARK, size=12):
    d.line((x, y, x+size, y), fill=color, width=2)
    d.line((x+size-5, y-5, x+size, y, x+size-5, y+5), fill=color, width=2, joint="curve")


def header(im, mobile=False):
    w = im.width
    d = ImageDraw.Draw(im)
    height = 74 if mobile else 88
    d.rectangle((0, 0, w, height), fill=DARK)
    d.line((0, height-1, w, height-1), fill=(52, 64, 48), width=1)
    brand(d, 20 if mobile else 48, 23 if mobile else 29, mobile)
    if mobile:
        d.line((345, 34, 371, 34), fill=PAPER, width=2)
        d.line((345, 43, 371, 43), fill=PAPER, width=2)
    else:
        nav = [(834, "Inicio", True), (892, "Marketing", False), (982, "Software", False), (1067, "Precios", False), (1141, "Iniciar sesión", False)]
        for x, label, active in nav:
            text(d, (x, 36), label, 13, LIME if active else PAPER, 700)
        rr(d, (1265, 22, 1400, 66), 24, LIME)
        text(d, (1283, 34), "Hablemos", 13, DARK, 800)
        arrow(d, 1375, 43, DARK, 9)


def shadow(im, box, radius=14, blur=20, opacity=80):
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    shifted = (box[0]+3, box[1]+7, box[2]+3, box[3]+7)
    ld.rounded_rectangle(shifted, radius=radius, fill=(0, 0, 0, opacity))
    im.alpha_composite(layer.filter(ImageFilter.GaussianBlur(blur)))


def paste_crop(im, path, box, radius=0, centering=(.5, .5)):
    x0, y0, x1, y1 = box
    photo = Image.open(path).convert("RGB")
    photo = ImageOps.fit(photo, (x1-x0, y1-y0), method=Image.Resampling.LANCZOS, centering=centering)
    if radius:
        mask = Image.new("L", photo.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, photo.width, photo.height), radius, fill=255)
        im.paste(photo, (x0, y0), mask)
    else:
        im.paste(photo, (x0, y0))


def google_card(im, box, small=False):
    x0, y0, x1, y1 = box
    d = ImageDraw.Draw(im)
    shadow(im, box, 13, 16, 85)
    rr(d, box, 13, (255, 255, 255), (137, 160, 132), 1)
    d.rounded_rectangle((x0, y0, x1, y0+42), radius=13, fill=(2, 18, 7))
    d.rectangle((x0, y0+29, x1, y0+42), fill=(2, 18, 7))
    rr(d, (x0+11, y0+10, x0+34, y0+33), 12, (255, 255, 255))
    text(d, (x0+16, y0+11), "G", 16, (52, 110, 220), 800, "manrope")
    text(d, (x0+43, y0+12), "Google Ads", 14 if not small else 12, PAPER, 700)
    if small:
        text(d, (x0+12, y0+52), "Patrocinado", 10, (50, 50, 50), 700)
        text(d, (x0+12, y0+78), "Cajas para", 15, (25, 62, 168), 700)
        text(d, (x0+12, y0+99), "tu negocio", 15, (25, 62, 168), 700)
        text(d, (x0+12, y0+135), "Solicita cotización", 10, (25, 62, 168), 600)
    else:
        text(d, (x0+16, y0+61), "Patrocinado", 11, (42, 48, 42), 700)
        text(d, (x0+16, y0+92), "Cajas de cartón", 18, (20, 59, 170), 700)
        text(d, (x0+16, y0+116), "para empresas", 18, (20, 59, 170), 700)
        text(d, (x0+16, y0+150), "Empaques para proteger", 12, (40, 49, 50))
        text(d, (x0+16, y0+167), "tus productos.", 12, (40, 49, 50))
        text(d, (x0+16, y0+201), "Solicita una cotización", 11, (22, 61, 180), 700)


def instagram_card(im, box, mobile=False):
    x0, y0, x1, y1 = box
    w = x1-x0
    d = ImageDraw.Draw(im)
    shadow(im, box, 15, 25, 105)
    rr(d, box, 15, (255, 255, 255), (159, 179, 155), 1)
    d.rounded_rectangle((x0, y0, x1, y0+43), radius=14, fill=(1, 18, 7))
    d.rectangle((x0, y0+29, x1, y0+43), fill=(1, 18, 7))
    rr(d, (x0+13, y0+9, x0+39, y0+35), 7, (225, 60, 130))
    rr(d, (x0+19, y0+15, x0+33, y0+29), 5, None, (255, 255, 255), 2)
    d.ellipse((x0+24, y0+19, x0+28, y0+23), outline=(255,255,255), width=2)
    text(d, (x0+48, y0+12), "INSTAGRAM", 15 if not mobile else 14, PAPER, 700)
    d.ellipse((x0+14, y0+55, x0+48, y0+89), fill=(208, 209, 211))
    text(d, (x0+59, y0+55), "Tu negocio", 14, DARK, 700)
    text(d, (x0+59, y0+74), "Anuncio", 11, (83, 88, 83))
    img_top = y0+100
    img_bottom = y1-48
    paste_crop(im, ASSETS / "packaging-products.webp", (x0+1, img_top, x1-1, img_bottom), 0)
    d = ImageDraw.Draw(im)
    title_size = 31 if not mobile else 30
    text(d, (x0+18, img_top+24), "Tu producto,", title_size, DARK, 800, "manrope")
    text(d, (x0+18, img_top+59), "bien presentado.", title_size, DARK, 800, "manrope")
    text(d, (x0+19, img_top+104), "Empaques para tu negocio", 13, DARK, 600)
    # Bottom row intentionally omits invented engagement counts.
    d.ellipse((x0+16, y1-30, x0+28, y1-18), outline=(30, 35, 30), width=2)
    text(d, (x0+38, y1-34), "Pieza ilustrativa", 11, (57, 64, 57), 600)
    arrow(d, x1-34, y1-24, (44, 50, 44), 12)


def tiktok_card(im, box, small=False):
    x0, y0, x1, y1 = box
    d = ImageDraw.Draw(im)
    shadow(im, box, 14, 18, 90)
    rr(d, box, 14, (19, 20, 18), (130, 151, 126), 1)
    paste_crop(im, ASSETS / "packaging-process.webp", (x0+1, y0+1, x1-1, y1-1), 13, (.52, .5))
    shade = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shade)
    sd.rectangle((x0+1, y0+1, x1-1, y0+105), fill=(0, 0, 0, 115))
    shade = shade.filter(ImageFilter.GaussianBlur(9))
    im.alpha_composite(shade)
    d = ImageDraw.Draw(im)
    text(d, (x0+13, y0+15), "TikTok Ads", 14 if not small else 12, PAPER, 700)
    if not small:
        text(d, (x0+13, y0+60), "Preparamos", 19, PAPER, 800, "manrope")
        text(d, (x0+13, y0+84), "tu próximo", 19, PAPER, 800, "manrope")
        text(d, (x0+13, y0+108), "envío.", 19, PAPER, 800, "manrope")
    d.ellipse(((x0+x1)//2-16, (y0+y1)//2-16, (x0+x1)//2+16, (y0+y1)//2+16), fill=(255,255,255,220))
    cx, cy = (x0+x1)//2, (y0+y1)//2
    d.polygon(((cx-4, cy-8), (cx+9, cy), (cx-4, cy+8)), fill=(20,25,20))


def desktop():
    im = background(1440, 810)
    header(im)
    d = ImageDraw.Draw(im)
    text(d, (48, 166), "PUBLICIDAD PARA ECOMMERCE Y EMPRESAS B2B", 12, LIME, 800)
    text(d, (48, 213), "Un equipo para", 59, PAPER, 800, "manrope")
    text(d, (48, 278), "crear y gestionar", 59, PAPER, 800, "manrope")
    text(d, (48, 343), "tu publicidad.", 59, LIME, 800, "manrope")
    text(d, (49, 439), "Órbita crea y gestiona tus campañas.", 19, PAPER, 500)
    text(d, (49, 469), "Con GISBA revisas información y pendientes", 19, SOFT, 400)
    text(d, (49, 499), "junto a nuestro equipo.", 19, SOFT, 400)
    rr(d, (48, 560, 352, 622), 31, LIME)
    text(d, (74, 579), "Agenda una reunión", 18, DARK, 800)
    arrow(d, 316, 591, DARK, 16)
    rr(d, (48, 649, 499, 689), 14, PANEL, (120, 149, 76), 1)
    text(d, (62, 661), "1 usuario GISBA incluido", 14, PAPER, 600)
    text(d, (252, 661), "Inversión publicitaria aparte", 13, PAPER, 600)

    text(d, (753, 139), "UN MISMO NEGOCIO. ANUNCIOS ADAPTADOS A CADA CANAL.", 12, LIME, 700)
    google_card(im, (572, 325, 794, 559))
    instagram_card(im, (807, 180, 1158, 625))
    tiktok_card(im, (1170, 270, 1374, 576))
    d = ImageDraw.Draw(im)
    text(d, (689, 660), "ESTRATEGIA", 13, PAPER, 800)
    arrow(d, 791, 670, LIME, 18)
    text(d, (832, 660), "CREACIÓN", 13, PAPER, 800)
    arrow(d, 931, 670, LIME, 18)
    text(d, (974, 660), "GESTIÓN", 13, PAPER, 800)
    arrow(d, 1055, 670, LIME, 18)
    text(d, (1098, 660), "AJUSTES", 13, PAPER, 800)
    text(d, (866, 700), "Ejemplos ilustrativos · Canales según el alcance acordado", 11, MUTED, 400)
    d.rectangle((0, 744, 1440, 810), fill=(246, 243, 235))
    im.convert("RGB").save(ROOT / "hero-01-desktop-1440.png", optimize=True)


def mobile():
    im = background(390, 1360)
    header(im, True)
    d = ImageDraw.Draw(im)
    text(d, (19, 105), "PUBLICIDAD PARA ECOMMERCE Y B2B", 10, LIME, 800)
    text(d, (18, 146), "Un equipo para", 39, PAPER, 800, "manrope")
    text(d, (18, 194), "crear y gestionar", 39, PAPER, 800, "manrope")
    text(d, (18, 242), "tu publicidad.", 39, LIME, 800, "manrope")
    text(d, (19, 316), "Órbita crea y gestiona tus campañas.", 16, PAPER, 500)
    text(d, (19, 340), "Con GISBA revisas información y", 16, SOFT, 400)
    text(d, (19, 364), "pendientes junto a nuestro equipo.", 16, SOFT, 400)
    rr(d, (18, 413, 372, 470), 28, LIME)
    text(d, (55, 430), "Agenda una reunión", 17, DARK, 800)
    arrow(d, 327, 443, DARK, 16)
    rr(d, (18, 487, 372, 549), 12, PANEL, (111, 147, 70), 1)
    text(d, (33, 499), "1 usuario GISBA incluido", 12, PAPER, 600)
    text(d, (33, 522), "Inversión publicitaria aparte", 12, PAPER, 600)
    text(d, (19, 578), "ANUNCIOS DE UN MISMO NEGOCIO", 11, LIME, 800)
    instagram_card(im, (27, 606, 363, 1082), True)
    google_card(im, (18, 1107, 187, 1282), True)
    tiktok_card(im, (202, 1107, 372, 1282), True)
    d = ImageDraw.Draw(im)
    text(d, (22, 1309), "Ejemplos ilustrativos · Canales según alcance", 10, MUTED, 400)
    im = im.convert("RGB")
    im.save(ROOT / "hero-01-mobile-completo-390.png", optimize=True)
    im.crop((0, 0, 390, 844)).save(ROOT / "hero-01-mobile-primer-pliegue-390.png", optimize=True)


if __name__ == "__main__":
    desktop()
    mobile()
    for name in ("hero-01-desktop-1440.png", "hero-01-mobile-primer-pliegue-390.png", "hero-01-mobile-completo-390.png"):
        path = ROOT / name
        print(name, Image.open(path).size, path.stat().st_size)
