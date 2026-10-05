# Marketing · Contáctanos · Directorio B

2026-10-04 · v1 · INDEPENDENT REVIEW · pass inicial anterior a la recomendación de A.

Entrada: `MARKETING_CONTACT_2A.md` v1.0 READY FOR 2A; reglas/contexto/foundation/memoria/decisiones locales; fuente actual `marketing.html`, `js/marketing-contact.js`, `css/marketing-compact.css`; inspección visual propia de `preview-marketing-three-quality-public-contact-1440.png` y `preview-marketing-three-quality-public-contact-390.png`. No he leído la propuesta ni conclusiones del revisor A en esta primera pasada. Este archivo es mi único ámbito de escritura; no modifica producto, memoria, brief o publicación.

## Problema observado y opinión propia

El cierre actual expresa un único servicio, pero no permite contar que se necesita campaña + sitio + software ni preparar una vía de respuesta. Añadir contexto puede mejorar la utilidad de una conversación comercial; no hay datos que permitan afirmar mejora de conversión. Mantendría el diseño oscuro/lima y la estructura de tres secciones. La propuesta del usuario es pertinente si se convierte en una consulta breve y combinable, no en un formulario de calificación obligatorio.

Observación → ecommerce y B2B describen dimensiones distintas: una tienda online puede vender a empresas. Impacto → obligar a elegir una sola categoría produce contexto incompleto o una decisión artificial. Recomendación → dos casillas independientes y opcionales: «Vendo online (ecommerce)» y «Vendo a empresas (B2B)», con posibilidad de ambas o ninguna. Prioridad → alta.

Observación → la fuente actual actualiza la selección de contacto ante cada evento `orbita:marketing-service` y una elección de contacto activa la pestaña del showcase. Lectura adicional de `js/marketing-autoplay.js` confirma que el autoplay usa `selectService(..., false)` y actualmente no emite ese evento: no declaro un bug de autoplay observado. Impacto → las elecciones manuales del showcase sí sobrescriben el interés de contacto; Software tampoco tiene una pestaña pertinente. Recomendación → separar intereses de la consulta del estado de las tres vistas. Solo un CTA de cotización explícito incorpora su servicio, sin borrar los otros intereses ni los datos; preservar la separación ya existente del autoplay. Prioridad → alta.

Observación → el receptor/envío no está configurado y el usuario pidió ignorar esa configuración. Impacto → un formulario que afirma «enviado» o «te contactaremos» promete una operación inexistente. Recomendación → mockup interactivo local con «Ver resumen de consulta» y advertencia visible de no envío; datos ficticios de prueba, sin almacenamiento ni transmisión. Prioridad → alta.

## Candidatas y counterfactual

| Candidata | Valor, claridad y ajuste | Complejidad / genericidad | Resultado inicial |
|---|---|---|---|
| Mantener V0: un interés y botón desactivado | Muy corto y honesto, pero no admite necesidades combinadas ni responde a la nueva solicitud | Baja; conserva una elección artificial | Pierde frente a una propuesta breve. No falla por estética. |
| Formulario amplio literal: elección única de Meta/Google/Web/Software, ecommerce o B2B obligatorio, empresa/nombre/teléfono/correo requeridos | Recoge más datos, pero exige clasificación incorrecta y dos vías cuando basta una | Penalización de complejidad; rasgos de CRM genérico sin beneficio demostrado | Rechazar por fricción no justificada y modelo de negocio excluyente. |
| Consulta combinable mínima: cuatro intereses, contexto opcional, empresa/marca opcional y una vía de respuesta | Permite campaña + sitio + software, contacto breve y contexto real | Complejidad acotada y justificable; no intenta parecer original con controles novedosos | Preferida para mockup y challenge cruzado. |
| Alternativa proactiva: asistente/wizard que recomienda servicios a partir del negocio | Solo sería útil con reglas/alcances confirmados | Oculta decisiones, incorpora pasos y capacidades no respaldadas | No hacer en esta ronda; una consulta breve alcanza el objetivo. |

No asigno números de rendimiento ni puntuación precisa: no hay investigación propia de visitantes ni conversiones observadas. La candidata mínima gana cualitativamente en utilidad y claridad, mantiene factibilidad local y respeta la oferta independiente. La diferenciación procede de poder combinar campañas gestionadas, sitio y bandeja comercial; no del patrón visual del formulario. No hace falta crear una versión B artificial.

## Campos y requisitos recomendados

