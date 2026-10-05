# Marketing · revisión B independiente

2026-10-04. Modo: **INDEPENDENT REVIEW**. Revisor separado `/root/marketing_2a_b`. Primera lectura realizada sin abrir propuestas, archivos ni conclusiones de A. Este resultado todavía no es 2A FINAL.

## Contexto y autorización

Alcance PAGE: solo tres bloques de contenido, **hero → selector dinámico Meta Ads / Google Ads / Desarrollo Web → Contáctanos**. Quitar las secciones independientes de lista de servicios, portal y precio secundario es una petición expresa ya autorizada; no corresponde volver a consultar por ese recorte. Navbar/footer compartidos quedan fuera del conteo. El encargo solicita más CTA para cotizar/contactar, no cifras CTR.

Leídos: AGENTS.md, SITE_PAGES_BRIEF.md v1.0, MARKETING_THREE_SECTIONS_2A.md v2.1, PROJECT_MEMORY.md, WEBMASTER_CONTEXT.md, WEBMASTER_DECISIONS.md, .webmaster/WEBMASTER_SHARED_RULES.md, .webmaster/directorio-b/CHALLENGE_PROTOCOL.md, .webmaster/2A_PROTOCOL.md y .webmaster/methods/ORIGINALITY_AND_ANTI_CONVERGENCE_REVIEW.md. La lectura inicial encontró el anterior MARKETING_TWO_SECTIONS_2A.md v2.0; posteriormente se leyó la versión corregida y renombrada v2.1, que registra USER APPROVED para los tres bloques. Este es el contrato vigente.

Inspección propia: marketing.html, css/marketing-hero.css, css/marketing-services.css, js/marketing-services.js y js/main.js; renders baseline 390/1440/1920, selector Meta móvil y estados Google/Web a 1440. No se modifica producto ni se publica. Los renders existentes se usan como evidencia de V0, no prueban la propuesta futura.

## Independent Pass

**Lectura propia: el recorte a tres bloques es defendible**. V0 repite Meta/Google en la lista posterior y repite precios con una segunda oferta ilustrativa de $690.000. Conservar un contacto visible como tercer bloque da un destino claro a todas las acciones. La simplificación debe retirar esas composiciones completas y mover únicamente las aclaraciones comerciales necesarias al selector, sin recrearlas como nuevas subsecciones extensas.

El hero aprobado ya tiene presencia y dos recorridos claros: Hablemos y Cómo trabajamos. Conservar su texto, portátil, órbita, canales e identidad. La mejora necesaria está en el recorrido después de elegir servicio, no en añadir otra decoración.

A 1440, V0 muestra el selector en tres columnas reconocibles. A 1920, el contenido queda centrado y el selector usa un máximo útil de 1440 px; conservar esta proporción. El hero también tiene límite de 1440 px. En móvil, el selector se apila introducción → pestañas → dashboard → tres tarjetas → cotizar. El render Meta móvil hace visible el problema: quien ya comprendió el servicio recorre toda la ilustración antes de llegar a una acción de cotizar. Un CTA contextual antes del dashboard resuelve ese caso sin retirar las vistas aprobadas.

## Hallazgos materiales y contrato para tres bloques

1. **Servicio seleccionado y solicitud deben coincidir.** Hoy `selectService()` cambia título, beneficios, panel y plan activo, pero el enlace `.ms-quote` es siempre “Cotizar proyecto” y el contacto es estático. Cada estado debe cambiar la etiqueta a “Cotizar Meta Ads”, “Cotizar Google Ads” o “Cotizar sitio web” y pasar ese servicio al bloque final. La selección por tarjeta y por pestaña debe generar el mismo estado. Hablemos genérico debe permitir una consulta general cuando el visitante aún no ha elegido un servicio; no asignarle Meta silenciosamente por ser la vista inicial.

2. **No transformar Desarrollo Web en mensualidad.** La tarjeta vigente muestra “$850.000 / mes”; el encabezado dice “Servicios mensuales, sin permanencia” para los tres. Esto contradice la compra por alcance documentada. Conservar el valor ilustrativo solo si queda marcado como ejemplo y por proyecto, sujeto a alcance. El encabezado común puede decir “Servicios y proyectos”; no anunciar permanencia contractual sin confirmación. Reportes mensuales y otros incluidos deben adaptarse al tipo de compra, evitando presentar mantenimiento mensual como parte del sitio por defecto.

