# Contáctanos — Directorio A

2026-10-04 · INDEPENDENT REVIEW · lectura inicial propia antes de conclusiones de B.

Foundation: `MARKETING_CONTACT_2A.md` v1.0 READY FOR 2A, `SITE_PAGES_BRIEF.md` v1.0, `MARKETING_THREE_SECTIONS_2A.md` v2.1 y `MARKETING_QUALITY_2A.md` v1.0. Leídos AGENTS, protocolo 2A, A CORE/WORKFLOW, reglas compartidas, contexto, memoria, decisiones y fuente vigente `marketing.html`, `js/marketing-contact.js`, `css/marketing-compact.css`. Evidencia visual inspeccionada: `preview-marketing-three-quality-public-contact-1440.png` y `preview-marketing-three-quality-public-contact-390.png`.

## Problema y criterio propio

El visitante puede querer campañas y otra solución al mismo tiempo, pero el cierre actual fuerza un único interés y no permite dar contexto ni escoger cómo recibir respuesta. Su continuidad visual oscuro/lima funciona y debe preservarse. Aclarar la necesidad y el canal de respuesta es útil; exigir muchos datos antes de conversar no tiene justificación disponible. No hay datos propios de abandono, conversión ni consultas.

La compra es consultiva y las ofertas son independientes, combinables. La página sigue siendo Marketing para ecommerce; aceptar B2B como contexto de una consulta no reposiciona el sitio. Software se ofrece como interés en el contacto y conserva su página propia, sin cuarta vista del bloque dinámico.

## Candidatas

1. **Mantener cierre actual:** muy breve, preserva composición, pero no responde a la necesidad de varios intereses/contexto y sigue sin canal operativo. Pierde por insuficiencia para el encargo.
2. **Formulario mínimo:** varias soluciones y un correo visible; empresa/contexto se conversan después. Alta claridad y baja complejidad, pero descarta la elección número/correo pedida por el usuario y el contexto comercial puede ser útil sin hacerlo obligatorio. Finalista de comparación, no rechazada por gate.
3. **Formulario breve flexible:** servicios múltiples, contexto/empresa opcionales y una vía de respuesta con su campo condicional. Preferida de A por utilidad concreta y proporcionalidad. No exige nombre personal, presupuesto, facturación, RUT, urgencia ni plazos.
4. **Cuestionario/wizard con calificación obligatoria:** rechazar por complejidad y preguntas no justificadas; el contacto actual no tiene evidencia que sostenga ese esfuerzo previo.

Comparación cualitativa, sin precisión artificial: la tercera gana en valor cliente/negocio, claridad de intención y ajuste a ofertas combinables; cuesta más que la segunda, pero sigue siendo viable en una sección. La diferenciación no viene de inventar campos ni de un formulario novedoso: viene de reconocer campañas gestionadas y software independiente. Penalización de complejidad si se exige todo; no sumar decoraciones ni pasos por defecto.

## Recomendación inicial

- **Servicios:** «¿En qué te podemos ayudar?» con Meta Ads, Google Ads, Desarrollo Web y Software; multiselección explícita «Puedes elegir más de una opción». Añadir «Aún no lo sé» para no exigir conocimiento previo de soluciones; si se usa, debe ser excluyente con servicios específicos y quedar claro que es una consulta general.
- **Contexto:** «¿Cómo vende tu negocio? (opcional)». Tienda online y Venta a empresas pueden coexistir: ecommerce es canal, B2B es comprador. Otro permite no encajar en esas dos categorías, sin forzar un nuevo campo libre. No usar elección única ecommerce/B2B.
- **Empresa:** «Nombre de tu empresa (opcional)», sin requerir razón social. No hay evidencia de que exigirlo sea imprescindible para responder.
- **Respuesta:** elegir WhatsApp o Correo; una sola vía necesaria y solo su campo requerido. Etiquetas visibles, no solo placeholders. Para número, explicar código de país; no usar automáticamente un prefijo que excluya prospectos. Valores conservados al alternar; el canal no visible no debe impedir revisión.
- **Intención:** el formulario mantiene su estado propio. La rotación o navegación del bloque de ejemplos no modifica elecciones ni datos. Un CTA específico añade el interés elegido sin borrar otros; un CTA general preserva lo ya preparado. No disparar cambios en showcase desde los controles del formulario.
- **Acción del mockup:** «Revisar consulta», resumen local identificado como vista previa y posibilidad de corregir. No afirmar envío, persistir en localStorage, inventar receptor ni transmitir datos. La configuración real se mantiene fuera de alcance por instrucción previa del usuario.

Observación → Impacto → Recomendación → Prioridad: única selección → pierde combinaciones reales de servicios → multiselección y estado independiente → P1 de la propuesta. Ecommerce/B2B excluyentes → clasifica mal a ecommerce que vende a empresas → contexto opcional múltiple → P1. Campos todos obligatorios → fricción sin necesidad acreditada → solo necesidad/canal/dato estrictamente útiles → P1.

## Criterios de mockup e implementación eventual

Preservar las tres secciones, marca, hero y vistas aprobadas. Desktop base1440 y optimización1920 con máximo útil1440 para la sección completa; tarjeta amplia sin estirarse indefinidamente. Mantener jerarquía de Contáctanos, pero evitar repetir en gran tamaño «Tu consulta» si ya aparece el selector. Móvil: una columna, selección legible, controles táctiles y labels persistentes; no overflow a320/390. Validar también768/1024.

Teclado para grupos y campos; estado seleccionado reconocido sin depender solo del color. Canal con campo condicional y errores junto al dato; revisión no debe vaciar elecciones ni otros campos. No usar el resumen como éxito de entrega. C debe comprobar intención desde todos los CTA, conservación al volver/alternar, eventos de showcase/autoplay y foco pertinente.

