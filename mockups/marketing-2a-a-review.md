# Directorio A · Marketing · lectura independiente y V1-A propuesta

2026-10-04. Entrada: `MARKETING_THREE_SECTIONS_2A.md` v2.1, READY FOR 2A / USER APPROVED para el recorte. A es un agente distinto de B; esta lectura no incorpora sus conclusiones. No se modificó código productivo ni se publicó. El encargo anterior de dos secciones queda sustituido por la instrucción explícita de **tres**: hero, bloque dinámico y Contáctanos.

## Evidencia y límites

Leídos AGENTS.md, SITE_PAGES_BRIEF.md v1.0, WEBMASTER_CONTEXT.md, WEBMASTER_DECISIONS.md, PROJECT_MEMORY.md y los protocolos locales 2A, Directorio A y Shared Rules. Inspeccionados marketing.html, marketing-services.js, main.js, home-contact.js y los estilos del hero/selector. Evidencia visual propia: preview-marketing-2a-baseline-390/1440/1920.png, preview-marketing-web-1440.png y preview-marketing-google-1440.png; los recortes existentes hero-390 y section2-390 permitieron leer los detalles móviles. Los baseline muestran seis secciones y un recorrido largo; sus alturas documentadas son 7.643/5.319/5.457 px. No se interpreta esa altura como evidencia de abandono o peor conversión.

El comprador es una tienda que evalúa campañas gestionadas o desarrollo web. Marketing conserva su ruta pública/indexable y Search Gate REQUIRED; no se crean páginas duplicadas por canal. Se mantienen Órbita y las tres vistas aprobadas, además del hero oscuro/lima, portátil y fondos claros del selector. No hay tarifas comerciales, datos propios de conversión ni resultados de clientes verificados.

## Decisión A

**REFINAR dentro del recorte ya autorizado.** Retirar íntegramente la lista de servicios, la sección del portal y el bloque secundario de precio. Conservar el contacto final como tercer bloque y migrar sus aclaraciones comerciales útiles a los planes. Navbar y footer siguen siendo navegación compartida. No pedir otra aprobación para este recorte.

Funciona y debe conservarse: el hero tiene una jerarquía clara y un visual distintivo; el selector hace reconocibles las tres compras; las vistas Meta, Google y Web ya ofrecen un cambio real de contenido. Los bloques eliminados repiten oferta y representación del portal. El segundo precio de $690.000 además introduce otra referencia ficticia que no ayuda a comparar los tres servicios actuales.

El riesgo concreto es borrar también información que evita una interpretación comercial equivocada. Hoy la inversión publicitaria separada vive en el bloque que se eliminará; Web aparece con `/ mes` bajo «Servicios mensuales, sin permanencia»; el CTA «Cotizar proyecto» es idéntico para las tres vistas y no transfiere la selección al contacto. Estos son problemas visibles en código/capturas, no hipótesis de CTR.

## Composición concreta V1-A

### 1. Hero

Preservar H1 «Marketing que no termina en el clic.», descripción aprobada, ilustración, canales y aclaración «Interfaz ilustrativa · Datos de ejemplo». Mantener los dos botones actuales: **Hablemos** lleva a `#contacto` con intención general; **Cómo trabajamos** lleva a `#como-trabajamos`. La navegación Hablemos hace lo mismo que el hero. No añadir una fila nueva de botones sobre el portátil ni cambiar la composición aprobada para aumentar el conteo.

Escritorio: mantener columna izquierda y visual a la derecha. A 1920, preservar el máximo útil de 1440; fondos y órbita pueden extenderse. Móvil: mantener texto → dos acciones → portátil → canales, sin barra flotante que tape la página.

### 2. Bloque dinámico Meta / Google / Web

Preservar las tres columnas a 1440 y la composición aprobada: beneficios a la izquierda, pestañas y representación en el centro, tarjetas de oferta a la derecha. No convertir el bloque en tres nuevas secciones ni eliminar las vistas de escritorio/móvil de Web.

