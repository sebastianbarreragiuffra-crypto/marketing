from pathlib import Path
from PIL import Image
import shutil

root = Path(__file__).resolve().parent
source = Path('C:/Users/shermii/.codex/generated_images/01a0e9e8-d133-7f62-bcbc-88ea3292180f/exec-c3251614-8a3e-48a1-9e47-46ad65549c28.png')
original = root / 'gisba-panel-layouts-v2-original.png'
output = root / 'gisba-panel-layouts-v2-1440.png'
if original.exists() or output.exists():
    raise FileExistsError('Preserve existing versions')
shutil.copy2(source, original)
with Image.open(original) as im:
    height = round(im.height * 1440 / im.width)
    im.resize((1440, height), Image.Resampling.LANCZOS).save(output)
with Image.open(output) as im:
    assert im.width == 1440
    print(f'{output}: {im.width} x {im.height}, {output.stat().st_size} bytes')
