from pathlib import Path
import hashlib, json, re, shutil

root = Path(__file__).resolve().parents[2]
out = Path(__file__).resolve().parent
archive = root / 'archive/2026-10-09-seccion-2-referencia'
archive.mkdir(parents=True, exist_ok=True)
files = ['index.html','css/home-offer-2a.css','css/directory-c-home.css','js/landing-motion.js','css/solutions-2a.css','css/solutions-new.css']
baseline = {str(p.relative_to(root)).replace('\\','/'): hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file() and p.parts[len(root.parts)] not in ['.git','archive','outputs','__pycache__']}
(out / 'baseline.json').write_text(json.dumps(baseline, indent=2), encoding='utf-8')
for name in files:
    target = archive / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / name, target)
html = (root / 'index.html').read_text(encoding='utf-8-sig')
start = html.index('    <section class="sol sol-offer-2a"')
end = html.index('    <section class="mk"', start)
html = html[:start] + (out / 'section.html').read_text(encoding='utf-8') + '\n' + html[end:]
for href in ['css/solutions-2a.css','css/solutions-new.css']:
    html = re.sub(r'<link rel="stylesheet" href="'+re.escape(href)+r'(?:\?[^\"]*)?">', '', html)
html = re.sub(r'^.*<script src="js/landing-motion.js[^\"]*" defer></script>\n', '', html, flags=re.M)
html = html.replace('css/home-offer-2a.css?v=20261009-c2','css/home-offer-2a.css?v=20261009-section2').replace('css/directory-c-home.css?v=20261009-c2','css/directory-c-home.css?v=20261009-section2')
(root / 'index.html').write_text(html, encoding='utf-8')
css = (root / 'css/directory-c-home.css').read_text(encoding='utf-8-sig')
start = css.index('  /* El servicio principal')
end = css.index('  #contenido > .mk', start)
css = css[:start] + css[end:]
css = re.sub(r'^.*#contenido > \.sol-offer-2a.*\n', '', css, flags=re.M)
css = re.sub(r'/\* En portátiles.*?@media.*?\{\s*\}\s*', '', css, flags=re.S)
(root / 'css/directory-c-home.css').write_text(css, encoding='utf-8')
shutil.copy2(Path('C:/Users/SEBAS/Documents/Codex/2026-10-05/want/outputs/seccion-2-marketing-v6/campana-ropa-deportiva.png'), root / 'assets/hero/campana-ropa-deportiva.png')
shutil.copy2(out / 'section.css', root / 'css/home-offer-2a.css')
print('Sección reemplazada; baseline y copia anterior guardados.')
