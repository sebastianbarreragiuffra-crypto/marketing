from pathlib import Path
from shutil import copy2
from PIL import Image

dest = Path(__file__).resolve().parent
source = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f\exec-dae12157-7239-424a-8f83-c7f45f1aae85.png')
original = dest / 'hero-comercial-v3-desktop-original.png'
output = dest / 'hero-comercial-v3-desktop-1440.png'
if original.exists() or output.exists():
    raise FileExistsError(output)
copy2(source, original)
with Image.open(original) as im:
    height = round(im.height * 1440 / im.width)
    assert height == 810
    im.resize((1440, height), Image.Resampling.LANCZOS).save(output)
with Image.open(output) as im:
    assert im.size == (1440, 810)
    print(output.name, im.size, output.stat().st_size)
