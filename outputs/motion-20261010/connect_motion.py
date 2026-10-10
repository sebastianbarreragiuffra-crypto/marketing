from pathlib import Path
import re

root = Path(__file__).resolve().parents[2]
for name in ['index.html', 'marketing.html', 'software.html', 'precios.html', 'hablemos.html', 'iniciar-sesion.html']:
    path = root / name
    html = path.read_text(encoding='utf-8')
    html = re.sub(r'^[ \t]*<(?:link[^>]*href="css/experience-motion\.css[^>]*|script[^>]*src="js/experience-motion\.js[^>]*)>(?:</script>)?\s*\n', '', html, flags=re.M)
    html = html.replace('</head>', '  <link rel="stylesheet" href="css/experience-motion.css?v=20261010-m1">\n  <script src="js/experience-motion.js?v=20261010-m1" defer></script>\n</head>')
    html = re.sub(r'js/main\.js\?v=[^"\s]+', 'js/main.js?v=20261010-m1', html)
    html = re.sub(r'css/directory-c-shared\.css\?v=[^"\s]+', 'css/directory-c-shared.css?v=20261010-m1', html)
    html = re.sub(r'js/hero-carousel\.js\?v=[^"\s]+', 'js/hero-carousel.js?v=20261010-m1', html)
    html = re.sub(r'css/landing-motion\.css\?v=[^"\s]+', 'css/landing-motion.css?v=20261010-m1', html)
    html = re.sub(r'css/faq-new\.css\?v=[^"\s]+', 'css/faq-new.css?v=20261010-m1', html)
    path.write_text(html, encoding='utf-8')

# Remove the older FAQ fade; disclosures have one shared motion owner now.
path = root / 'css/faq-new.css'
css = path.read_text(encoding='utf-8')
css = re.sub(r'@media\(prefers-reduced-motion:no-preference\)\{\.fq details\[open\] \.fq-a\{animation:fq-in[^\n]+\n', '', css)
path.write_text(css, encoding='utf-8')
