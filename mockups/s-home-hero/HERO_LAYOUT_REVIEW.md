# Inicio / hero — elección de layout (2026-10-11)

**Estado:** wireframes comparativos y mockup visual de la dirección 01 preparados para revisión. No están aprobados, implementados ni publicados. Revisión Z/A/B/C/S/2A realizada por el **mismo agente**; no representa opiniones independientes.

## Brief y evidencia

- Fuente comercial aprobada: `.cursor/rules/brief-orbita.mdc`. Órbita vende gestión publicitaria a ecommerce y B2B; GISBA apoya información y coordinación; el bot es un complemento previsto, fuera del mensaje principal.
- H1 y CTA conservados literalmente: «Un equipo para crear y gestionar tu publicidad.» y «Agenda una reunión».
- Página pública inspeccionada el 2026-10-11 a 1440 × 810 y en vista móvil. El H1 actual dice «Gestionamos tus campañas. Tu equipo sigue cada consulta.» y el control presenta «Marketing digital» y «Software de ventas» con peso similar. Los anuncios ilustrativos Google/Meta/TikTok ya ofrecen una representación visual concreta del trabajo de la agencia.
- El CTA público actual apunta a un contacto de vista previa sin envío. Su destino funcional queda pendiente para una implementación/publicación posterior.

## Comparación

| Dirección | Gana | Pierde / riesgo | Decisión |
|---|---|---|---|
| 01 Actual refinado | Conserva la composición y los anuncios reconocibles; cambia jerarquía de oferta sin rehacer imágenes. La promesa y el CTA aparecen antes del visual también en móvil. | GISBA queda como texto de apoyo; la sección siguiente debe explicar cómo el cliente revisa información. | **Recomendada** para el mockup de alta fidelidad. |
| 02 Promesa + proceso | Hace evidente la secuencia de trabajo y permite lectura rápida. | Sustituye el visual más concreto por cajas genéricas; repite la sección de proceso que ya existe en Marketing. | No desarrollar por ahora. |
| 03 Responsabilidades | Separa con claridad lo que hace Órbita y lo que revisa el cliente con GISBA. | Da demasiado peso visual al software en el primer pliegue y exige representar una interfaz aún no aprobada para esta portada. | Reservar la lógica para una sección posterior. |

La recomendación del mismo agente pasó estas perspectivas: **Z** confirma oferta y estado del bot; **A** prioriza la pregunta «¿quién hará mi publicidad?»; **B** desafía las tres alternativas y evita una caja de proceso intercambiable; **C/S** conserva el visual frontal y pide un móvil propio; **2A** sintetiza en 01. No hay medición de comprensión, rebote o conversión.

## Contenido y movimiento propuestos para 01

1. Etiqueta: «Publicidad para ecommerce y B2B».
2. H1 acordado, sin mencionar software ni bot.
3. Apoyo provisional: «Creamos tus anuncios y gestionamos tus campañas. GISBA ayuda a mostrarte lo que se hizo y qué sigue.» El copy se refinará en alta fidelidad para evitar repetir el H1 y no prometer funciones no verificadas.
4. CTA único: «Agenda una reunión».
5. Nota visible: un usuario GISBA contemplado/incluido en gestión y pauta publicitaria aparte. El costo extra de usuarios adicionales debe quedar claramente accesible en la sección siguiente/FAQ.
6. Visual: anuncios ilustrativos de un mismo negocio por canal, conservando el material aprobado; sin pestañas de «dos productos». En móvil, mostrar primero la promesa/CTA y luego el ejemplo principal, con acceso claro a los demás ejemplos.
7. Preferencia anterior de cambio cada 3 segundos: si se conserva, aplicarla solo a los ejemplos de anuncios, nunca a la promesa central. Dar pausa/control manual y estado estático con `prefers-reduced-motion`; probar que el móvil ve el cambio sin tener que volver a subir. La decisión exacta de movimiento queda para el mockup/prototipo.

## QA de esta fase

- Archivos generados: `hero-layout-01/02/03-desktop.png` a **1440 × 810** y `hero-layout-01/02/03-mobile.png` a **390 × 844**; collage a 1440 × 1790. Dimensiones comprobadas por script y lectura de imágenes.
- Wireframes inspeccionados visualmente. Son escala de grises deliberada para decidir jerarquía; paleta, fuentes, anuncios y accesibilidad final quedan para el mockup/prototipo.
- En una implementación posterior revisar 1440/1920/390/360/320, contraste, teclado, pausa, imágenes, JS desactivado, enlaces y destino funcional del CTA. Sin prueba humana de cinco segundos ni datos de conversión por ahora.

## Mockup visual de 01 — 2026-10-11

El usuario pidió expresamente **solo imágenes**, sin editar la página. Se desarrolló la dirección recomendada 01 como propuesta visual no aprobada: `hero-01-desktop-1440.png` (1440 × 810), `hero-01-mobile-primer-pliegue-390.png` (390 × 844) y `hero-01-mobile-completo-390.png` (390 × 1360). Los tres archivos se abrieron e inspeccionaron; dimensiones verificadas. El primero incluye cabecera y el borde de la sección siguiente sin proponerle contenido. Se reutilizan las dos fotografías ya activas del hero publicado para representar anuncios de un negocio ilustrativo; no se afirma que sean campañas reales. El dibujo de marca, anuncios y controles es una **recreación generada** para el mockup, no una captura funcional.

