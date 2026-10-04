# Hero de Inicio · revisión 2A · 2026-09-28

Nota posterior: la ejecución visual de este hero fue refinada nuevamente en `HERO_SOLUCIONES_2A_V2.md` tras feedback del usuario. Este documento conserva la decisión de mensaje y responsabilidades, pero ya no describe la composición vigente.

Alcance: solo el hero de `index.html`. Foundation heredada de `SITE_PAGES_BRIEF.md` v1.0 y `HOME_PAGE_BRIEF.md` v1.0: ecommerce en Chile, oferta principal de marketing gestionado, software disponible por suscripción independiente, sitio público con Search REQUIRED. No cambia buyer, navegación, pricing ni conversión prevista. El usuario pidió explícitamente corregir la imagen y correr 2A para esta sección; dirección delegada dentro de esos límites.

## V0 y A

V0: hero con fotografía generada de packaging y un titular abstracto. El usuario observó que la imagen no tenía relación suficiente con lo vendido. La crítica se confirma: podría leerse como una tienda de cosméticos. A propone que el hero nombre las dos responsabilidades y que el visual muestre, sin datos inventados, trabajo de campañas y seguimiento de consultas.

## B · SAME-RUNTIME CHALLENGE

- La foto de packaging, aunque contextualiza ecommerce, no ayuda a entender la oferta. El texto contiguo no corrige esa primera impresión.
- Un mockup que parezca captura real del software podría prometer funciones o interfaz no verificadas. Un diagrama meramente abstracto repetiría el problema.
- Comparación: mantener la foto conserva impacto estético pero genera confusión; usar solo texto explica el servicio pero pierde apoyo visual; dos paneles editoriales etiquetados muestran quién hace qué sin fingir evidencia de producto.
- Premortem: si el hero falla, el visitante puede creer que vendemos productos, que la agencia atiende las consultas o que ambas soluciones se contratan obligatoriamente juntas.

## 2A FINAL · REEMPLAZAR

Titular directo: «Gestionamos tus campañas. Tu equipo sigue cada consulta.» Texto de apoyo: estrategia, anuncios y creatividad gestionados por la agencia; bandeja comercial para el equipo del cliente; contratación conjunta o separada. CTA principal a Marketing, secundario a Software. Media: composición HTML/CSS con dos paneles conceptuales, uno de campaña y otro de bandeja/seguimiento, cada uno con responsabilidad explícita y leyenda visible de concepto. No fotografía de productos, métricas, conectores ni clientes ficticios.

Originalidad: REFINAR THROUGH C resuelto con una composición basada en la división real de trabajo de este negocio. La propuesta evita residuo de plantilla fotográfica de ecommerce. Search contribution: H1 y texto explican la oferta amplia del Inicio; no se crean keywords ni claims de ranking. CTR orgánico observado y conversión CTA: NOT AVAILABLE.

Criterios: en tres tamaños, la oferta y responsabilidad se leen antes del selector de soluciones, los dos enlaces llevan a sus páginas, el hero no carga la fotografía cuestionada, no hay desbordamiento y la leyenda conceptual permanece visible. Pruebas: `landing-validation.json`; inspección visual de `preview-home-390.png` y `preview-home-1440.png`.
