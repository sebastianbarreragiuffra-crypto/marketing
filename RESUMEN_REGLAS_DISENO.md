# Resumen de reglas para diseñar la web de Órbita — 2026-10-11

Documento de traspaso para otro chat que diseñará páginas en paralelo. Resume todas las reglas vigentes; ante cualquier duda, el archivo original manda. Si trabajas en esta misma carpeta, lee los archivos citados; si no, este resumen es tu fuente.

---

## 0. Precedencia de fuentes (de mayor a menor)

1. **Instrucción actual del usuario** en el chat.
2. **`.cursor/rules/brief-orbita.mdc`** — brief comercial y de diseño (2026-10-11). Regla local vigente mientras se diseña la web; prevalece sobre todo lo anterior que la contradiga.
3. **Reglas locales del proyecto**: `AGENTS.md` y `.cursor/rules/*.mdc` (Z, A, B, C, S, Flow 2A, diseño, validación, mockups, sincronización, lecciones).
4. **Webmaster canónico instalado** en `.webmaster/` (v2.8.0): método general y perfiles de especialistas.
5. Documentos históricos (`PROJECT_MEMORY.md`, `*_REVIEW.md`, `archive/`, `outputs/`): contexto, nunca órdenes.

Detectar contradicciones entre fuentes y resolverlas con la aclaración más reciente del usuario, no por la fecha del archivo. Distinguir siempre: CONFIRMADO, PROPUESTO, RECHAZADO, PENDIENTE y OBSERVADO.

**Nada de esto autoriza publicar, hacer commit/push ni modificar páginas reales.** Eso requiere un encargo explícito del usuario.

---

## 1. El negocio (brief-orbita.mdc)

**Relación**: Órbita y GISBA son del **mismo holding**. Órbita es la **agencia** (su equipo crea, gestiona y ajusta la publicidad). GISBA **desarrolla y vende el software** para agencias, freelancers y equipos internos. Órbita usa GISBA en su trabajo y da a sus clientes el acceso acordado.

**A quién vende Órbita**: ecommerce y empresas B2B que quieren delegar la creación y gestión de sus campañas. Necesidad central: «Quiero que un equipo se encargue de mi publicidad y me ayude a entender qué está haciendo». Quien busca sólo software se deriva a GISBA.

**Qué vende Órbita** (oferta principal = gestión de publicidad):
- **Gestión publicitaria**: anuncios, campañas y ajustes según alcance; Google, Meta y TikTok según la propuesta. Incluye **1 usuario de GISBA**; **usuarios adicionales con costo extra**; **inversión publicitaria aparte**.
- **Gestión publicitaria con atención automatizada** (opcional): suma el nuevo módulo de **bot y conversaciones unificadas de GISBA**; Órbita lo configura, pone en marcha y mantiene dentro del alcance. Contratar publicidad no obliga a contratar el bot.
- Secundarios (reglas previas, siguen vigentes salvo nueva indicación): **Diseño/Desarrollo Web** por proyecto (visible); **Automatizaciones** a medida (menor protagonismo).

**Qué aporta GISBA**: al equipo de Órbita, análisis, señales, recomendaciones y coordinación de decisiones. Al cliente, consultar su cuenta, revisar pendientes y coordinarse con la agencia. El cliente **no** recibe necesariamente los permisos operativos del equipo. La diferencia de Órbita es trabajo profesional + criterio humano + tecnología; **nunca afirmar que el software garantiza mejores resultados**.

**Bot**: pertenece a GISBA. Alcance **previsto** (rotular «previsto»): respuestas automatizadas, conversaciones unificadas, organización de leads, contexto y seguimiento. **No asumir** pagos, agendamiento, llamadas, integraciones específicas (no nombrar un canal concreto), ni atribución por anuncio. El contrato definirá cuándo interviene el equipo del cliente.

**Jerarquía que debe comunicar la web**: (1) Órbita crea y gestiona tu publicidad; (2) GISBA aporta información y coordinación; (3) atención automatizada como complemento opcional. **No** poner publicidad, software independiente y bot como tres ofertas iguales en un hero. **No** destacar GISBA independiente ni sus planes en la web de Órbita.

**Título acordado**: «Un equipo para crear y gestionar tu publicidad.» **CTA principal**: «Agenda una reunión» (lleva a contacto/reserva).

