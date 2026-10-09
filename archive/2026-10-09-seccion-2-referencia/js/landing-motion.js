/* Local illustrative task. Never sends a message or calls a service. */
(() => {
  const demo = document.querySelector('.sol-offer-2a .sol-task-demo');
  if (!demo) return;
  const button = demo.querySelector('.sol-demo-run');
  const status = demo.querySelector('.sol-demo-status');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  let timers = [];
  function stop() {
    timers.forEach(timer => window.clearTimeout(timer));
    timers = [];
    demo.removeAttribute('aria-busy');
    button.disabled = false;
  }
  function finish() {
    stop();
    demo.dataset.step = 'complete';
    status.textContent = 'Ejemplo completo: cotización enviada, cliente sin responder y próximo paso de seguimiento.';
  }
  button.disabled = false;
  button.addEventListener('click', () => {
    stop();
    if (reduced.matches) { finish(); return; }
    button.disabled = true;
    demo.setAttribute('aria-busy', 'true');
    demo.dataset.step = 'quote';
    status.textContent = 'Cotización del 12 de mar seleccionada.';
    timers.push(window.setTimeout(() => {
      demo.dataset.step = 'state';
      status.textContent = 'Estado: cliente sin responder hace 2 días.';
    }, 650));
    timers.push(window.setTimeout(() => {
      demo.dataset.step = 'next';
      status.textContent = 'Próximo paso: hacer seguimiento. No se envía ningún mensaje.';
    }, 1300));
    timers.push(window.setTimeout(finish, 1950));
  });
  reduced.addEventListener('change', event => {
    if (event.matches && timers.length) finish();
  });
  document.addEventListener('visibilitychange', () => {
    if (document.hidden && timers.length) finish();
  });
})();
