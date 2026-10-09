# Traspaso de Órbita entre PC1 y PC2

Procedimiento vigente desde el 7 de octubre de 2026. Sirve en ambas direcciones.
Repositorio esperado: https://github.com/sebastianbarreragiuffra-crypto/marketing

## Antes de salir del PC de origen

1. Verificar carpeta, remoto, rama y cambios locales. Guardar los archivos; el túnel puede mostrar trabajo que todavía no existe en GitHub.
2. Aplicar `AGENTS.md` y `.cursor/rules/site-source-sync.mdc`. La fuente actual son las páginas raíz. Un histórico o una propuesta no restaura la web automáticamente.
3. Al terminar los cambios autorizados, actualizar y comprobar el inventario:

   ```powershell
   python site_state.py --write
   python site_state.py --check
   python site_state.py
   ```

4. Revisar todas las dependencias que informa la herramienta: HTML, CSS, JS, imágenes, reglas y scripts del cambio. Incluir archivos nuevos y retiradas necesarios; excluir secretos, estado local, logs y propuestas ajenas. Nunca añadir todo indiscriminadamente.
5. Si commit/push está autorizado, guardar un commit enfocado y subirlo a la misma rama. Si existe una prohibición o falta autorización, dejar el traspaso PENDIENTE; la vista en vivo no sustituye este paso.
6. Verificar el SHA de la rama remota. Anotar **remoto, rama, SHA, versión de contenido, archivos necesarios aún locales y pruebas pendientes**. No afirmar que PC1/PC2 tiene la versión nueva sin esta comparación.

## Al llegar al PC destino

Desde el checkout correcto, verificar primero:

```powershell
git status --short
git remote get-url origin
git branch --show-current
git fetch origin --prune
```

Conservar cambios locales. Si hay divergencia o faltan archivos, no hacer reset, force-push ni sobrescribir. Resolver el estado antes de mezclar versiones.

Cuando la rama sea la indicada en el traspaso, el árbol esté limpio y el upstream sea correcto:

```powershell
git pull --ff-only
python site_state.py --check
python site_state.py
```

Comparar el SHA y la versión con el origen. Si el manifiesto falta, difiere o hay recursos activos sin seguimiento, el traslado no está verificado. No compensarlo copiando un `dist/`, un mockup o archivos de otro proyecto.

## Abrir la versión correcta

```powershell
python live_preview.py --port 8767
```

El enlace raíz sirve el checkout donde está ese script. `/__site.json` identifica su versión sin exponer rutas del equipo. Abrir un Quick Tunnel hacia ese mismo puerto cuando se solicite vista pública; verificar su página real y compararla con la versión local.

Una URL `trycloudflare.com` anterior puede seguir sirviendo el otro PC o haber caducado. No guardarla como URL vigente del repositorio. Consultar el estado del proceso actual en `.preview-sync/live_service_state.json`, si el supervisor está activo.

Cloudflare Pages usa una publicación separada. No confundir “guardado local”, “commit”, “push”, “túnel activo” y “Pages desplegado”. Después de un pull puede ser necesario reiniciar el servidor para cargar cambios en sus scripts; los cambios HTML/CSS/JS guardados se ven con F5.

## Contenido y referencias

Conservar la versión que el usuario haya confirmado en la web activa. En octubre de 2026, Precios tiene el recibo de mensualidad y el cierre “Descubramos qué necesita tu negocio” con “Antes de agendar”; la invitación redundante a ver GISBA fue retirada. El manifiesto, no esta descripción, verifica los archivos exactos.

Las guías que describían la restauración del 4 de octubre y URLs antiguas están en `archive/2026-10-07-source-cleanup/`. No son instrucciones de restauración. Formularios, reservas, login, tarifas y capacidades de GISBA pendientes no se consideran conectados o aprobados por verse en una captura.
