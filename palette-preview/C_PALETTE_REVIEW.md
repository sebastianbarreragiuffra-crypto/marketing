# Directorio C · auditoría focalizada de color

Fecha: 2026-09-28. Solicitud: revisar secciones que no combinan. Modo AUDIT / FOCUSED COLOR. Resultado: diagnóstico y propuesta visual separada; los HTML y CSS del sitio no fueron modificados. Las páginas en esta carpeta son copias de revisión, no nuevas rutas del producto.

## Hallazgos
- TUNE: Inicio acumula marfil #f4f1e8, beige #eae6dc, verde pastel #e1efbe, bosque #14231a y otro pastel #dcefa8 antes de regresar a negro. La variación es observable; que debilite continuidad es juicio visual de C, no dato de usuarios.
- TUNE: interiores usan héroes #142016 y paneles oscuros #172017 distintos del encabezado/footer #0b0d0b. Software añade otro gris verdoso #e9eee3. Se propone una jerarquía consistente de fondo y panel.
- FIX: énfasis verde del título Soluciones: contraste calculado 2,79:1 contra su fondo actual. Propuesta 6,18:1. Se midieron colores computados, sin inferir accesibilidad completa del sitio.
- KEEP: lima #c7f45b en acentos y rutas destacadas; negro de header/footer; marfil cálido. No se modifica layout, oferta, copy, estado del acceso ni contacto desactivado. No se implementa el mockup de footer anterior.

## Propuesta
| Función | Color |
|---|---|
| Fondo oscuro | #0b0d0b |
| Panel sobre oscuro | #171d17 |
| Fondo claro | #f6f3eb |
| Superficie secundaria | #eeeae0 |
| Acento | #c7f45b |
| Verde de texto sobre claro | #48622e |

Inicio: Soluciones marfil; Marketing y Antes de empezar gris cálido, con separación fina; FAQ negro; Contacto marfil; footer negro. Reservar los verdes intensos para contenido destacado. Las ilustraciones pueden mantener matices funcionales, sin convertir cada sección en una paleta propia.

## Validación de propuesta
`validation.json`: seis páginas a 320/390/768/1440 px, sin desbordamiento, un H1, imágenes cargadas y sin errores JS. FAQ con teclado y menú móvil comprobados. Render inspeccionado de Inicio escritorio/móvil; Contacto y FAQ en capturas móviles de tamaño real. Contraste de énfasis de cinco títulos de Inicio medido antes/después: propuesta entre 5,71:1 y 15,34:1. No se afirma auditoría WCAG global; Safari/iPhone real no verificados. C no ejecutó research Search ni motion/performance exhaustivo: alcance focalizado, sin dependencias nuevas ni cambios de comportamiento.

## Entrega
`index.html` permite recorrer el preview de Inicio; `index-1440.png` muestra la composición completa; `contact-390.png` y `faq-390.png` permiten revisar el detalle móvil. `palette.css` contiene únicamente la propuesta cromática. No hay despliegue. Los enlaces de navegación de estas copias apuntan a las páginas existentes, no a otras copias; abrir cada HTML de esta carpeta para revisar la paleta propuesta en interiores.

Cierre: auditoría completada, propuesta renderizada y verificada; aplicación al sitio pendiente de decisión sobre esta propuesta. Sin cambios a Webmaster ni aprendizajes canónicos. NOTHING REUSABLE.

## Aplicación posterior autorizada
2026-09-28: tras «hazlo», propuesta aplicada como `css/palette.css` en los seis HTML del sitio. COMPLETE. `palette-applied-validation.json`: 24 combinaciones a 320/390/768/1440 px aprobadas, colores computados de contacto y heroes confirmados, navegación móvil y FAQ por teclado correctas, sin errores JS. Inspección de captura de Inicio aplicado en escritorio. Se conserva limitación de Safari/iPhone real no verificado. Memoria/decisiones actualizadas; no hubo despliegue externo.
