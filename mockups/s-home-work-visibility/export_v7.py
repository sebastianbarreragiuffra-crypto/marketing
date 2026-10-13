from pathlib import Path
from shutil import copy2
from PIL import Image

dest = Path(__file__).resolve().parent
source = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f')
exports = [
    ('exec-ca35039a-74c3-450e-899e-6e6c605e028d.png', 'seccion-02-trabajo-v7-desktop', 1440),
    ('exec-672256c3-11cc-4f74-9169-3d7f24bc932e.png', 'seccion-02-trabajo-v7-mobile', 390),
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
        print(output.name, check.size, output.stat().st_size)
