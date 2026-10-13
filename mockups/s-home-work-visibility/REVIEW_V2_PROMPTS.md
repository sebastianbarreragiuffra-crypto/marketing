# Sección 2 — coordinación agencia/cliente — V2

2026-10-11. Propuesta de imágenes; no implementación ni publicación. Se conserva V1. Generación y retoque con imagegen integrado.

## Brief y decisión

Inicio conserva la oferta de agencia del brief-orbita.mdc. Pregunta: ¿cómo delego la publicidad y sigo participando cuando corresponde?

V1 repetía información/trabajo/pendientes del hero de Software y contenía gráficos de relleno. V2 muestra una sola situación de coordinación: equipo prepara una propuesta, cliente la revisa y ambos acuerdan el siguiente paso. Los responsables de Órbita mantienen el control de los ajustes.

Alternativas SAME_AGENT: mantener dashboard simplificado (repite Software); proceso genérico sin muestra de coordinación (no explica el acceso del cliente); propuesta compartida y revisión humana (elegida). No se afirma superioridad comercial ni conversión observada. Se preservan un usuario incluido, costo adicional de usuarios extra e inversión publicitaria aparte.

## Fuente

Fuente primaria consultada en navegador el 2026-10-11: https://www.gisba.cl/#experiencia-cliente, pestaña Acciones. El sitio público representa propuestas para revisión, aprobaciones y solicitudes de cambios, responsables y piezas pendientes. Es una demostración pública, no una prueba del producto contratado ni de permisos de clientes de Órbita.

La captura pública fue referencia funcional para imagegen junto a la imagen antigua del usuario. No se copian nombres, cifras, fechas, aumentos de inversión o resultados del ejemplo público. El diseño adapta la representación a la marca Órbita y por eso se rotula como recreación ilustrativa basada en GISBA, no captura oficial.

## Diferencias frente al resto del sitio

- Inicio V2: relación entre agencia y cliente en una propuesta puntual; sin tablero de métricas.
- Marketing local: escena de personas trabajando con piezas; no se replica esa foto ni sus anuncios.
- Software local: conserva portal amplio y reportes; no se modifica ni se reproduce el dashboard completo aquí.
- Precios: no se copian planes, cifras ni ejemplos publicitarios.
- Bot: no aparece en esta sección y continúa siendo un add-on previsto separado.

## Verificación y límites

- Inspeccionados originales generados y exportaciones proporcionales. Escritorio1440 y móvil390 de ancho verificados por export_v2.py. Originales preservados.
- Móvil reordena la escena, conserva funciones/responsables/condiciones y abrevia párrafos explicativos de agencia; se corrigió un primer render con márgenes demasiado grandes.
- Botones del portal son representaciones estáticas. No se probó interacción del producto ni envío, aprobación, integración o automatización reales.
- Contraste numérico, reflow320/360, prototipo, rendimiento y prueba con compradores quedan pendientes de implementación o validación futura. La imagen no prueba responsive ni movimiento.
- No se tocaron HTML/CSS/JS/assets del sitio. Ya había cambios de otras tareas en Inicio, Marketing, Software y Precios; se preservaron.
- Lecciones aplicadas: S-001/S-004/S-005/S-012/S-013/S-014/S-015 y composición móvil. El aprendizaje de revisión entre páginas ya está cubierto por reglas de coherencia y no duplicación: NOTHING REUSABLE nuevo.

## Prompts exactos

### Escritorio

Use case: ui-mockup / image redesign. Create one high-fidelity desktop mockup of the SECOND SECTION of the Órbita Spanish marketing agency homepage, wide16:9 designed1440x810, section only with NO navbar. Redesign the old attached ivory section substantially rather than merely restyling it. Two recent images are supplied: the ivory Órbita mockup with a full GISBA dashboard is the OLD DESIGN TARGET; the purple-and-white public gisba.cl screenshot showing Acciones and proposal approval is the FUNCTIONAL REFERENCE only. Do not copy the full software dashboard, the laptop hero, the agency team photo or the ad cards used on other pages. This scene must look different from Software, Marketing and Precios.

