from pathlib import Path
from shutil import copyfile
from PIL import Image

DEST = Path(__file__).resolve().parent
SOURCE = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f')
EXPORTS = [
    ('exec-4f827579-3dfc-4c27-a853-cebefe037bc1.png', 'seccion-02-whatsapp-v4-desktop', 1440),
    ('exec-0845e98e-579e-446b-ba03-7e87f8926467.png', 'seccion-02-whatsapp-v4-mobile', 390),
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
    with Image.open(target) as im:
        assert im.width == width
        print(f'{target.name}: {im.width}x{im.height}; {target.stat().st_size} bytes')