Search contribution SUPPORTING heredada; no altera URL/H1/temas/page mapping. CTR orgánico y conversión NOT AVAILABLE. El efecto esperado es facilitar expresar la consulta y recibir respuesta por una vía elegida; es una hipótesis de diseño, no una mejora demostrada.

Estado: recomendación inicial independiente, PENDING challenge cruzado y revisión del V1. No modificaciones de producto ni publicación desde A.

## Challenge de Orchestrator antes de V1

El Orchestrator cuestionó dos extras de A: quinta opción «Aún no lo sé» y etiqueta WhatsApp. A acepta la mejora por razones concretas. Los intereses pueden ser opcionales y dejarse vacíos: «Puedes elegir más de uno o dejarlo en blanco si aún no lo tienes claro» evita exigir conocimientos previos sin añadir una quinta opción ni reglas de exclusión. Una necesidad ya abierta justifica conversar, aun sin servicio elegido.

**Correo / Teléfono** refleja mejor «número/correo» solicitado por el usuario. WhatsApp procedía de la conversión histórica, pero su configuración fue expresamente omitida. No conviene forzar una modalidad de respuesta aún no definida. Label propuesto «¿Dónde prefieres que te contactemos?»; sigue siendo un dato de contacto seleccionado, sin promesa de envío, llamada o receptor real. Se muestra y valida únicamente el dato activo; se conserva el otro al alternar. Esta corrección cambia la recomendación inicial, no es consenso fabricado con B, cuya primera lectura aún no se ha recibido.

## Lectura del V1 y challenge cruzado

Artefacto leído: `mockups/marketing-contact-v1-a.html`, `marketing-contact-proposal.css` y `marketing-contact-proposal.js`. B había formado recomendación independiente similar antes de recibir A: cuatro servicios opcionales/múltiples, contexto independiente opcional, empresa opcional y una vía con solo el dato activo. No se presenta la coincidencia inicial como debate.

A preguntó a B si «Otro» era útil o si dejaba una clasificación poco accionable. B prefería inicialmente la mínima de dos contextos, pero observa que «Otro» permite expresar venta presencial/B2C frente a la ambigüedad de omitir el campo. A acepta ese argumento y conserva Otro opcional y combinable, sin textarea ni promesa de calificación comercial extra. No es una tercera categoría exclusiva: puede existir otra vía de venta junto a ecommerce y B2B.

A y B rechazan un wizard y compactar320 a costa de texto/targets legibles. El recorrido mayor se debe evaluar visualmente, no justificar por una mejora de conversión inexistente. Pendiente inspección de renders.

Dos hallazgos acotados para C en el prototipo: (1) el HTML sin guardia nativa podría hacer GET con los datos si falla el script: bloquear controles/envío antes de interceptación JS; (2) B pide verificar que «Volver a editar» móvil enfoque un control dentro del viewport después del resumen centrado. El segundo es una hipótesis a comprobar, no un bug declarado sin evidencia. No se toca producto desde A.

El autoplay actual usa `announce=false` y no emite el evento de selección en su rotación; el contrato de formulario independiente protege la intención, pero no se cita la rotación como bug actual.

## Inspección visual y acuerdo de A

A inspeccionó con `view_image` los renders reales `preview-marketing-contact-2a-390.png`, `-1440.png`, `-1920.png` y `-review-390.png`. En390, servicios/contextos son legibles y los controles no están comprimidos; Desarrollo Web en dos líneas es aceptable. La longitud mayor es proporcional a las preguntas útiles y no justifica añadir un wizard. El ejemplo con ecommerce/B2B simultáneos demuestra la combinabilidad. El resumen mantiene las elecciones y señala que no se ha enviado.

En1440 y1920, Contáctanos conserva jerarquía, paleta y contraste de marca; la composición permanece centrada y la tarjeta no se amplía indefinidamente. La nota de propuesta izquierda aparecía algo grande por specificity del estilo heredado: Orchestrator ajustará su escala secundaria. Las sublabels se corrigen de11 a12px. No son razones para reemplazar la dirección.

Correcciones de fuente re-leídas por A: `fieldset.cp-controls` deshabilitado nativamente en HTML y habilitado solo al final después de instalar el handler local; editar retorna el foco al primer checkbox y hace `scrollIntoView({block:'center',behavior:'auto'})`. Root informa QA a320/390/768/1024/1440/1920 de campos, estado, CTA aditivo, teclado, conservación al alternar canales, ausencia de transmisión/storage y overflow. A no presenta esa batería como una ejecución propia.

**A acepta REFINAR por V1**, sin objeción material de dirección. La alternativa mínima con solo correo pierde la preferencia de respuesta explícita del usuario y contexto útil opcional; mantener V0 pierde necesidades combinadas; wizard pierde simplicidad sin ganancia acreditada. No se requiere una variante estética de B para simular deliberación.

Originalidad/interchangeability: el formulario usa patrones familiares y no demuestra una ventaja exclusiva por sus campos. Es específico por la combinación explícita de gestión Meta/Google, proyecto Web y software independiente, dentro de Órbita; **KEEP — SPECIFIC AND DEFENSIBLE** para esta ejecución sin claim de novedad absoluta. Medición de conversión NOT AVAILABLE. Capacidad del resumen local BUILD NOW; envío real LATER, fuera del scope y sin receptor inventado.

Aceptación de diseño, no aprobación humana de un cambio material de conversión. La sustitución pública del cierre requiere la decisión del usuario sobre este mockup concreto conforme al section package; A no modifica producto ni publica. Pendiente únicamente inspección de captures finales si cambia el ajuste de nota/sublabel, sin reabrir estrategia por spacing.
