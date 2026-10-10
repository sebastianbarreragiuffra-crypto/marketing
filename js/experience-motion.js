/* Progressive motion only: existing page scripts own selection, focus and data. */
(() => {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const timers = new Map();
  const entered = new WeakSet();
  const enterSelector = [
    'main h1', '.hm-copy', '.hm-example', '.purchase-heading',
    '.purchase-project-card', '.mk-head', '.mk-step', '.contact-copy',
    '.contact-card', '.hc-copy', '.hc-card', '.fq-head',
    '.gs-copy', '.cf-section-head', '.gr-heading', '.sw-closing-inner',
    '.pmo-heading', '.pg-heading', '.pca-intro', '.login-intro', '.login-card'
  ].join(',');

  function finish(element) {
    window.clearTimeout(timers.get(element));
    timers.delete(element);
    element.classList.remove('site-motion-enter', 'site-motion-switch', 'site-motion-detail', 'site-motion-view');
  }
  function play(element, className, duration) {
    if (!element || reduced.matches || document.hidden || element.contains(document.activeElement)) return;
    finish(element);
    void element.offsetWidth;
    element.classList.add(className);
    timers.set(element, window.setTimeout(() => finish(element), duration));
  }

  if (!reduced.matches && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting || entered.has(entry.target)) return;
        entered.add(entry.target);
        observer.unobserve(entry.target);
        play(entry.target, 'site-motion-enter', 400);
      });
    }, { threshold: .08 });
    document.querySelectorAll(enterSelector).forEach(element => {
      // Animate a containing introduction once, rather than its heading twice.
      if (element.parentElement.closest(enterSelector)) return;
      observer.observe(element);
    });
    reduced.addEventListener('change', event => { if (event.matches) observer.disconnect(); });
  }

  document.querySelectorAll('.hx-tabs, .purchase-tabs').forEach(list => {
    const tabs = [...list.querySelectorAll('[role="tab"]')];
    const initial = tabs.find(tab => tab.getAttribute('aria-selected') === 'true');
    if (!initial || !('ResizeObserver' in window) || !('MutationObserver' in window)) return;
    const style = getComputedStyle(initial);
    const indicator = document.createElement('span');
    indicator.className = 'motion-tab-indicator';
    indicator.setAttribute('aria-hidden', 'true');
    indicator.style.background = style.backgroundColor;
    indicator.style.borderRadius = '999px';
    list.append(indicator);
    list.classList.add('motion-tablist');
    let resizeFrame;
    function position(animate) {
      const selected = tabs.find(tab => tab.getAttribute('aria-selected') === 'true');
      if (!selected) return;
      const parent = list.getBoundingClientRect();
      const bounds = selected.getBoundingClientRect();
      if (!bounds.width || !bounds.height) return;
      if (!animate) list.classList.remove('motion-tabs-ready');
      // A moving underline preserves label contrast throughout the transition.
      indicator.style.width = `${Math.max(0, bounds.width - 24)}px`;
      indicator.style.height = '3px';
      indicator.style.transform = `translate(${bounds.left - parent.left + list.scrollLeft - list.clientLeft + 12}px, ${bounds.bottom - parent.top + list.scrollTop - list.clientTop + 4}px)`;
      if (!animate) {
        window.cancelAnimationFrame(resizeFrame);
        resizeFrame = window.requestAnimationFrame(() => list.classList.add('motion-tabs-ready'));
      }
    }
    position(false);
    const selectionObserver = new MutationObserver(() => position(true));
    tabs.forEach(tab => selectionObserver.observe(tab, { attributes: true, attributeFilter: ['aria-selected'] }));
    const resizeObserver = new ResizeObserver(() => position(false));
    resizeObserver.observe(list);
    tabs.forEach(tab => resizeObserver.observe(tab));
    reduced.addEventListener('change', () => position(false));
  });

  document.addEventListener('orbita:hero-view', event => {
    play(document.getElementById(event.detail.panelId), 'site-motion-view', 240);
  });

  document.addEventListener('orbita:marketing-service', () => {
    const section = document.querySelector('.purchase-services');
    if (!section) return;
    [section.querySelector('[data-channel-title]'), section.querySelector('[data-channel-copy]'),
      section.querySelector('[data-channel-work]')].forEach(element => play(element, 'site-motion-switch', 240));
    // Wait for the chosen asset, and never fade an older image back in.
    const image = section.querySelector('[data-channel-image]');
    finish(image);
    if (image.complete && image.naturalWidth) play(image, 'site-motion-switch', 240);
  });
  const channelImage = document.querySelector('[data-channel-image]');
  channelImage?.addEventListener('load', () => play(channelImage, 'site-motion-switch', 240));

  const nativeDetailsMotion = window.CSS && CSS.supports('selector(::details-content)') &&
    CSS.supports('interpolate-size: allow-keywords');
  if (!nativeDetailsMotion) {
    document.querySelectorAll('main details').forEach(detail => {
      detail.addEventListener('toggle', () => {
        finish(detail);
        if (detail.open) play(detail, 'site-motion-detail', 180);
      });
    });
  }
  document.addEventListener('focusin', event => {
    for (const element of timers.keys()) if (element.contains(event.target)) finish(element);
  });
  const stop = () => { for (const element of [...timers.keys()]) finish(element); };
  document.addEventListener('visibilitychange', () => { if (document.hidden) stop(); });
  reduced.addEventListener('change', event => { if (event.matches) stop(); });
  // Apply disclosure transitions after page scripts have chosen initial defaults.
  void document.documentElement.offsetHeight;
  document.documentElement.classList.add('site-motion-ready');
})();
