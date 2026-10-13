from pathlib import Path
from shutil import copy2
from PIL import Image

dest = Path(__file__).resolve().parent
source = Path(r'C:\Users\shermii\.codex\generated_images\01a0e9e8-d133-7f62-bcbc-88ea3292180f\exec-ce866cc1-7127-4c75-a6d2-55edd0387fb1.png')
original = dest / 'seccion-02-trabajo-v8-mobile-ampliado-original.png'
output = dest / 'seccion-02-trabajo-v8-mobile-ampliado-390.png'
if original.exists() or output.exists():
    raise FileExistsError(output)
copy2(source, original)
with Image.open(original) as im:
    im.resize((390, round(im.height * 390 / im.width)), Image.Resampling.LANCZOS).save(output)
with Image.open(output) as im:
    assert im.width == 390
    print(output.name, im.size, output.stat().st_size)
