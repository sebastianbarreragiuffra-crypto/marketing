from pathlib import Path
from PIL import Image
import shutil

root = Path(__file__).resolve().parent
generated = Path('C:/Users/shermii/.codex/generated_images/01a0e9e8-d133-7f62-bcbc-88ea3292180f')
variants = [('editorial', 'exec-05f50e99-84c3-489c-be9f-cdeb126b1884.png'), ('panoramico', 'exec-6bd714ab-2324-4734-b1e3-9b63f69fbf67.png')]
for name, file in variants:
    original = root / f'hero-reset-v8-{name}-original.png'
    output = root / f'hero-reset-v8-{name}-1440.png'
    if original.exists() or output.exists():
        raise FileExistsError('Preserve earlier versions')
    shutil.copy2(generated / file, original)
    with Image.open(original) as im:
        assert abs(im.width / im.height - 16 / 9) < .01
        im.resize((1440, 810), Image.Resampling.LANCZOS).save(output)
    with Image.open(output) as im:
        assert im.size == (1440, 810)
        print(f'{output}: {im.width} x {im.height}, {output.stat().st_size} bytes')
