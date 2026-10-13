from pathlib import Path
from shutil import copy2
from PIL import Image

dest = Path(__file__).resolve().parent
source = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f\exec-16a4c8f9-c3dd-4580-9224-60954891878c.png')
original = dest / 'hero-comercial-v4-desktop-original.png'
output = dest / 'hero-comercial-v4-desktop-1440.png'
if original.exists() or output.exists():
    raise FileExistsError(output)
copy2(source, original)
with Image.open(original) as im:
    height = round(im.height * 1440 / im.width)
    assert height == 810
    im.resize((1440, height), Image.Resampling.LANCZOS).save(output)
with Image.open(output) as im:
    assert im.size == (1440, 810)
    print(output.name, im.size)
