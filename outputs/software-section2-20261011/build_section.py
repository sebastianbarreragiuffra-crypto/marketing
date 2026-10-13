from pathlib import Path

def icon(name):
    return f'<svg class="sc-icon" aria-hidden="true"><use href="#{name}"/></svg>'

def avatar(name, size=64):
    return f'<img class="sc-avatar" src="assets/software-consultas/{name}.webp" width="{size}" height="{size}" alt="" loading="lazy" decoding="async">'

paths = {
 'sc-chat':'<path d="M21 11.5a9 9 0 0 1-9 9 10 10 0 0 1-4-.9L3 21l1.4-4.8A9 9 0 1 1 21 11.5Z"/><path d="M8 11h.01M12 11h.01M16 11h.01"/>',
 'sc-list':'<path d="M9 5h12M9 12h12M9 19h12"/><circle cx="3" cy="5" r="1.5"/><circle cx="3" cy="12" r="1.5"/><circle cx="3" cy="19" r="1.5"/>',
 'sc-users':'<circle cx="12" cy="6" r="3"/><path d="M6 21v-3a6 6 0 0 1 12 0v3ZM4 8a3 3 0 0 0 0 6M20 8a3 3 0 0 1 0 6M2 21v-2a5 5 0 0 1 2-4M22 21v-2a5 5 0 0 0-2-4"/>',
 'sc-phone':'<path d="m6 3 4 5-3 3c1.6 3.2 3.8 5.4 7 7l3-3 5 4c-1 4-5 4-9 2C7 18 3 13 2 8c-1-3 0-5 4-5Z"/>',
 'sc-clip':'<path d="m8 13 7-7a3 3 0 0 1 4 4L10 19a5 5 0 0 1-7-7L13 2m-7 12 8-8"/>',
 'sc-arrow':'<path d="M4 12h16m-6-6 6 6-6 6"/>',
 'sc-search':'<circle cx="10" cy="10" r="6"/><path d="m15 15 6 6"/>',
 'sc-light':'<path d="M9 18h6M10 21h4M8 14a7 7 0 1 1 8 0c-1 1-1 2-1 4H9c0-2 0-3-1-4ZM12 17v-6m-3-2 3 2 3-2"/>',
 'sc-bolt':'<path d="m14 2-9 12h7l-2 8 9-12h-7z"/>'
}
symbols='\n'.join(f'<symbol id="{key}" viewBox="0 0 24 24">{value}</symbol>' for key,value in paths.items())
benefits='\n'.join(f'<li><span class="sc-benefit-icon">{icon(svg)}</span><div><h3>{title}</h3><p>{copy}</p></div></li>' for svg,title,copy in [
 ('sc-chat','Conversaciones unificadas','Organiza las consultas de los canales habilitados en una misma bandeja.'),
 ('sc-list','Estados y prioridades','Identifica rápidamente qué necesita atención y qué está en seguimiento.'),
 ('sc-users','Todo el contexto del cliente','Consulta su historial, responsable y próximos pasos desde un mismo lugar.')])
queries=[]
for name,image,message,time,state,style,origin in [
 ('Cliente 01','cliente-01','Solicita llamada','10:24','Alta','high','Meta Ads'),
 ('Contacto 02','contacto-02','Solicita información','10:18','Sin respuesta','waiting','Meta Ads'),
 ('Cliente 03','cliente-03','Cotización enviada','09:42','Esperando al cliente','waiting','Google Ads'),
 ('Cliente 04',None,'Consulta por precios','Ayer','En seguimiento','follow','Instagram'),
 ('Cliente 05','ana','Información de productos','Ayer','Cerrada','closed','WhatsApp')]:
    profile=avatar(image,48 if image=='ana' else 64) if image else '<span class="sc-avatar sc-initials" aria-hidden="true">04</span>'
    stamp=f'<time datetime="{time}">{time}</time>' if ':' in time else '<span class="sc-query-time">Ayer</span>'
    queries.append(f'<li class="{"is-current" if name=="Cliente 01" else ""}">{profile}<div><div class="sc-query-title"><strong>{name}</strong>{stamp}</div><p>{message}</p><div class="sc-query-detail"><span class="sc-status sc-{style}">{state}</span><span class="sc-origin">Origen: {origin}</span></div></div></li>')
