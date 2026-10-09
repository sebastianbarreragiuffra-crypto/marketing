# Órbita · Marketing

Sitio estático editable: las páginas HTML de la raíz, con sus estilos, scripts e imágenes. No necesita build. Órbita es la agencia; GISBA es el software. Las tarifas y pantallas de demostración no validan condiciones comerciales ni capacidades del producto.

## Fuente vigente

La única fuente activa es el checkout abierto de este repositorio:
https://github.com/sebastianbarreragiuffra-crypto/marketing

`archive/`, `mockups/`, `outputs/` y copias de publicación son históricos o propuestas. No copiar su contenido a la web ni servirlas como versión actual por su fecha o nombre. Las versiones reemplazadas se retiran del layout; los recursos sin uso se archivan después de comprobar dependencias compartidas.

`site-manifest.json` identifica la versión terminada mediante rutas relativas y hashes de contenido. La misma versión tiene la misma huella en PC1 y PC2, aunque cambie la ruta, la fecha o los finales de línea LF/CRLF de Git; las imágenes y otros binarios se comparan por sus bytes.

```powershell
python site_state.py
python site_state.py --check
```

El primer comando informa el estado; el segundo verifica integridad. Una huella coincidente no confirma que los cambios estén subidos a GitHub: revisar también el estado Git que informa la herramienta.

## Vista inmediata y F5

```powershell
python live_preview.py --port 8767
```

Abrir http://127.0.0.1:8767/ . El enlace raíz sirve siempre este checkout; `/b/<rama>/` selecciona explícitamente otro worktree local. El preview evita caché de HTML/CSS/JS y recarga cambios guardados.

Un Cloudflare Quick Tunnel puede exponer ese servidor. Su URL temporal pertenece al PC que lo ejecuta y deja de funcionar cuando se apaga. F5 lee ese PC: no trae cambios de GitHub ni cambios sin guardar del editor. Para identificar la versión realmente servida, consultar `/__site.json` y compararla con `python site_state.py`.

## Cambiar de PC

Seguir [PC2_HANDOFF.md](PC2_HANDOFF.md), válido para ambos equipos. Antes del traslado hay que guardar, comprobar y, cuando esté autorizado, hacer commit y push de páginas **y todas sus dependencias**. Un pull no recibe archivos modificados o nuevos que siguen solo en el PC de origen.

No anunciar traspaso completo hasta comprobar SHA remoto y huella de contenido. No sobrescribir un árbol con cambios locales en el destino.

## Cloudflare Pages

`https://orbita-marketing.pages.dev` es un despliegue independiente del Quick Tunnel. Un commit/push no lo actualiza por sí solo. `auto_publish.py --dry-run` prepara únicamente los archivos activos sin publicar; `--once` y `--watch` sí despliegan y requieren autorización y acceso a la cuenta del proyecto existente.

No usar dos publicadores de la misma rama simultáneamente. La autenticación, los procesos y `.preview-sync/` son locales; no viajan por Git. No crear un proyecto Cloudflare duplicado para resolver un acceso pendiente.

## Estado funcional

La reserva, el envío de consultas y la autenticación siguen pendientes de habilitar. Consultas y reportes de GISBA son demostraciones visuales. Las propuestas de revisión no son implementaciones automáticas. Las reglas vigentes están en `AGENTS.md` y `.cursor/rules/`.
