# Selector de soluciones · 2A · 2026-09-28

Nota posterior: esta sección recibió una segunda pasada visual junto al hero. La dirección vigente está en `HERO_SOLUCIONES_2A_V2.md`.

Alcance: sección `#soluciones` de `index.html`, inmediatamente después del hero. Hereda `SITE_PAGES_BRIEF.md` v1.0 y `HOME_PAGE_BRIEF.md` v1.0: Inicio público/indexable, ecommerce, tres ofertas independientes y posibilidad de combinar marketing y software. Search Gate REQUIRED ya resuelto para la página; esta sección ayuda a orientar la visita, sin crear otra página ni términos nuevos. El usuario pidió correr 2A sobre esta sección.

## V0

Tres filas enlazadas a Marketing, Software y Automatizaciones, con descripción breve y modalidad de compra. La frase introductoria dice que marketing y software pueden combinarse.

## A / V1-A

Conservar las tres rutas y el título interrogativo, porque permiten reconocer la necesidad antes de elegir página. Reescribir las descripciones desde la situación del comprador y la responsabilidad de cada oferta. Mostrar una nota explícita al final: marketing y software pueden contratarse juntos o por separado. No añadir fotografía: el trabajo de esta sección es navegación y comparación, no prueba visual.

## B · SAME-RUNTIME CHALLENGE

- Buyer reality: tres nombres de servicios no bastan si la persona aún no sabe qué comprar. Cada fila debe responder «esto encaja si...».
- Commercial reality: «gestión mensual» puede sonar a tarifa definida; conviene describir modalidad sin fijar duración o precio. «Suscripción independiente» hace visible que el software no exige contratar campañas.
- Fricción: una cuarta tarjeta para «ambos» competiría con las tres páginas existentes. Una nota breve después de las rutas comunica la combinación sin inventar una nueva oferta ni un destino inexistente.
- Counterfactual: mantener V0 conserva simplicidad, pero deja la combinación y el papel de cada equipo menos claros. Añadir imágenes o mockups a cada fila alargaría la decisión sin evidencia nueva. V1-A con nota breve resuelve mejor el trabajo de la sección.
- Premortem: si la elección falla, un comprador podría suponer que el software viene obligado con la agencia, que automatizaciones es una función incluida en la suscripción o que existe un precio mensual ya definido.

Resultado B: MODIFICAR A solo en el detalle comercial de las etiquetas. 2A FINAL: REFINAR, mantener tres enlaces y el título; usar descripciones basadas en necesidad y modalidades «servicio gestionado», «suscripción independiente» y «proyecto a medida»; incluir nota discreta sobre contratación conjunta. Sin fotografías, métricas, clientes ni conectores simulados.

Originalidad: KEEP — SPECIFIC AND DEFENSIBLE para la sección refinada. La distinción entre agencia operadora, equipo que atiende y proyecto por alcance nace de esta oferta. Se evita la tarjeta genérica de «servicios» repetida tres veces.

Mensaje/proof/action: qué problema atiende cada oferta; evidencia disponible es el alcance declarado por el usuario, sin resultados verificados; acción principal por fila: abrir su página. Desktop: filas escaneables con modalidad al lado. Móvil: modalidad debajo del texto y fila completa operable. Search contribution: enlaces internos descriptivos a las tres páginas temáticas. CTR orgánico observado y conversión CTA: NOT AVAILABLE.

Criterios: tres rutas llevan a páginas correctas, nota de combinación visible, ningún valor ficticio incorporado, teclado y móvil permiten elegir sin desbordamiento. La revisión no altera hero ni páginas interiores.

## Cierre de implementación y validación

Resultado: COMPLETE para esta sección. Se implementó en `index.html` y `css/solutions-2a.css`. Edge headless verificó las cuatro páginas a 390, 768 y 1440 px sin errores de JavaScript ni desbordamiento horizontal. En esta sección se comprobaron tres filas, ausencia de imágenes, visibilidad de la nota conjunta y navegación efectiva de las tres rutas. Capturas de 390 y 1440 px inspeccionadas. No se verificó conversión de contacto porque el número comercial aún no está configurado. Aprendizaje metodológico: NOTHING REUSABLE. Siguiente acción: revisión 2A de la sección editorial de marketing, si el usuario desea continuar por orden.
