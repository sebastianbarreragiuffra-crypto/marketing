/* Manual views; only the ads receive a single entrance per page load. */
(() => {
  const hero = document.querySelector('.hx-marketing-reference');
  if (!hero) return;
  const tabs = [...hero.querySelectorAll('.hx-tab')];
  const panels = tabs.map(tab => document.getElementById(tab.getAttribute('aria-controls')));
  const ads = hero.querySelector('.ha-ads');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  let active = tabs.findIndex(tab => tab.getAttribute('aria-selected') === 'true');
  let entered = reduced.matches;
  let entranceTimer, switchTimer, observer;
  function finishEntrance() {
    window.clearTimeout(entranceTimer);
    ads.classList.remove('is-entering');
  }
  function enterAds() {
    if (entered || panels[0].hidden) return;
    entered = true;
    observer?.disconnect();
    if (reduced.matches) return;
    ads.classList.add('is-entering');
    entranceTimer = window.setTimeout(finishEntrance, 660);
  }
  function show(index, focus = false) {
    if (index !== active) {
      finishEntrance();
      window.clearTimeout(switchTimer);
      panels.forEach((panel, i) => {
        panel.classList.remove('is-switching');
        panel.hidden = i !== index;
        tabs[i].setAttribute('aria-selected', String(i === index));
        tabs[i].tabIndex = i === index ? 0 : -1;
      });
      active = index;
      hero.dataset.slide = String(index);
      if (!reduced.matches) {
        panels[index].classList.add('is-switching');
        switchTimer = window.setTimeout(() => panels[index].classList.remove('is-switching'), 240);
      }
      if (index === 0) enterAds();
    }
    if (focus) tabs[index].focus();
  }
  tabs.forEach((tab, i) => {
    tab.disabled = false;
    tab.addEventListener('click', () => show(i));
    tab.addEventListener('keydown', event => {
      const last = tabs.length - 1;
      const next = { ArrowRight: i === last ? 0 : i + 1, ArrowLeft: i === 0 ? last : i - 1, Home: 0, End: last }[event.key];
      if (next === undefined) return;
      event.preventDefault();
      show(next, true);
    });
  });
  if (!entered && 'IntersectionObserver' in window) {
    observer = new IntersectionObserver(entries => {
      if (entries.some(entry => entry.isIntersecting)) enterAds();
    }, { threshold: 0.08 });
    observer.observe(ads);
  } else if (!entered) enterAds();
  reduced.addEventListener('change', event => {
    if (!event.matches) return;
    entered = true;
    observer?.disconnect();
    finishEntrance();
    window.clearTimeout(switchTimer);
    panels.forEach(panel => panel.classList.remove('is-switching'));
  });
})();
