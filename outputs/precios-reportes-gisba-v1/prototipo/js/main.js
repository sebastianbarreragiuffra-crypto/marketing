const menuButton = document.querySelector('.menu-toggle');
const menu = document.querySelector('.main-nav');
const siteHeader = document.querySelector('.site-header');
if (siteHeader) {
  const updateHeader = () => siteHeader.classList.toggle('is-scrolled', window.scrollY > 20);
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });
}
if (menuButton && menu) {
  menuButton.addEventListener('click', () => {
    const expanded = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!expanded));
    menuButton.setAttribute('aria-label', expanded ? 'Abrir menú' : 'Cerrar menú');
    menu.classList.toggle('open', !expanded);
  });
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Abrir menú');
    menu.classList.remove('open');
  }));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu.classList.contains('open')) {
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.setAttribute('aria-label', 'Abrir menú');
      menu.classList.remove('open');
      menuButton.focus();
    }
  });
}
document.querySelectorAll('.year').forEach(el => { el.textContent = String(new Date().getFullYear()); });
if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  document.documentElement.classList.add('motion-on');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
} else {
  document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
}