PURPOSE: show how the human Órbita agency and its client coordinate a proposal while the agency creates/manages campaigns. GISBA is a supporting tool, not a separate equal offer. Use only the publicly demonstrated concept of agency proposals, client review, requesting changes, and agreeing the next step. Keep campaign adjustments under human agency control. No chatbot, leads inbox, automated ad edits, fabricated KPI, numeric results, prices or client identities. It is a generated illustrative adaptation, not a real GISBA product capture.

VISUAL DIRECTION: refined editorial section, warm ivory #f6f3eb, deep black #0b0d0b, greenblack panel #171d17, lime #c7f45b as accents/buttons and dark olive #48622e for readable accents on ivory. Manrope-like bold type and DM Sans-like body. Straight frontal flat website layout, clean vector-like line icons, crisp legible Spanish typography, no tilted widgets, laptop frame, decorative globe/orbit or floating cards. Purposeful whitespace, thin olive separators, around60px side margins. Completely different hierarchy from old left-title/right-full-dashboard layout: TOP is a horizontal editorial heading area, LOWER is a connected collaboration scene across the width.

TOP: small eyebrow "TRABAJAMOS EN EQUIPO". Large heading taking about60% width, exact text in2lines:
"Delegas las campañas."
"Seguimos coordinados."
Second line dark olive (never lime on ivory).
To the right of the heading a short body paragraph exactly:
"Órbita crea y gestiona tu publicidad. Con GISBA puedes revisar propuestas y coordinar el próximo paso."

MAIN SCENE (below the heading, about300–630px vertical, spans availablewidth): left agency panel about30% width, right a focused proposal view about65%, joined by ONE fine drawn directional arrow that means sharing a proposal, not an automatic integration. Above left panel a subtle step label "01 · NUESTRO EQUIPO". Left dark rounded panel has wordmark "ÓRBITA." as plain text, label "Creamos y gestionamos", then3 elegant short rows with simple line symbols: "Preparamos anuncios", "Gestionamos campañas", "Revisamos qué ajustar". Avoid decorative thumbnails, KPI, graphs or photos. Agency panel must be subordinate to the understandable proposal scene.

Above right card step label "02 · TU REVISIÓN". Right card is ONE large frontal white proposal-detail card with a restrained dark topbar: simple text "GISBA" and "Coordinación con tu agencia", plus an easily readable pill "Ejemplo ilustrativo". NO sidebar, tabs, metric cards, charts, reports or customer sales inbox. Focused task below: heading "Propuesta de tu agencia", short example task "Revisar nuevas piezas", olive status tag "Pendiente de tu revisión". One short agency note exactly "Te compartimos la propuesta para revisar juntos el siguiente paso." Responsible label "Preparada por el equipo de Órbita". Two real-looking preview buttons using the public site's action labels: lime "Aprobar propuesta" and outlined "Solicitar cambios". These controls are illustrative only. Keep the proposal text and buttons large and readable, no fake data or names. A simple document icon can accompany the proposal; do NOT put invented creative images inside it.

Below both panels a single modest full-width strip with outlined simple coordination icon and text "03 · Acordamos el siguiente paso", followed by body "Tu negocio aporta el contexto. Órbita gestiona los ajustes." This must clarify human responsibility, not promise that every campaign adjustment waits for a customer approval.

BOTTOM: left lime CTA rounded button exactly "Agenda una reunión". Near it one line of conditions exactly "1 usuario GISBA incluido · Usuarios adicionales con costo extra". A separate short note "Inversión publicitaria aparte". Beneath proposal or at bottom-right, readable disclosure on two short lines: "Recreación ilustrativa basada en GISBA" / "Acceso y funciones según alcance acordado". No more content. Ensure no garbled typography, cutoffs or labels overlapping. This is a premium visual proposal for review.

### Móvil

