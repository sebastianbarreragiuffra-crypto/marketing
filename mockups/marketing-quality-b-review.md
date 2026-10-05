# Marketing · Directorio B · revisión de calidad

2026-10-04 · **INDEPENDENT REVIEW** · revisor `/root/marketing_quality_b`.

## Independent Pass

Esta lectura se formó antes de recibir las conclusiones del nuevo revisor A. Leídos: AGENTS.md, Shared Rules, Challenge Protocol, Originality & Anti-Convergence Review, Repository Policy, Release Review Protocol, WEBMASTER_CONTEXT.md, PROJECT_MEMORY.md, WEBMASTER_DECISIONS.md y MARKETING_THREE_SECTIONS_2A.md. La deliberación anterior del brief es contexto histórico aprobado; no es la conclusión de esta ronda. Fuente vigente: marketing.html, css/marketing-hero.css, css/marketing-services.css, css/marketing-compact.css y scripts de servicios/contacto.

Alcance: valorar «¿es lo mejor que podemos hacer?», sin obligación de producir un rediseño. Conservar exactamente hero / bloque dinámico Meta-Google-Web / Contáctanos; navbar y footer compartidos. Conservar Órbita y referencias aprobadas. Máximo útil completo de 1440 px en escritorio ancho. Ignorar configuración de WhatsApp por instrucción del usuario; no solicitar número ni inventar contacto. No editar producto; persistencia limitada a este informe.

Evidencia visual examinada mediante view_image: preview-marketing-polish-public-hero-1440/1920/390.png, preview-marketing-polish-public-contact-1440/390.png, preview-marketing-three-public-meta/google/web-1440/1920/390.png y preview-marketing-three-public-full-1440.png. El full corresponde a evidencia histórica de la pasada de tres secciones; hero/cierre vigentes se juzgan por los renders polish y fuente. No ejecuté una nueva verificación de producción/interacciones; las pruebas previas son evidencia documental, no pruebas propias.

## Lectura inicial

**Mantener y refinar, sin rediseño total.** El hero actual tiene jerarquía clara, conserva una identidad reconocible y contiene su composición a 1440/1920. El cierre oscuro recoge el lenguaje del hero y presenta una consulta concreta con posibilidad de corregir servicio. El bloque intermedio contrasta los tres servicios y sus ejemplos en la referencia solicitada. No hay evidencia de que cambiar todo mejore comprensión o conversión.

La oportunidad principal es el orden de elección en móvil y la pertinencia del contenido. Una mayor cantidad de botones ya está resuelta; añadir otros no solucionaría los problemas observados.

## Hechos observados

- A 390 el bloque dinámico comienza por título, lead, tres beneficios y CTA de la oferta activa; las pestañas aparecen después. El CSS usa columna flex y ese orden procede del DOM. La elección que cambia la introducción está después de su resultado.
- Google tiene tres anuncios ilustrativos apilados a 390. Sus temas son software de gestión, automatización y soluciones digitales, no ejemplos de búsqueda de un producto de ecommerce. Esto se observa también en marketing.html.
- Desarrollo Web muestra el mismo sitio en escritorio y móvil, apilados a 390; el ejemplo ocupa una parte extensa del bloque antes de las opciones de servicio. Es una referencia completa aprobada, no un error de rendering por sí misma.
- El rótulo ilustrativo del hero usa 10 px en escritorio y 8 px a 390 según CSS. Las notas ilustrativas de servicios/precios ya usan 12 px mediante marketing-compact.css.
- Hay copy principal «Anuncios que destacan y generan resultados», «Sitios veloces, seguros y listos para escalar» y franja «Trabajamos con las principales plataformas / Y muchas más...». Las capacidades/plataformas completas no están verificadas en el contexto; no hay evidencia de resultados propios.
- Los precios y las métricas están rotulados como ejemplos, y la nota distingue coordinación con agencia de bandeja comercial independiente. Mantener estas aclaraciones.

## Supuestos débiles y buyer reality

1. **Supuesto:** la persona móvil advertirá las otras ofertas después de leer Meta. **Inferencia:** podría abandonar o cotizar antes de conocer que hay una elección; no hay datos de abandono. Ajuste defendible: mostrar las pestañas primero, porque el control define el contenido que sigue.
2. **Supuesto:** cualquier anuncio de ejemplo demuestra el servicio de Google igual de bien. **Inferencia:** software/automatización puede confundir la oferta de Órbita con el producto anunciado y no muestra la intención de compra del buyer ecommerce. Un ejemplo de búsqueda de producto es más pertinente, sin afirmar que sea caso real.
3. **Supuesto:** el rótulo pequeño del hero basta porque las cifras son parte del visual. **Inferencia:** 8 px dificulta apreciar que no son resultados reales. Subirlo a 12 px no requiere reconstruir el portátil.
4. **Supuesto:** más recorrido ilustrativo aporta más entendimiento móvil. **Inferencia:** las dos vistas completas y tres anuncios repiten estructura; posible compactación, pero no justifica retirar la referencia aprobada sin comprobar una alternativa concreta.
5. **Supuesto:** «seguros», «listos para escalar» y «muchas más» son beneficios demostrados. La evidencia disponible no respalda esos alcances. Conviene describir trabajo y alcance acordado, no ampliar capacidad o garantía.

