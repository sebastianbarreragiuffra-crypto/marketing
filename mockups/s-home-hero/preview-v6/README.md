# Hero v6 — preview local aislado

Objetivo: implementar y revisar el hero aprobado de Inicio, con tres anuncios HTML/CSS y rotación móvil Meta → Google → TikTok cada tres segundos. La página raíz `index.html`, las demás secciones y la publicación permanecen intactas.

Para regenerar el preview: `python mockups/s-home-hero/preview-v6/build-preview.py`. Servir la raíz del proyecto con un servidor local y abrir `/mockups/s-home-hero/preview-v6/index.html`.

## Cierre de implementación

- **Resultado:** completo como preview local; no publicado.
- **Validaciones realizadas:** navegador a 320, 360 y 390 px sin desbordamiento, con botones de al menos 44 px, imágenes cargadas y altura del panel estable; a 1440 y 1920 px se ven las tres tarjetas, con composición centrada y ancho máximo de 1440 px. Se observó espera por visibilidad menor al 50 %, cambio cada tres segundos cuando supera el umbral, orden correcto, pausa tras selección manual, reanudación y navegación con Enter/Espacio. Sin errores de consola en la vista probada. `node test-hero.js` pasó para orden, umbral, pestaña oculta, pausa manual, movimiento reducido y escritorio. `python site_state.py --check` pasó sin cambios activos en el sitio.
- **No verificado directamente en navegador:** preferencia real del sistema `prefers-reduced-motion` y transición a pestaña oculta; esos caminos se comprobaron con el test aislado porque el navegador de preview no ofreció emulación y no reportó `document.hidden` al abrir otra pestaña. La reserva/contacto final y cualquier despliegue están fuera del alcance de este preview.
- **Estado del proyecto:** archivos de preview en este directorio y lección S-020 registrada en `.cursor/rules/directory-s-lecciones.mdc`. La fuente pública y el manifiesto no cambiaron.
- **Aprendizaje de método:** nada reutilizable fuera de las lecciones locales ya registradas.
- **Siguiente paso:** revisión visual del usuario; cualquier integración en `index.html` o publicación requiere una instrucción posterior.
