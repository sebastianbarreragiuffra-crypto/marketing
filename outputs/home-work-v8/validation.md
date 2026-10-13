# Segunda sección de Inicio — preview local

Fecha: 2026-10-12. Estado: implementado en archivos locales; sin publicación ni despliegue.

Vista previa: `http://127.0.0.1:8879/index.html#soluciones`

Archivos activos: `index.html`, `css/home-work-v8.css`, `js/home-work-v8.js`, `assets/section-work/mochila-ejemplo.webp`. La hoja anterior se archivó en `archive/2026-10-12-home-section2-before/`.

La foto de la mochila se generó con la herramienta integrada de imagegen a partir de una descripción de fotografía editorial del producto del mockup: mochila de lona/cuero marrón sobre roca, montañas suaves, espacio para texto HTML a la izquierda, sin texto, marca ni interfaz en el bitmap. El recurso WebP pesa 179 054 bytes.

Validación ejecutada en el navegador local:

- 320, 360 y 390 px: tres escenas apiladas, texto legible, botones de al menos 44 px, CTA sin recortes y sin desbordamiento horizontal.
- 1440 y 1920 px: tres columnas; a 1920 px el contenido se centra y limita a 1440 px. Sin desbordamiento horizontal.
- Pausa durante 3,25 s: los tres estados permanecieron iguales. Selección manual de Versión 2: el estado cambió y el control pasó a «Reanudar animaciones». Tras reanudar, el anuncio cambió a los 3,25 s. La altura de la sección permaneció en 1565,44 px durante la prueba móvil.
- Tras desplazar la sección fuera de pantalla y esperar 3,3 s, los tres estados permanecieron iguales.
- La selección «Costo por consulta» con Enter activó `aria-pressed=true`, pausó el ciclo y mostró foco visible.
- La imagen cargó con anchura natural de 1448 px; no hubo errores de consola. El CTA conserva el destino `marketing.html#contacto`, cuyo ancla existe.
- `node --check js/home-work-v8.js` y `python site_state.py --check` pasaron sin errores; el manifiesto coincide y no faltan recursos.
- `node outputs/home-work-v8/reduced-motion.test.cjs` confirmó que, con movimiento reducido activo, no se programa ningún temporizador y la selección manual sigue funcionando.

Comprobación de código y prueba de comportamiento aislada: `prefers-reduced-motion` impide programar temporizadores, oculta el botón de pausa redundante y elimina las transiciones; la selección manual sigue disponible. Los títulos, filas y CTA están en HTML, por lo que siguen presentes si falla JavaScript. La emulación visual del ajuste del sistema no se ejecutó en el navegador de esta sesión.
