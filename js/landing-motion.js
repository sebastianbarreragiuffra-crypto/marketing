(() => {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (reduced.matches || !('IntersectionObserver' in window)) return;

  const targets = [
    ...document.querySelectorAll('.sol-card, .mk-card, .mk-team'),
  ];
  const viewportHeight = window.innerHeight;

  targets.forEach(element => {
    element.classList.add('landing-motion-target');
    if (element.getBoundingClientRect().top > viewportHeight * 0.88) {
      element.classList.add('landing-pending');
    } else {
      element.classList.add('landing-entered');
    }
    if (element.matches('.mk-card')) {
      const step = [...element.parentElement.querySelectorAll('.mk-card')].indexOf(element);
      element.style.setProperty('--landing-delay', `${step * 90}ms`);
    }
  });

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.remove('landing-pending');
      entry.target.classList.add('landing-entered');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -6% 0px' });

  targets.filter(element => element.classList.contains('landing-pending')).forEach(element => observer.observe(element));

  reduced.addEventListener('change', event => {
    if (!event.matches) return;
    observer.disconnect();
    targets.forEach(element => {
      element.classList.remove('landing-pending');
      element.classList.add('landing-entered');
    });
  });
})();
