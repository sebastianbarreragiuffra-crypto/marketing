(() => {
  const section = document.querySelector('.marketing-services-showcase');
  if (!section) return;

  const tabs = [...section.querySelectorAll('[role="tab"]')];
  const plans = [...section.querySelectorAll('[data-ms-plan]')];
  const panel = section.querySelector('[role="tabpanel"]');
  const defaultIntro = {
    title: ['Campañas', 'diseñadas alrededor', 'de tu negocio.'],
    lead: 'Estrategia, creatividad y optimización constante para que llegues a las personas correctas y consigas más clientes.',
    benefits: [
      ['people', 'Captación', ['Llega a nuevos clientes con', 'audiencias inteligentes.']],
      ['refresh', 'Remarketing', ['Vuelve a conectar con quienes', 'ya mostraron interés.']],
      ['bars', 'Creatividad', ['Anuncios que destacan', 'y generan resultados.']]
    ]
  };
  const defaultSidebar = [['home', 'Resumen'], ['campaign', 'Campañas'], ['people', 'Audiencias'], ['check', 'Creatividades'], ['bars', 'Reportes'], ['settings', 'Configuración']];
  const defaultSecondaryLine = 'M30 108 60 105 90 101 120 98 150 90 180 95 210 96 240 90 270 82 300 85 330 73 360 81 390 69 405 65';
  const services = {
    meta: {
      name: 'Meta Ads', heading: 'Campañas Meta Ads',
      metrics: [['318.421', 'Personas alcanzadas', '↑ 42%'], ['1.245', 'Conversaciones', '↑ 68%'], ['$438', 'Costo por conversación', '↓ 27%'], ['4,8x', 'ROAS estimado', '↑ 35%']],
      chart: 'Rendimiento de campañas', legend: 'Conversaciones', growth: '+43%', growthLabel: 'más conversaciones que el período anterior',
      creatives: 'Creatividades en vivo', status: 'Activa',
      intro: defaultIntro, sidebar: defaultSidebar, presentation: 'creative',
      secondaryLegend: 'Inversión', scale: [300, 200, 100], secondaryLine: defaultSecondaryLine,
      line: 'M30 99 60 96 90 87 120 89 150 72 180 79 210 78 240 69 270 62 300 66 330 47 360 59 390 40 405 32'
    },
    google: {
      name: 'Google Ads', heading: 'Campañas Google Ads',
      metrics: [['24.532', 'Clics', '↑ 42%'], ['1.256', 'Conversiones', '↑ 68%'], ['$432', 'Costo por conversión', '↓ 27%'], ['6,8x', 'ROAS estimado', '↑ 35%']],
      chart: 'Rendimiento de campañas', legend: 'Clics', growth: '+43%', growthLabel: 'más conversiones que el período anterior',
      creatives: 'Anuncios que generan resultados', status: 'En marcha', presentation: 'search',
      intro: {
        title: ['Tu próximo', 'cliente ya está', 'buscando.'],
        lead: 'Convertimos esa intención en oportunidades reales con campañas orientadas a resultados.',
        benefits: [
          ['search', 'Search', ['Aparece en el momento justo', 'cuando te buscan.']],
          ['refresh', 'Remarketing', ['Vuelve a conectar con quienes', 'ya mostraron interés.']],
          ['bars', 'Optimización', ['Análisis y mejoras constantes', 'para maximizar tus resultados.']]
        ]
      },
      sidebar: [['home', 'Resumen'], ['campaign', 'Campañas'], ['people', 'Audiencias'], ['keywords', 'Palabras clave'], ['check', 'Anuncios'], ['bars', 'Reportes'], ['settings', 'Configuración']],
      secondaryLegend: 'Conversiones', scale: [600, 400, 200],
      secondaryLine: 'M30 105 60 103 90 95 120 94 150 85 180 89 210 84 240 72 270 76 300 81 330 63 360 74 390 62 405 57',
      line: 'M30 92 60 89 90 72 120 75 150 62 180 67 210 64 240 51 270 43 300 45 330 27 360 35 390 22 405 15'
    },
    web: {
      name: 'Desarrollo Web', heading: 'Rendimiento del sitio web',
      metrics: [['12.480', 'Visitas al sitio', '↑ 38%'], ['428', 'Consultas recibidas', '↑ 26%'], ['1,2 s', 'Tiempo de carga', '↓ 31%'], ['3,4%', 'Conversión estimada', '↑ 22%']],
      chart: 'Visitas y oportunidades', legend: 'Consultas', growth: '+26%', growthLabel: 'más consultas que el período anterior',
      creatives: 'Páginas de campaña', status: 'Publicada',
      intro: defaultIntro, sidebar: defaultSidebar, presentation: 'creative',
      secondaryLegend: 'Inversión', scale: [300, 200, 100], secondaryLine: defaultSecondaryLine,
      line: 'M30 108 60 103 90 95 120 96 150 85 180 88 210 70 240 77 270 68 300 60 330 55 360 47 390 34 405 28'
    }
  };

  function setLines(element, lines) {
    const nodes = lines.flatMap((line, i) => {
      const text = document.createTextNode(line + (i < lines.length - 1 ? ' ' : ''));
      return i ? [document.createElement('br'), text] : [text];
    });
    element.replaceChildren(...nodes);
  }

  function renderSidebar(items) {
    const rows = items.map(([icon, label], i) => {
      const row = document.createElement('span');
      if (i === 1) row.classList.add('is-selected');
      const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.classList.add('ms-icon');
      svg.setAttribute('aria-hidden', 'true');
      const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
      use.setAttribute('href', `#ms-${icon}`);
      svg.append(use);
      row.append(svg, document.createTextNode(label));
      return row;
    });
    section.querySelector('.ms-dashboard-nav').replaceChildren(...rows);
  }

  function renderChartDots(line) {
    const coordinates = line.match(/\d+(?:\.\d+)?/g).map(Number);
    const dots = [];
    for (let i = 2; i < coordinates.length; i += 4) {
      const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      circle.setAttribute('cx', coordinates[i]);
      circle.setAttribute('cy', coordinates[i + 1]);
      circle.setAttribute('r', '2.5');
      dots.push(circle);
    }
    section.querySelector('.ms-chart-dots').replaceChildren(...dots);
  }

  function selectService(id, announce = true) {
    const service = services[id];
    if (!service) return;
    section.dataset.msActive = id;
    setLines(section.querySelector('#ms-title'), service.intro.title);
    section.querySelector('.ms-intro-lead').textContent = service.intro.lead;
    section.querySelectorAll('.ms-benefits li').forEach((benefit, i) => {
      const [icon, title, lines] = service.intro.benefits[i];
      benefit.querySelector('use').setAttribute('href', `#ms-${icon}`);
      benefit.querySelector('h3').textContent = title;
      setLines(benefit.querySelector('p'), lines);
    });
    renderSidebar(service.sidebar);
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
    section.querySelector('[data-ms-secondary-legend]').textContent = service.secondaryLegend;
    section.querySelectorAll('.ms-chart-labels text').forEach((label, i) => {
      if (i < service.scale.length) label.textContent = service.scale[i];
    });
    section.querySelector('[data-ms-growth]').textContent = service.growth;
    section.querySelector('[data-ms-growth-label]').textContent = service.growthLabel;
    section.querySelector('[data-ms-creatives-title]').textContent = service.creatives;
    section.querySelector('[data-ms-chart-line]').setAttribute('d', service.line);
    section.querySelector('.ms-chart-purple').setAttribute('d', service.secondaryLine);
    renderChartDots(service.line);
    section.querySelector('.ms-chart').setAttribute('aria-label', `Gráfico ilustrativo de ${service.legend.toLowerCase()} y ${service.secondaryLegend.toLowerCase()} durante un mes`);
    section.querySelector('.ms-creatives').hidden = service.presentation === 'search';
    section.querySelector('[data-ms-search-ads]').hidden = service.presentation !== 'search';
    section.querySelectorAll('[data-ms-status]').forEach(status => { status.textContent = service.status; });
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
