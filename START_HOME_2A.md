# Así empezamos en Inicio · sección 05 · 2A · 2026-09-28

Identidad: sección material de `index.html`, después de Automatizaciones y antes de Preguntas frecuentes. Brief padre: `SITE_PAGES_BRIEF.md` v1.0 (Inicio público/indexable, Search Gate REQUIRED); contexto comercial en `WEBMASTER_CONTEXT.md`. Buyer: ecommerce en Chile. Se heredan tres compras diferentes: marketing gestionado, software por suscripción y proyectos a medida. Esta sección explica el comienzo de la relación sin cambiar la conversión ni simular un contacto operativo.

V0: tres tarjetas iguales — conversamos, definimos, implementamos — con copy correcto pero intercambiable con cualquier agencia. El paso decisivo (elegir modalidad y acordar límites) no destaca.

A / V1-A: convertir las tarjetas en un recorrido editorial de tres decisiones. 01 Entender la tienda y el trabajo que se frena. 02 Elegir juntos entre gestión, suscripción y proyecto; las compras pueden combinarse. 03 Acordar alcance, entregables, responsabilidades y costos antes de ponerlo en marcha. Jerarquía visual mayor para el paso 02 y un cierre que deje claro qué se define.

B / SAME-RUNTIME CHALLENGE: no asumir diagnóstico gratuito, plazo fijo, demo automática, onboarding idéntico o resultados garantizados. La pregunta del comprador no es «¿cuáles son sus fases?» sino «¿voy a entender qué me ofrecen y quién se hará cargo?». Mantener tres pasos, porque añadir una fase artificial alargaría una portada que ya enlaza a páginas específicas. Counterfactual: las tarjetas actuales son más compactas pero genéricas; una línea de tiempo con fechas inventadas añade falsa certeza; filas editoriales con las modalidades reales mejoran la elección sin prometer más. Premortem: el usuario cree que debe comprar todo junto o que la agencia responderá mensajes por él. Paso 02 debe distinguir modalidades y paso 03 debe hablar de responsabilidades.

2A FINAL: REFINAR. Titular centrado en entender la tienda antes de acordar el alcance. Tres filas: conversación sobre el problema, elección visible de modalidad y acuerdo concreto antes de implementar. Sin CTA nuevo mientras WhatsApp siga sin destino real. Se preservan paleta, arquitectura, buyer y ofertas.

Originalidad/interchangeability: la decisión entre servicio gestionado, suscripción comercial y proyecto de automatización viene del modelo de Órbita; una lista genérica de «descubrir/diseñar/entregar» no. Search contribution: apoyo semántico al proceso de compra y a las tres rutas, sin competir con las páginas interiores. Organic CTR observado y conversión CTA: NOT AVAILABLE.

Desktop: encabezado a la izquierda y tres filas amplias a la derecha. Móvil: encabezado primero, pasos apilados con orden lógico, etiquetas legibles y sin columnas comprimidas. Sin motion necesario. Criterios: modalidades claramente distinguibles, alcance/responsabilidad/costos explícitos, ningún plazo o garantía inventada, sin CTA ficticio, sin desbordamiento y sin errores JS.

Approval basis: DELEGATED WITHIN BOUNDS por la autorización vigente de revisar Inicio sección por sección y la solicitud actual de continuar con flujo 2A. No se cambia el brief padre.

## Implementación y validación

Se reemplazó la sección 05 de `index.html` y se agregó `css/start-home-2a.css`. El segundo paso concentra la elección de modalidad; el tercero deja visibles alcance, entregables, responsabilidades y costos. No se añadió CTA a un contacto todavía inoperativo.

`verify-landing.cjs` aprobó Inicio, Marketing, Software y Automatizaciones a 390, 768 y 1440 px: carga, imágenes, un H1, anclas, navegación activa, menú móvil, FAQ, ausencia de desbordamiento y errores JS. Comprobación focalizada de Inicio a 320, 390, 768 y 1440 px: tres pasos y tres modalidades presentes, texto de responsabilidades/costos y sin desbordamiento. Inspección visual de la composición de escritorio y del encabezado y tramo final móvil a 320/390 px. Evidencia: `preview-start-home-1440.png`, `preview-start-home-390.png`, `preview-start-process-320.png`, `preview-start-process-390.png`.

Estado: sección cerrada para esta iteración de maqueta. Los recorridos exactos de contratación y el canal de contacto siguen pendientes de definición operativa.
