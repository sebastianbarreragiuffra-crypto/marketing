from pathlib import Path
from html.parser import HTMLParser
import json
from urllib.parse import urlsplit
from PIL import Image
root=Path(__file__).resolve().parents[2]
out=root/'outputs/redesign-20261008/qa'
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.links=[]; self.h1=0; self.robots=''
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='a' and 'href'in a:self.links.append(a['href'])
        if tag=='h1':self.h1+=1
        if tag=='meta' and a.get('name')=='robots':self.robots=a.get('content')
pages={}
for name in ['marketing','software','precios']:
    p=Page();p.feed((root/(name+'.html')).read_text(encoding='utf-8-sig'));errors=[]
    for href in p.links:
        u=urlsplit(href)
        if u.scheme or u.netloc:continue
        target=root/(u.path or name+'.html')
        if not target.exists():errors.append(href);continue
        if u.fragment and target.suffix=='.html':
            t=Page();t.feed(target.read_text(encoding='utf-8-sig'))
            if u.fragment not in t.ids:errors.append(href)
    pages[name]={'h1':p.h1,'duplicate_ids':len(p.ids)!=len(set(p.ids)),'broken_links':errors,'robots':p.robots}
    assert p.h1==1 and not errors and len(p.ids)==len(set(p.ids)) and 'noindex' in p.robots
screens={p.name:Image.open(p).size for p in out.glob('*.jpg')}
(out/'estructura.json').write_text(json.dumps({'pages':pages,'screenshots':screens},indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(pages,ensure_ascii=False))
