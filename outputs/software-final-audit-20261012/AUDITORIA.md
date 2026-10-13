# Auditoría final de Software — 2026-10-12

Resultado de implementación local: COMPLETE. Preparada para revisión visual, no para lanzamiento funcional. A/B/C/D/Z y especialidades revisadas por el mismo agente (SAME_AGENT_CHALLENGE); sin votos ni revisores independientes. Autorización: corregir Software localmente, sin deploy/commit/push ni cambios en otras páginas.

## Hallazgos y correcciones

1. Estado comercial contradictorio en Sección 3: retirados «En desarrollo», «previsto» y nombres accesibles futuros. Etiqueta «ATENCIÓN AUTOMATIZADA · COMPLEMENTO OPCIONAL». Firma visible «Muebles Norte · Asistente virtual». El responsable confirma disponibilidad; este trabajo no verifica backend/canales. Se mantienen datos ficticios/chat ilustrativo no operativo y condiciones según contrato.
2. Caso comercial equivocado en Sección 2: ahora un comprador B2B pide escritorios a Muebles Norte; Ana consulta cantidad, comparte un catálogo ficticio y el comprador pide 10 unidades y llamada. Ficha: cotización por preparar, última respuesta 10:22, responsable Ana, llamada 16:00 por confirmar. Cliente 01 continúa siendo un cliente existente con una compra anterior. Menú, estados y estructura conservados.
3. Menú de tres puntos del teléfono producía desbordamiento interno por escritura vertical. Sustituido por el mismo motivo visual en SVG de 12×22, sin función nueva ni cambio de composición.
4. CTA: siete enlaces iguales a hablemos.html#contacto. Añadidos nombre accesible y tooltip con limitación de vista previa. El texto visible permanece «Agenda una reunión». Tab/Enter llegan al destino: formulario y envío deshabilitados, aviso explícito «Tu consulta no se enviará». No se transmitieron datos ni se conectaron servicios.
5. Contenido repetido: Reportes y FAQ ya estaban eliminados localmente; se confirmó que siguen ausentes. La URL pública observada todavía muestra siete bloques, bot futuro y consulta de marketing; esa publicación permanece intacta.
6. Subtítulo del hero: no había duplicación simultánea. Se conservó; desktop y móvil muestran variantes excluyentes, ambas mantienen el trabajo del equipo de Órbita. No se corrigió un problema inexistente.

## Revisión por perspectivas

| Perspectiva | Resultado y límites |
|---|---|
| A / marketing | Agencia gestiona publicidad; GISBA aporta visibilidad; comprador final en el ejemplo. Comprensión revisada por el agente, sin pruebas con usuarios. |
| B / crítica | La principal objeción sigue siendo CTA sin reserva/recepción funcional; no se declara conversión completa. |
| Z / oferta | Un acceso incluido, adicionales de pago y pauta aparte preservados. Bot opcional disponible según usuario; integraciones y alcances específicos no certificados. |
| C / producto y datos | Cinco anchos sin overflow ni colisión interna; contraste mínimo 5,46:1 en texto HTML muestreado. Tres vistas manuales y teclado probados. No se afirma cumplimiento WCAG completo. |
| D / entrega | Apta para revisión visual con notas. NOT READY FOR HANDOFF / LAUNCH funcional: contacto real pendiente. Sin lanzamiento ni prueba de recepción. |
| Diseño gráfico / layout / UX | Paleta, tipografía y composiciones aprobadas conservadas; transición hero oscuro → contenidos marfil → Hablemos oscuro; imágenes cargadas, sin sección duplicada. |
| Copywriting | Coherencia de actores, disponibilidad, documento, horarios y etapa; ilustraciones diferenciadas de funciones reales. |
| Frontend / SEO / rendimiento | Sin IDs duplicados ni archivos faltantes, un H1, sin nuevas dependencias/JS/raster. Noindex de entorno de diseño conservado. Reduced-motion revisado en código; no emulado en SO. No Lighthouse/CWV de campo ni analítica de conversión. |

## Pruebas

- 1440, 1920, 768, 390 y 375: cinco secciones en orden, sin overflow horizontal/interno; ancho útil máximo 1440 a 1920.
- Variantes hero excluyentes en los cinco anchos; tablet conserva párrafo de apoyo del asistente.
- Consultas / Conversación / Ficha: probadas en 768/390/375. Un panel visible por vez, rol/selección/tabindex coherentes; resultado visible debajo de la cabecera.
- Flechas, Home, End y wrap de pestañas; foco visible, menú/Escape y CTA por teclado.
- Destino CTA: contacto de vista previa deshabilitado, no reserva ni envía datos.
- Capturas completas verificadas: 1440×4534 y 390×7100 PNG, conversión de formato sin cambiar píxeles.
- Regresión en fuente: H1, dashboard y métricas, términos, tarjetas/cierre (excepto metadata de contacto) y footer intactos; otras fuentes/páginas idénticas a la baseline en la primera comprobación. Al cerrar se detectaron cambios concurrentes en precios.html y css/pricing-comparison-20261011.css, preservados sin editarlos desde esta auditoría.

Evidencia: responsive-final.json, tabs.json, keyboard-cta.json, focus-recheck.json, regression.json, technical.json, public-observation.json y capturas. Versiones anteriores: archive/2026-10-12-software-final-audit-before.

## Decisiones pendientes del responsable

1. Elegir y autorizar un mecanismo real de reunión/contacto: calendario o receptor de consultas con canal y cuenta oficiales. Luego integrar, revisar privacidad y comprobar reserva/recepción. Actualmente no existe uno operativo configurado.
2. Confirmar por contrato las capacidades/canales/configuración/precio del complemento. Disponibilidad confirmada no equivale a auditoría técnica ni SLA de respuesta instantánea.
3. Aprobar visualmente esta versión y autorizar posteriormente cualquier publicación; no se realizó despliegue, commit ni push.

## Evaluación

7/10 global, juicio cualitativo del agente y no medida de conversión. La composición y la implementación visual son coherentes y las pruebas pasan; el recorrido principal de contacto todavía no termina en una solicitud recibida o reunión reservada. No se considera listo para producción.

## Archivos

Código: software.html y css/software-asistente.css (con versión de carga actualizada). Soporte: site-manifest.json, PROJECT_MEMORY.md, .cursor/rules/brief-orbita.mdc, .cursor/rules/directory-s-lecciones.mdc. Informe/QA/PNG y archivo recuperable fuera de rutas públicas. Ninguna otra página o footer editado por esta auditoría. Los cambios paralelos de Precios se distinguen del alcance de Software.
