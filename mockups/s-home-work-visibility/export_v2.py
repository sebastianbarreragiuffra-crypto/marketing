from pathlib import Path
from shutil import copyfile
from PIL import Image

DEST = Path(__file__).resolve().parent
SOURCE = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f')
EXPORTS = [
    ('exec-832d8a18-ed85-4026-9317-bd278c486029.png', 'seccion-02-coordinacion-v2-desktop', 1440),
    ('exec-cc1b4034-17f8-488e-afd2-b1e0cd5a1e22.png', 'seccion-02-coordinacion-v2-mobile', 390),
    ('exec-c584ea15-c1c4-4dc8-a621-ece5b8484d44.png', 'seccion-02-coordinacion-v2-mobile-legible', 390),
]

for source_name, stem, width in EXPORTS:
    source = SOURCE / source_name
    original = DEST / f'{stem}-original.png'
    target = DEST / f'{stem}-{width}.png'
    if not original.exists():
        copyfile(source, original)
    if not target.exists():
        with Image.open(source) as im:
            height = round(im.height * width / im.width)
            im.resize((width, height), Image.Resampling.LANCZOS).save(target)
    with Image.open(target) as exported:
        assert exported.width == width
        print(f'{target.name}: {exported.width}x{exported.height}, {target.stat().st_size} bytes')
