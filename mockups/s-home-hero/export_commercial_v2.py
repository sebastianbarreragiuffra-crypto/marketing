from pathlib import Path
from shutil import copy2
from PIL import Image

dest = Path(__file__).resolve().parent
source = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f\exec-2d18357a-b52f-4fd5-9a7f-39cf44c46122.png')
original = dest / 'hero-comercial-v2-desktop-original.png'
output = dest / 'hero-comercial-v2-desktop-1440.png'
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
