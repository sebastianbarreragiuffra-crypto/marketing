// Native disclosures: choose defaults once, then preserve the visitor's choices.
(() => {
  const ads = [...document.querySelectorAll('.precios-page .purchase-ad-detail')];
  const mobileAtLoad = window.matchMedia('(max-width: 760px)').matches;
  ads.forEach((detail, index) => {
    const label = detail.querySelector('[data-ad-label]');
    const updateLabel = () => {
      label.textContent = `${detail.open ? 'Ocultar' : 'Mostrar'} ejemplo de ${detail.dataset.adChannel}`;
    };
    detail.open = !mobileAtLoad || index === 0;
    updateLabel();
    detail.addEventListener('toggle', updateLabel);
  });
})();
