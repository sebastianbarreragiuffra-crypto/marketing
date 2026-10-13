from pathlib import Path
from PIL import Image
import shutil

root = Path(__file__).resolve().parent
source = Path('C:/Users/shermii/.codex/generated_images/01a0e9e8-d133-7f62-bcbc-88ea3292180f/exec-cf713270-e2fe-4a2c-a51c-00f2e1d20bbe.png')
original = root / 'hero-editorial-v9-color-original.png'
output = root / 'hero-editorial-v9-color-1440.png'
if original.exists() or output.exists():
    raise FileExistsError('Preserve existing mockups')
shutil.copy2(source, original)
with Image.open(original) as im:
    assert abs(im.width / im.height - 16 / 9) < .01
    im.resize((1440, 810), Image.Resampling.LANCZOS).save(output)
with Image.open(output) as im:
    assert im.size == (1440, 810)
    print(f'{output}: {im.width} x {im.height}, {output.stat().st_size} bytes')
