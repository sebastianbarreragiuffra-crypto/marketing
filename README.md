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
- El número de WhatsApp es una muestra; los botones de contacto están desactivados y no envían datos.
- Las interfaces del portal y la bandeja son ilustraciones conceptuales. El portal se inspira en la experiencia de cliente compartida, no está conectado a GISBA OS; la bandeja ya está construida según el usuario, pero las conexiones específicas no se verificaron.
- No hay clientes, resultados, testimonios ni métricas inventadas.
- La dirección de las seis páginas está en `SITE_PAGES_BRIEF.md`.

## Sitio público

Cloudflare Pages: https://orbita-marketing.pages.dev

https://orbita-marketing-ecommerce.s-barrera651416.chatgpt.site

Cada URL muestra la última versión publicada en su plataforma. Los cambios locales posteriores necesitan una nueva publicación. `cloudflare-pages-dist/` contiene los archivos de la versión enviada a Cloudflare Pages y `site-publish-current/dist/` la copia utilizada para Sites.

## Código fuente

GitHub: https://github.com/sebastianbarreragiuffra-crypto/marketing

La carpeta principal contiene el código editable. Las copias de publicación y los archivos temporales quedan fuera del repositorio. Subir cambios a GitHub no actualiza por sí solo las URL públicas; cada plataforma necesita una nueva publicación.
