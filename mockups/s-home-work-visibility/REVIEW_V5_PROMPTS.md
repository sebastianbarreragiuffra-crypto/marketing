# Sección 2 V5 — prioridad agencia/cliente

Fecha: 2026-10-11. Retoque autorizado de mockups, no de la web. Se conservan versiones anteriores y originales.

## Feedback y cambios

El usuario pidió reducir el espacio de la pieza publicitaria, priorizar la coordinación entre agencia y cliente y retirar el bloque inferior de condiciones. La pieza pasa a banner secundario; la conversación ilustrativa es más visible. Tres mensajes muestran contexto, comentario del cliente y respuesta humana de Órbita. No representan automatización, bot ni una interacción real.

Se conserva el mensaje de agencia, GISBA como apoyo y CTA «Agenda una reunión». Se retiran de esta sección los tres renglones de condiciones y el pie redundante de referencia. Se mantiene una identificación ilustrativa junto al chat.

## Información preservada

Antes de retirar las condiciones de las imágenes se verificó el código actual de Inicio: index.html contiene el usuario incluido, el costo adicional de usuarios extra y presupuesto publicitario aparte en el hero (v6-hero__terms) y en la respuesta de la primera FAQ. Por tanto no se propone eliminar esos hechos del sitio. No se cambió el código ni se afirmó una publicación nueva.

## Evidencia y límites

El aspecto de WhatsApp se usa como representación familiar de coordinación humana. Fuente conceptual vigente de la vuelta anterior: https://www.gisba.cl/#experiencia-cliente, pestaña WhatsApp con contexto. Imagen generada y conversación ficticia rotulada como ilustrativa; no es una captura real ni prueba de integración. Canal y acceso según alcance acordado.

Comprobados visualmente: reducción de espacio de la pieza, aumento de protagonismo del chat, actores y mensajes correctos, ausencia del bloque inferior, CTA y etiqueta ilustrativa. Exportaciones proporcionales de ancho1440 y390 comprobadas con export_v5.py. No se edita contenido gráfico en la exportación.

Pendientes: aprobación de la propuesta, contraste numérico, responsive/interacción del prototipo, accesibilidad y comprensión con personas. No se midió conversión ni rendimiento. Solo se escribieron archivos en mockups/s-home-work-visibility.

Aprendizaje metodológico: NOTHING REUSABLE nuevo. La prioridad de cada escena y conservación de información al fusionar/retirar ya forman parte de los protocolos existentes. Esta preferencia es específica de la sección.

## Prompts exactos — imagegen integrada

### Escritorio

Edit this DESKTOP Órbita section mockup in the same approved brand/composition. User requests the illustrative industrialad to occupy LESS SPACE and the HUMAN agency–clientconversation to be the main visual. Also remove the bottom purchaseconditions band, since those facts remain in the homepage hero and FAQ.
Preserve all LEFT-column headline/body/creativity-management-reviewicons and "Agenda una reunión" CTA. No navbar. Keep landscape16:9.
On the RIGHT, recompose as a compact landscape industrialadbanner at the TOP, approx180–220logicalpxhigh, instead of a giantproductadvertisement. Its valve subject must still be recognisable; image sitsRIGHT, adheadlineLEFT: "Equipamiento para tu operación." A small "Pieza de ejemplo" label. Remove the adsubheading and adCTA to declutter ifnecessary. Do not imitate a productcatalogue or cover the product with thechat.
Below thatbanner a LARGER, full-width WhatsApp-style chat excerpt, about250–300logicalpx high, clearly dominant over thebanner. Add ONE outside heading "Así nos coordinamos contigo". GreenWhatsAppheader, contact "Órbita · Tu agencia", pale beigebackground, outgoing greenclientbubble alignedRIGHT, incoming whiteagencybubbles alignedLEFT. Three exacthumanmessages:
"Te compartimos la propuesta." (agencyincoming)
"¿Podemos destacar más el producto?" (clientoutgoing)
"Ajustamos la propuesta." (agencyincoming)
Readable text, familiar paperclip/message/sendcomposer. No fakeonline status, dates, numbers or endbuyer chatbot. This is coordination between client and human agency.
Replace all olddisclosurelines near chat with ONE readable caption "Conversación ilustrativa · Canal según alcance." It is a generated depiction, not genuineWhatsAppcapture or evidence of actualintegration.
REMOVE the entire bottom conditionsline containing includeduser, extrausers and investmentapart, plus its dividingrule. Remove the otherbottomsourcecaption. No blank empty reservedstrip where thefooterusedtobe. Preserve side margins and stop at ordinarysectionbottompadding. Keep the agencyservice as mainmessage, GISBA mentioned in the unchanged supportingcopy. No newfeatures, metrics or promises.

### Móvil

Edit this MOBILE Órbita section mockup. The user wants a much SMALLER advertising-image area and more emphasis on the HUMAN AGENCY–CLIENT CONVERSATION. Also remove the purchaseconditions footer beneath the mainCTA, as these are already retained in the homepage hero and FAQ.

Preserve headline, supporting paragraph, brand colours/type, industrialvalve creative subject and brief admessage, WhatsApp look and mainCTA. Recompose mobile to be meaningfully shorter and readable at390width, high-resolution portrait output. Do not keep a tall enlarged productadvertisement.
1. SHRINK the ad photo area to a compact LANDSCAPE BANNER about170–190 CSSpx high at390width, around60–65% less height than the previousad. Preserve the valve visibly on theRIGHT side and small brief adheadline on theLEFT: "Equipamiento para tu operación." Remove adbody "Soluciones industriales" and the ad's "Conoce más" button if needed; the user wants to focus on coordination, not sell industrialequipment. Keep a small "Pieza de ejemplo" label. Do not crop the whole valve into an unrecognizablefragment; reframe the product for the smallerlandscapebanner.
2. The WHATSAPP conversation is now the main visual, full-width and around260–300 logicalpx tall, larger/readable than thebanner. Header familiargreen, WhatsApp name/logo, contact "Órbita · Tu agencia". Lightbeige chatbackground, outgoingclientgreen bubble onRIGHT, incomingwhite agencybubbles onLEFT. Three humanmessages exactly:
incomingagency "Te compartimos la propuesta."
outgoingclient "¿Podemos destacar más el producto?"
incomingagency "Ajustamos la propuesta."
Keep a simplecomposer "Mensaje" with paperclip/send icons. No fake times, online status, bot, AI or customer-sales message.
Add one short clear heading above the conversation "Así nos coordinamos contigo". Do not add other titles.
3. Replace ALL the previous3 disclosurelines near chat with just ONE modest readable line: "Conversación ilustrativa · Canal según alcance." This represents an example, not a genuine screenshot.
4. Retain a full-width prominent lime "Agenda una reunión" button BELOW the conversation and its disclosure.
5. REMOVE completely the3rows "1 usuario GISBA incluido", "Usuarios adicionales con costo extra", "Inversión publicitaria aparte", their icons, separatingrules and the very bottom "Recreación generada · Referencia: GISBA". Do not put them anywhere else in this mockup. END the section shortly after the mainCTA, with a smallnormalbottompadding. No emptyspace where removedfooterusedtobe.
No sidebar, charts, KPI, stepdiagrams, additionalfeatures, names, pricing or commercial promises. Do not change the overall copy into an independentsoftware offer. Output a realmobilelayout, widecontent with16–20CSSpx sidemargins, legible14–16CSSpx body, no giantpresentationborders. Generatedmockup only.

