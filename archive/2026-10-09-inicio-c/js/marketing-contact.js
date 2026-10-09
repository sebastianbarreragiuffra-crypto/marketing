(() => {
  const form = document.querySelector('#contact-proposal-form');
  if (!form) return;
  const contact = document.querySelector('#contacto');
  const showcase = document.querySelector('.marketing-services-showcase');
  const review = document.querySelector('#cp-review');
  const error = form.querySelector('#cp-error');
  const services = { meta: 'Meta Ads', google: 'Google Ads', tiktok: 'TikTok Ads', web: 'Desarrollo Web', software: 'GISBA (software)' };
  const business = { ecommerce: 'Tienda online (Ecommerce)', b2b: 'Venta a empresas (B2B)', other: 'Otro' };
  const channels = ['email', 'phone'];
  const fields = Object.fromEntries(channels.map(id => [id, form.querySelector(`#cp-${id}`)]));
  const activeChannel = () => form.querySelector('[name="channel"]:checked').value;

  function clearError() {
    error.hidden = true;
    error.textContent = '';
    channels.forEach(id => fields[id].removeAttribute('aria-invalid'));
  }
  function edit() {
    review.hidden = true;
    form.hidden = false;
  }
  function showChannel() {
    clearError();
    channels.forEach(id => {
      const active = id === activeChannel();
      form.querySelector(`[data-cp-channel="${id}"]`).hidden = !active;
      fields[id].disabled = !active;
      fields[id].required = active;
    });
  }
  form.querySelectorAll('[name="channel"]').forEach(input => input.addEventListener('change', showChannel));
  form.addEventListener('input', clearError);

  document.querySelectorAll('a[href="#contacto"]').forEach(link => link.addEventListener('click', () => {
    edit();
    if (link.hasAttribute('data-ms-quote')) {
      const selected = showcase?.dataset.msActive;
      const choice = form.querySelector(`[name="services"][value="${selected}"]`);
      if (choice) choice.checked = true;
    }
    requestAnimationFrame(() => contact.querySelector('#contact-title').focus({ preventScroll: true }));
  }));

  form.addEventListener('submit', event => {
    event.preventDefault();
    clearError();
    const channel = activeChannel();
    const field = fields[channel];
    field.value = field.value.trim();
    const value = field.value;
    let message;
    if (!value) message = channel === 'email' ? 'Escribe un correo para que podamos responderte.' : 'Escribe un número con código de país.';
    else if (channel === 'email' && !field.checkValidity()) message = 'Revisa el correo. Por ejemplo: nombre@empresa.cl';
    else if (channel === 'phone' && (!/^\+[\d\s().-]+$/.test(value) || value.replace(/\D/g, '').length < 7 || value.replace(/\D/g, '').length > 15)) message = 'Revisa el número e incluye el código de país. Por ejemplo: +56 9 1234 5678';
    if (message) {
      error.textContent = message;
      error.hidden = false;
      field.setAttribute('aria-invalid', 'true');
      field.focus();
      return;
    }
    const selected = name => [...form.querySelectorAll(`[name="${name}"]:checked`)].map(input => input.value);
    const summaries = {
      services: selected('services').map(id => services[id]).join(' · ') || 'Por definir',
      business: selected('business').map(id => business[id]).join(' · ') || 'Sin especificar',
      company: form.querySelector('#cp-company').value.trim() || 'Sin especificar',
      contact: `${channel === 'email' ? 'Correo' : 'Teléfono'}: ${value}`
    };
    Object.entries(summaries).forEach(([key, text]) => { review.querySelector(`[data-cp-summary="${key}"]`).textContent = text; });
    form.hidden = true;
    review.hidden = false;
    review.querySelector('#cp-review-title').focus({ preventScroll: true });
    review.scrollIntoView({ block: 'center', behavior: 'auto' });
  });
  review.querySelector('[data-cp-edit]').addEventListener('click', () => {
    edit();
    const firstChoice = form.querySelector('[name="services"]');
    firstChoice.focus({ preventScroll: true });
    firstChoice.scrollIntoView({ block: 'center', behavior: 'auto' });
  });
  showChannel();
  // The form remains disabled unless its local submit handler is ready.
  form.querySelector('.cp-controls').disabled = false;
})();
