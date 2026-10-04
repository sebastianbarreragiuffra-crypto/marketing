# Software en Inicio · sección 03 · 2A · 2026-09-28

Identidad: sección de Inicio posterior al marketing gestionado y anterior a automatizaciones. Brief padre: `SITE_PAGES_BRIEF.md` v1.0 y `HOME_PAGE_BRIEF.md` v1.0. Página pública/indexable, Search Gate REQUIRED resuelto a nivel Inicio. Buyer secundario: equipo ecommerce que atiende consultas y puede contratar el software sin campañas gestionadas. La sección debe orientar hacia `software.html`, no reemplazar su explicación completa.

V0: titular emotivo y mock de una conversación de producto. La vista muestra un ejemplo de mensaje y respuesta, pero no deja suficientemente clara la función de bandeja, responsables y seguimiento. Puede parecer captura real de un producto cuya interfaz no se ha verificado.

A / V1-A: titular y copy centrados en el trabajo del equipo: ordenar consultas, asignar responsable y registrar próximo paso. Destacar que es una suscripción independiente. Mostrar un tablero editorial con una cola de consultas y ficha de una consulta, identificado como ejemplo conceptual. Un CTA a `software.html`.

B / SAME-RUNTIME CHALLENGE: evitar nombres de canales e integraciones no verificadas; no fingir cifras de conversaciones, usuarios o resultados; no convertir el tablero en promesa de interfaz exacta. La bandeja es distinta del portal de coordinación agencia-cliente. La automatización avanzada pertenece al detalle del producto o al proyecto a medida según alcance. Counterfactual: mantener el chat actual conserva calidez pero explica menos; quitar el visual dificulta entender la herramienta; una vista conceptual de asignación y siguiente paso expresa la compra de software con precisión. Premortem: comprador cree que la agencia responderá sus mensajes, que contratar software exige campañas, o que el mock es captura real. Copy y leyenda deben resolverlo.

2A FINAL: REFINAR. Mostrar software como suscripción independiente para el equipo del cliente, con tres tareas: ver consultas, asignar responsables y seguir próximos pasos. Visual editorial sin canales específicos ni métricas. Mantener CTA a Software y aclaración sobre configuración. No alterar buyer, oferta ni arquitectura.

Originalidad: KEEP — SPECIFIC AND DEFENSIBLE si la vista usa la separación real entre agencia, portal y bandeja comercial. Search contribution: H2 descriptivo y enlace interno a la página Software, sin crear contenido redundante para posicionar otro término. CTR y conversión observados: NOT AVAILABLE. Desktop: explicación y tablero lado a lado. Móvil: explicación primero, tablero después; texto legible sin zoom. Criterios: CTA funcional, leyenda conceptual visible, sin canales/medidas inventados, sin desbordamiento ni errores JS.

## Implementación y verificación

Se reemplazó la sección 03 de `index.html` y se agregó `css/software-home-2a.css`. El texto identifica al equipo del cliente como usuario de la bandeja y explica la suscripción independiente. El tablero representa consultas, responsable y próximo paso sin nombrar integraciones ni fingir una interfaz verificada. La leyenda aclara su carácter conceptual.

Regresión: `verify-landing.cjs` aprobó Inicio, Marketing, Software y Automatizaciones a 390, 768 y 1440 px (carga, imágenes, un H1, anclas, navegación activa, menú móvil, FAQ, desbordamiento y consola). Comprobación focalizada adicional a 320, 390, 768 y 1440 px: sección sin desbordamiento, leyenda visible, sin nombres de canales no verificados y CTA hacia `/software.html`. Inspección visual de la composición en escritorio y de texto y tablero en viewport móvil de 390 px. Evidencia: `preview-software-home-1440.png`, `preview-software-home-390-viewport.png` y `preview-software-board-390-viewport.png`.

Estado: sección aprobada para esta iteración de maqueta. La vista real, conexiones y canales siguen sujetos a demostración/confirmación del producto.
