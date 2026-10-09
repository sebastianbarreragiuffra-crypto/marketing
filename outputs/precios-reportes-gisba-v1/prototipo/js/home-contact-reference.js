/* Vista previa de Inicio: cambia el canal en pantalla, sin guardar ni enviar datos. */
(() => {
  const form = document.querySelector('#hc-form');
  if (!form) return;
  const controls = form.querySelector('.hc-controls');
  const channels = form.querySelectorAll('input[name="hc-channel"]');
  const fields = form.querySelectorAll('[data-hc-channel]');

  // Impide también el envío implícito con Enter. No hay destino de contacto configurado.
  form.addEventListener('submit', event => event.preventDefault());
  function updateChannel() {
    const active = form.querySelector('input[name="hc-channel"]:checked').value;
    fields.forEach(field => {
      const input = field.querySelector('input');
      const selected = field.dataset.hcChannel === active;
      field.hidden = !selected;
      input.disabled = !selected;
      input.required = selected;
    });
  }
  channels.forEach(channel => channel.addEventListener('change', updateChannel));
  updateChannel();
  // Si el script no carga, los campos permanecen deshabilitados; no se genera un GET.
  controls.disabled = false;
})();