Use case: ui-mockup. Adapt the supplied redesigned Órbita SECOND HOMEPAGE SECTION into one genuine MOBILE mockup, logical width390px, high-resolution render about780x2200px, full section only, no navbar, phone frame, browser chrome, or existing hero. Same approved ivory/black/olive/lime brand and exact main message. Recompose into a compact vertical narrative, not a downscaled desktop layout. All body text and buttons must stay large enough to read at390wide. Use around20px logical margins, strong Manrope-like headline and DM Sans-like body.

Top small eyebrow "TRABAJAMOS EN EQUIPO". Heading exact "Delegas las campañas." then "Seguimos coordinados.", naturally wrapping into3or4shortlines. Second sentence dark olive. Short supporting paragraph exactly "Órbita crea y gestiona tu publicidad. Con GISBA puedes revisar propuestas y coordinar el próximo paso."

Step01 "NUESTRO EQUIPO": a compact dark horizontal full-width agency panel "ÓRBITA." with three short rows "Preparamos anuncios", "Gestionamos campañas", "Revisamos qué ajustar". REMOVE the secondary explanatory paragraphs from the desktop agency panel; the roles remain understandable with these labels. Use small elegant line icons, not large iconboxes, no metrics, photos or thumbnails. No repeated advertisement examples.

Step02 "TU REVISIÓN": one focused proposal card, not a software dashboard. Dark header wordmark "GISBA" and small clearly readable "Ejemplo ilustrativo". White interior includes "Propuesta de tu agencia", "Revisar nuevas piezas", olive status "Pendiente de tu revisión". Short note "Te compartimos la propuesta para revisar juntos el siguiente paso." Responsible line "Equipo de Órbita". Two full-width stacked preview buttons: lime "Aprobar propuesta", outlined "Solicitar cambios". Every text comfortably readable, no nested many boxes or giant blank margins. A restrained document icon is enough. These are illustrative controls, drawn from the publicly demonstrated agency-client proposal flow, not proof of a deployed function. No chat with purchasers or bot.

Step03 plain editorial line, not another big panel: "Acordamos el siguiente paso." followed by "Tu negocio aporta el contexto. Órbita gestiona los ajustes."
Main CTA below: full-width lime "Agenda una reunión" with clean drawnarrow.
Conditions below in three simple readable rows: "1 usuario GISBA incluido", "Usuarios adicionales con costo extra", "Inversión publicitaria aparte".
Final disclosure in two readable lines: "Recreación ilustrativa basada en GISBA" / "Acceso y funciones según alcance acordado".

Do not invent a logo or any numeric commercial results, prices, customer names, dates, channels/integrations, autoexecution, available chatbot or payment features. No dashboard sidebar, charts, KPIs, abstract orbits or testimonials. Copy all Spanish accurately. Keep a simple flat layout maximum2levels of surface nesting. Preserve design intent and distinguish it from the Software page. Extend the portrait height when needed for legibility rather than shrink text.

### Corrección móvil

Precisely improve the supplied MOBILE website mockup. Its current huge empty LEFT/RIGHT margins are a defect: the layout looks like a narrow strip centered inside a larger canvas. REDESIGN THE MOBILE WIDTH so the content fills the image. The result must be a real edge-to-edge390pxmobile page, not a presentation sheet around a page. Use a high-resolution portrait780pxwide canvas, approximately2100–2500pxheight as needed. Side margins ONLY32–40px on the780canvas (16–20px at390). Agency card, GISBA proposal card, mainCTA and conditions should span700–716px of the780width. The header/title and paragraph use the same left margin. No broad blank borders, no extra outer frame.

Keep every concept and all Spanish copy from the supplied image, including headline, numbered agency/client/nextstep roles, no metrics, example label, illustrative buttons, main CTA, conditions and disclosure. Allow the main heading to reflow according to the wider content rather than keeping narrow4linewrapping. All ordinary body text and conditions must be rendered at least28px on780width (logical14px), important labels32px (16px). Proposal header/body should be simple and readable. The document icon can shrink to give text space. Buttons span the full card width and stay stacked. Keep the brand ivory #f6f3eb, dark #0b0d0b and#171d17, olive #48622e, lime#c7f45b. Same exact content and visualintent, no added text, no invented functions, client results, dates or prices. Do not shrink the entire center column; expand and reflow it for actualmobile legibility. Generated illustrative mockup, not a functioning product capture.

