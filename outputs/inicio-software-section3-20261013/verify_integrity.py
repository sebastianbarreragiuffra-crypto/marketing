from pathlib import Path
from PIL import Image
import hashlib, json, re

out = Path(__file__).parent
before = Path('archive/2026-10-13-inicio-software-section3-before/index.html').read_bytes()
now = Path('index.html').read_bytes()
cleaned = re.sub(rb'    <section class="ois-section"[\s\S]+?</section>\r?\n\r?\n', b'', now, count=1)
cleaned = re.sub(rb'  <link rel="stylesheet" href="css/home-software-section3-20261013.css\?v=1">\r?\n', b'', cleaned, count=1)
baseline = json.loads((out / 'baseline.json').read_text())
changed = [p for p, h in baseline.items() if not Path(p).exists() or hashlib.sha256(Path(p).read_bytes()).hexdigest() != h]
ids = re.findall(r'\bid="([^"]+)"', now.decode('utf-8'))
def lum(h):
    rgb = [int(h[i:i+2], 16)/255 for i in (1,3,5)]
    v = [c/12.92 if c <= .04045 else ((c+.055)/1.055)**2.4 for c in rgb]
    return sum(c*w for c,w in zip(v, [.2126,.7152,.0722]))
def contrast(a,b):
    v = sorted([lum(a),lum(b)])
    return round((v[1]+.05)/(v[0]+.05),2)
pairs = [('#10164c','#ffffff'),('#5363a0','#ffffff'),('#5363a0','#f0edff'),('#5422de','#e7dfff'),('#78490d','#fff0d7'),('#246223','#e0fbd8'),('#a34308','#ffffff'),('#c7f45b','#0b0d0b'),('#d5d7cd','#0b0d0b'),('#e4e4dd','#0b0d0b')]
result = {
    'outsideSectionByteIdentical': cleaned == before,
    'previousFilesChanged': changed,
    'otherPagesAndExistingStylesPreserved': changed == ['index.html'],
    'duplicateIds': sorted({i for i in ids if ids.count(i)>1}),
    'contrast': [{'text':a,'background':b,'ratio':contrast(a,b)} for a,b in pairs],
    'captures': [{'file':p.name,'dimensions':Image.open(p).size} for p in out.glob('section-*.png')],
    'logo': {'file':'assets/home-software-section3/gisba-logo-reference.png','source':'User-supplied mobile reference, logo-only extraction, not redrawn','size': Image.open('assets/home-software-section3/gisba-logo-reference.png').size},
}
(out/'integrity-checks.json').write_text(json.dumps(result,indent=2), encoding='utf-8')
print(json.dumps(result,indent=2))
assert result['outsideSectionByteIdentical']
assert result['otherPagesAndExistingStylesPreserved']
assert not result['duplicateIds']
assert all(p['ratio']>=4.5 for p in result['contrast'])
