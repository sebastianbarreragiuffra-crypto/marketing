(() => {
  const hero = document.querySelector('.hx');
  if (!hero) return;
  const tabs = [...hero.querySelectorAll('.hx-tab')];
  const panels = tabs.map(t => document.getElementById(t.getAttribute('aria-controls')));

  function show(index, focus) {
    tabs.forEach((tab, i) => {
      const on = i === index;
      tab.setAttribute('aria-selected', String(on));
      tab.tabIndex = on ? 0 : -1;
      panels[i].hidden = !on;
      panels[i].classList.toggle('is-switching', on);
    });
    hero.dataset.slide = String(index);
    if (focus) tabs[index].focus();
  }

  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => show(i));
    tab.addEventListener('keydown', e => {
      const last = tabs.length - 1;
      const next = { ArrowRight: i === last ? 0 : i + 1, ArrowLeft: i === 0 ? last : i - 1, Home: 0, End: last }[e.key];
      if (next === undefined) return;
      e.preventDefault();
      show(next, true);
    });
  });
})();
