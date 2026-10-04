# Inicio · longitud y densidad · Directorios A+B / 2A · 2026-09-28

Alcance: estrategia de la portada `index.html`, no cambio de las páginas interiores. Brief padre: `SITE_PAGES_BRIEF.md` v1.0 (Inicio público/indexable, Search Gate REQUIRED), con dirección vigente en `WEBMASTER_CONTEXT.md` y decisiones project-local. Buyer principal: ecommerce que busca gestión de marketing; ruta secundaria: software para equipo interno; tercera compra: proyecto a medida. Trabajo de Inicio: entender la oferta y escoger la página adecuada. Tráfico, scroll, CTR y conversión observados: NOT AVAILABLE.

## V0 medido

La portada tiene ocho secciones antes del footer: hero, selector, Marketing, Software, Automatizaciones, «Así empezamos», FAQ y contacto. En viewport de 390 × 844 px, `scrollHeight` es 12.035 px (unas 14,3 alturas de pantalla); a 768 × 900, 9.819 px; a 1440 × 900, 8.158 px. La medición es de layout local, no de comportamiento de usuarios.

| Sección | Alto móvil 390 px | Función actual | Lectura de A |
|---|---:|---|---|
| Hero | 1.407 px | Promesa y rutas Marketing/Software | Mantener el mensaje; ajustar altura en ejecución |
| Selector | 1.789 px | Tres compras distintas | Mantener; reducir altura de tarjetas en móvil |
| Marketing | 1.638 px | Profundizar servicio principal | Mantener una prueba editorial más breve |
| Software | 1.465 px | Reexplicar bandeja y suscripción | Llevar el detalle a `software.html`; conservar ruta temprana |
| Automatizaciones | 1.529 px | Reexplicar proyecto a medida | Llevar el detalle a `automatizaciones.html`; conservar ruta temprana |
| Así empezamos | 1.331 px | Compra consultiva y responsabilidades | Convertir en franja corta de alcance antes de empezar |
| FAQ | 1.054 px | Resolver objeciones | Conservar tres dudas de mayor alcance; otras en páginas interiores |
| Contacto | 898 px | Conversación prevista | Conservar como maqueta; requiere número real para convertir |

Los tres bloques de ofertas ocupan 4.632 px en móvil después de que el hero y el selector ya han presentado esas ofertas y enlazado a sus páginas. Esto explica la sensación de longitud mejor que el número de palabras por sí solo. El contacto comienza cerca del píxel 10.289 en móvil y permanece desactivado por falta de número de ventas.

## Directorio A · V1-A

La información central es pertinente, pero está desarrollada con profundidad de página interior en Inicio. Propuesta de seis bloques: (1) hero actual, (2) selector de tres modalidades más compacto, (3) Marketing gestionado como prueba principal en un solo bloque breve, (4) franja de «cómo se acuerda el alcance» con responsabilidades, (5) FAQ de tres preguntas transversales — compras separadas, quién responde, inversión en anuncios —, (6) contacto. El detalle de bandeja, canales, agentes y proyecto queda en las páginas interiores ya enlazadas. Mantener los dos enlaces del hero y los tres del selector. Desktop: ritmo de un bloque por decisión; móvil: menos paneles de más de una pantalla y lectura por escaneo.

Efecto esperado, como hipótesis: llegar antes a una decisión sin perder la explicación de las tres compras. No se predice una mejora numérica de conversión ni Search. La portada conserva suficiente contenido propio: promesa, diferencias de modalidad, alcance del servicio principal y responsabilidades.

## Directorio B · SAME-RUNTIME CHALLENGE

Modo real: desafío del mismo runtime, no revisión independiente. Independent pass: «larga» por sí sola no demuestra abandono; las personas pueden saltar mediante enlaces tempranos. El problema más defendible es la repetición de oferta en bloques completos. B cuestiona eliminar demasiado: el software es una oferta independiente y debe seguir visible antes de abandonar Inicio; Marketing no puede quedar solo en una tarjeta porque es la compra primaria. También cuestiona usar un objetivo fijo de píxeles o de “pantallas” sin datos de usuarios. El contacto desactivado es una fricción de conversión mayor que la longitud y no se resuelve con recortes.

