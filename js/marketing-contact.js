(() => {
  const contact = document.querySelector('#contacto');
  const showcase = document.querySelector('.marketing-services-showcase');
  if (!contact || !showcase) return;
  const choices = [...contact.querySelectorAll('[data-contact-service]')];
  const heading = contact.querySelector('#contact-title');
  const request = contact.querySelector('[data-contact-request]');
  const submit = contact.querySelector('[data-contact-submit]');
  const services = { meta: 'Meta Ads', google: 'Google Ads', web: 'Desarrollo Web' };

  function selectContact(id) {
    request.textContent = services[id] || 'Consulta de marketing';
    submit.textContent = services[id] ? (id === 'web' ? 'Cotizar sitio web' : `Cotizar ${services[id]}`) : 'Solicitar propuesta';
    choices.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.contactService === id)));
  }
  document.addEventListener('orbita:marketing-service', event => selectContact(event.detail.service));
  choices.forEach(button => button.addEventListener('click', () => {
    const id = button.dataset.contactService;
    showcase.querySelector(`[data-ms-service="${id}"]`).click();
  }));
  document.querySelectorAll('a[href="#contacto"]').forEach(link => link.addEventListener('click', () => {
    if (link.hasAttribute('data-ms-quote')) selectContact(showcase.dataset.msActive);
    else selectContact(null);
    requestAnimationFrame(() => heading.focus({preventScroll: true}));
  }));
})();
