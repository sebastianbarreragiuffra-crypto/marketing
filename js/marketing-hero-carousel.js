/* Two examples, manual native scroll. No timer advances the carousel. */
(() => {
  const root = document.getElementById('marketing-hero');
  if (!root) return;
  const track = root.querySelector('.mp-carousel');
  const slides = [...root.querySelectorAll('.mp-slide')];
  const selectors = [...root.querySelectorAll('[data-mp-select]')];
  const previous = root.querySelector('.mp-prev');
  const next = root.querySelector('.mp-next');
  const position = root.querySelector('.mp-position');
  const mobile = window.matchMedia('(max-width:767px)');
  const reduced = window.matchMedia('(prefers-reduced-motion:reduce)');
  let selected = 0;
  let settled;
  let resizeFrame;
  function paint(index) {
    selected = Math.max(0, Math.min(1, index));
    selectors.forEach((button, i) => {
      button.disabled = false;
      button.setAttribute('aria-pressed', String(i === selected));
    });
    previous.disabled = !mobile.matches || selected === 0;
    next.disabled = !mobile.matches || selected === 1;
    position.textContent = `${selected + 1} de 2`;
    slides.forEach((slide, i) => {
      if (mobile.matches) {
        slide.setAttribute('aria-hidden', String(i !== selected));
        slide.inert = i !== selected;
      } else {
        slide.removeAttribute('aria-hidden');
        slide.inert = false;
      }
    });
  }
  function go(index, animate = true) {
    paint(index);
    if (!mobile.matches) return;
    const edge = selected === 0 ? 0 : track.scrollWidth - track.clientWidth;
    track.scrollTo({ left: edge, behavior: animate && !reduced.matches ? 'smooth' : 'instant' });
  }
  function syncScroll() {
    if (!mobile.matches) return;
    const maximum = track.scrollWidth - track.clientWidth;
    if (maximum > 0) paint(track.scrollLeft > maximum / 2 ? 1 : 0);
  }
  selectors.forEach(button => button.addEventListener('click', () => go(Number(button.dataset.mpSelect))));
  previous.addEventListener('click', () => go(selected - 1));
  next.addEventListener('click', () => go(selected + 1));
  track.addEventListener('scroll', () => {
    window.clearTimeout(settled);
    settled = window.setTimeout(syncScroll, 160);
  }, { passive: true });
  track.addEventListener('scrollend', syncScroll);
  function keyboard(event) {
    if (!mobile.matches || event.altKey || event.ctrlKey || event.metaKey) return;
    let index;
    if (event.key === 'ArrowLeft') index = selected - 1;
    else if (event.key === 'ArrowRight') index = selected + 1;
    else if (event.key === 'Home') index = 0;
    else if (event.key === 'End') index = 1;
    else return;
    event.preventDefault();
    go(index);
    if (event.currentTarget.classList.contains('mp-tabs')) selectors[selected].focus({ preventScroll: true });
  }
  root.querySelector('.mp-tabs').addEventListener('keydown', keyboard);
  track.addEventListener('keydown', keyboard);
  function layout() {
    window.cancelAnimationFrame(resizeFrame);
    resizeFrame = window.requestAnimationFrame(() => {
      track.tabIndex = mobile.matches ? 0 : -1;
      go(selected, false);
    });
  }
  mobile.addEventListener('change', layout);
  reduced.addEventListener('change', () => go(selected, false));
  const observer = new ResizeObserver(layout);
  observer.observe(track);
  layout();
})();