Counterfactuals: mantener todo preserva detalle pero duplica páginas interiores; solo reducir padding acorta algo sin corregir el trabajo repetido; suprimir todos los bloques explicativos convertiría Inicio en un índice superficial. Premortem de V1-A: un comprador interpreta que Órbita solo vende marketing o no distingue el portal de la bandeja. Condición de B: el hero y el selector deben conservar la independencia del software, quién atiende consultas y una ruta clara hacia `software.html`; el FAQ debe preservar la distinción agencia/equipo.

Resultado de B: MODIFICAR A para fijar esos mínimos semánticos y no tratar la reducción de altura como objetivo aislado.

## 2A FINAL — REFINAR, aprobado e implementado

Portada más corta con seis bloques. Se conservan hero, selector, explicación breve de Marketing, FAQ esencial y contacto; se fusiona «Así empezamos» en una franja de alcance. Los bloques completos de Software y Automatizaciones salen de Inicio, pero sus rutas y proposiciones permanecen en hero/selector, con detalle en páginas interiores. Se comprobó el diseño en móvil y escritorio; 12.035 px es la línea base, no una cuota obligatoria. El resultado busca menos repetición y mejor page mapping, no un ranking o tasa de conversión prometidos.

Originalidad/interchangeability: conservar la división real entre agencia, equipo que usa la bandeja y proyecto a medida; eliminar la repetición de paneles, no esa diferencia comercial. Search: Inicio mantiene tema amplio; las páginas interiores poseen el detalle de cada intención. Organic CTR hypothesis: una ruta más clara podría atraer visitas más pertinentes a interiores; NOT OBSERVED. CTA conversion: NOT AVAILABLE.

Criterios de implementación: todas las ofertas distinguibles en primer recorrido; enlaces funcionales a tres páginas; roles agencia/equipo/portal claros; inversión publicitaria separada; sin canales o resultados inventados; móvil sin bloques redundantes, desbordamiento ni errores JS; comparación visual antes/después. Contacto real se verifica cuando exista el número.

Estado: el usuario aprobó acortar la portada con «puedes hacerlo o reacortarlo». Se implementó la estructura de seis bloques en `index.html`; la versión anterior se conserva en `mockups/home-before-compact-2a.html`. Las páginas interiores mantienen el detalle de Software y Automatizaciones.

## Ejecución y validación

La portada presenta hero, selector de las tres compras, Marketing gestionado, franja de acuerdo de alcance, tres preguntas frecuentes transversales y contacto. El hero y el selector conservan rutas a Marketing, Software y Automatizaciones; la tarjeta de Software explicita la suscripción independiente para el equipo del cliente. Se retiraron los bloques completos de Software y Automatizaciones y la repetición del proceso. Los estilos específicos están en `css/home-compact-2a.css`.

| Viewport | V0 | Implementado | Reducción |
|---|---:|---:|---:|
| 390 × 844 | 12.035 px | 6.920 px | 42,5 % |
| 768 × 900 | 9.819 px | 5.443 px | 44,6 % |
| 1440 × 900 | 8.158 px | 4.811 px | 41,0 % |

A 320 × 844 px, la portada mide 7.545 px. En 320, 390, 768 y 1440 px no se detectó desbordamiento horizontal. La regresión `verify-landing.cjs` pasó para las cuatro páginas de oferta a 390, 768 y 1440 px: H1 único, imágenes, enlaces/anclas, menú, FAQ y ausencia de errores JS. Evidencia: `landing-validation.json` y `preview-home-compact-*.png`. Se inspeccionaron visualmente las capturas de móvil y escritorio. Estas medidas describen layout local, no uso ni conversión. El contacto sigue desactivado hasta disponer de un número real.

Iteración posterior, autorizada tras la revisión independiente A+B: `LANDING_FINAL_REVIEW_AB.md`. El Inicio a 390 px pasa a 6.308 px, con selector y hero móvil más contenidos. La medición anterior queda como registro de la primera compactación; las capturas actuales son `preview-home-final-*.png`.
