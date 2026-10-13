(() => {
  const rotator = document.querySelector('[data-hero-rotator]');
  if (!rotator) return;

  const deck = rotator.querySelector('.v6-showcase__deck');
  const cards = [...rotator.querySelectorAll('[data-ad]')];
  const channels = [...rotator.querySelectorAll('[data-channel]')];
  const playButton = rotator.querySelector('[data-play-toggle]');
  const status = rotator.querySelector('[data-rotator-status]');
  const mobile = window.matchMedia('(max-width: 700px)');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const order = ['meta', 'google', 'tiktok'];
  let active = 'meta';
  let userPaused = false;
  let panelVisible = false;
  let timer = null;

  function stopTimer() {
    if (timer !== null) window.clearTimeout(timer);
    timer = null;
  }

  function canPlay() {
    return mobile.matches && !reducedMotion.matches && !userPaused && panelVisible && !document.hidden;
  }

  function setActive(name, announce = false) {
    active = name;
    rotator.dataset.activeChannel = name;
    cards.forEach((card) => card.classList.toggle('is-active', card.dataset.ad === name));
    channels.forEach((button) => {
      const selected = button.dataset.channel === name;
      button.classList.toggle('is-active', selected);
      button.setAttribute('aria-pressed', String(selected));
    });
    syncAccessibility();
    if (announce) status.textContent = `Ejemplo de ${name === 'meta' ? 'Meta' : name === 'google' ? 'Google' : 'TikTok'} seleccionado. Cambio automático pausado.`;
  }

  function syncAccessibility() {
    cards.forEach((card) => {
      if (mobile.matches && card.dataset.ad !== active) {
        card.setAttribute('aria-hidden', 'true');
        card.inert = true;
      } else {
        card.removeAttribute('aria-hidden');
        card.inert = false;
      }
    });
  }

  function syncPlayButton() {
    const stopped = userPaused || reducedMotion.matches;
    playButton.classList.toggle('is-paused', stopped);
    playButton.disabled = reducedMotion.matches;
    const label = reducedMotion.matches
      ? 'Cambio automático desactivado por preferencia de movimiento'
      : userPaused ? 'Reproducir cambio automático' : 'Pausar cambio automático';
    playButton.setAttribute('aria-label', label);
    playButton.title = label;
    rotator.dataset.autoState = reducedMotion.matches ? 'reduced-motion' : userPaused ? 'paused' : canPlay() ? 'playing' : 'waiting';
  }

  function schedule() {
    stopTimer();
    syncPlayButton();
    if (!canPlay()) return;
    timer = window.setTimeout(() => {
      const next = order[(order.indexOf(active) + 1) % order.length];
      setActive(next);
      schedule();
    }, 3000);
  }

  channels.forEach((button) => button.addEventListener('click', () => {
    userPaused = true;
    setActive(button.dataset.channel, true);
    schedule();
  }));

  playButton.addEventListener('click', () => {
    if (reducedMotion.matches) return;
    userPaused = !userPaused;
    status.textContent = userPaused ? 'Cambio automático pausado.' : 'Cambio automático reanudado.';
    schedule();
  });

  const observer = new IntersectionObserver((entries) => {
    panelVisible = entries[0].intersectionRatio >= 0.5;
    schedule();
  }, { threshold: [0, 0.5, 1] });
  observer.observe(deck);

  document.addEventListener('visibilitychange', schedule);
  mobile.addEventListener('change', () => { syncAccessibility(); schedule(); });
  reducedMotion.addEventListener('change', schedule);
  window.addEventListener('pagehide', stopTimer);

  setActive('meta');
  schedule();
})();
