from pathlib import Path
import re, shutil
root=Path(__file__).resolve().parents[2]
backup=root/'archive/2026-10-08-jerarquia-tres-paginas'
backup.mkdir(parents=True,exist_ok=True)
for name in ['marketing.html','software.html','precios.html','js/marketing-services.js']:
    dest=backup/name; dest.parent.mkdir(parents=True,exist_ok=True)
    if not dest.exists(): shutil.copy2(root/name,dest)
for name in ['marketing.html','software.html','precios.html']:
    p=root/name; s=p.read_text(encoding='utf-8')
    s=s.replace('</head>','  <link rel="stylesheet" href="css/compra-clara-20261008.css?v=1">\n</head>')
    s=s.replace('Servicio por proyecto · GISBA no incluido','Servicio por proyecto · alcance por acordar')
    s=s.replace('Se cotiza por proyecto; no incluye GISBA.','Se cotiza por proyecto; la inclusión de GISBA no se extiende automáticamente a Web.')
    if name=='marketing.html':
        s=s.replace('para organizar consultas y seguimiento.','para revisar avances y organizar consultas y seguimiento.')
        start=s.index('    <section class="marketing-services-showcase"')
        end=s.index('    <section class="contact ',start)
        s=s[:start]+'''    <section class="marketing-services-showcase purchase-services" id="como-trabajamos" aria-labelledby="ms-title" data-ms-active="meta">
      <div class="purchase-shell">
        <header class="purchase-heading"><p class="purchase-kicker">GESTIÓN DE CAMPAÑAS</p><h2 id="ms-title">Un objetivo. Los canales que tu negocio necesita.</h2><p>Órbita prepara y ajusta tus anuncios. Definimos contigo el alcance; tu equipo atiende las consultas.</p></header>
        <div class="purchase-campaign">
          <div class="purchase-explanation">
            <div class="purchase-tabs" role="tablist" aria-label="Canales publicitarios">
              <button id="ms-tab-meta" role="tab" aria-selected="true" aria-controls="ms-service-panel" tabindex="0" data-ms-service="meta">Meta Ads</button>
              <button id="ms-tab-google" role="tab" aria-selected="false" aria-controls="ms-service-panel" tabindex="-1" data-ms-service="google">Google Ads</button>
              <button id="ms-tab-tiktok" role="tab" aria-selected="false" aria-controls="ms-service-panel" tabindex="-1" data-ms-service="tiktok">TikTok Ads</button>
            </div>
            <h3 data-channel-title>Que te descubran en Facebook e Instagram.</h3>
            <p data-channel-copy>Campañas para presentar lo que vendes a personas que podrían interesarse.</p>
            <h4>Qué gestiona Órbita</h4><ul class="purchase-work" data-channel-work><li>Audiencias según tu objetivo.</li><li>Anuncios y creatividad según el alcance.</li><li>Revisión de resultados y ajustes.</li></ul>
            <p class="purchase-terms">GISBA para 1 usuario contemplado con Marketing. Usuarios adicionales y presupuesto publicitario aparte; condiciones por confirmar.</p>
            <a class="purchase-primary" href="#contacto">Agenda una reunión <span aria-hidden="true">→</span></a>
            <a class="purchase-secondary" href="precios.html">Ver modalidades e inversión en Precios</a>
          </div>
          <figure class="purchase-example" id="ms-service-panel" role="tabpanel" aria-labelledby="ms-tab-meta" tabindex="0">
            <p class="purchase-kicker">UN ANUNCIO, UN OBJETIVO</p>
            <img data-channel-image src="assets/hero/pricing-meta-ad.webp" width="546" height="432" alt="Anuncio ilustrativo de Meta de la marca ficticia Paso Norte." loading="lazy">
            <figcaption data-channel-caption>Ejemplo ilustrativo · Marca ficticia · No representa resultados reales.</figcaption>
            <div class="purchase-example-note"><strong>Después del anuncio, sigue la gestión.</strong><p>Revisamos avances y acordamos qué ajustar. Tu equipo organiza la atención y el seguimiento con apoyo de GISBA.</p></div>
          </figure>
        </div>
        <div class="purchase-projects">
          <article><p class="purchase-kicker">POR PROYECTO</p><h3>Diseño y desarrollo Web</h3><p>Diseñamos y construimos tu sitio según el alcance acordado. Hosting, dominio y mantenimiento por definir; GISBA no se incluye automáticamente.</p><a href="#contacto">Consultar por un sitio web →</a></article>
          <article><p class="purchase-kicker">CAPACIDAD ADICIONAL</p><h3>Automatizaciones a medida</h3><p>Revisamos el proceso que necesitas resolver. Bot de WhatsApp, conexiones y costos según propuesta; disponibilidad por confirmar.</p><a href="#contacto">Conversar sobre tu proceso →</a></article>
        </div>
        <p class="purchase-independent">¿Ya tienes agencia o equipo interno? <a href="software.html">Consulta por GISBA independiente.</a></p>
        <p class="ms-selection-status" role="status" aria-live="polite"></p>
      </div>
    </section>

'''+s[end:]
    if name=='software.html':
        s=s.replace('GISBA contempla un usuario incluido al contratar el servicio de marketing con Órbita. También puedes consultar por GISBA independiente para tu agencia o equipo interno.','Con Marketing: GISBA para 1 usuario. ¿Ya tienes agencia o equipo interno? Puedes consultar por GISBA independiente.')
        s=s.replace('<details class="cf-record-details" data-mobile-details open>','<details class="cf-record-details">')
        s=s.replace('<summary>Ver ficha del cliente</summary>','<summary>Ver ficha y prioridad del cliente</summary>')
        s=s.replace('<span>Enviada por Ana · 10:20</span>','<span>Documento de ejemplo</span>')
        s=s.replace('Mockup conceptual · Datos de ejemplo · Perfiles ficticios','Vista propuesta · Funciones por confirmar · Datos y perfiles ficticios')
        s=s.replace('<div class="cf-list-head"><h4 id="cf-list-title">Consultas</h4><p>2 por responder</p></div>','<details class="purchase-other-queries"><summary id="cf-list-title">Ver otras consultas de ejemplo</summary>')
        s=s.replace('</ul>\n              </aside>\n              <details class="cf-list-mobile">','</ul></details>\n              </aside>\n              <details class="cf-list-mobile">')
        match=re.search(r'              <article class="gr-kpi gr-qualified">.*?</article>',s,re.S)
        s=s[:match.start()]+s[match.end():]
        pos=s.index('            <div class="gr-panels">')
        detail='''            <details class="purchase-quality"><summary>Ver calidad de las solicitudes y definiciones</summary><div><p><strong>24 de 42 formularios aptos para cotizar</strong>, según la evaluación del equipo. Función por confirmar.</p><p>Costo por formulario apto: $8.435 CLP ($202.440 ÷ 24). Costo promedio: $4.820 CLP ($202.440 ÷ 42).</p><p>Los 42 son formularios recibidos en el ejemplo, no personas únicas ni ventas. El gasto corresponde solo a anuncios. Las variaciones comparan la semana anterior.</p></div></details>
'''
        s=s[:pos]+detail+s[pos:]
    if name=='precios.html':
        s=s.replace('<span class="pg-recommended">Recomendado</span>','')
        s=re.sub(r'            <dl class="offer-mode-includes">.*?</dl>\n','',s,flags=re.S)
        s=s.replace('Para negocios que contemplan ambos canales. Gestión según alcance y GISBA para 1 usuario; inversión publicitaria y usuarios adicionales aparte.','Para coordinar búsqueda y redes. Alcance y contratación de la combinación por confirmar.')
        s=s.replace('<p>Usuarios adicionales: <span>$25.000 por usuario/mes</span></p>','<p>Usuarios adicionales con costo extra · <a href="#mensualidad">Ver desglose mensual</a></p>')
        # Keep each advertisement as optional evidence, after the cost information.
        s=re.sub(r'            <figure class="pr-example">(.*?)</figure>',r'            <details class="purchase-ad-detail"><summary>Ver anuncio de ejemplo</summary><figure class="pr-example">\1</figure></details>',s,flags=re.S)
    p.write_text(s,encoding='utf-8')