rail=''.join(f'<li class="{"is-current" if name=="Conversaciones" else ""}">{icon(svg)}{name}</li>' for name,svg in [('Conversaciones','sc-chat'),('Clientes','sc-users'),('Tareas','sw-check'),('Calendario','sw-clock'),('Reportes','sw-bars')])
tabs=''.join(f'<button type="button" role="tab" id="sc-tab-{key}" aria-controls="sc-panel-{key}" aria-selected="{str(index==0).lower()}" tabindex="{0 if index==0 else -1}">{label}</button>' for index,(key,label) in enumerate([('consultas','Consultas'),('conversacion','Conversación'),('ficha','Ficha')]))
outcomes=''.join(f'<li><span>{icon(svg)}</span><p><strong>{title}</strong>{copy}</p></li>' for svg,title,copy in [('sc-bolt','Más claridad','para tu equipo'),('sw-clock','Seguimiento organizado','para saber qué sigue'),('sc-users','Mejor coordinación','con tus clientes')])
new=f'''    <section class="sc-section" id="flujo-consultas" aria-labelledby="sw-flow-title">
      <div class="sc-shell">
        <svg class="sc-symbols" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">{symbols}</svg>
        <div class="sc-layout">
          <div class="sc-copy">
            <p class="sc-eyebrow">DE LA CONSULTA AL SEGUIMIENTO</p>
            <h2 id="sw-flow-title">Cada consulta,<br><span>con su contexto<br>y próximo paso.</span></h2>
            <p class="sc-lead">Una bandeja para organizar conversaciones, revisar lo pendiente y ayudar a tu equipo a dar seguimiento.</p>
            <ul class="sc-benefits">{benefits}</ul>
          </div>
          <figure class="sc-demo" aria-label="Bandeja GISBA ilustrativa" aria-describedby="sc-demo-note">
            <div class="sc-demo-heading"><p class="sc-annotation">Conoce el origen<br>de cada consulta.<svg viewBox="0 0 90 78" aria-hidden="true"><path d="M75 4C37 10 16 36 18 68m-7-8 7 10 7-9"/></svg></p><div class="sc-aligned">{icon('sc-light')}<p><strong>Tu equipo, siempre alineado.</strong><span>Toda la información en un solo lugar.</span></p></div></div>
            <div class="sc-window" data-consultas-demo>
              <aside class="sc-rail" aria-label="Menú ilustrativo de GISBA, sin acciones"><strong class="sc-wordmark">GISBA<span>.</span></strong><ul>{rail}<li>{icon('sc-list')}Configuración</li></ul></aside>
              <div class="sc-app">
                <div class="sc-app-bar"><div><strong class="sc-mobile-brand">GISBA</strong><strong class="sc-app-title">Conversaciones</strong></div><span class="sc-search" aria-label="Buscador ilustrativo, no interactivo">{icon('sc-search')}Buscar por nombre, canal o mensaje…</span><span class="sc-new" aria-label="Nueva consulta: control ilustrativo, no interactivo"><span aria-hidden="true">+</span> Nueva consulta</span><span class="sc-mobile-example">Ejemplo</span></div>
                <div class="sc-panels">
                  <div class="sc-panel sc-queries" id="sc-panel-consultas" role="region" aria-label="Consultas de ejemplo" tabindex="-1">
                    <div class="sc-query-filter" aria-label="Estados ilustrativos, sin filtros interactivos"><span class="is-current">Todas <b>5</b></span><span>Pendientes <b>2</b></span><span>En seguimiento <b>2</b></span></div>
                    <ul class="sc-query-list">{''.join(queries)}</ul>
                  </div>
                  <div class="sc-panel sc-conversation" id="sc-panel-conversacion" role="region" aria-label="Conversación de ejemplo" tabindex="-1">
                    <div class="sc-contact">{avatar('cliente-01')}<div><strong>Cliente 01</strong><span class="sc-status sc-follow">Solicita llamada</span><p class="sc-origin">Origen: Meta Ads</p></div><span class="sc-more" aria-hidden="true">···</span></div>
                    <ol class="sc-messages" aria-label="Historial de mensajes ficticios">
                      <li class="sc-message-in"><p>Hola, me gustaría una cotización para sus servicios de marketing digital.</p><time datetime="10:20">10:20</time></li>
                      <li class="sc-message-out"><span class="sc-message-author">Ana · Tu equipo</span><p>Te comparto la cotización que solicitaste.</p><time datetime="10:22">10:22</time><div class="sc-document"><span class="sc-pdf" aria-hidden="true">PDF</span><div><strong>Cotización.pdf</strong><small>Documento de ejemplo</small></div><button type="button" disabled title="Documento ficticio, no descargable">Ver documento</button></div></li>
                      <li class="sc-message-in"><p>Gracias. ¿Me pueden llamar hoy por la tarde?</p><time datetime="10:24">10:24</time></li>
                    </ol>
                    <div class="sc-composer" aria-label="Campo de respuesta ilustrativo, no envía mensajes">{icon('sc-clip')}<span>Escribe un mensaje…</span><button type="button" disabled aria-label="Enviar mensaje, deshabilitado en esta demostración">{icon('sc-arrow')}</button></div>
                  </div>
                  <div class="sc-panel sc-record" id="sc-panel-ficha" role="region" aria-label="Ficha del cliente de ejemplo" tabindex="-1">
                    <div class="sc-record-title"><strong>Ficha del cliente</strong><span>Actividad reciente</span></div>
                    <div class="sc-record-person">{avatar('cliente-01')}<div><strong>Cliente 01</strong><span class="sc-status sc-closed">Cliente existente</span><p>Empresa · Ecommerce</p></div></div>
                    <dl class="sc-facts"><div><dt>Etapa</dt><dd>Cotización enviada</dd></div><div><dt>Responsable</dt><dd>{avatar('ana',48)}Ana</dd></div><div><dt>Última respuesta del equipo</dt><dd>Ana · 10:22</dd></div><div><dt>Historial</dt><dd>1 compra anterior</dd></div><div><dt>Prioridad</dt><dd class="sc-priority">Alta · Marcada por el equipo</dd></div></dl>
                    <div class="sc-next"><strong>Próximo paso</strong><div><span class="sc-next-icon">{icon('sc-phone')}</span><p><b>Llamar hoy · 16:00</b><span>Hora por confirmar</span><span>Responsable: Ana</span></p></div></div>
                  </div>
                </div>
                <div class="sc-mobile-tabs" role="tablist" aria-label="Vistas de la bandeja GISBA">{tabs}</div>
              </div>
            </div>
            <figcaption class="sc-caption" id="sc-demo-note">Vista ilustrativa · Datos de ejemplo · Funciones sujetas a confirmación.<span>Los orígenes y perfiles son ficticios; no acreditan conexiones disponibles.</span></figcaption>
          </figure>
          <div class="sc-responsibility"><p>Órbita gestiona las campañas. Tu equipo atiende las consultas, salvo que se acuerde otro alcance.</p></div>
          <div class="sc-actions"><a class="sc-cta" href="hablemos.html#contacto">Agenda una reunión {icon('sc-arrow')}</a><a class="sc-secondary" href="https://gisba.cl/" target="_blank" rel="noopener noreferrer">Conoce más sobre <span>GISBA {icon('sc-arrow')}</span><span class="sc-sr-only"> (abre en otra pestaña)</span></a></div>
        </div>
        <ul class="sc-outcomes" aria-label="Beneficios del seguimiento organizado">{outcomes}</ul>
      </div>
    </section>

'''
p=Path('software.html'); text=p.read_text(encoding='utf-8')
start=text.index('    <section class="sw-flow"'); end=text.index('    <section class="gr-section"',start)
text=text[:start]+new+text[end:]
text=text.replace('  <link rel="stylesheet" href="css/software-flow.css">\n','')
text=text.replace('</head>','  <link rel="stylesheet" href="css/software-consultas.css?v=20261011-section2">\n  <script src="js/software-consultas.js?v=20261011-section2" defer></script>\n</head>',1)
p.write_text(text,encoding='utf-8')
print('Section 2 replaced; remaining sections preserved.')
