from pathlib import Path
from shutil import copy2
from PIL import Image

dest = Path(__file__).resolve().parent
source = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f\exec-73557b90-5fe1-4d76-a58c-b9b665bb7fc0.png')
original = dest / 'hero-comercial-v1-desktop-original.png'
output = dest / 'hero-comercial-v1-desktop-1440.png'
if original.exists() or output.exists():
    raise FileExistsError(output)
copy2(source, original)
with Image.open(original) as im:
    height = round(im.height * 1440 / im.width)
    assert height == 810, (im.size, height)
    im.resize((1440, height), Image.Resampling.LANCZOS).save(output)
with Image.open(output) as im:
    assert im.size == (1440, 810)
    print(output.name, im.size, output.stat().st_size)
