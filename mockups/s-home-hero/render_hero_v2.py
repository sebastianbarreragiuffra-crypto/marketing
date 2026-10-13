"""Mockup V2: servicio primero, responsabilidades explícitas y móvil compacto."""
from PIL import Image, ImageDraw
from render_mockups import ROOT, DARK, PANEL, LIME, PAPER, SOFT, MUTED, f, text, rr, background, header, arrow, google_card, instagram_card, tiktok_card


def ticks(d, x, y, label, size=14):
    d.line((x, y+7, x+4, y+11, x+12, y+2), fill=LIME, width=2)
    text(d, (x+22, y-3), label, size, PAPER, 600)


def desktop():
    im = background(1440, 810)
    header(im)
    d = ImageDraw.Draw(im)
    # Quiet background behind the primary reading area.
    d.rectangle((0, 89, 550, 810), fill=DARK)
    text(d, (48, 146), "PARA ECOMMERCE Y EMPRESAS B2B", 12, LIME, 800)
    for y, label, color in [(191, "Un equipo para", PAPER), (257, "crear y gestionar", PAPER), (323, "tu publicidad.", LIME)]:
        text(d, (48, y), label, 59, color, 800, "manrope")
    text(d, (49, 427), "Nos ocupamos de los anuncios y los ajustes.", 18, SOFT)
    text(d, (49, 456), "Con GISBA puedes revisar el trabajo", 18, SOFT)
    text(d, (49, 485), "y los próximos pasos.", 18, SOFT)
    rr(d, (48, 544, 374, 607), 32, LIME)
    text(d, (74, 563), "Agenda una reunión", 18, DARK, 800)
    arrow(d, 336, 576, DARK, 16)
    ticks(d, 50, 638, "1 usuario de GISBA incluido")
    text(d, (72, 663), "Usuarios adicionales con costo extra.", 13, MUTED)
    text(d, (49, 707), "La inversión publicitaria se paga aparte.", 14, PAPER, 500)

    text(d, (610, 131), "LA PUBLICIDAD, A CARGO DE ÓRBITA", 12, LIME, 800)
    google_card(im, (586, 301, 808, 535))
    instagram_card(im, (823, 174, 1174, 619))
    tiktok_card(im, (1187, 263, 1391, 569))
    d = ImageDraw.Draw(im)
    text(d, (710, 639), "Ejemplos ilustrativos · Canales según el alcance acordado", 12, MUTED)
    # Editorial explanation, deliberately unlike a product interface.
    rr(d, (586, 681, 1391, 775), 16, PANEL, (77, 100, 58), 1)
    text(d, (610, 697), "ÓRBITA", 11, LIME, 800)
    text(d, (610, 722), "Prepara, gestiona y ajusta.", 17, PAPER, 700)
    arrow(d, 943, 735, LIME, 23)
    text(d, (996, 697), "TU ACCESO A GISBA", 11, LIME, 800)
    text(d, (996, 722), "Información, pendientes", 17, PAPER, 700)
    text(d, (996, 746), "y coordinación con la agencia.", 14, SOFT)
    im.convert("RGB").save(ROOT / "hero-v2-desktop-1440.png", optimize=True)


def mobile(channel="meta"):
    im = background(390, 1080)
    header(im, True)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 75, 390, 512), fill=DARK)
    text(d, (19, 102), "PARA ECOMMERCE Y EMPRESAS B2B", 10, LIME, 800)
    for y, label, color in [(138, "Un equipo para", PAPER), (183, "crear y gestionar", PAPER), (228, "tu publicidad.", LIME)]:
        text(d, (18, y), label, 37, color, 800, "manrope")
    text(d, (19, 291), "Nos ocupamos de anuncios y ajustes.", 16, SOFT)
    text(d, (19, 315), "Con GISBA revisas el trabajo", 16, SOFT)
    text(d, (19, 339), "y los próximos pasos.", 16, SOFT)
    rr(d, (18, 384, 372, 442), 29, LIME)
    text(d, (43, 401), "Agenda una reunión", 17, DARK, 800)
    arrow(d, 328, 413, DARK, 15)
    text(d, (20, 465), "1 usuario GISBA incluido · Adicionales con costo extra", 12, PAPER, 500)
    text(d, (20, 486), "La inversión publicitaria se paga aparte.", 12, SOFT)
    text(d, (20, 529), "ANUNCIOS GESTIONADOS POR ÓRBITA", 11, LIME, 800)
    if channel == "meta":
        instagram_card(im, (27, 557, 363, 938), True)
    elif channel == "google":
        google_card(im, (56, 624, 334, 858))
    else:
        tiktok_card(im, (85, 557, 306, 938))
    d = ImageDraw.Draw(im)
    for x, w, label, key in [(18, 94, "Google", "google"), (120, 94, "Meta", "meta"), (222, 94, "TikTok", "tiktok")]:
        rr(d, (x, 957, x+w, 998), 20, LIME if key == channel else PANEL, (86, 106, 69), 1)
        text(d, (x+20, 969), label, 13, DARK if key == channel else PAPER, 700)
    rr(d, (326, 957, 372, 998), 20, PANEL, (86, 106, 69), 1)
    d.line((344, 971, 344, 984), fill=PAPER, width=3)
    d.line((353, 971, 353, 984), fill=PAPER, width=3)
    text(d, (20, 1016), "Ejemplos ilustrativos · Canales según alcance", 12, MUTED)
    text(d, (20, 1042), "Vista propuesta · recreación para revisión", 10, MUTED)
    im = im.convert("RGB")
    im.save(ROOT / f"hero-v2-mobile-{channel}-390.png", optimize=True)
    if channel == "meta":
        im.crop((0, 0, 390, 844)).save(ROOT / "hero-v2-mobile-primer-pliegue-390.png", optimize=True)


desktop()
for channel in ("meta", "google", "tiktok"):
    mobile(channel)
for path in sorted(ROOT.glob("hero-v2-*.png")):
    print(path.name, Image.open(path).size, path.stat().st_size)