## Prioridades propuestas

**B1 · ajuste de experiencia:** mover pestañas al comienzo del bloque dinámico en móvil. Conservar escritorio aprobado si no hay una necesidad visual verificable. El control debe anteceder al conjunto que modifica, con una etiqueta corta del tipo «Elige un servicio». Validar que al cambiar título/beneficios/visual/cotización sigan sincronizados y que foco/lectura resulten coherentes.

**B2 · pertinencia y originalidad:** cambiar el texto de los anuncios ilustrativos de Google por búsquedas y ofertas plausibles de una tienda, manteniendo su diseño y el rótulo de ejemplo. No inventar cliente, descuentos, disponibilidad, resultado o conexión real. La especificidad puede salir de intención/producto, no de agregar otra sección.

**B3 · ejecución C:** hacer el rótulo ilustrativo del hero legible (12 px mínimo propuesto, sobre fondo contrastante), revisar ubicación a 1440/1920/390 y no incrementar tamaño del hero ni del portátil. No exigir que cada microdato de una representación visual sea texto comercial legible.

**B4 · claridad factual:** conservar títulos aprobados y sustituir beneficios genéricos por trabajo que ya forma parte del servicio: audiencias/creatividad/revisión, búsquedas relevantes/anuncios/optimización, diseño adaptable/estructura/alcance por proyecto. Suavizar «generan resultados», «seguros y listos para escalar» y «Y muchas más...». Esto no autoriza eliminar los canales de la referencia ni redefinir oferta.

**B5 · explorar solo si hace falta:** comparar compactación de los ejemplos en móvil con actual. Sería razonable reducir espacio/repetición, sin esconder oferta/precio/CTA ni convertir la sección en un carrusel complejo. No es condición para aceptar B1–B4; no retirar una de las vistas Web o dos anuncios sin un render revisable y acuerdo con A.

## Contrafactual previo a A

| Opción | Valor defendible | Límite |
| --- | --- | --- |
| Mantener actual | Preserva referencias, jerarquía y trabajo ya validado | Mantiene elección tardía móvil, rótulo hero pequeño y ejemplos poco pertinentes |
| Refinamiento mínimo B1–B4 | Mejora orden/comprensión/factualidad dentro de tres secciones | Debe comprobarse en renders y recorrido; no acredita más conversiones |
| Compactación móvil adicional | Podría reducir repetición visual | Hipótesis todavía sin versión concreta; no convertirla en rediseño obligatorio |

La propuesta de A y el counterfactual definitivo se añadirán después de recibirlos. No hay consenso A+B todavía.

## Originalidad y premortem

**Resultado provisional: REFINE THROUGH C.** Órbita, órbita/lima, elección de servicio, creatividad y distinción agencia/software forman una composición defendible dentro de referencias del usuario. Los encabezados generales y anuncios de soluciones digitales son intercambiables; el ajuste de ejemplos/copy aporta relevancia sin novedad decorativa aleatoria. No hay base para REOPEN A/2A de toda la dirección ni afirmación de originalidad legal.

Si el refinamiento falla, las razones plausibles son: pestañas demasiado compactas para descubrirlas; cambio de texto sin suficiente relación entre servicio y entregable; compactar el visual ocultando lo aprobado; o añadir texto que vuelva a alargar el móvil. Validaciones pertinentes: 390/1440/1920, ancho útil y overflow, los tres estados, elección por pestaña/plan/contacto/teclado y llegada al contacto. No uso CTR, puntuaciones artificiales ni tasas de mejora como argumento.

## Estado

IndependentPass cerrado. Producto sin editar. Los problemas de ejecución se derivan a C; B desafía las decisiones y no declara delivery/producción listos.

## Challenge a la propuesta inicial de A

Después de cerrar y comunicar la lectura independiente, recibí y leí mockups/marketing-quality-a-review.md. A también propone REFINAR sin rediseño, con copy de trabajo, ejemplos Google de tiendas, selector antes de intro móvil y rótulo de 12 px. La coincidencia no sustituye inspección de V1 ni prueba de conversión.

