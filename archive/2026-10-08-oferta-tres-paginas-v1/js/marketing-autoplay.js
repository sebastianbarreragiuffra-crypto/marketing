(() => {
  const section = document.querySelector('.marketing-services-showcase');
  if (!section) return;
  const tablist = section.querySelector('.ms-tabs');
  const dashboard = section.querySelector('.ms-dashboard');
  const tabs = [...tablist.querySelectorAll('[data-ms-service]')];
  const plans = [...section.querySelectorAll('[data-ms-plan]')];
  const label = section.querySelector('.ms-preview-label');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const canObserve = 'IntersectionObserver' in window;
  const interval = 3000;
  if (!label || !dashboard || tabs.length < 2) return;

  const controls = document.createElement('div');
  controls.className = 'ms-preview-controls';
  const toggle = document.createElement('button');
  toggle.className = 'ms-auto-toggle';
  toggle.type = 'button';
  label.before(controls);
  controls.append(label, toggle);

  let playing = !reducedMotion.matches && canObserve;
  let visible = false;
  let tabsVisible = false;
  let dashboardVisible = false;
  let hovering = false;
  let timer;
  let frame;

  function canRotate() {
    return playing && visible && !hovering && !document.hidden && !reducedMotion.matches;
  }

  function schedule() {
    window.clearTimeout(timer);
    window.cancelAnimationFrame(frame);
    section.classList.remove('is-ms-rotating');
    toggle.hidden = reducedMotion.matches || !canObserve;
    toggle.textContent = playing ? 'Pausar' : 'Reanudar';
    toggle.setAttribute('aria-label', `${toggle.textContent} cambio automático de servicios`);
    if (!canRotate()) return;
    frame = window.requestAnimationFrame(() => {
      if (!canRotate()) return;
      section.classList.add('is-ms-rotating');
      timer = window.setTimeout(() => {
        const current = tabs.findIndex(tab => tab.getAttribute('aria-selected') === 'true');
        const next = tabs[(current + 1) % tabs.length];
        section.dispatchEvent(new CustomEvent('orbita:marketing-auto-select', { detail: next.dataset.msService }));
        section.classList.remove('is-ms-switching');
        window.requestAnimationFrame(() => section.classList.add('is-ms-switching'));
        schedule();
      }, interval);
    });
  }

  function pause() {
    if (!playing) return;
    playing = false;
    schedule();
  }

  tabs.forEach(tab => {
    tab.addEventListener('click', event => { if (event.isTrusted) pause(); });
    tab.addEventListener('keydown', pause);
  });
  plans.forEach(plan => plan.addEventListener('click', event => { if (event.isTrusted) pause(); }));
  section.addEventListener('focusin', event => { if (event.target !== toggle) pause(); });
  section.addEventListener('pointermove', event => {
    if (event.pointerType !== 'mouse') return;
    if (event.movementX === 0 && event.movementY === 0) return;
    if (hovering) return;
    hovering = true;
    schedule();
  });
  section.addEventListener('pointerleave', event => {
    if (event.pointerType !== 'mouse') return;
    hovering = false;
    schedule();
  });
  toggle.addEventListener('click', () => {
    playing = !playing;
    if (playing) hovering = false;
    schedule();
  });
  document.addEventListener('visibilitychange', schedule);
  reducedMotion.addEventListener('change', () => {
    if (reducedMotion.matches) playing = false;
    schedule();
  });
  if (canObserve) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.target === tablist) tabsVisible = entry.intersectionRatio >= .5;
        if (entry.target === dashboard) dashboardVisible = entry.intersectionRatio >= .1;
      });
      visible = tabsVisible || dashboardVisible;
      schedule();
    }, { threshold: [0, .1, .5] });
    observer.observe(tablist);
    observer.observe(dashboard);
  }
  schedule();
})();