3. **Mantener la separación económica junto a la cotización.** Eliminar el bloque “Gestión clara. Inversión separada.” es correcto por el encargo; conservar su significado cerca de planes/CTA: “La gestión de campañas y la inversión en anuncios se cotizan por separado. El sitio web se define por alcance.” La advertencia “Precios de ejemplo · no son tarifas comerciales” debe estar a la vista, legible, y no quedar reducida a una nota de 10 px bajo todos los planes.

4. **Retirar el portal como bloque, conservar su distinción brevemente.** La página no debe parecer una venta de dashboard porque la ilustración ocupa su centro. Una frase contextual basta: “El panel ilustra la coordinación con la agencia; la bandeja para atender compradores se ofrece por separado”, con enlace rastreable a Software. Automatizaciones mantiene su ruta propia si se necesita aclarar el canal mencionado en el hero. No añadir una cuarta sección ni prometer acceso/integraciones del mockup.

5. **Distribuir CTA por trabajo concreto.** Hero: contacto general y exploración. Selector: acción contextual inmediatamente después de la descripción/beneficios, y acción en el panel de planes para quienes comparan. Contacto final: preparar la consulta elegida. No convertir las tres tarjetas de selección en tres cotizaciones indistinguibles, ni sumar botones dentro de gráficos ilustrativos.

6. **El tercer bloque debe llamarse Contáctanos y reflejar el servicio elegido con honestidad.** Debe mostrar Meta/Google/Web según la acción de origen; una consulta general sigue disponible desde el hero. WhatsApp de ventas continúa pendiente; no inventar teléfono, correo, destinatario ni presentar “enviar” como una operación real. Es válido conservar el contacto actual y aclarar junto al botón desactivado que el canal aún no está configurado. No agregar formulario, CRM o modal para cumplir este encargo. Como alternativa opcional, una acción “Copiar solicitud” podría habilitar un paso local concreto, siempre rotulada como preparación sin envío; no es requisito ni bloqueo de B. Si se incorporase, debería usar feedback accesible y texto seleccionable cuando falla el portapapeles.

## Assumption Attack, buyer y realidad comercial

No hay evidencia de que menos bloques o más botones produzcan más ventas. Se defiende la dirección por la petición del usuario y por reducir duplicación identificable, no por una mejora medida. El comprador necesita saber qué gestiona la agencia, cuándo elegir Meta/Google/Web, cómo se cotiza y qué ocurre al pulsar contacto. Esas respuestas pueden coexistir en tres bloques; no requieren un FAQ o proceso nuevo.

El visual con ROAS, variaciones verdes y estados “Activa/Publicado” puede interpretarse como prueba. Los rótulos ilustrativos deben acompañar cada vista, preferiblemente también antes de las cifras, porque una nota al pie llega después de la impresión principal. Mantener las métricas ya aprobadas como ejemplo no autoriza agregar resultados, clientes, garantías, integraciones o CTR nuevos. No confundir el “CTR” del anuncio ficticio existente con el pedido de CTA del usuario.

## Search y originalidad

