from pathlib import Path
from PIL import Image
import shutil

root = Path(__file__).resolve().parent
source = Path('C:/Users/shermii/.codex/generated_images/01a0e9e8-d133-7f62-bcbc-88ea3292180f/exec-03c9c700-c77c-4f6c-a1b8-357833ef16c7.png')
original = root / 'gisba-panel-research-v3-original.png'
output = root / 'gisba-panel-research-v3-1440.png'
if original.exists() or output.exists():
    raise FileExistsError('Preserve earlier exports')
shutil.copy2(source, original)
with Image.open(original) as im:
    im.resize((1440, round(im.height * 1440 / im.width)), Image.Resampling.LANCZOS).save(output)
with Image.open(output) as im:
    assert im.width == 1440
    print(f'{output}: {im.width} x {im.height}, {output.stat().st_size} bytes')
