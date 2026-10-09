from pathlib import Path
import hashlib, json, shutil

root = Path(__file__).resolve().parents[2]
output = Path(__file__).parent
archive = root / 'archive/2026-10-09-software-ficha'
archive.mkdir(parents=True, exist_ok=False)
files = ['software.html', 'css/compra-clara-20261008.css', 'css/software-claridad-v1.css']
manifest = json.loads((root / 'site-manifest.json').read_text(encoding='utf-8'))
hashes = {str(p.relative_to(root)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in [*root.glob('*.html'), *root.glob('css/*.css'), *root.glob('js/*.js')]}
(output / 'baseline-archivos.json').write_text(json.dumps(hashes, indent=2), encoding='utf-8')
for name in [*files, 'site-manifest.json']:
    destination = archive / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / name, destination)

page = root / 'software.html'
html = page.read_bytes().decode('utf-8')
assert html.count('<details class="cf-record-details">') == 1
html = html.replace('<details class="cf-record-details">', '<details class="cf-record-details" open>')
page.write_bytes(html.encode('utf-8'))

clarity = root / 'css/software-claridad-v1.css'
css = clarity.read_bytes().decode('utf-8')
# The visible native control is owned by the purchase stylesheet at every width.
css = css.replace('.software-page #flujo-consultas .cf-record-details > summary { display: none; }\r\n', '')
clarity.write_bytes(css.encode('utf-8'))

purchase = root / 'css/compra-clara-20261008.css'
css = purchase.read_bytes().decode('utf-8')
old = '.software-page #flujo-consultas .cf-record-details>summary{display:list-item;font-size:15px;font-weight:700;cursor:pointer;padding:12px 0}'
assert old in css
css = css.replace(old, '.software-page #flujo-consultas .cf-record-details>summary{display:list-item;min-height:44px;font-size:15px;font-weight:700;cursor:pointer;padding:12px 0}')
# Use the full-width contact strip on tablet; on desktop reclaim its vertical row.
anchor = '@media(max-width:1000px)'
assert css.count(anchor) == 1
desktop = '''/* Software conversations: use width instead of shrinking the interface.
   Tablet keeps the horizontal list; mobile keeps its native stacked layout. */
@media(min-width:1200px) {
  .software-page #flujo-consultas { padding:18px 0 16px; }
  .software-page #flujo-consultas .cf-section-head { margin-bottom:12px; }
  .software-page #flujo-consultas .cf-responsibility { margin-bottom:12px; }
  .software-page #flujo-consultas .cf-body {
    grid-template-columns:minmax(250px,.85fr) minmax(0,1.45fr) minmax(330px,1fr);
    align-items:stretch;padding:0;
  }
  .software-page #flujo-consultas .cf-list-desktop {
    grid-column:auto;border-bottom:0;padding:10px 14px;
  }
  .software-page #flujo-consultas .cf-list { grid-template-columns:minmax(0,1fr);gap:0; }
  .software-page #flujo-consultas .cf-client { padding-block:12px; }
  .software-page #flujo-consultas .cf-conversation,
  .software-page #flujo-consultas .cf-record { padding:10px 16px 12px; }
  .software-page #flujo-consultas .cf-bubble { font-size:17px;line-height:1.5; }
  .software-page #flujo-consultas .cf-compose-box textarea { height:auto;min-height:45px; }
  .software-page #flujo-consultas .cf-task { margin-top:12px; }
  .software-page #flujo-consultas .cf-task-main { grid-template-columns:34px minmax(0,1fr); }
  .software-page #flujo-consultas .cf-task-main > .cf-state { grid-column:2;justify-self:start; }
}
'''
css = css.replace(anchor, desktop.replace('\n','\r\n') + anchor)
purchase.write_bytes(css.encode('utf-8'))
print(json.dumps({'modified': files, 'archive':str(archive)}, ensure_ascii=False))