## Móvil seleccionado tras inspección a 390 px

La primera adaptación y el retoque de márgenes aún reducían demasiado la tipografía al exportar. Se conservaron como borradores. La versión elegida es seccion-02-coordinacion-v2-mobile-legible-390.png: una composición vertical propia, con menos texto secundario dentro de las tarjetas y todas las categorías y condiciones preservadas. La extensión vertical corresponde a una sección inferior, no a un hero; no se afirma cumplimiento de accesibilidad ni validación responsive a partir de una imagen.

### Prompt móvil seleccionado

Create a NEW mobile web-section mockup image, ui-mockup, extremely TALL portrait aspect ratio1:2.9, requested780x2262px. This aspect ratio is mandatory: it is NOT a9:16poster or a landscape presentation. Full-bleed mobile website390CSSpixels, render at2x. All text is HTML-like clean typesetting and at least28pixels on780output (14at390); headline52–58pixels (26–29at390), not giant type. Body and buttons32pixels (16at390). Side padding40pixels (20at390). Use height for breathing room and readable text. Show this SECOND HOMEPAGE SECTION only, no preceding hero/nav, no phone frame. Manrope/DM Sans-like typography, warm ivory#f6f3eb background, dark#0b0d0b and#171d17 panels, readable olive#48622e accenttext, lime#c7f45b buttons. Frontal flat professional UI, no photos, ad creatives, metrics, sidebar, graphs, automation bot, prices or performance claims.

Exact top content:
small eyebrow "TRABAJAMOS EN EQUIPO"
heading "Delegas las campañas." then "Seguimos coordinados." with natural wrapping, second sentence olive.
supporting paragraph "Órbita crea y gestiona tu publicidad. Con GISBA puedes revisar propuestas y coordinar el próximo paso."

Below a compact agency work block:
label "01 · NUESTRO EQUIPO"
dark card wordmark "ÓRBITA."
three easy-to-read rows with small simple lineicons:
"Preparamos anuncios"
"Gestionamos campañas"
"Revisamos qué ajustar"
No secondary paragraphs or oversized iconcircles.

Then the large main visual:
label "02 · TU REVISIÓN"
One dark-bordered proposal card; header wordmark "GISBA" and "Ejemplo ilustrativo" as a clearly readable small badge on its own line ifneeded.
White interior shows a small document icon, title "Propuesta de tu agencia", task "Revisar nuevas piezas", olive tag "Pendiente de tu revisión".
Responsible line "Equipo de Órbita".
Two full-width tall stacked staticpreviewbuttons each at least88pxhigh on780output: lime "Aprobar propuesta", outlined "Solicitar cambios".
No additional paragraphs in the proposal card. This is a focused illustrative representation based on the proposal review actions publicly demonstrated on gisba.cl, not a literal product screenshot or proof of availability.

Next a simple textblock:
"03 · Acordamos el siguiente paso."
"Tu negocio aporta el contexto. Órbita gestiona los ajustes."

Then a lime CTA at least88pxhigh:
"Agenda una reunión" plus small drawnarrow.

Then three readable conditions stacked with simple smalllineicons:
"1 usuario GISBA incluido"
"Usuarios adicionales con costo extra"
"Inversión publicitaria aparte"

Final readable disclosure:
"Recreación ilustrativa basada en GISBA"
"Acceso y funciones según alcance acordado"

Make it comfortable to read on an actual390px phone, not a miniature of a desktopcomposition. Keep full-size content spanning700px of780width with actual typographic sizes above. Use the tall2.9ratio so buttons and conditions do not shrink. No wording additions, invented names, figures, capabilities or overlapping text. This is a design proposal image, no site implementation.


