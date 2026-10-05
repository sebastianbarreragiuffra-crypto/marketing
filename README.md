# Sitio base de la agencia

Maqueta editable de seis páginas para una agencia de marketing y tecnología enfocada inicialmente en ecommerce.

## Abrir

Abre `index.html` en el navegador o inicia un servidor estático en esta carpeta. No requiere compilación.

## Páginas

- `index.html`: propuesta general y rutas de compra.
- `marketing.html`: campañas Meta/Google, contenido, páginas de campaña y portal del cliente.
- `software.html`: bandeja comercial, automatización y seguimiento como suscripción independiente.
- `automatizaciones.html`: agentes, integraciones y desarrollo a medida.
- `precios.html`: comparación de las tres ofertas con precios ficticios.
- `iniciar-sesion.html`: vista previa del acceso, pendiente de conectar autenticación; no recibe credenciales.
- `css/styles.css`: diseño responsive.
- `js/main.js`: menú móvil, año y aparición progresiva.

## Estado de maqueta

- **Órbita** y su símbolo son provisionales.
- Los precios están identificados como **ficticios** y no son tarifas comerciales.
- El formulario de Marketing permite preparar y revisar una consulta localmente; no envía datos. Los contactos de muestra todavía no tienen un receptor configurado.
- Las interfaces del portal y la bandeja son ilustraciones conceptuales. El portal se inspira en la experiencia de cliente compartida, no está conectado a GISBA OS; la bandeja ya está construida según el usuario, pero las conexiones específicas no se verificaron.
- No hay clientes, resultados, testimonios ni métricas inventadas.
- La dirección de las seis páginas está en `SITE_PAGES_BRIEF.md`.

## Sitio público

Cloudflare Pages: https://orbita-marketing.pages.dev

https://orbita-marketing-ecommerce.s-barrera651416.chatgpt.site

Con `python auto_publish.py --watch` activo y esta computadora autenticada en Cloudflare, cada rama local abierta en un worktree se publica por separado. `main` usa `https://orbita-marketing.pages.dev`; una rama como `diseno/hero` usa `https://diseno-hero.orbita-marketing.pages.dev`. Al guardar un archivo público, el publicador espera cuatro segundos sin más cambios y luego inicia la publicación. Cuando Cloudflare termina, F5 muestra la versión nueva en la URL de esa rama, sin hacer commit ni push. `__preview.json` identifica la rama y la versión publicada. La copia `cloudflare-pages-dist/` queda para publicaciones manuales y `site-publish-current/dist/` corresponde a Sites.

Para ver cada cambio inmediatamente en este computador, `python live_preview.py --port 8767` sirve únicamente las páginas y recursos públicos, con recarga automática. Abre `http://127.0.0.1:8767/branches/` para ver la página web de `main`; `http://127.0.0.1:8767/branch-list/` muestra las demás ramas locales. Cada enlace conserva su rama al refrescar con F5. Un Cloudflare Quick Tunnel puede exponer estas rutas temporalmente sin esperar la publicación de Pages. La dirección `trycloudflare.com` cambia si se reinicia el túnel y deja de funcionar al apagar este computador. El editor debe escribir los cambios en los archivos, ya sea manualmente o con guardado automático; Cloudflare no puede leer cambios que aún estén solo en el editor.

Para iniciar o reiniciar el publicador: `npx --yes wrangler login` una vez en esta computadora y luego `python auto_publish.py --watch`. Para una publicación puntual de la rama actual: `python auto_publish.py --once`. El estado local queda en `.preview-sync/` (ignorado por Git). Las ramas sin worktree local requieren abrirse aquí o publicarse desde el otro computador. Pages tarda unos segundos en terminar cada publicación; el túnel sirve los archivos directamente y es la opción inmediata mientras se edita.

## Código fuente

GitHub: https://github.com/sebastianbarreragiuffra-crypto/marketing

La carpeta principal contiene el código editable. Las copias de publicación y los archivos temporales quedan fuera del repositorio. Subir cambios a GitHub no actualiza por sí solo las URL públicas; cada plataforma necesita una nueva publicación.

## Continuar en otro computador

Clona el repositorio en PC 2 y abre la carpeta `marketing`. La guía [PC2_HANDOFF.md](PC2_HANDOFF.md) incluye el estado actual, cómo ver los cambios locales y cómo volver a publicar. Antes de trabajar en cualquiera de los dos computadores, trae la última versión de `main`; al terminar, confirma y sube los cambios antes de pasar al otro.