Añadir **un botón contextual bajo los beneficios**, antes de la nota manuscrita: «Cotizar Meta Ads», «Cotizar Google Ads» o «Cotizar desarrollo web». Es el nuevo punto de acción para quien entiende la oferta sin necesitar leer el dashboard ilustrativo. El CTA actual de planes adopta exactamente la misma intención y label; deja de decir «Cotizar proyecto» para las campañas.

Añadir junto al CTA de planes, con jerarquía secundaria, **«Consultar alcance»**. Es la salida de quien todavía no eligió un servicio: lleva al contacto con intención general, no al plan que aparece activo por defecto. Estos dos botones nuevos dan un trabajo concreto a la petición de más CTA. No agregar además un botón de cotizar dentro de cada tarjeta: recargaría el panel y mezclaría selección y navegación. Las tarjetas siguen siendo controles de selección, nunca botones anidados.

Copy comercial visible, sin una nueva sección:

- Título del panel: «Opciones de servicio». Subtítulo: «Campañas gestionadas y desarrollo por proyecto.»
- Mantener los montos de ejemplo del diseño; Web muestra «$850.000 / proyecto», no `/ mes`. Cerca del título o montos, etiqueta «Precios de ejemplo · Solo maqueta». La nota inferior puede ampliar: «CLP · Valores ficticios, no son tarifas comerciales.»
- Junto a los CTA: «En Meta y Google, los honorarios no incluyen inversión publicitaria. El desarrollo web se cotiza según alcance.» Debe ser legible como texto normal, no un pie minúsculo.
- Retirar «sin permanencia» si no existe confirmación de esa condición contractual. No inferirla de una referencia de diseño.
- Conservar la gestión, revisión y optimización; en el estado Web, adaptar «Reportes mensuales» a «Alcance y entregables acordados». No universalizar condiciones mensuales a un proyecto.
- Una nota breve dentro del bloque reemplaza el trabajo explicativo del portal retirado: «La coordinación con la agencia puede apoyarse en un portal. La bandeja comercial para tu equipo es un producto independiente.» Enlazar la segunda frase a software.html. No recrear la sección del portal en miniatura.

El contenido útil que desaparece de la lista debe quedar en descripciones ya existentes, sin otro listado: Meta gestiona campañas, mensajes y creatividades; Google atiende intención de búsqueda y ajustes; Web conserva diseño a medida, SEO básico y velocidad. Los números y estados del dashboard siguen siendo ejemplos. No tratar sus anuncios, ROAS ni gráficas como proof comercial.

Móvil: mantener lectura en columna. El nuevo CTA bajo beneficios queda antes de la representación larga, por lo que la persona puede ir al contacto sin atravesar métricas/anuncios de muestra. Mantener pestañas y selección de planes sincronizadas. Los botones del panel usan ancho disponible, mínimo táctil de 44 px, sin dos etiquetas largas comprimidas en una fila. La nota comercial se coloca inmediatamente tras las acciones, antes de la franja de plataformas.

### 3. CTA final Contáctanos

Conservar `#contacto`, layout de texto más tarjeta y estado de maqueta. H2 fijo **«Contáctanos»**. Texto general: «Cuéntanos qué vende tu tienda y qué necesitas resolver. Definimos el servicio y el alcance antes de preparar una propuesta.»

Sustituir tags estáticos Meta/Google/Contenido por opciones **Meta Ads / Google Ads / Desarrollo Web** si se necesita permitir corregir la intención. Mostrar una línea corta «Tu consulta: Google Ads», por ejemplo, según el CTA utilizado. La selección activa, el resumen y el label del botón final deben coincidir. Hablemos/Consultar alcance muestran «Tu consulta: Orientación para mi tienda» sin seleccionar Meta por defecto. No cambiar el H2 fijo al alternar.

Conservar «WhatsApp de ventas» y su botón desactivado, con texto contextual «Cotizar Meta Ads», «Cotizar Google Ads», «Cotizar desarrollo web» o «Solicitar propuesta». Explicación visible: «Contacto de muestra. El número y el enlace real aún no están configurados.» El placeholder actual no se convierte en enlace ni destinatario. No incorporar modal, formulario, CRM o envío externo; la acción funcional de esta etapa es llegar al contacto con la intención preservada. La solicitud real sigue pendiente del número.