**Siempre visible o accesible**: inversión publicitaria aparte, usuario incluido y adicionales con costo.

**PENDIENTE (no inventar)**: precios, planes, modalidades y elegibilidad del usuario incluido (no extenderlo a Web automáticamente); disponibilidad real del bot; TikTok **no** figura entre las integraciones públicas de gisba.cl (mostrarlo como canal gestionado por Órbita, no como integración de GISBA).

**Observado en gisba.cl (2026-10-11, no es garantía)**: centraliza clientes, campañas, tareas, aprobaciones y reportes; «GISBA Pulse» detecta, explica y recomienda, y el equipo decide (no modifica campañas solo; no reemplaza un CRM); portal del cliente; integraciones Meta Ads y WhatsApp «disponibles», Google Ads y Analytics «configurables», según implementación.

---

## 2. Páginas, función y estado actual

| Página | Función | H1 actual | Estado |
|---|---|---|---|
| `index.html` (Inicio) | Qué contratamos, para quién, relación agencia/software, próximo paso; resolver dudas básicas de compra sin obligar a navegar | «Gestionamos tus campañas. Tu equipo sigue cada consulta.» | Indexable. **El título acordado del brief aún no está aplicado** (decisión de implementación pendiente) |
| `marketing.html` | Demostrar el trabajo de campañas | «Marketing que no termina en el clic.» | noindex. Hero aprobado (portátil + órbita verde); conservar |
| `software.html` | Demostrar seguimiento/coordinación con GISBA | «Sigue tus campañas y atiende tus consultas.» | noindex. Secciones aprobadas; **hero en rediseño** (ver §11) |
| `precios.html` | Entender modalidades e inversión | «Tus anuncios, gestionados por Órbita.» | noindex. Importes de ejemplo rotulados |
| `hablemos.html` | Contacto | «Contáctanos.» | Formulario de vista previa: **envío y reserva pendientes** (no llamar conversión) |
| `iniciar-sesion.html`, `automatizaciones.html` | Acceso / capacidad secundaria | — | noindex |

- Web publicada: https://orbita-marketing.pages.dev/ (Cloudflare Pages). La fuente vigente son las páginas raíz de este checkout.
- No rediseñar páginas o secciones aprobadas por cambios en otra página. Una recomendación no es aprobación.
- WhatsApp de contacto desactivado (no hay número real). No pedirlo ni inventarlo.

---

## 3. Identidad visual

- **Paleta Órbita** (`css/palette.css`): `--dark #0b0d0b`, `--palette-panel #171d17`, `--lime #c7f45b`, `--paper #f6f3eb`, `--cream #eeeae0`, `--palette-accent-text #48622e`; apoyo: `--palette-muted #596152`, `--palette-light-muted #bbc3b4`, `--palette-border #cccdbf`.
- **Tipografía**: Manrope 800 en titulares; DM Sans 400–700 en texto e interfaz.
- **CTA**: lima con texto negro (15,3:1). Lima **nunca** como texto sobre fondo claro (1,15:1); en claro, el acento de texto es `#48622e` (6,2:1).
- **Contraste objetivo mínimo 4.5:1** (brief). Comprobado: `#596152` sobre marfil 5,8:1. En la interfaz azul de GISBA, `#4174df` (4,4:1) y `#6683c6` (3,7:1) **no** sirven para texto pequeño.
- **Dos capas de color hoy**: marca Órbita (negro/lima/marfil) y, en Software, interfaz ilustrativa de GISBA en blanco/azules (navy `#071440`, azul `#4174df`/`#2d67c1`, fondos `#e9f3ff`). El azul es sólo del producto. **Decisión abierta**: si Software pasa a la identidad Órbita (el brief pide mantenerla).
- Alternar fondos dark/paper/cream cuando cambia la pregunta del comprador, no por decoración.
- **Hero de Inicio/Marketing**: conservar composición, dashboard frontal, tipografía y paleta; los mockups posteriores no son el master.
- **Layout**: diseñar a **1440 px** (ancho útil 1344, márgenes 48); a **1920** el contenido útil máximo es **1440 px centrado** (márgenes 240), incluida toda la composición del hero; móvil propio a **390** (comprobar 360 y 320).
- Composiciones frontales. Íconos en **SVG** (oficiales cuando existan; si no, placeholders), nunca emoji ni flechas Unicode.