- «¿Qué te interesa?» con casillas nativas Meta Ads, Google Ads, Desarrollo Web y Software. Múltiple explícito. Admitir ninguna selección como consulta general evita obligar al visitante indeciso a elegir una compra; no añadir una quinta oferta «asesoría».
- Empresa o marca, opcional. No razón social ni RUT. Pedirla mejora contexto pero no es imprescindible para poder responder; un negocio en creación sigue siendo un prospecto válido.
- Contexto de negocio opcional, ambas casillas independientes. No reinterpretar la audiencia global de la página a B2B por este dato.
- «¿Cómo prefieres que te contactemos?» con selección exclusiva Correo / Teléfono. Mostrar únicamente el campo elegido y requerir solo ese campo para la validación de la vista previa. No exigir ambas vías ni forzar un país/rango estrecho.
- Conservar valores al alternar canal dentro de la sesión; usar el activo en el resumen. Etiquetas persistentes, estados nativos y foco visible. No guardar datos en localStorage ni enviar por red.
- No añadir nombre personal, presupuesto, facturación, URL, mensaje largo o plazo a esta primera propuesta sin una necesidad adicional. Cada pregunta extra necesita un uso real acreditado.
- No preseleccionar intereses por el servicio ilustrativo visible al cargar. Un CTA específico agrega el interés correspondiente; Hablemos genérico conserva lo ya preparado y no fuerza un reseteo.

La elección de una vía de respuesta y su requisito es una hipótesis práctica para poder responder una consulta, no evidencia de conversión. En el mockup se valida interacción con datos ficticios; no es captación pública ni backend listo.

## Premortem

Si el cambio empeorase la página: 1) el cierre podría alargarse en móvil y parecer registro obligatorio; mitigar haciendo contexto y empresa opcionales y dejando una sola vía visible; 2) el visitante podría creer que Software es parte incluida del plan elegido; conservar oferta separada y mostrarlo como interés; 3) entrar desde Google podría borrar una selección previa de Web o sus datos; aceptar adición explícita y no resetear; 4) nadie recibiría la consulta aunque se mostrase éxito; resumen local claramente identificado y sin envío; 5) «ecommerce / B2B» podría excluir negocios que son ambos o ninguno; casillas opcionales independientes.

La alternativa más fuerte todavía por contrastar con A es si empresa debe ser obligatoria o si un contexto de negocio único podría ser más claro. Mi criterio independiente es opcional y combinable; espero una justificación comercial observable para imponer más.

## Evidencia externa consultada

