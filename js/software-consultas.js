// Manual illustration: no messages, calls, downloads or API connections.
(() => {
  const module = document.querySelector('[data-consultas-demo]');
  if (!module) return;
  const tabs = [...module.querySelectorAll('[role="tab"]')];
  const panels = tabs.map(tab => document.getElementById(tab.getAttribute('aria-controls')));
  const mobile = window.matchMedia('(max-width: 1199px)');
  let selected = 0;
  const render = () => tabs.forEach((tab, index) => {
    tab.setAttribute('aria-selected', String(index === selected));
    tab.tabIndex = index === selected ? 0 : -1;
    const panel = panels[index];
    panel.hidden = mobile.matches && index !== selected;
    panel.setAttribute('role', mobile.matches ? 'tabpanel' : 'region');
    panel.tabIndex = mobile.matches ? 0 : -1;
    if (mobile.matches) panel.setAttribute('aria-labelledby', tab.id);
    else panel.removeAttribute('aria-labelledby');
  });
  const select = (index, keyboard = false) => {
    selected = index;
    render();
    if (keyboard) tabs[index].focus({ preventScroll: true });
    // Keep the selector visible when switching long mobile panels.
    const rect = tabs[index].getBoundingClientRect();
    const headerBottom = document.querySelector('.site-header')?.getBoundingClientRect().bottom ?? 0;
    if (rect.top < headerBottom || rect.bottom > window.innerHeight) {
      tabs[index].scrollIntoView({ block: 'center', behavior: 'instant' });
    }
  };
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => select(index));
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) { event.preventDefault(); select(next, true); }
    });
  });
  render();
  module.classList.add('is-ready');
  mobile.addEventListener('change', render);
})();
