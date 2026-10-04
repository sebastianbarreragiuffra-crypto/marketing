# Preguntas frecuentes en Inicio · sección 06 · 2A · 2026-09-28

Identidad: sección material de `index.html`, después de «Así empezamos» y antes del contacto. Brief padre: `SITE_PAGES_BRIEF.md` v1.0, Inicio público/indexable, Search Gate REQUIRED. Buyer: ecommerce que evalúa gestión de marketing, software por suscripción o un proyecto a medida. La sección resuelve objeciones de compra y confianza; no sustituye las páginas interiores ni activa el contacto de muestra.

V0: cinco preguntas pertinentes en un acordeón simple. Las respuestas ya cubren contratación separada, portal/bandeja, inversión publicitaria, canales y automatización a medida. Falta priorizar la responsabilidad práctica de atender compradores; el encabezado y las filas tienen poca jerarquía visual.

A / V1-A: conservar cinco preguntas y el acordeón nativo. Abrir con modalidades de compra, seguir con «¿Quién responde a los compradores?» para distinguir agencia, equipo y portal, y mantener inversión, canales y proyectos a medida. Presentar números y estado abierto de forma visible, con primera respuesta abierta por defecto para mostrar el tono y la separación de ofertas.

B / SAME-RUNTIME CHALLENGE: no añadir preguntas inventadas sobre plazos, precios definitivos, integraciones o soporte. Abrir todo el acordeón lo volvería largo, especialmente en móvil; la primera respuesta abierta basta. La pregunta de responsabilidad no debe borrar la distinción portal/bandeja. Counterfactual: mantener copy actual conserva precisión pero deja una duda central implícita; una lista estática mostraría todo pero haría densa la sección; acordeón nativo con mejor priorización equilibra claridad y espacio. Premortem: el visitante cree que Órbita responde los mensajes o que Meta/Google están incluidos en el precio de gestión; las respuestas deben asignar roles y costos con precisión.

2A FINAL: REFINAR. Mantener cinco dudas comerciales, reescribir la segunda sobre quién responde, explicitar que marketing y software pueden contratarse por separado y que los proyectos se presupuestan por alcance, conservar cautela sobre canales. Visual oscuro para separar «Así empezamos» del contacto, con preguntas numeradas y estado abierto claro. No cambiar buyer, oferta, pricing ni navegación.

Originalidad/interchangeability: las preguntas reflejan la combinación específica de agencia, bandeja y proyectos. FAQ genérica sobre «por qué elegirnos» no aportaría evidencia. Search contribution: respuestas útiles sobre modalidades y responsabilidades, sin promesas de rich results ni competir con páginas interiores. Organic CTR observado y conversión CTA: NOT AVAILABLE.

Desktop: introducción a la izquierda y acordeón a la derecha. Móvil: introducción antes de preguntas; resúmenes amplios y legibles, sin hover necesario. Accesibilidad: `details/summary` nativos, estado perceptible, teclado y foco visible. Criterios: cinco preguntas, primera abierta, respuesta sobre equipo/agencia/portal, inversión publicitaria separada, canales sujetos a confirmación, sin desbordamiento ni errores JS.

Approval basis: DELEGATED WITHIN BOUNDS por la autorización vigente de revisar Inicio sección por sección y la solicitud actual de continuar con flujo 2A. El cambio permanece dentro del brief padre.

## Implementación y validación

Se reemplazó la sección 06 de `index.html` y se agregó `css/faq-home-2a.css`. El acordeón mantiene `details/summary` nativos, muestra cinco preguntas numeradas y abre la primera respuesta al cargar. La segunda respuesta asigna expresamente la atención de compradores al equipo del cliente, la gestión de campañas a Órbita y la coordinación al portal.

`verify-landing.cjs` aprobó Inicio, Marketing, Software y Automatizaciones a 390, 768 y 1440 px: carga, imágenes, un H1, anclas, navegación activa, menú móvil, FAQ, ausencia de desbordamiento y errores JS. Se actualizó su comprobación del acordeón para verificar apertura y cierre desde el estado inicial abierto. Comprobación focalizada a 320, 390, 768 y 1440 px: cinco preguntas, una abierta inicialmente, contenido esperado y sin desbordamiento. Enter sobre la segunda pregunta abrió la respuesta y mostró foco visible. Inspección visual en escritorio y móvil. Evidencia: `preview-faq-home-1440.png`, `preview-faq-home-390.png`, `preview-faq-open-390.png`.

Estado: sección cerrada para esta iteración de maqueta. Canales concretos, precios finales y contacto operativo permanecen sin verificar/configurar.