Consulta propia el 2026-10-04: [W3C, instrucciones de formularios](https://www.w3.org/WAI/tutorials/forms/instructions/) respalda etiquetas, formatos e instrucciones accesibles, y la distinción de campos obligatorios/opcionales. [GOV.UK, estructura de formularios](https://www.gov.uk/service-manual/design/form-structure) pide justificar el uso de cada pregunta y evitar preguntas irrelevantes mediante ramificaciones. Aplicar estos principios a un contacto comercial y usar una sola sección en vez de un wizard es una inferencia contextual; no una promesa de conversión ni una norma que dicte los campos comerciales.

## Estado

Preferencia inicial: REFINAR hacia consulta combinable mínima, pendiente del challenge de A y de un mockup real a 390/1440/1920. Aprobación estratégica final del formulario PENDING conforme al brief; no implementar/publicar un flujo de captación ni inventar un destino. El canal real permanece fuera de alcance por instrucción del usuario.

## Challenge cruzado sobre V1-A concreto

Tras mi pass independiente recibí la propuesta de A y sus dos revisiones previas: eliminar «Aún no lo sé» y cambiar WhatsApp a Correo / Teléfono. Leí `mockups/marketing-contact-a-review.md`, `mockups/marketing-contact-v1-a.html`, `mockups/marketing-contact-proposal.js` y `mockups/marketing-contact-proposal.css`.

A ya retiró la quinta opción para consulta general: B coincide porque intereses opcionales resuelven ese caso con menos controles. Correo / Teléfono conserva la elección solicitada sin forzar un canal histórico cuya configuración quedó fuera de alcance. Empresa opcional y contexto multiselección coinciden con mi preferencia independiente. La tercera casilla «Otro» no es mi mínima propuesta inicial, pero puede expresar una forma de venta no representada sin obligar a describirla; no encuentro una mejora material que obligue a retirarla ni a fabricar otro mockup. No debe convertir el contexto en una clasificación mutuamente excluyente.

La fuente V1 desacopla intereses de los eventos del showcase, incorpora el servicio del CTA específico y mantiene otros valores. No duplica una cuarta vista Software ni utiliza el resumen para afirmar entrega. Esa dirección satisface el problema identificado con complejidad acotada.

**Objeción material P1 antes de aceptar V1:** el HTML contiene un formulario con botón submit habilitado y depende de `preventDefault` en JavaScript. Si el script no carga o JavaScript está deshabilitado, la acción nativa es GET a la propia URL con los campos en la query: contradice «no envía ni guarda tu consulta» y puede exponer datos de prueba o visitantes en URLs. Un texto noscript no impide esa acción. Recomendación → guardia inicial nativa, como campos y botón deshabilitados en HTML y habilitación únicamente tras instalar la interceptación local, o controles sin envío nativo. C debe verificar el fallo/deshabilitación del script sin envío ni valores en URL. Es una limitación real de ejecución de la propuesta, no un desacuerdo de estrategia.

**Chequeo de retorno requerido:** al revisar un formulario largo, el resumen lleva el scroll al centro; «Volver a editar» enfoca el primer interés con `preventScroll`. C debe comprobar en móvil que el control enfocado queda visible al restituir el formulario y corregir el scroll si queda fuera del viewport. Pendiente de observar render/interacción; no lo declaro todavía como fallo reproducido.

Resultado provisional: MANTENER dirección V1-A / MODIFICAR ejecución antes de aceptación. Sin objeciones estratégicas pendientes; aceptación visual/funcional pendiente de renders y corrección P1.

## Inspección del mockup revisado

Inspeccioné personalmente `preview-marketing-contact-2a-390.png`, `preview-marketing-contact-2a-1440.png`, `preview-marketing-contact-2a-1920.png` y `preview-marketing-contact-2a-review-390.png`. V1 conserva la identidad y jerarquía de Contáctanos, muestra cuatro intereses sin exclusividad, ambas dimensiones del negocio seleccionadas juntas y una sola vía de contacto. En 390 las opciones se leen y activan con targets amplios; su mayor altura corresponde a las preguntas elegidas, no a una nueva sección ni al cuestionario de calificación rechazado. En 1920 el shell va de x240 a x1680: máximo útil 1440 centrado; la composición no se estira para llenar el ancho. En 1440 conserva márgenes y balance con la tarjeta.

La revisión local resume Meta Ads + Software y Ecommerce + B2B, identifica valores ficticios y no afirma entrega. «Volver a editar» es visible. No encuentro un cambio material más fuerte que justifique reemplazar esta dirección; el formulario mínimo de solo correo pierde la elección de número y el contexto opcional pedido, y el wizard añade pasos sin reglas comerciales suficientes.

Fuente revisada después de mis objeciones: `.cp-controls` está deshabilitado inicialmente en HTML y se habilita al final de la inicialización JS tras instalar el handler de submit; sublabels pasan a 12 px; al volver a editar se enfoca y desplaza al mismo primer interés. P1 de fuente resuelto, pendiente constatar evidencia de fallback/foco de C.

Originalidad/interchangeability: **KEEP — SPECIFIC AND DEFENSIBLE** para la dirección de sección. Los controles son patrones familiares; la especificidad justificable es combinar campañas gestionadas, sitio y software independiente con contexto no excluyente. No se inventa diferencial legal ni una estética nueva para simular originalidad. Se preservan buyer y Search direction de la página; registrar B2B no reposiciona el sitio.

Acuerdo cruzado real con A: A aceptó quitar quinta opción y usar Correo/Teléfono antes de V1; al preguntarme por «Otro», B lo acepta como dato opcional que distingue una forma de venta no representada de una omisión. Ambos mantienen targets y claridad en móvil, rechazando apretar el diseño o crear un wizard únicamente para disminuir altura. No hay consenso fabricado: las objeciones GET sin JS y retorno de edición exigieron correcciones concretas, y mi pass inicial precedió la lectura de A.

Estado: **MANTENER V1-A / REFINAR frente a V0**, aceptación de dirección y visual final; QA de guardia de fallo y foco pendiente de evidencia del Implementation Owner. Formulario final sigue PENDING decisión del usuario, sin producto editado/publicado desde B.

## Cierre de B — evidencia directa de las objeciones

Además de leer la fuente corregida, ejecuté una comprobación propia con Edge/Playwright a 390 × 844 sobre el mockup local, utilizando exclusivamente `demo@empresa.example`. En un contexto con JavaScript deshabilitado, todos los inputs y el botón del formulario cumplen `:disabled`: la guardia nativa bloquea entrada y envío. En un segundo contexto con JS, revisé la consulta y volví a editar: el foco termina en la casilla Meta Ads, su rectángulo vertical queda entre 322,8 y 339,8 px dentro del viewport de 844 y debajo de la navegación. La URL conserva query vacía. Prueba terminada con código 0; no se enviaron mensajes ni se almacenaron datos. La simulación de archivo bloqueado y la regresión de seis anchos corresponden al QA del owner, no los presento como pruebas propias.

Leí también `marketing-contact-validation.json` del owner: seis anchos 320/390/768/1024/1440/1920 sin desbordamiento ni errores registrados, input de 16 px y shell centrado <=1440. Esto respalda el alcance responsive; no acredita rendimiento comercial ni prueba de usuarios reales.

**B FINAL: MANTENER V1-A, REFINAR el cierre frente a V0.** Las dos objeciones concretas han sido corregidas y observadas en mi prueba; no quedan objeciones materiales de B para la propuesta. No hace falta otra variante estética. Aprobación pública del nuevo formulario PENDING; receptor/envío real fuera de alcance. B no editó ni publicó archivos de producto.
