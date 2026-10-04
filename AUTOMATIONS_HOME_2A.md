# Automatizaciones en Inicio · sección 04 · 2A · 2026-09-28

Identidad: sección material de `index.html`, después de Software y antes de «Así empezamos». Brief padre: `SITE_PAGES_BRIEF.md` v1.0 (Inicio público/indexable, Search Gate REQUIRED) y contexto de `WEBMASTER_CONTEXT.md`. Buyer: ecommerce chileno. Oferta congelada: proyectos de desarrollo/automatización por alcance, separados de la suscripción de software. Conversión de la sección: ir a `automatizaciones.html`.

## V0 / A / B

V0: titular «Menos copiar y pegar. Más procesos conectados», párrafo breve y línea genérica «Consulta → Regla → Acción». No explica qué problema amerita un proyecto ni lo diferencia bien de la bandeja comercial.

A / V1-A: expresar el disparador de compra —una tarea que cruza herramientas, condiciones y personas— y presentar el trabajo como diseño de un recorrido a medida. Usar un caso conceptual de devolución en ecommerce para mostrar entrada, criterio y derivación/registro. Enlace único a la página de Automatizaciones.

B / SAME-RUNTIME CHALLENGE: una devolución puede sugerir una integración implementada o un resultado garantizado; etiquetar el caso como ejemplo potencial y no nombrar sistemas, conectores, SLA ni capacidades sin verificar. Evitar que la ilustración parezca un flujo ya entregado. El caso debe revelar el punto distintivo: decidir qué automatizar, con qué límites y dónde interviene una persona. Counterfactual: conservar la línea genérica ocupa menos espacio pero deja la oferta intercambiable; una foto de almacén no explica el servicio; un esquema específico y honesto sí muestra por qué existe esta compra. Premortem: el visitante supone que esto viene incluido en el SaaS, que la integración está lista o que Órbita promete resolver cualquier devolución. El copy y la leyenda deben prevenirlo.

2A FINAL: REFINAR. Sección editorial de proyecto a medida: encabezado que nombra trabajo entre herramientas, texto sobre definición del proceso y validación de sistemas/permisos, caso conceptual de devolución con decisión y revisión humana, y CTA a `automatizaciones.html`. Mantener paleta aprobada. No cambiar buyer, oferta, pricing ni arquitectura.

Originalidad/interchangeability: el ejemplo de devolución de ecommerce y el límite entre bandeja, proyecto y persona hacen el mensaje específico; la sección se volvería genérica si solo hablara de «innovación» o «IA». Search contribution: apoyo semántico sobre automatizaciones a medida y enlace interno; el detalle de agentes/integraciones pertenece a la página interior. Organic CTR observado y conversión CTA: NOT AVAILABLE.

Desktop: encabezado con explicación lateral, seguido de panel oscuro con recorrido visible. Móvil: explicación primero y tres pasos apilados en orden de lectura. Sin interacción ni motion necesarios. Criterios: texto que explicita modalidad por proyecto, caso marcado como conceptual, sin conectores ni promesas inventados, CTA funcional, sin desbordamiento ni errores JS.

Approval basis: DELEGATED WITHIN BOUNDS por la autorización vigente de revisar Inicio sección por sección y la solicitud actual de continuar con flujo 2A. El cambio permanece dentro del brief padre.

## Implementación y validación

Se reemplazó la sección 04 de `index.html` y se agregó `css/automations-home-2a.css`. El panel editorial distingue entrada, decisión y salida de un posible proceso de devolución; la modalidad por proyecto aparece junto al CTA. La leyenda impide leer el diagrama como integración implementada.

`verify-landing.cjs` aprobó las cuatro páginas a 390, 768 y 1440 px: carga de imágenes, un H1, anclas, navegación activa, menú móvil, FAQ, ausencia de desbordamiento y errores JS. Comprobación focalizada de Inicio a 320, 390, 768 y 1440 px: sin desbordamiento, leyenda presente y CTA a `automatizaciones.html`. Inspección visual de encabezado y diagrama en escritorio (1440) y móvil (320/390). Evidencia: `preview-automations-home-1440.png`, `preview-automations-home-390.png`, `preview-automations-flow-1440.png`, `preview-automations-flow-390.png` y `preview-automations-flow-320.png`.

Estado: sección cerrada para esta iteración de maqueta. Integraciones y alcance final de cualquier proyecto se confirman comercial y técnicamente antes de ofrecerlos.