Search Gate heredado: REQUIRED. Se contrastaron las fuentes del brief el 2026-10-04: [Reflector](https://reflector.cl/), [Melmac](https://melmac.cl/) y [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). El benchmark confirma la reconocibilidad de servicios; no demuestra volumen, rankings ni una ventaja de tres bloques. Google centra la utilidad en resolver la necesidad y no prescribe longitud. Por ello conservar descripciones reales de Meta/Google/Web y metaetiquetas coherentes tiene más fundamento que mantener bloques repetidos por supuesta obligación SEO. No crear páginas finas nuevas por canal. C deberá verificar la presencia de contenido descriptivo útil en HTML y el comportamiento sin JS; el copy dinámico creado solo tras interacción no debe ser la única explicación de Google/Web.

Organic CTR hypothesis: NOT OBSERVED. Observed organic CTR: NOT AVAILABLE. CTA conversion: NOT AVAILABLE.

Originalidad: la identidad y el hero aprobados son preservables. El selector con dashboard, beneficios genéricos y precio puede intercambiarse con muchas agencias; la especificidad se gana al explicar campañas gestionadas para ecommerce, prueba de piezas/mensajes, intención de búsqueda y contratación por alcance. No exige otra composición ni copiar benchmarks. **Resultado provisional: KEEP — SPECIFIC AND DEFENSIBLE para la estructura de tres bloques, condicionado a esas aclaraciones; REFINE THROUGH C para legibilidad y ubicación de acciones**. Ninguna afirmación de originalidad legal o marca disponible.

## Contrafactual y premortem

| Alternativa | Lectura de B |
| --- | --- |
| V0 con seis bloques | Conserva aclaraciones, pero repite servicios/precios y contradice el recorte pedido. No se recomienda mantenerlo. |
| Tres bloques autorizados | Conserva elección, significado comercial y destino visible con menos repetición. Recomendado con las condiciones anteriores. |
| Contacto solo en diálogo/dentro del selector | Puede acortar el scroll, pero contradice el último bloque Contáctanos solicitado y oculta el destino. Descartado. |
| Propuesta concreta de A | Pendiente: no leída durante Independent Pass. Se evaluará con renders propios antes del acuerdo. |

Si la propuesta falla, causas plausibles: CTA genéricos pierden intención; copia sin destinatario se interpreta como envío; el precio Web parece mensual; el recorte elimina responsabilidad de la agencia; móvil conserva mucha ilustración antes de la primera cotización; cifras de muestra parecen resultados. Las correcciones de esta revisión atacan esas causas. No hace falta producir una “versión B” estética artificial.

## Criterios observables para el cruce con A

- Exactamente hero, selector y Contáctanos en `main`; navbar/footer compartidos.
- Los tres estados visuales aprobados permanecen completos; no se sustituyen por tarjetas genéricas.
- A 1440/1920, centro, proporciones y máximo útil 1440 px; a 390, acciones visibles antes del dashboard y sin desbordamiento. C verificará además 320/768/1024.
- Acciones específicas en hero/selector/contacto, con destino común visible y preservación exacta del servicio. Pestañas/planes no quedan desincronizados.
- Precios/cifras/interfaz marcados como ejemplos; Web por proyecto y campañas con inversión publicitaria separada.
- Menú móvil, anclas, teclado de pestañas y foco de llegada a contacto funcionan; no envío externo. Feedback de copia solo si se adopta esa alternativa opcional.
- El contacto conserva consulta general y selección Meta/Google/Web; ningún teléfono o destinatario inventado.
- Las aclaraciones sobrevivientes no crean un cuarto bloque ni un informe comercial extenso en la página.

**Resultado B de esta pasada: REFINAR la dirección autorizada de tres bloques.** Pendiente cruce con V1-A y evidencia de las tres vistas/responsive. No se declara consenso ni 2A FINAL hasta ese cruce.

## Challenge sobre V1-A y acuerdo cruzado — 2026-10-04

Tras cerrar la lectura independiente anterior, B leyó `mockups/marketing-2a-a-review.md`, `mockups/marketing-three-sections-v1-a.html`, `mockups/marketing-three-services.js`, `css/marketing-compact.css` y `js/marketing-contact.js`. Inspección visual propia de V1-A: Meta 1440/1920/390, Google 390, Web 1440/390, contacto 1440/390 y página completa 1440/390. La evidencia está en `preview-marketing-three-v1-a-*.png`. El Implementation Owner comunicó QA a seis tamaños sin errores/desbordamiento y con estados, teclado, intención y foco aprobados; B distingue esa evidencia recibida de su lectura propia del código y renders. Intentó abrir el navegador de revisión, pero no había superficies de navegador disponibles; no afirma una prueba de interacción propia que no realizó.

**V1-A resuelve materialmente los hallazgos iniciales.** El hero conserva la composición aprobada. Hay exactamente tres bloques y un destino Contáctanos visible. El CTA de introducción aparece antes del dashboard en móvil; las dos acciones contextuales cambian entre Meta/Google/“Cotizar sitio web”. Web muestra `/ proyecto`, desaparece “sin permanencia”, sus incluidos dejan de imponer reportes mensuales, y el panel diferencia gestión/inversión/alcance. El precio ficticio se advierte antes de las tarjetas. La nota de software conserva la separación entre agencia y bandeja sin recrear el portal como cuarta sección. La tarjeta final explica que WhatsApp todavía no está configurado, con botón desactivado y sin destinatario inventado. Estos son cambios observables; no son conversiones medidas.

### Objeción concreta de B

**Quitar “Consultar alcance”.** El enlace extra está directamente debajo de “Cotizar Google Ads” o “Cotizar sitio web”, pero `marketing-contact.js` trata cualquier enlace sin `data-ms-quote` como general. Su etiqueta sugiere preguntar por el alcance de la oferta que se acaba de comparar; su comportamiento borra esa intención. Además, abre el mismo bloque sin contenido, paso o acción distinta. El hero/nav Hablemos y el propio contacto ya atienden una consulta general. Quitar este extra simplifica el panel y evita el cambio de intención inesperado; el botón nuevo bajo beneficios más la cotización contextual existente cumplen el pedido de más CTA. No agregar una nueva salida, modal o formulario como sustituto.

B transmitió esta objeción a A antes de recibir su argumento sobre el extra. A también la identificó al revisar V1-A. A contempló pasar el servicio a un enlace “Consultar alcance de [servicio]”; B prefiere retirarlo porque no aporta un recorrido adicional. **A aceptó retirarlo.** Esto documenta la objeción y resolución, no un consenso anticipado.

### Decisiones preservadas y ajustes pequeños

- **“Ver servicios” queda como etiqueta secundaria del hero.** Describe el destino que ahora es un selector de ofertas. “Cómo trabajamos” sugeriría un proceso que ya no se presenta como bloque. La composición, H1 y CTA Hablemos permanecen aprobados; es un ajuste de precisión del vínculo.
- **Hablemos queda general.** Código: los enlaces genéricos reinician solo la intención del contacto; los CTA con `data-ms-quote` pasan el servicio activo. Las opciones de contacto permiten corregir Meta/Google/Web y sincronizan el selector. No asignar Meta por estar visible al cargar. No hace falta añadir una cuarta opción u otro control para aprobar esta propuesta.
- **Legibilidad de notas: mínimo 12 px.** Los textos de inversión/alcance y precio en `marketing-compact.css` están a 11 px y son mucho menores que las cifras. A 1440 se pueden leer en la captura, pero constituyen información de decisión, no solo decoración. Aumentarlos a 12 px, preservando el panel y comprobando sus saltos, es refinamiento de C.
- **Ejemplos identificados antes de interpretarlos.** El caption ilustrativo sigue al pie del dashboard, después de ROAS/variaciones/estados. Añadir el rótulo correspondiente antes de métricas/estados —bajo el encabezado o al inicio del panel— preserva las tres vistas y reduce la posible lectura como resultados reales. Mantener también la aclaración inferior si resulta útil. A aceptó este ajuste.
- **Capturas completas limpias.** Los renders full muestran navbar/skip-link a mitad del documento tras estado de scroll/foco. Esto requiere recapturar desde arriba sin foco antes de presentar el artefacto; no demuestra desbordamiento ni un diseño de navbar roto. A y B lo derivan a C.

### Acuerdo y límites

**Resultado acordado A+B: REFINAR V1-A con la eliminación de “Consultar alcance”, “Ver servicios”, notas legibles y rótulo ilustrativo superior.** A confirmó por mensaje su aceptación de los cuatro puntos y no declaró otro desacuerdo material. El Implementation Owner integra/valida estos refinamientos sobre el mismo mockup; no hay razón para crear una composición B artificial. B no encontró una mejora material adicional que justifique alterar hero, tres vistas, contacto o arquitectura autorizada.

Originalidad después del cruce: **KEEP — SPECIFIC AND DEFENSIBLE**, con las correcciones comerciales acordadas y **REFINE THROUGH C** para sus detalles de ejecución. La elección del servicio y la modalidad de compra explican la estructura; no se importaron diseños privados, nuevos motivos o proof fabricado. La diferenciación se limita a lo que el proyecto puede sostener, sin declarar exclusividad o rendimiento.

Para cerrar, el render ajustado debe conservar las tres vistas, verificar 1440/1920 con máximo útil 1440 y móvil, y repetir únicamente las comprobaciones afectadas: desaparición del enlace redundante, nueva ubicación/legibilidad de notas y recorrido CTA → Contáctanos con foco e intención. El contacto externo seguirá desactivado hasta el número real. **La dirección queda acordada; verificación del render ajustado pendiente de C.** Organic CTR/CTA conversion permanecen NOT OBSERVED / NOT AVAILABLE. No se modificó producto ni se publicó durante esta revisión B.
