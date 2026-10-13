from pathlib import Path
from shutil import copy2
from PIL import Image

dest = Path(__file__).resolve().parent
source = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f\exec-fe052ac5-7956-4d07-b293-99c794ce8d4c.png')
original = dest / 'gisba-bandeja-panel-v1-original.png'
output = dest / 'gisba-bandeja-panel-v1-desktop-1440.png'
if original.exists() or output.exists():
    raise FileExistsError(output)
copy2(source, original)
with Image.open(original) as im:
    im.resize((1440, round(im.height * 1440 / im.width)), Image.Resampling.LANCZOS).save(output)
with Image.open(output) as im:
    assert im.width == 1440
    print(output.name, im.size)
