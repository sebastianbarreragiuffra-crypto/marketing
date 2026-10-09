// Native disclosures adapt once per breakpoint; users retain control within it.
(() => {
  const mobile = window.matchMedia('(max-width: 700px)');
  const disclosures = document.querySelectorAll('.software-page details[data-mobile-details]');
  const adapt = () => disclosures.forEach(detail => { detail.open = !mobile.matches; });
  adapt();
  mobile.addEventListener('change', adapt);
})();