- **Aceptación provisional A1/A2/A4/A5:** describen trabajo existente, corrigen pertinencia y orden sin cambiar oferta ni referencias. «Ajustamos anuncios e inversión» describe gestión de campaña; conservar separación honorarios/inversión en las notas.
- **Objeción A3:** «Canales del ecosistema digital» tiene poca utilidad por sí solo, y «Según el alcance del proyecto» junto a seis logos puede seguir sugiriendo disponibilidad de todos. Alternativa mínima: «Canales representados en esta vista» + «Ejemplo ilustrativo», conservando franja, iconos y nota agencia/bandeja. No es una exigencia estética; se juzga si evita interpretar ilustración como proof de capacidad.
- **Objeción de alcance en A1/Web:** «Estructura, títulos y contenido base definidos para tu sitio» puede sonar a producción de contenido incluida. La evidencia admite SEO básico y estructura, pero no precisa quién redacta. Alternativa mínima: «Estructura y títulos definidos para tu sitio», o verbo de revisión si no se promete una entrega de copy.
- **A6 / B5:** mantener ejemplos completos. B no exige compactación ni una variante artificial; simple reducción de espacios solo si la ejecución conserva legibilidad.

Objeciones comunicadas al coordinador y A mediante herramientas de colaboración del equipo.

### Respuesta cruzada recibida

A acepta retirar «contenido base» y V1 usará «Estructura y títulos definidos para tu sitio». Esto resuelve la objeción de un entregable no confirmado.

A y el coordinador cuestionan que mi alternativa para la franja describía demasiado la maqueta y aportaba poco al comprador. Acepto el contrapunto. A propone «Publicidad, web y atención de consultas» + «Canales ilustrativos». B no detecta una promesa residual material con la nota vigente de bandeja separada; conserva trabajos conocidos y no afirma conectores. Preferencia menor de B: «contenido» alinea mejor con logos sin icono Web y «Selección ilustrativa» distingue canales reales de una selección ejemplar. No constituye desacuerdo material ni justifica bloquear la versión de A.

La franja final de A adopta «Publicidad, contenido y atención de consultas / Selección ilustrativa», propuesta en la deliberación. Ambas objeciones de contenido quedaron resueltas.

## Challenge sobre V1-A concreto

Revisé marketing-quality-v1-a.html, marketing-quality-v1-a.css y marketing-quality-services.js, además de renders mediante view_image: preview-marketing-quality-v1-hero/meta/google/web/contact-390/1440/1920.png. Meta/Web390 tuvieron un overlay de la captura inicialmente; inspeccioné nuevamente las versiones limpias. No atribuyo ese artefacto de herramienta al diseño del producto.

**Observación visual:** móvil ahora ofrece elección antes de título, beneficios y CTA. La franja conserva logos y separa explícitamente lo ilustrativo; la nota de coordinación/bandeja está presente. El hero mantiene su H1, portátil, acciones y escala, con buyer en eyebrow y rótulo legible. A 1440 las frases nuevas caben sin invadir el visual o las opciones; a 1920 la composición permanece centrada y equilibrada. Google conserva tres anuncios con productos reconocibles, y Web conserva ambas vistas aprobadas. Contáctanos conserva la composición vigente y muestra la intención seleccionada.

No encontré una objeción material pendiente en V1. No exige nuevos entregables, condiciones comerciales, pricing real, integraciones o garantías. «Rendimiento y móvil» describe cuidado de carga/navegación y evita seguridad/escalabilidad no acreditadas. Las cifras siguen siendo ejemplos; no se usan para probar la calidad de la agencia.

### Counterfactual definitivo

| Opción | Comparación sobre evidencia | Decisión B |
| --- | --- | --- |
| Mantener V0 íntegro | Conserva un visual defendible, pero control móvil sigue después de resultado y Google demuestra software/automatización ajenos al ejemplo de tienda | Inferior a V1 por esas fricciones observables; no implica menor conversión medida |
| Adoptar V1-A revisado | Corrige orden y pertinencia; nombra comprador; aclara trabajo; hace legible lo ilustrativo; conserva composición, tres vistas y precios de muestra | **MANTENER A** |
| Alternativa mínima: solo selector + caption12px | Resuelve dos problemas de ejecución, pero deja anuncios menos pertinentes, promesas genéricas y franja abierta | Viable si se limitara alcance, sin ventaja defendible frente a V1 con copy ya revisado |
| Compactar o reemplazar visuales móviles | Podría reducir recorrido, pero no tiene evidencia de beneficio y sacrifica vistas aprobadas | Descartar como requisito de esta ronda |

## Resultado final de B

**MANTENER A — V1-A acordado tras challenge; 2A puede sintetizar REFINAR.** No hay desacuerdo material pendiente. La secuencia independiente, las objeciones y las respuestas están registradas; el resultado no fue consenso preasumido. La propuesta no abre una nueva dirección material: mantiene buyer, oferta, identidad, referencias, estructura y conversión del brief aprobado. Es refinamiento de contenido y ejecución.

