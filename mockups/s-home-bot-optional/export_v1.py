from pathlib import Path
from shutil import copy2
from PIL import Image

dest = Path(__file__).resolve().parent
source = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f')
exports = [
    ('exec-bfc160f5-4dfb-4e11-9c7e-785a2af591d7.png', 'seccion-03-atencion-v1-desktop', 1440),
    ('exec-a7c1b087-23d4-47eb-b366-6e127428ccd1.png', 'seccion-03-atencion-v1-mobile', 390),
]
for filename, name, width in exports:
    original = dest / f'{name}-original.png'
    output = dest / f'{name}-{width}.png'
    if original.exists() or output.exists():
        raise FileExistsError(name)
    copy2(source / filename, original)
    with Image.open(original) as im:
        im.resize((width, round(im.height * width / im.width)), Image.Resampling.LANCZOS).save(output)
    with Image.open(output) as im:
        assert im.width == width
        print(output.name, im.size)