Escritorio: dos columnas centradas y suficiente contraste. Móvil: Contáctanos → explicación/selección → tarjeta. No añadir otra sección intermedia. Tras el contacto viene el footer compartido.

## Criterios para revisar el render y el recorrido

1. `main` tiene exactamente tres secciones principales. Desaparecen service-section, portal-section y price-section; no sobreviven anclas rotas. Hero y selector conservan sus referencias.
2. En 390/1440/1920 se leen CTA y notas comerciales sin desbordamiento; ancho útil máximo 1440. El nuevo botón de beneficios no invade título, ilustración o nota manuscrita. No se mide éxito por reducir una altura arbitraria.
3. Meta → Cotizar → contacto muestra Meta; Google → Cotizar → contacto muestra Google; Web → Cotizar → contacto muestra Web. Mismo resultado desde el CTA de intro y desde planes. Seleccionar desde tarjetas o teclado también actualiza el CTA.
4. Hablemos/Consultar alcance muestran intención general; volver a cotizar un servicio corrige la intención. Se puede corregir la elección en contacto. La navegación interna llega a un título visible y el foco no se pierde; comprobar menú móvil y teclas de pestañas.
5. Cifras y estados siguen rotulados como ilustrativos; montos ficticios se reconocen antes de cotizar. Inversión publicitaria separada y contratación Web por alcance son visibles.
6. Contacto sigue sin envío externo ni número inventado. No afirmar conversión completada al llegar a una tarjeta desactivada.
7. Conservar título/meta/H1 coherentes y enlaces rastreables a páginas existentes. La nota sobre agencia/software mantiene la distinción al retirar el portal.

## Tradeoffs y contraste pendiente

El panel de planes crecerá algo por las aclaraciones y el segundo botón, pero reemplaza un bloque entero de precio y protege la comprensión comercial. Dos CTA contextuales en momentos distintos repiten intención de forma deliberada: uno después de entender el servicio y otro después de comparar. «Consultar alcance» sirve al indeciso; si el render lo vuelve redundante o saturado, B debe cuestionarlo sobre el artefacto concreto.

La redacción «sin permanencia» y el mensual de Web son residuos de una plantilla, no decisiones comerciales autorizadas. Corregirlos aumenta especificidad. La diferenciación del sitio aún depende en parte de la ilustración; su contenido sigue bastante intercambiable con otra agencia. La dirección aprobada no justifica añadir claims, casos ni decoración para resolverlo. La especificidad defendible está en quién gestiona cada trabajo, qué servicio se está cotizando y las modalidades independientes.

No hay evidencia de que tres secciones o más botones mejoren CTR/conversión. Organic CTR hypothesis: NOT OBSERVED. Observed organic CTR: NOT AVAILABLE. CTA conversion: NOT AVAILABLE. El resultado verificable es menos duplicación y un recorrido de contacto consistente. Pendiente: inspección de V1-A y objeciones cruzadas con B antes de registrar 2A FINAL; calidad de ejecución y QA corresponden a C/Implementation Owner.

## Segunda pasada A · V1-A concreto y deliberación con B

Se revisó `mockups/marketing-three-sections-v1-a.html`, sus estilos `css/marketing-compact.css` y comportamiento `js/marketing-contact.js`, más los renders V1-A Meta 1440, Google 1920, Web 1440, contacto 390 y full 390. La lectura de `mockups/marketing-2a-b-review.md` ocurrió después de la propuesta independiente A. B respondió a objeciones concretas de A, y envió sus propias observaciones sobre renders separados: este acuerdo no procede de un cambio de rol del mismo agente.