**Originalidad final: KEEP — SPECIFIC AND DEFENSIBLE para la dirección; REFINE THROUGH C para integrar V1.** La especificidad procede de ecommerce, el trabajo gestionado y ejemplos de productos, con el lenguaje visual Órbita aprobado. No exige decoraciones nuevas ni elimina referencias para parecer único. No afirmo originalidad legal ni superioridad comercial demostrada.

C debe verificar implementación/recorrido, especialmente selector antes de intro también en DOM/tablet, los tres estados y CTAs, lectura del caption, máximo útil completo y no desbordamiento. B hizo inspección visual y de source; no ejecutó regresión funcional propia ni producción nueva. Esta aceptación del mockup no concede publicación. Producto sin editar por B; persistencia solo en este informe. NOTHING REUSABLE: se aplicó el método vigente, sin writeback canónico.

## Reapertura por evidencia concurrente del usuario

Posteriormente el coordinador informó de un ajuste de otra tarea del mismo repositorio: usuario pidió que elegir una opción inferior en móvil desplazara la página y luego precisó «un poco más bajo, mostrando la imagen». Fuente actual inspeccionada: js/marketing-services.js mueve foco a la pestaña seleccionada y scroll a .ms-tabs cuando viewport <=760; css/marketing-services.css tiene scroll-margin-top104 para pestañas. El control actual estaba justo antes del dashboard. La tarea concurrente cerró Marketing en ab11dda según coordinación; B no editó sus cambios ni envió mensajes a chats de la app.

**Nuevo riesgo observable:** V1 pone tabs antes de intro. Tras integrar sin adaptación, elegir un plan inferior llevaría a beneficios, dejando el ejemplo más abajo, y perdería el feedback real reciente. Esta evidencia modifica la aceptación funcional de V1 anterior aunque su calidad visual siga defendible.

**Acuerdo provisional A/B:** mantener selector inicial antes de intro para primera elección; solo elegir plan inferior en <=760 selecciona servicio, enfoca .ms-dashboard con preventScroll y desplaza ese panel a la parte visible. Panel ya tiene role=tabpanel, tabindex0 y aria-labelledby sincronizado al servicio; es un destino semántico coherente. No duplicar selectores, añadir sticky ni desplazar al pulsar las pestañas iniciales. Desktop conserva selección sin salto.

Scroll-margin104 es compatible con header móvil de76 +28 de separación en source; es un valor a validar en viewport real, no una regla universal. «Imagen» se interpreta como ejemplo del servicio: Meta incluye creatividades, Google muestra anuncios de búsqueda, Web su vista de sitio. La captura postclick debe comprobar que se ve contenido del ejemplo, no únicamente el rótulo bajo el header. No ampliar el ajuste a tablet/escritorio sin evidencia.

**Counterfactual nuevo:** mantener scroll a tabs pierde intención con DOM nuevo; deshacer el orden móvil pierde mejora de elección inicial; saltar al panel solo desde planes conserva ambos trabajos con una adaptación mínima. B acepta esta tercera solución como refinamiento del brief, sin dirección material nueva. Pendiente V1 actualizado y evidencia postclick a320/390 para los tres planes, foco/estado/teclado, movimiento reducido y desktop sin salto. La aceptación final necesita esa evidencia añadida; no se da por pasada todavía.

### Verificación del mockup actualizado y cierre de reapertura

B inspeccionó personalmente con view_image las seis capturas preview-marketing-quality-jump-meta/google/web-320/390.png y leyó el callback actualizado en marketing-quality-services.js y regla móvil de marketing-quality-v1-a.css. Las vistas postclick muestran panel bajo el header sin volver a beneficios: a390 Meta muestra las tres creatividades, Google el primer anuncio completo y comienzo del siguiente, Web la vista de escritorio completa y comienzo del teléfono. A320 también se ve contenido del ejemplo de los tres servicios; no queda limitado a un rótulo de servicio.

La fuente concreta selecciona primero, enfoca panel con preventScroll y usa scrollIntoView al panel solo en mobileLayout<=760; respeta reducedMotion con auto. El coordinador reportó QA para320/390/1440/1920 y tres planes: panel top≈104, header bottom77, foco ms-service-panel, ausencia de overflow y escritorio sin desplazamiento. Es evidencia ejecutada por coordinador, no prueba funcional propia de B. A informó de su inspección independiente y aceptación.

**B ratifica MANTENER A sobre V1 actualizado**, con ese destino móvil integrado en el mockup. Las dos intenciones quedan preservadas: primera selección antes de explicación, reselección inferior vuelve a ejemplo. No quedan objeciones materiales ni dirección nueva; este refinamiento absorbe feedback real y protege el trabajo concurrente. El acuerdo se refiere al mockup revisado y no autoriza publicación. Producto sin editar por B.
