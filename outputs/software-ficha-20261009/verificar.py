from pathlib import Path
from html.parser import HTMLParser
import hashlib, json, re

root = Path(__file__).resolve().parents[2]
output = Path(__file__).parent
archive = root / 'archive/2026-10-09-software-ficha'
baseline = json.loads((output/'baseline-archivos.json').read_text(encoding='utf-8'))
changed = [name for name, digest in baseline.items()
           if hashlib.sha256((root/name).read_bytes()).hexdigest() != digest]
expected = ['software.html','css/compra-clara-20261008.css','css/software-claridad-v1.css']
assert set(changed) == set(expected), changed
before = (archive/'software.html').read_bytes()
after = (root/'software.html').read_bytes()
assert before.replace(b'<details class="cf-record-details">',b'<details class="cf-record-details" open>') == after
old = (archive/'css/compra-clara-20261008.css').read_text(encoding='utf-8')
new = (root/'css/compra-clara-20261008.css').read_text(encoding='utf-8')
new = re.sub(r'/\* Software conversations:.*?(?=@media\(max-width:1000px\))', '', new, flags=re.S)
new = new.replace('cf-record-details>summary{display:list-item;min-height:44px;', 'cf-record-details>summary{display:list-item;')
assert new == old, 'Shared stylesheet has unexpected changes'
assert (root/'css/software-claridad-v1.css').read_text(encoding='utf-8') == (archive/'css/software-claridad-v1.css').read_text(encoding='utf-8').replace('.software-page #flujo-consultas .cf-record-details > summary { display: none; }\n','')

class IDs(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]
    def handle_starttag(self,tag,attributes):
        attrs=dict(attributes)
        if 'id' in attrs:self.ids.append(attrs['id'])
parser=IDs(); parser.feed(after.decode('utf-8'))
assert len(parser.ids)==len(set(parser.ids)), 'Duplicate IDs'
report = {
    'date':'2026-10-09','phase':'implementación local','review':'SAME_AGENT_CHALLENGE',
    'scope':'Software: ficha abierta y menor altura de la sección Conversaciones',
    'modified':expected+['site-manifest.json'],
    'preservation':'HTML idéntico salvo open; otras páginas y scripts idénticos. CSS compartido: sólo selectores de flujo-consultas.',
    'decision':{'A':'Ficha visible sin clic; mantiene el próximo paso y las responsabilidades.',
                'B':'Se descarta reducir toda la interfaz por escala o recorte. Se mueve la lista a la izquierda desde 1200 px.',
                'C':'Layout de tres columnas; texto de mensajes a 17 px, fotos originales; sin nuevos assets ni animaciones.',
                'Z':'Información comercial, datos ficticios y funciones pendientes conservados.'},
    'verified':['Apertura inicial a 320, 360, 390, 760, 1440, 1739 y 1920 px.',
                'Sin desbordamiento horizontal; imágenes cargadas.',
                'Enter y Espacio; foco visible; independencia y elección conservada al redimensionar.',
                'Mensajes a 17 px; control de ficha de al menos 44 px.',
                'noindex, textarea de solo lectura y botones deshabilitados conservados.',
                'HTML sin IDs duplicados; preservación exacta fuera del cambio.'],
    'heights':{'baseline_1440_810':934.296875,'final_1440_810':692.21875,'final_1739_782':692.21875},
    'pending':['Pruebas con usuarios, medición de conversión y rendimiento de campo no realizadas.',
               'Funciones reales, mensajería y contacto continúan pendientes; la interfaz es ilustrativa.'],
    'not_applicable':['Cambio de oferta, precios, navegación o arquitectura general: no solicitado.',
                      'Publicación, commit y push: no autorizados; no ejecutados.',
                      'Nueva imagen o movimiento: no incorporados.'],
    'git':'Cambios previos conservados. Versión local pendiente de commit/push; no sincronizada con otro PC.',
    'evidence':['antes-1440.jpg','despues-1440.jpg','despues-1920.jpg','despues-1739.jpg','despues-390-ficha.jpg','navegador.json']
}
(output/'entrega.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'preservation':'VERIFICADO','modified':changed,'duplicate_ids':False},ensure_ascii=False))