---

## 4. Contenido y copy

- Español breve y claro para empresarios sin conocimientos de marketing: qué recibe el cliente, quién hace cada trabajo, qué está incluido y qué se paga aparte.
- **No inventar** cifras, resultados, testimonios, clientes, logos, integraciones, precios ni condiciones. Datos de interfaz y precios de maqueta se rotulan «ilustrativo / datos de ejemplo».
- Conservar FAQ útil y la función de reportes/transparencia; al fusionar o mover, decir dónde queda cada respuesta.
- No fijar cantidad de secciones (ni 3 ni 5); decidir por función y evidencia. No añadir un bloque por cada idea.
- **Primer pliegue** (lección S-011): como máximo etiqueta + H1 + una frase + condiciones en chips + acción; el detalle va a FAQ o secciones inferiores, sin duplicar texto. Las interfaces ilustrativas **no** usan etiquetas `h2–h6`.
- Revisar coherencia entre hero, oferta, FAQ, CTA, navegación y metadatos.
- No retirar Precios ni Iniciar sesión de la navegación/footer sin aprobación.

---

## 5. Método de trabajo

**Flow 2A** (`flow-2a.mdc`) para cambios mayores: alcance → reconciliar fuentes → inspeccionar la página real (render 1440/390) → problema del comprador → Z/A/B/C → contrastar la versión actual refinada + 2 alternativas realmente distintas → rechazar por contradicción comercial, función perdida, prueba inventada o inviabilidad → puntuar (valor 25, claridad 20, diferenciación 20, viabilidad 15, interés 10, estrategia 10) → decisión por sección (CONSERVAR / REFINAR / FUSIONAR / MOVER / RETIRAR). Para retoques, evaluar sólo el delta.

**Perspectivas locales**: **Z** oferta y verdad comercial · **A** comprador y comprensión · **B** desafío y alternativas · **C v2** dirección de arte, imágenes, movimiento, SEO/rendimiento e investigación. Declarar SAME_AGENT si las ejerce un solo agente; no simular votos ni independencia.

**Directorio S (Studio)** (`directory-s.mdc`) — produce cada sección:
- **META**: el mejor diseño posible, bien optimizado, con buen bounce rate, user friendly, mobile friendly, buenos layouts y fácil de entender lo que vendemos. El bounce rate real sólo se afirma con GA4 (hoy PENDIENTE); el diseño trabaja sus causas: primer pliegue claro, carga rápida (LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1), CTA visible, nada que tape la lectura.
- **Atajo**: «corre S» o «corre S [sección/página]».
- **Flujo**: 0 brief (leer lecciones) → 1 inventario (render real 1440/390, archivos, activos con bytes) → 2 contenido → 3 layout: actual refinada + 2 alternativas en wireframe gris → **punto de control 1: el usuario elige** → 4 dirección visual → 5 mockup alta fidelidad 1440 + 390 con antes/después → **punto de control 2: el usuario aprueba** → 6 especificación técnica → 7 QA. Implementar sólo con encargo aparte.
- **Roles propios**: diseño gráfico y producción de activos; sistema de diseño; mockups y prototipos. El resto se convoca de Webmaster: layout C1+A4; UX A4/C3/C7; redacción A3; motion C2; front-end C4; SEO C5/C6; medición A7; desafío B; entrega D.
- Máximo tres prioridades por vuelta; no generar otra versión sin delta ligado al feedback.

**Webmaster** (`.webmaster/`, no editar): A crecimiento y conversión, B desafío, C experiencia/motion/Search, **D entrega y lanzamiento** (no confundir con S). Para trabajo web material, leer `.webmaster/adapters/CODEX_BOOTSTRAP.md`. Nunca escribir en Webmaster canónico.

**Revisión fresca** (`fresh-review-google.mdc`): si el usuario pide otra mirada, briefing neutral sin conclusiones previas.

---

## 6. Imágenes, movimiento, SEO y rendimiento

