# Inicio · acciones de conversión · 2026-09-28

El usuario señaló que la portada explicaba la oferta, pero después del hero faltaban acciones directas para agendar reunión, agendar demo o cotizar. Autorizó agregar estas llamadas a la acción antes de conectar el número de WhatsApp. Este cambio no modifica las seis secciones ni la oferta aprobada.

| Lugar | Acción visible | Destino en la maqueta |
|---|---|---|
| Selector, después de las tres tarjetas | Cotizar marketing · Agendar demo · Cotizar proyecto | Contacto con intención correspondiente |
| Método de Marketing | Cotizar marketing (principal) · Ver el servicio (secundaria) | Contacto o `marketing.html` |
| Acuerdo de alcance | Agendar reunión | Contacto general |
| FAQ | Agendar reunión | Contacto general |
| Contacto | Marketing · Software · Proyecto | Cambia título, explicación y texto de la acción final |

Las tarjetas de oferta conservan sus enlaces a las páginas interiores. Los nuevos enlaces están fuera de las tarjetas para evitar enlaces anidados. El bloque final muestra `WhatsApp de ventas por configurar` y mantiene el botón externo desactivado; así no simula un envío ni una reserva real. Un único WhatsApp de ventas será el destino de las tres rutas cuando se proporcione el número completo. Aún no se ha facilitado ese número, por lo que tampoco se crean URLs `wa.me` ficticias.

Validación local: `verify-landing.cjs` pasó en 390/768/1440 px para las cuatro páginas de oferta. La revisión específica de Inicio comprobó 320/390/768/1440 px sin desbordamiento ni errores JS; los enlaces de cada intención llevan a `#contacto`, actualizan título/acción y dejan seleccionado el camino correcto. La reunión general no marca una oferta arbitraria. Capturas: `preview-home-cta-*.png`.

Se añadieron CTA (llamadas a la acción). No hay analítica ni datos observados para calcular CTR orgánico o tasa de clic en estos CTA. Cuando exista medición, cada ubicación e intención deberá registrarse con un denominador y periodo explícitos.