Delta visible: H1 acordado, publicidad gestionada como única oferta del primer pliegue, anuncios ilustrativos sin pestañas que equiparen software y agencia, GISBA en texto subordinado, CTA dominante y condiciones «1 usuario GISBA incluido» / «Inversión publicitaria aparte». El bot queda fuera del hero porque sigue previsto. Usuarios adicionales con costo extra debe seguir claramente accesible fuera del hero.

Validación de esta fase: composición y legibilidad inspeccionadas visualmente a 1440 y 390; fuentes Manrope/DM Sans y paleta aprobada en la imagen. Aún **no** están probados comportamiento responsive real a 1920/360/320, contraste computado de cada texto, teclado, interacción de anuncios, movimiento de 3 segundos, rendimiento ni recepción de la reunión; son pruebas de implementación y publicación futuras. El CTA público actual sigue sin envío real.

**Lecciones comprobadas:** S-001 (visual de trabajo concreto e ilustrativo), S-002 (flechas dibujadas, no emoji), S-003 (composición dentro de 1440), S-004 (dimensiones finales leídas), S-005 (delta frente al hero publicado y alternativas), S-006 (navegación conservada en el mockup), S-011 (primer pliegue breve), S-013/014 (sin bot disponible ni integración atribuida). S-007 no aplica a imágenes estáticas; se verificará en prototipo interactivo.

**Siguiente punto de control:** el usuario aprueba el mockup 01 o pide ajustes concretos. No modificar sitio ni publicar por esta revisión.

**Aprendizaje metodológico:** NOTHING REUSABLE; `FIRST_SCREEN_MESSAGE_AUDIT.md` ya cubre la revisión de promesa, visual, calificaciones y CTA como grupo.

## Rediseño V2 y continuidad de la segunda sección — 2026-10-11

Solicitud: «corre todo el directorio y rediseña», conservando la restricción anterior de entregar imágenes y no editar el sitio. Resultado: propuesta V2 de hero y sección inmediata de trabajo de agencia. Los PNG anteriores se conservan. No hay aprobación de implementación, commit ni publicación.

Revisión **SAME_AGENT**, con evidencia publicada y de mockup ya inspeccionada en esta conversación:
- **Z:** publicidad gestionada primero; un usuario incluido, adicionales con costo extra y presupuesto publicitario aparte visibles. GISBA apoya información/coordinación; el bot sigue previsto para un bloque posterior subordinado.
- **A:** el hero responde qué se contrata y cómo revisar el trabajo; la siguiente sección responde qué hace el equipo, sin repetir literalmente el H1 ni otra imagen de Instagram.
- **B:** compara (1) hero anterior con cambios de copy, (2) proceso como visual principal y (3) anuncios más responsabilidades explícitas. Recomienda 3: conserva evidencia visual concreta y explica el servicio. El proceso solo desplaza los anuncios con cajas genéricas; software/bot como ofertas equivalentes falla el brief y se descarta sin puntuar. El texto de anuncios es ejemplo, no evidencia de resultados propios.
- **C:** móvil con un ejemplo visible y controles propuestos para Google/Meta/TikTok; inicio del visual a y557 frente a y606 de V1. Se conservan estados accesibles estáticos conceptualmente. Propuesta de cambio de ejemplo cada 3 segundos cuando visible, pausa, selección manual y movimiento reducido; no se implementó ni probó. Escritorio conserva los tres ejemplos a la vista; cualquier movimiento futuro puede destacar el ejemplo seleccionado sin ocultar la oferta.
- **S:** produce `hero-v2-desktop-1440.png` (1440×810), `hero-v2-mobile-meta/google/tiktok-390.png` (390×1080), `hero-v2-mobile-primer-pliegue-390.png` (390×844), `seccion-02-agencia-desktop-1440.png` (1440×810) y `seccion-02-agencia-mobile-390.png` (390×1030). Son recreaciones dibujadas para revisión; no pantallas reales ni interfaces GISBA inventadas.
- **2A:** propuesta REFINAR hero + explicar trabajo en sección distinta. Pendiente de feedback del usuario, sin congelar arquitectura nueva.
- **D:** entregable apto para revisión visual con límites; no estado de lanzamiento. Navegación conservada en los dibujos. El formulario público sigue sin envío, fuera de esta entrega.

QA: imágenes finales abiertas e inspeccionadas; dimensiones leídas desde archivos; texto de condiciones móvil mide314px dentro de354px disponibles; título móvil de segunda sección339px dentro de354px. Contraste de colores sólidos: marfil/negro17,59:1, lima/negro15,34:1, texto secundario/marfil5,82:1 y verde/marfil6,18:1. Esto no verifica todos los píxeles sobre fotos, cumplimiento WCAG, responsive real, teclado, movimiento, SEO publicado, rendimiento ni conversión. Lecciones S-001/002/003/004/005/006/011/013/014 aplicadas; interacción S-007 pendiente de prototipo.

Cierre: objetivo de rediseño visual completado para estas dos escenas; sitio y assets activos intactos. Siguiente: feedback sobre estas imágenes y luego escena GISBA/atención opcional prevista, una por vez. Aprendizaje metodológico nuevo: **NOTHING REUSABLE**; las reglas existentes ya cubren jerarquía, estados del producto y diferenciación entre mockup e implementación.
