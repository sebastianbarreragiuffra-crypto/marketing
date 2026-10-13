# Contexto para continuar Órbita en ChatGPT

Fecha: 2026-10-12. Carpeta local del proyecto: `C:\Users\shermii\Desktop\marketing`.

## Qué estamos construyendo

La web de **Órbita**, agencia que crea anuncios, gestiona campañas y revisa ajustes para ecommerce y empresas B2B. **GISBA** es el software del mismo holding que apoya la información y coordinación con el cliente. El foco comercial de esta web es la gestión publicitaria de Órbita, no vender GISBA de forma independiente. Google Ads, Meta Ads y TikTok Ads se ofrecen según el alcance acordado. La inversión publicitaria se paga aparte. El servicio contempla un usuario de GISBA; los usuarios adicionales tienen costo extra. Desarrollo Web es un servicio por proyecto. Automatizaciones son secundarias y personalizadas. El bot y las conversaciones unificadas son complementos opcionales futuros, con funciones y alcance pendientes de validar; no presentarlos como disponibles o incluidos. Precios y planes no confirmados.

La fuente local prioritaria es `.cursor/rules/brief-orbita.mdc`, seguida por `AGENTS.md` y las reglas del proyecto. No inventar cifras, resultados, integraciones, testimonios, precios ni capacidades de GISBA. Copy público en español sencillo. CTA principal literal: **«Agenda una reunión»**.

## Preferencias de trabajo del usuario

- Diseñar primero mockups visuales para aprobarlos; no insertar imágenes nuevas en la web antes de esa aprobación cuando se esté explorando un diseño.
- Mostrar las imágenes directamente en la conversación cuando sea posible, evitando enlaces remotos difíciles de abrir en móvil.
- Trabajar rápido y con alcance estrecho: no ejecutar revisiones amplias ni modificar otras páginas/secciones por una corrección puntual.
- Para las secciones de Inicio ya aprobadas, conservar su composición salvo instrucción expresa. Móvil debe ser legible y sin espacios vacíos excesivos; verificar escritorio también.
- El hero vigente usa negro, lima y marfil; su título literal es «Un equipo para crear y gestionar tu publicidad.»
- No publicar ni desplegar cambios cuando el usuario pida solo preview local. Distinguir siempre **propuesto / implementado localmente / publicado**.

## Estado de la web al 2026-10-12

El trabajo local se guardó en Git para el traspaso PC1 → PC2 del 2026-10-12; consultar PC2_HANDOFF.md para rama, commit y comprobaciones. No asumir que Cloudflare Pages coincide con el preview. La portada local se puede ver en `http://127.0.0.1:8879/index.html` si el servidor local está encendido. La versión pública histórica `https://orbita-marketing.pages.dev/` puede estar atrasada.

La **segunda sección de Inicio** se acaba de implementar solo en local: «Así trabajamos tu publicidad.» con tres escenas: «Creamos tus anuncios», «Gestionamos tus campañas» y «Tú ves el trabajo». Cada visual alterna automáticamente cada 3 segundos, con controles manuales y pausa, sin cambiar títulos, descripciones ni CTA. Se generó una foto ilustrativa de mochila; el anuncio, la revisión de campaña y la recreación de GISBA están construidos con HTML/CSS. CTA posterior a las escenas conserva el enlace `marketing.html#contacto`. Archivos: `index.html`, `css/home-work-v8.css`, `js/home-work-v8.js`, `assets/section-work/mochila-ejemplo.webp`. Preview: `http://127.0.0.1:8879/index.html#soluciones`. Evidencia de pruebas: `outputs/home-work-v8/validation.md`. **No se publicó ni desplegó.**

La sección anterior quedó archivada en `archive/2026-10-12-home-section2-before/`. `python site_state.py --check` pasó después del reemplazo.

## Cómo continuar

Primero preguntar o identificar si la siguiente tarea es **diseño/mockup** o **implementación**. Para diseño, usar el brief comercial, los mockups aprobados y la retroalimentación original. Para implementación, leer la sección actual y modificar solo el alcance autorizado. No asumir que una propuesta equivale a aprobación. Explicar el resultado de forma breve, con preview visible y con pruebas realmente ejecutadas.

ChatGPT Work local necesita acceso a esta carpeta para leer los archivos. ChatGPT en la nube no puede acceder por sí solo a `C:\Users\shermii\Desktop\marketing`; en ese caso, adjuntar este documento o pegar su contenido.