- Cada visual responde una pregunta del comprador y muestra trabajo real de la agencia o la interfaz que recibirá el cliente; nada de fotos genéricas (rechazadas 3 veces). Cada imagen explica una parte distinta del servicio; **no repetir anuncios entre páginas**.
- Texto e interfaz en HTML/CSS/SVG editable; bitmap sólo para foto/ilustración. Por activo: dimensiones, bytes, formato (WebP/AVIF), `srcset/sizes`, prioridad (un solo `fetchpriority="high"`, lazy salvo LCP). Presupuesto interno: imagen principal ≤ 250 KB, miniaturas ≤ 30 KB.
- Capas flotantes sólo si explican un estado o acción; nunca tapan texto, controles ni foco.
- **Movimiento**: inventariar lo existente antes de añadir; sólo con función (orientar, contexto, feedback, enseñar tarea); especificar disparador, duración (feedback 120–200 ms, transición 180–300 ms, entrada 300–500 ms como punto de partida), estado final, `prefers-reduced-motion` y respaldo estático; nada esencial depende de animación, hover o carrusel; no secuestrar scroll; no librerías nuevas.
- **Accesibilidad**: AA, teclado, foco visible, objetivos táctiles 44 px (mínimo AA 24 px), reflow a 320.
- **SEO**: no quitar `noindex` en maquetas; títulos/encabezados semánticos reales; no prometer rankings.

---

## 7. Mockups (`mockup-1440.mdc` + S)

- Crear mockups en `mockups/<pagina>-<seccion>/` (fuera de rutas públicas). Preferir HTML/CSS que copie la página real y reemplace sólo la sección, para máxima fidelidad.
- Exportar: **primer pliegue 1440 × 810 con cabecera incluida**; sección completa a 1440 px reales; comprobar 1920; móvil 390. **Verificar dimensiones y bytes del archivo final** antes de mostrarlo. Conservar el original con sufijo.
- Esperar fuentes, imágenes y animaciones antes de capturar; una captura defectuosa no justifica rediseñar.
- **Revisar cada captura a la vista**, no sólo con script (superposiciones, textos tapados).
- Señalar si un mockup o imagen es una recreación generada. Entregar siempre antes/después.
- Script de captura de referencia: Playwright en `C:/Users/shermii/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright` con `channel: "msedge"`; servidor estático `python -m http.server 8743` (configurado en `.claude/launch.json`).

---

## 8. Lecciones aprendidas (`directory-s-lecciones.mdc`) — leer antes de diseñar, verificar antes de mostrar

- **S-001** Visual = lo que vendemos, nunca foto genérica; rotular ilustrativo.
- **S-002** Íconos SVG, nunca emoji ni flechas Unicode.
- **S-003** Todo dentro de 1440 útil a 1920; nada escala con `vw` sin tope.
- **S-004 (reincidencia)** Exportar 1440 × 810 / 1440 reales; verificar dimensiones.
- **S-005** «Rehacer» = mejorar, no recapturar; comparar con una alternativa y mostrar antes/después.
- **S-006** No quitar ítems de navegación/footer sin aprobación.
- **S-007** En móvil, toda interacción deja visible su resultado.
- **S-008** Sin datos de contacto inventados; sin cajas redundantes.
- **S-009** Extraer colores de la página real antes de usarlos.
- **S-010** Revisar `.webmaster/` y `.cursor/rules/` antes de crear reglas, roles o nombres.
- **S-011** Primer pliegue mínimo; interfaces ilustrativas sin encabezados reales.
- **S-012 (positiva)** Preferir visuales que muestran quién hace qué, una tarea por actor, frente a dashboards llenos.
- **S-013** Contrastar cada capacidad del producto con su fuente antes de dibujarla.
- **S-014** Revisar contra el brief: jerarquía publicidad > GISBA > bot opcional; bot «previsto», sin canal ni atribución por anuncio; no destacar GISBA independiente; inversión aparte visible.

**Aprendizaje autónomo**: tras cada corrección o falla de diseño, anotar la lección en ese archivo sin pedir permiso (síntoma → causa → regla → verificación), fusionando duplicados, y avisar en una línea.

---

## 9. Fuente única y sincronización (`site-source-sync.mdc`)

