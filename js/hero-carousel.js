(() => {
  const hero = document.querySelector('.hx');
  if (!hero) return;
  const tabs = [...hero.querySelectorAll('.hx-tab')];
  const panels = tabs.map(t => document.getElementById(t.getAttribute('aria-controls')));
  const toggle = hero.querySelector('.hx-auto-toggle');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const canObserve = 'IntersectionObserver' in window;
  const interval = 7500;
  let activeIndex = tabs.findIndex(tab => tab.getAttribute('aria-selected') === 'true');
  let playing = !reduced.matches && canObserve;
  let visible = false;
  let timer;
  let frame;

  function canRotate() {
    return playing && visible && !document.hidden && !reduced.matches && tabs.length > 1;
  }

  function schedule() {
    window.clearTimeout(timer);
    window.cancelAnimationFrame(frame);
    const rotating = canRotate();
    hero.classList.remove('is-rotating');
    toggle.hidden = reduced.matches || !canObserve;
    toggle.textContent = playing ? 'Pausar' : 'Reanudar';
    toggle.setAttribute('aria-label', `${playing ? 'Pausar' : 'Reanudar'} cambio automático de vistas`);
    if (!rotating) return;
    frame = window.requestAnimationFrame(() => {
      if (!canRotate()) return;
      hero.classList.add('is-rotating');
      timer = window.setTimeout(() => {
        show((activeIndex + 1) % tabs.length, false);
        schedule();
      }, interval);
    });
  }

  function pause() {
    if (!playing) return;
    playing = false;
    schedule();
  }

  function show(index, focus) {
    tabs.forEach((tab, i) => {
      const on = i === index;
      tab.setAttribute('aria-selected', String(on));
      tab.tabIndex = on ? 0 : -1;
      panels[i].hidden = !on;
      panels[i].classList.toggle('is-switching', on);
    });
    activeIndex = index;
    hero.dataset.slide = String(index);
    if (focus) tabs[index].focus();
  }

  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => {
      pause();
      show(i);
    });
    tab.addEventListener('keydown', e => {
      const last = tabs.length - 1;
      const next = { ArrowRight: i === last ? 0 : i + 1, ArrowLeft: i === 0 ? last : i - 1, Home: 0, End: last }[e.key];
      if (next === undefined) return;
      e.preventDefault();
      pause();
      show(next, true);
    });
  });

  toggle.addEventListener('click', () => {
    playing = !playing;
    schedule();
  });
  hero.addEventListener('focusin', event => {
    if (!toggle.contains(event.target)) pause();
  });
  document.addEventListener('visibilitychange', schedule);
  reduced.addEventListener('change', () => {
    if (reduced.matches) playing = false;
    schedule();
  });
  if (canObserve) {
    const observer = new IntersectionObserver(entries => {
      visible = entries[0].intersectionRatio >= 0.5;
      hero.classList.toggle('is-in-view', visible);
      schedule();
    }, { threshold: 0.5 });
    observer.observe(hero.querySelector('.hx-tabs'));
  }
  schedule();
})();
