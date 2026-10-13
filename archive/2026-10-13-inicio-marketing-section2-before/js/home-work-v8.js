(() => {
  const section = document.querySelector('[data-work-section]');
  if (!section) return;

  const pauseButton = section.querySelector('[data-work-pause]');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const sceneNames = ['creative', 'management', 'client'];
  const counts = { creative: 2, management: 3, client: 2 };
  const positions = { creative: 0, management: 0, client: 0 };
  const timers = new Map();
  let isVisible = false;
  let isPaused = false;

  function render(name) {
    const scene = section.querySelector(`[data-work-scene="${name}"]`);
    if (!scene) return;
    scene.dataset.workState = String(positions[name]);
    scene.querySelectorAll(`[data-work-choice="${name}"]`).forEach(button => {
      const active = Number(button.dataset.index) === positions[name];
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    if (name === 'creative') {
      scene.querySelectorAll('[data-work-variant]').forEach(variant => {
        const active = Number(variant.dataset.workVariant) === positions[name];
        variant.classList.toggle('is-active', active);
        variant.setAttribute('aria-hidden', String(!active));
      });
    }
  }

  function stopTimers() {
    timers.forEach(timer => window.clearTimeout(timer));
    timers.clear();
  }

  function canRun() {
    return isVisible && !document.hidden && !isPaused && !reducedMotion.matches;
  }

  function schedule(name, delay) {
    const timer = window.setTimeout(() => {
      timers.delete(name);
      if (!canRun()) return;
      positions[name] = (positions[name] + 1) % counts[name];
      render(name);
      schedule(name, 3000);
    }, delay);
    timers.set(name, timer);
  }

  function syncPlayback() {
    stopTimers();
    pauseButton.hidden = reducedMotion.matches;
    pauseButton.textContent = isPaused ? 'Reanudar animaciones' : 'Pausar animaciones';
    pauseButton.setAttribute('aria-pressed', String(isPaused));
    if (!canRun()) return;
    sceneNames.forEach((name, index) => schedule(name, 3000 + index * 1000));
  }

  section.querySelectorAll('[data-work-choice]').forEach(button => {
    button.addEventListener('click', () => {
      const name = button.dataset.workChoice;
      positions[name] = Number(button.dataset.index);
      render(name);
      isPaused = true;
      syncPlayback();
    });
  });

  pauseButton.addEventListener('click', () => {
    isPaused = !isPaused;
    syncPlayback();
  });

  document.addEventListener('visibilitychange', syncPlayback);
  reducedMotion.addEventListener('change', syncPlayback);

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      isVisible = entries[0].isIntersecting;
      syncPlayback();
    }, { threshold: 0 });
    observer.observe(section);
  } else {
    const checkVisibility = () => {
      const bounds = section.getBoundingClientRect();
      const visibleNow = bounds.top < window.innerHeight && bounds.bottom > 0;
      if (visibleNow !== isVisible) {
        isVisible = visibleNow;
        syncPlayback();
      }
    };
    window.addEventListener('scroll', checkVisibility, { passive: true });
    window.addEventListener('resize', checkVisibility);
    checkVisibility();
  }

  sceneNames.forEach(render);
  syncPlayback();
})();