- La web vigente son las páginas raíz y sus dependencias; `mockups/`, `outputs/`, `archive/` y copias `dist` son referencia.
- Al reemplazar una sección autorizada: una sola implementación activa, retirar HTML/CSS/JS exclusivos de la anterior, guardarla en Git o `archive/<fecha>-<motivo>/`, comprobar referencias rotas e IDs duplicados.
- Tras una versión terminada: `python site_state.py --write`; `--check` debe pasar antes de trasladar o publicar.
- **No hacer commit/push ni desplegar sin autorización**; nunca `git add -A`. Separar: local, en Git, en GitHub, servido por túnel y desplegado en Pages. Cambio de PC: `PC2_HANDOFF.md`.
- Cada página carga ~16 hojas CSS: consolidar en el archivo dueño de la sección; no añadir otra hoja correctora.

---

## 10. Coordinación entre chats en paralelo

- **Repartir páginas**: cada chat trabaja páginas/secciones distintas y no edita HTML/CSS de la página del otro.
- **Archivos compartidos** (`css/palette.css`, `css/styles.css`, `AGENTS.md`, reglas, `directory-s-lecciones.mdc`): releer justo antes de editar; cambios mínimos; las lecciones se agregan al final con el siguiente ID libre; nunca revertir cambios ajenos (un archivo que cambió en disco es un cambio deliberado).
- Los mockups de cada chat van en su propia carpeta de `mockups/`.
- **Importante**: las reglas nuevas (`brief-orbita.mdc`, `directory-s.mdc`, `directory-s-lecciones.mdc`) y cambios en `AGENTS.md`/`directory-z.mdc` **aún no tienen commit**. Si el otro chat trabaja en otro computador o en otra copia, no los verá hasta un commit/push autorizado; usar este resumen.

---

## 11. Estado actual y pendientes registrados (sin actuar salvo encargo)

**En curso — hero de Software (`mockups/s-software-hero/`)**: elegido el layout B (tarjeta «Lo gestiona Órbita» + segunda tarjeta). El mockup actual **no cumple el brief** y debe corregirse cuando el usuario lo pida: quitar el enlace a GISBA independiente; cambiar la segunda tarjeta a «Lo revisas tú» (pendientes, reporte, coordinación con Órbita); bot sólo como «complemento opcional, previsto», sin nombrar canal; quitar «Origen: Meta Ads» y la línea campaña→consulta; añadir chip «Inversión publicitaria aparte». **Decisiones abiertas del usuario**: H1 de Software (propuestas: «Sigue tus campañas y coordina con Órbita» / «Mira cómo avanza tu publicidad») y si Software pasa a la paleta Órbita.

**Registrado, sin rediseñar todavía** (el usuario pidió no rediseñar anuncios aún):
- `assets/hero/pricing-meta-ad.webp` se repite en Marketing y Precios.
- Activos pesados: `marketing-laptop.png` 1,39 MB (1536×1024, se muestra a 1040 px máx., sin srcset); `marketing-web-office.png` 2,31 MB usado como miniatura de 58 px en Software.
- ~930 colores hex distintos en `css/`; hojas de Software sin variables; `experience-motion.css` anulado por `directory-c-shared.css`.
- Cierre de Software usa flecha Unicode «→»; secciones Flujo y Reportes de Software tienen `h3/h4` dentro de maquetas.
- Etiqueta superior azul de Software con contraste 4,27:1.
- FAQ de Software menciona GISBA independiente (contradice el brief; revisar al trabajar esa sección).
- Inicio aún no usa el título acordado.
- Contacto sin envío ni reserva reales; páginas interiores con `noindex`.

---

## 12. Prompt de arranque sugerido para el otro chat

> Trabajarás en el diseño de [PÁGINA] del sitio de Órbita, en paralelo con otro chat que trabaja otras páginas. Lee primero `RESUMEN_REGLAS_DISENO.md` (o el texto pegado) y, si estás en la carpeta del proyecto, `.cursor/rules/brief-orbita.mdc`, `AGENTS.md`, `.cursor/rules/directory-s.mdc` y `.cursor/rules/directory-s-lecciones.mdc`. El brief prevalece sobre reglas anteriores. Usa el flujo de Directorio S («corre S [sección]») con dos puntos de control: yo elijo el layout y apruebo el mockup. No toques páginas ni CSS de otras páginas, no hagas commit/push ni publiques, y no rediseñes anuncios salvo que te lo pida. Antes de mostrar un mockup, verifica dimensiones (1440 × 810 / 390), revísalo a la vista y comprueba el brief y las lecciones.