**El artefacto respeta la arquitectura autorizada.** El hero conserva composición y oferta; el bloque dinámico conserva las tres representaciones; el último bloque se llama Contáctanos. La nueva acción bajo beneficios aparece antes de la ilustración en móvil y mantiene buen peso visual a 1440. Web ya tiene `/ proyecto`, incluidos específicos y CTA «Cotizar sitio web». La advertencia de precio de muestra aparece antes de los montos. La distinción del portal frente a la bandeja independiente quedó reducida a una frase enlazada, sin recrear una sección eliminada.

El render de contacto muestra elección, resumen «Tu consulta», botón final coherente y aclaración visible del canal pendiente. El código conserva intención desde ambos CTA de cotizar, permite corregirla en contacto y usa consulta general desde Hablemos. Eso satisface el recorrido local; no constituye una solicitud enviada. La QA funcional de seis tamaños comunicada por Implementation Owner es evidencia de ese propietario, no se presenta como una ejecución de pruebas propia de A.

### Objeción cruzada y corrección de la propuesta A

**A retira su recomendación inicial de «Consultar alcance».** En el render real, la acción queda inmediatamente debajo de «Cotizar Google Ads» o «Cotizar sitio web», pero su código cambia la intención a consulta general. La etiqueta no hace explícito ese cambio y no ofrece otra capacidad. Añade altura al panel que ya debe contener las condiciones comerciales. B identificó independientemente el mismo problema y recomendó quitarlo; A acepta por esa evidencia concreta.

Se conservan Hablemos en hero/navbar para quien necesita orientación, el CTA nuevo bajo beneficios y el CTA contextual del panel. Sigue habiendo más oportunidades de cotizar que V0, sin fabricar un segundo destino. No se sustituye el extra por otro botón ni se añade modal, formulario, copia o CRM. No tiene sentido optimizar solo el número de controles.

**A acepta «Ver servicios»** en el botón secundario del hero. El destino actual es una comparación de ofertas, por lo que describe el recorrido mejor que «Cómo trabajamos» tras retirar portal/proceso. Preserva la exploración ya aprobada. **A acepta «Cotizar sitio web»**: nombra con claridad la intención de Desarrollo Web y permanece coherente con la selección del contacto.

### Ajustes finales acordados A+B

1. Quitar `ms-scope-cta` / «Consultar alcance» y su espacio. Mantener CTA contextual tanto en beneficios como en planes.
2. Aumentar a **12 px como mínimo** la aclaración honorarios/inversión/alcance y las advertencias de precios. A 1440 el panel derecho es el elemento más alto; retirar el CTA redundante compensa en parte el crecimiento por legibilidad. No reducir el tamaño de esas aclaraciones para alinearlo artificialmente con el dashboard.
3. Mostrar **«Interfaz ilustrativa · Cifras de ejemplo» antes de las métricas de Meta/Google**, y el equivalente «Interfaz ilustrativa · Sitio y estados de ejemplo» antes de la representación Web. Puede conservarse el caption inferior. B había advertido que el pie llega después de la impresión del ROAS/variaciones/Publicado; A confirma que el aviso al comienzo mejora la lectura honesta sin cambiar vistas ni inventar prueba comercial.
4. Recapturar full-page desde el inicio y sin foco de navegación antes de presentar el resultado. Full390 muestra navbar/skip-link a mitad por el estado de scroll/foco de la captura. Es una condición de evidencia a corregir por C, no se afirma que exista una barra permanentemente rota en el layout.

La observación B sobre contenido útil sin JS es válida para C: Google/Web deben conservar resúmenes descriptivos en HTML; las tarjetas visibles ya contienen descripciones básicas. No se exige otra página, sección o bloque SEO por ese motivo. Search direction y rutas existentes permanecen congelados.

**Resultado A para el acuerdo 2A: REFINAR V1-A únicamente con los ajustes anteriores.** B confirmó el mismo acuerdo tras el intercambio; no hay desacuerdo material pendiente entre los revisores. No hace falta una versión B estética ni reabrir la aprobación del recorte. Implementation Owner debe aplicar y validar esos ajustes dentro de los tres bloques y preservar menú, teclado, anclas y contexto del contacto. No hay datos que permitan afirmar mejora CTR o conversión.
