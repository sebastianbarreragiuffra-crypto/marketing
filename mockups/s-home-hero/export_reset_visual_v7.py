from pathlib import Path
from PIL import Image
import shutil

root = Path(__file__).resolve().parent
source = Path('C:/Users/shermii/.codex/generated_images/01a0e9e8-d133-7f62-bcbc-88ea3292180f/exec-0d11d279-4eb9-46fe-895c-644ef65317ac.png')
original = root / 'reset-visual-v7-original.png'
output = root / 'reset-visual-v7-1440.png'
if original.exists() or output.exists():
    raise FileExistsError('Preserve previous mockups')
shutil.copy2(source, original)
with Image.open(original) as im:
    im.resize((1440, round(im.height * 1440 / im.width)), Image.Resampling.LANCZOS).save(output)
with Image.open(output) as im:
    assert im.width == 1440
    print(f'{output}: {im.width} x {im.height}, {output.stat().st_size} bytes')
