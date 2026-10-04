(() => {
  const section = document.querySelector('.marketing-services-showcase');
  if (!section) return;

  const tabs = [...section.querySelectorAll('[role="tab"]')];
  const plans = [...section.querySelectorAll('[data-ms-plan]')];
  const panel = section.querySelector('[role="tabpanel"]');
  const services = {
    meta: {
      name: 'Meta Ads', heading: 'Campañas Meta Ads',
      metrics: [['318.421', 'Personas alcanzadas', '↑ 42%'], ['1.245', 'Conversaciones', '↑ 68%'], ['$438', 'Costo por conversación', '↓ 27%'], ['4,8x', 'ROAS estimado', '↑ 35%']],
      chart: 'Rendimiento de campañas', legend: 'Conversaciones', growth: '+43%', growthLabel: 'más conversaciones que el período anterior',
      creatives: 'Creatividades en vivo', status: 'Activa',
      line: 'M30 99 60 96 90 87 120 89 150 72 180 79 210 78 240 69 270 62 300 66 330 47 360 59 390 40 405 32'
    },
    google: {
      name: 'Google Ads', heading: 'Campañas Google Ads',
      metrics: [['124.680', 'Impresiones', '↑ 32%'], ['3.210', 'Clics', '↑ 24%'], ['$210', 'Costo por clic', '↓ 18%'], ['5,2x', 'ROAS estimado', '↑ 29%']],
      chart: 'Rendimiento de búsqueda', legend: 'Clics', growth: '+32%', growthLabel: 'más clics que el período anterior',
      creatives: 'Destinos de campaña', status: 'En marcha',
      line: 'M30 103 60 99 90 91 120 83 150 87 180 72 210 67 240 62 270 71 300 54 330 43 360 49 390 31 405 23'
    },
    web: {
      name: 'Desarrollo Web', heading: 'Rendimiento del sitio web',
      metrics: [['12.480', 'Visitas al sitio', '↑ 38%'], ['428', 'Consultas recibidas', '↑ 26%'], ['1,2 s', 'Tiempo de carga', '↓ 31%'], ['3,4%', 'Conversión estimada', '↑ 22%']],
      chart: 'Visitas y oportunidades', legend: 'Consultas', growth: '+26%', growthLabel: 'más consultas que el período anterior',
      creatives: 'Páginas de campaña', status: 'Publicada',
      line: 'M30 108 60 103 90 95 120 96 150 85 180 88 210 70 240 77 270 68 300 60 330 55 360 47 390 34 405 28'
    }
  };

  function selectService(id, announce = true) {
    const service = services[id];
    if (!service) return;
    tabs.forEach(tab => {
      const active = tab.dataset.msService === id;
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
      tab.classList.toggle('is-active', active);
    });
    plans.forEach(plan => {
      const active = plan.dataset.msPlan === id;
      plan.setAttribute('aria-pressed', String(active));
      plan.classList.toggle('is-active', active);
    });
    panel.setAttribute('aria-labelledby', `ms-tab-${id}`);
    section.querySelector('[data-ms-heading]').textContent = service.heading;
    service.metrics.forEach(([value, label, delta], i) => {
      section.querySelector(`[data-ms-value="${i}"]`).textContent = value;
      section.querySelector(`[data-ms-label="${i}"]`).textContent = label;
      section.querySelector(`[data-ms-delta="${i}"]`).textContent = delta;
    });
    section.querySelector('[data-ms-chart-title]').textContent = service.chart;
    section.querySelector('[data-ms-legend]').textContent = service.legend;
    section.querySelector('[data-ms-growth]').textContent = service.growth;
    section.querySelector('[data-ms-growth-label]').textContent = service.growthLabel;
    section.querySelector('[data-ms-creatives-title]').textContent = service.creatives;
    section.querySelector('[data-ms-chart-line]').setAttribute('d', service.line);
    section.querySelector('.ms-chart').setAttribute('aria-label', `Gráfico ilustrativo de ${service.legend.toLowerCase()} e inversión durante un mes`);
    section.querySelectorAll('[data-ms-status]').forEach(status => { status.textContent = service.status; });
    // The other chart series stays decorative when the selected sample changes.
    section.querySelector('.ms-chart-dots').style.display = id === 'meta' ? '' : 'none';
    if (announce) section.querySelector('.ms-selection-status').textContent = `Servicio seleccionado: ${service.name}. El panel muestra datos de ejemplo.`;
  }

  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => selectService(tab.dataset.msService));
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (i + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (i - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next === undefined) return;
      event.preventDefault();
      selectService(tabs[next].dataset.msService);
      tabs[next].focus();
    });
  });
  plans.forEach(plan => plan.addEventListener('click', () => selectService(plan.dataset.msPlan)));
  selectService('meta', false);
})();
