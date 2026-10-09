(() => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (reducedMotion.matches || !('IntersectionObserver' in window)) return;

  const isHome = Boolean(document.querySelector('.hx'));
  const selectors = isHome
    ? '.sol-head, .mk-head, .ag-head, .ag-card, .ag-banner, .fq-head, .fq-list details, .ct-head, .ct-card'
    : '.ms-tabs, .ms-intro, .ms-dashboard, .ms-plans, .ms-platforms, .ms-software-note';
  const items = [...document.querySelectorAll(selectors)];
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.remove('experience-pending');
      entry.target.classList.add('experience-entered');
      observer.unobserve(entry.target);
    });
  }, { threshold: .06, rootMargin: '0px 0px -5% 0px' });

  items.forEach(item => {
    item.classList.add('experience-item');
    const bounds = item.getBoundingClientRect();
    if (bounds.top > innerHeight * .9) {
      item.classList.add('experience-pending');
      observer.observe(item);
    } else {
      item.classList.add('experience-entered');
    }
  });

  const hero = document.querySelector('.marketing-campaign-hero');
  const section = document.querySelector('.marketing-services-showcase');
  const heroObserver = hero && new IntersectionObserver(entries => {
    hero.classList.toggle('experience-in-view', entries[0].isIntersecting);
  }, { rootMargin: '-10% 0px -10% 0px' });
  if (heroObserver) heroObserver.observe(hero);

  if (section) {
    document.addEventListener('orbita:marketing-service', () => {
      section.classList.remove('is-ms-switching');
      requestAnimationFrame(() => section.classList.add('is-ms-switching'));
    });
  }

  reducedMotion.addEventListener('change', event => {
    if (!event.matches) return;
    observer.disconnect();
    if (heroObserver) heroObserver.disconnect();
    hero?.classList.remove('experience-in-view');
    items.forEach(item => {
      item.classList.remove('experience-pending');
      item.classList.add('experience-entered');
    });
  });
})();
