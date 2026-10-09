from pathlib import Path
from html.parser import HTMLParser
import hashlib, json, re
root = Path(__file__).resolve().parents[2]
out = Path(__file__).resolve().parent
baseline = json.loads((out/'baseline.json').read_text(encoding='utf-8'))
changed=[]
for name, digest in baseline.items():
    file=root/name
    if not file.exists() or hashlib.sha256(file.read_bytes()).hexdigest()!=digest:
        changed.append(name)
before=(root/'archive/2026-10-09-seccion-2-referencia/index.html').read_text(encoding='utf-8-sig')
after=(root/'index.html').read_text(encoding='utf-8-sig')
hero=lambda html:html[html.index('    <section class="hx'):html.index('    <section class=', html.index('    <section class="hx')+1)]
tail=lambda html:html[html.index('    <section class="mk"'):]
class IDs(HTMLParser):
    def __init__(self):super().__init__();self.ids=[]
    def handle_starttag(self,tag,attrs):
        for name,value in attrs:
            if name=='id':self.ids.append(value)
parser=IDs();parser.feed(after)
report={'changed_existing_files':changed,'hero_identical':hero(before)==hero(after),'following_sections_identical':tail(before)==tail(after),'duplicate_ids':[v for v in set(parser.ids) if parser.ids.count(v)>1],'old_section_removed':'sol-offer-2a' not in after,'new_section_count':after.count('class="home-marketing-example"'),'other_pages_identical':all(name not in changed for name in ['marketing.html','software.html','precios.html','automatizaciones.html','hablemos.html','iniciar-sesion.html']),'photo_bytes':(root/'assets/hero/campana-ropa-deportiva.webp').stat().st_size}
(out/'preservacion.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
assert report['hero_identical'] and report['following_sections_identical'] and report['other_pages_identical']
assert not report['duplicate_ids'] and report['new_section_count']==1
