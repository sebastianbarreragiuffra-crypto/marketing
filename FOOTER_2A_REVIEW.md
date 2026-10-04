# Footer compartido · 2A · 2026-09-28

## Contexto y alcance
SITE / componente compartido de las seis páginas existentes. Foundation: `SITE_PAGES_BRIEF.md` v1.0, `WEBMASTER_CONTEXT.md`, decisiones y ampliación a Precios/Iniciar sesión solicitada por el usuario. BUILD autorizado por «Hazme el footer, corre flujo 2A para crearlo». Se preservan buyer ecommerce, ofertas independientes, marca provisional, paleta y destinos existentes; no se introduce una nueva decisión estratégica. No hay publicación ni cambios a Webmaster.

Search Gate de esta intervención: NOT APPLICABLE a investigación nueva; no crea páginas ni cambia intención o arquitectura. Contribución SUPPORTING mediante enlaces HTML descriptivos a las páginas existentes. Sin afirmaciones sobre rankings, tráfico o conversión observados.

## V0 → A → B → 2A
V0: footer actual con marca, descriptor y copyright en una sola fila. Conserva identidad, pero obliga a volver al encabezado para cambiar de solución o encontrar precios/acceso.

A / V1-A: tres columnas con identidad y descripción breve, soluciones y exploración del sitio; acceso directo a las seis páginas y retorno al encabezado. Un cierre comercial grande adicional se considera innecesario después del contacto existente.

B / SAME-RUNTIME CHALLENGE, no revisión independiente: lectura del problema desde el visitante que termina una página y necesita orientarse. Assumption attack: un footer lleno no implica más utilidad. Buyer/commercial reality: debe distinguir campañas gestionadas, bandeja para el equipo y proyectos, sin presentar una nueva oferta. Trust: redes, email, políticas y contacto reales no están disponibles; no crear enlaces vacíos ni inventar destinos. El acceso existe como maqueta: acompañarlo de «Acceso de clientes próximamente». Friction: navegación siempre visible en móvil, sin acordeones ni JavaScript nuevo.

Counterfactual: conservar V0 es más compacto pero mantiene el problema de orientación; un footer con gran CTA duplica el bloque anterior y sugiere contacto operativo; navegación agrupada resuelve la necesidad con destinos existentes. Premortem: el visitante espera autenticación activa o no encuentra una solución entre demasiadas opciones. La nota del acceso y dos grupos breves reducen esas ambigüedades. Resultado B: MODIFICAR A con nota de disponibilidad del acceso; preservar composición y enlaces.

2A FINAL: REFINAR. Marca y descriptor «Marketing y tecnología. Para tu ecommerce.»; Soluciones con Marketing/Software/Automatizaciones y subtítulos que expresan su trabajo; Explora Órbita con Inicio/Precios/Iniciar sesión; copyright provisional y Volver arriba. Sin repetición de precios ni CTA de contacto adicional. Se preservan los significados y la arquitectura autorizados; los cambios son de presentación y navegación secundaria.

Originalidad: combina las tres modalidades reales del proyecto, con vocabulario de campañas y consultas y la identidad visual aprobada; no incorpora imágenes decorativas ni novedades sin propósito. Evaluación interna cualitativa, no investigación de usuarios.

## Contrato de implementación / C
Desktop: identidad dominante y dos columnas de enlaces. Intermedio: identidad arriba y dos grupos debajo. Móvil: identidad y grupos apilados, sin contenido oculto. Sin imágenes, dependencias ni motion nuevo. Footer semántico, navs con nombres accesibles distintos, foco visible heredado, enlaces de al menos 44 px de alto, flechas decorativas fuera del nombre accesible. Misma estructura en las seis páginas. Verificar enlaces y anclas, retorno arriba, teclado, año, contraste, desbordamiento a 320/390/768/1024/1440 px y ausencia de errores JS.

Implementación: `css/footer-2a.css` y footer de los seis HTML. Validación y cierre se registran a continuación al terminar QA.

## C / validación y cierre
COMPLETE para el alcance de maqueta local. `verify-footer.cjs` y `footer-validation.json`: 30 combinaciones (seis páginas × 320/390/768/1024/1440 px) sin desbordamiento, un footer, destinos existentes, navegación etiquetada y objetivos de enlaces de al menos 44 px. Se recorrieron las seis páginas desde el footer móvil; teclado Tab/Enter con foco visible, año dinámico y retorno arriba correctos; sin errores JS. El retorno apunta al inicio del documento (`body#inicio-pagina`) porque el encabezado sticky no era un destino fiable.

Inspección visual: `preview-footer-1440.png` y `preview-footer-390.png`; también capturas a 320/768 px. Contraste calculado sobre #0b0d0b: texto secundario 9,47:1, principal 17,59:1 y lima 15,34:1. No representa auditoría WCAG completa ni prueba de producción. Contacto y autenticación reales siguen fuera de esta maqueta.

Completion & Learning Review: objetivo cumplido; memoria y decisiones actualizadas, sin cambios canónicos. Method learning: NOTHING REUSABLE (se aplicaron patrones existentes). Próximo paso: revisión visual del usuario, sin dependencia bloqueante para este footer.

## Reapertura v2 — feedback visual del usuario
Entrada: captura móvil aportada por el usuario y petición de modificar diseño/icono con 2A. La captura evidencia flechas representadas como emojis azules; no permite concluir un fallo de todo el layout porque es un recorte estrecho. Alcance autorizado: refinamiento de presentación, mismos contenidos/destinos. Foundation y Search Gate se mantienen.

V0: seis flechas diagonales de texto y filas separadas tanto en Soluciones como en Explora. A / V1-A: sustituir glifos por SVG de trazo fino y compactar el footer. B / SAME-RUNTIME CHALLENGE: desde la necesidad de orientación, reemplazar seis dibujos no resuelve la repetición visual; las flechas diagonales además pueden sugerir salida externa. Counterfactual: conservar glifos mantiene el problema observado; seis SVG corrigen el render pero conservan ruido; tres chevrons para soluciones y enlaces secundarios sin iconos mantienen orientación con menos decoración. Premortem: compactar demasiado reduce áreas táctiles o elimina claridad del acceso; conservar altura mínima de 44 px y nota de disponibilidad. Resultado B: MODIFICAR A.

2A FINAL v2: REFINAR. Tres chevrons neutros para soluciones; Inicio/Precios/Iniciar sesión sin flechas ni divisores individuales; tipografía y espaciado móvil más contenidos; retorno arriba en SVG. Mantener marca, paleta, descriptor y arquitectura. La corrección de la misma flecha diagonal en el HTML del resto del sitio usa SVG sin alterar sus acciones. La marca no se rediseña: el icono observado en la evidencia es la flecha. No se requieren imágenes raster.

C: 30 combinaciones responsive y seis recorridos de navegación aprobados nuevamente (`footer-validation.json`), teclado/foco/retorno correctos. `footer-icons-validation.json` verifica SVG decorativos con dimensiones visibles en las seis páginas, cuatro SVG por footer (tres chevrons y retorno), ningún icono en Explora y ninguna flecha diagonal de texto en enlaces. Se inspeccionaron capturas actualizadas móvil/escritorio y hero móvil. Pruebas locales en Edge/Chromium; iPhone físico y Safari no verificados (WebKit no instalado). El SVG elimina la dependencia de fuente emoji para estos iconos.

Completion Review v2: COMPLETE para el refinamiento local; no desplegado. Memoria y decisiones actualizadas. Aprendizaje: NOTHING REUSABLE, corrección técnica conocida de iconografía.
