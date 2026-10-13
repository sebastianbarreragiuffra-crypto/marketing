from pathlib import Path
from shutil import copy2
from PIL import Image

dest = Path(__file__).resolve().parent
source = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f')
exports = [
    ('exec-8c44f019-c0ac-470f-96c0-d762975176d8.png', 'seccion-02-coordinacion-v6-mobile', 390),
    ('exec-8506f02e-0d63-45e1-99c1-cc2b5c883417.png', 'seccion-02-coordinacion-v6-desktop', 1440),
]
for filename, name, width in exports:
    original = dest / f'{name}-original.png'
    output = dest / f'{name}-{width}.png'
    if original.exists() or output.exists():
        raise FileExistsError(name)
    copy2(source / filename, original)
    with Image.open(original) as im:
        height = round(im.height * width / im.width)
        im.resize((width, height), Image.Resampling.LANCZOS).save(output)
    with Image.open(output) as check:
        assert check.width == width
        print(output.name, check.size)
