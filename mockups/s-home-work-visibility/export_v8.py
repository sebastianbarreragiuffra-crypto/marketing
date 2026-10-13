from pathlib import Path
from shutil import copy2
from PIL import Image

dest = Path(__file__).resolve().parent
source = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f')
exports = [
    ('exec-34ed8a6c-97f9-4f85-bf92-ac7b1f93d2c0.png', 'seccion-02-trabajo-v8-desktop', 1440),
    ('exec-3680921f-a1e5-432f-8b34-9e5e93501eaf.png', 'seccion-02-trabajo-v8-mobile', 390),
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
