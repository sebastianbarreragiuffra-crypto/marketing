from pathlib import Path
from shutil import copyfile
from PIL import Image

DEST = Path(__file__).resolve().parent
SOURCE = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f')
EXPORTS = [
    ('exec-da7d0d6b-dab0-46e6-9335-e3c13d6d3302.png', 'seccion-02-trabajo-gisba-v1-desktop', 1440),
    ('exec-b4087a13-cf38-4128-8267-09aaf1201413.png', 'seccion-02-trabajo-gisba-v1-mobile', 390),
]

for source_name, stem, width in EXPORTS:
    source = SOURCE / source_name
    original = DEST / f'{stem}-original.png'
    target = DEST / f'{stem}-{width}.png'
    copyfile(source, original)
    with Image.open(source) as im:
        height = round(im.height * width / im.width)
        im.resize((width, height), Image.Resampling.LANCZOS).save(target)
    with Image.open(target) as exported:
        assert exported.width == width
        print(f'{target.name}: {exported.width} x {exported.height}; {target.stat().st_size} bytes')
