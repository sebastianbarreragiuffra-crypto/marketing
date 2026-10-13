"""Build an isolated, local-only home preview; leave the source landing untouched."""
from pathlib import Path

preview_dir = Path(__file__).resolve().parent
root = preview_dir.parents[2]
source = (root / "index.html").read_text(encoding="utf-8")
hero = (preview_dir / "hero.html").read_text(encoding="utf-8")
start = source.index('    <section class="hx hx-marketing-reference"')
end = source.index('    <section class="home-marketing-example"', start)
preview = source[:start] + hero + source[end:]
preview = preview.replace("<head>", '<head>\n  <base href="../../../">\n  <meta name="robots" content="noindex, nofollow">', 1)
preview = preview.replace("</head>", '  <link rel="stylesheet" href="mockups/s-home-hero/preview-v6/hero.css">\n</head>', 1)
preview = preview.replace("</body>", '  <script src="mockups/s-home-hero/preview-v6/hero.js" defer></script>\n</body>', 1)
(preview_dir / "index.html").write_text(preview, encoding="utf-8")
print(preview_dir / "index.html")
