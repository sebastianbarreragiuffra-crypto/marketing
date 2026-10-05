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

La URL de Cloudflare Pages recibe automáticamente los cambios locales mientras `auto_publish.py --watch` esté activo. Cada edición de una página, CSS, JS o recurso público inicia una nueva publicación tras cuatro segundos sin más cambios; al terminar, F5 muestra la versión nueva. El archivo público `__preview.json` indica de qué rama o worktree procede la versión visible. La copia `cloudflare-pages-dist/` queda para publicaciones manuales y `site-publish-current/dist/` corresponde a Sites.

Para ver cada guardado inmediatamente, `python live_preview.py --port 8767` sirve únicamente las páginas y recursos públicos, con recarga automática. El túnel actual apunta a ese puerto. `auto_publish.py --watch` detecta las ramas y worktrees de Git y cambia el origen del túnel al que se editó más recientemente. La dirección `trycloudflare.com` cambia si se reinicia el túnel; tanto la actualización instantánea como la publicación automática dependen de que este computador y sus procesos sigan encendidos.

El publicador usa **una sola URL** de Pages: la última rama editada reemplaza la versión anterior, incluso si sus cambios no están confirmados en Git. Para iniciarlo o reiniciarlo: `python auto_publish.py --watch`; para una publicación puntual: `python auto_publish.py --once`. El estado y los registros locales se guardan en `.preview-sync/` (ignorado por Git). Pages tarda unos segundos en terminar cada publicación; el túnel sirve los archivos directamente y es la opción inmediata mientras se edita.

## Código fuente

GitHub: https://github.com/sebastianbarreragiuffra-crypto/marketing

La carpeta principal contiene el código editable. Las copias de publicación y los archivos temporales quedan fuera del repositorio. Subir cambios a GitHub no actualiza por sí solo las URL públicas; cada plataforma necesita una nueva publicación.

## Continuar en otro computador

Clona el repositorio en PC 2 y abre la carpeta `marketing`. La guía [PC2_HANDOFF.md](PC2_HANDOFF.md) incluye el estado actual, cómo ver los cambios locales y cómo volver a publicar. Antes de trabajar en cualquiera de los dos computadores, trae la última versión de `main`; al terminar, confirma y sube los cambios antes de pasar al otro.
