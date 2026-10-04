# Revisión de imágenes · Marketing y Automatizaciones · 2A · 2026-09-28

Alcance: imágenes visibles en los seis HTML principales vigentes (Inicio, Marketing, Software, Automatizaciones, Precios e Iniciar sesión). Brief padre para las cuatro páginas de oferta: `SITE_PAGES_BRIEF.md` v1.0, Search Gate REQUIRED en páginas públicas. Buyer: ecommerce general; ofertas: marketing gestionado, software comercial independiente y proyectos a medida. El usuario ya rechazó fotografías que no representaban lo vendido.

Inventario: Inicio usa composiciones editoriales de campaña, bandeja y proyecto identificadas como conceptuales; Software usa una interfaz ilustrativa; Marketing y Automatizaciones mostraban dos fotografías generadas de cosmética/skincare. Precios e Iniciar sesión no contienen imágenes de contenido. `assets/logo-concepts/*` no aparece en las páginas. Las dos fotografías eran los únicos `<img>` raster visibles del sitio.

V0: `campaign-studio.webp` muestra envases y fotos cosméticas en un escritorio. `ecommerce-studio.webp` muestra productos cosméticos, cajas y laptop. Aunque sugieren ecommerce, dominan los productos de una categoría concreta y no el trabajo que Órbita vende. Pueden leerse como portafolio o cliente real pese al pie de «escena ilustrativa».

A / V1-A: retirar ambas fotografías de las páginas y sustituirlas por visuales editoriales nativos de la web. Marketing: brief, concepto creativo y gestión/revisión de publicidad. Automatizaciones: proceso actual repetitivo y diseño de datos, reglas y revisión humana. Etiquetar cada esquema como conceptual, sin cifras, clientes, interfaces verificadas ni conectores concretos.

B / SAME-RUNTIME CHALLENGE: repetir diagramas de Inicio puede aplanar la identidad visual; las composiciones interiores deben tener forma propia y explicar un nivel más concreto. Otra foto generada de un computador/equipo sería genérica y tampoco probaría el servicio. Capturas reales del portal o producto serían mejores cuando su uso y contenido estén verificados, pero no están disponibles hoy. Counterfactual: conservar fotos preserva textura editorial, a costa de una categoría falsa; eliminarlas sin sustituto deja páginas demasiado textuales; esquemas visuales específicos y honestos son la opción más segura ahora. Premortem: el visitante cree que Órbita vende cosmética o presenta un caso real; la sustitución resuelve esa confusión.

2A FINAL: REEMPLAZAR las dos fotografías visibles de Marketing y Automatizaciones por composiciones semánticas y responsivas. MANTENER los diagramas conceptuales de Inicio y la vista de Software en esta revisión: se relacionan directamente con las ofertas y están identificados como ilustraciones, aunque sus capturas reales deberán evaluarse cuando existan. No alterar marca, oferta, buyer ni arquitectura.

Originalidad/interchangeability: las nuevas piezas visuales se justifican por el trabajo de campaña y de diseño de procesos de este negocio; las fotos de cosmética podían servir a cualquier tienda de belleza. Search contribution: pies/etiquetas que describen el servicio sin afirmar experiencia o resultados. Desktop: paneles horizontales; móvil: lectura secuencial sin recorte. Criterios: cero fotos de productos cosméticos visibles, esquemas comprensibles, leyendas conceptuales, sin desbordamiento ni errores JS.

Approval basis: DELEGATED WITHIN BOUNDS por la solicitud vigente de corregir imágenes incongruentes y la preocupación actual del usuario. Los cambios no alteran decisiones estratégicas aprobadas.

## Implementación y validación

Se reemplazaron los banners fotográficos de `marketing.html` y `automatizaciones.html` por figuras HTML/CSS en `css/service-visuals-2a.css`. La primera muestra brief, concepto de anuncio y gestión/revisión; la segunda muestra una tarea repetida y las preguntas de datos, regla y decisión humana. Ambas llevan leyendas conceptuales. Los archivos fotográficos originales permanecen sin uso en `assets/` como antecedentes de diseño.

`verify-landing.cjs` aprobó Inicio, Marketing, Software y Automatizaciones a 390, 768 y 1440 px: carga, un H1, anclas, navegación activa, menú móvil, FAQ, ausencia de desbordamiento y errores JS. Comprobación focalizada de Marketing y Automatizaciones a 320, 390, 768 y 1440 px: un visual semántico por página, ninguna foto `studio` visible y sin desbordamiento. Inspección visual de ambas composiciones en móvil y escritorio. Evidencia: `preview-marketing-visual-390.png`, `preview-marketing-visual-1440.png`, `preview-automatizaciones-visual-390.png`, `preview-automatizaciones-visual-1440.png`.

Estado: las fotografías cosméticas ya no se usan en las páginas. Las vistas conceptuales deberán contrastarse con capturas o material reales solo cuando estén disponibles y autorizados.
