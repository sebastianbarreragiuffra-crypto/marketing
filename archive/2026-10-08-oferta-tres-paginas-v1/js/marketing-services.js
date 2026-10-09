(() => {
  const section = document.querySelector('.marketing-services-showcase');
  if (!section) return;

  const tabs = [...section.querySelectorAll('[role="tab"]')];
  const plans = [...section.querySelectorAll('[data-ms-plan]')];
  const panel = section.querySelector('[role="tabpanel"]');
  const mobileLayout = window.matchMedia('(max-width: 760px)');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const defaultIntro = {
    title: ['Campañas', 'diseñadas alrededor', 'de tu negocio.'],
    lead: 'Gestionamos tus campañas en Facebook e Instagram: audiencias, anuncios y ajustes según su rendimiento.',
    benefits: [
      ['people', 'Captación', ['Definimos audiencias según tus productos y el objetivo de campaña.']],
      ['refresh', 'Remarketing', ['Preparamos campañas para volver a conectar con quienes mostraron interés.']],
      ['bars', 'Creatividad', ['Desarrollamos anuncios que muestran tus productos y su propuesta.']]
    ]
  };
  const defaultSidebar = [['home', 'Resumen'], ['campaign', 'Campañas'], ['people', 'Audiencias'], ['check', 'Creatividades'], ['bars', 'Reportes'], ['settings', 'Configuración']];
  const defaultSecondaryLine = 'M30 108 60 105 90 101 120 98 150 90 180 95 210 96 240 90 270 82 300 85 330 73 360 81 390 69 405 65';
  const services = {
    meta: {
      name: 'Meta Ads', heading: 'Campañas Meta Ads',
      metrics: [['318.421', 'Personas alcanzadas', '↑ 42%'], ['1.245', 'Conversaciones', '↑ 68%'], ['$438', 'Costo por conversación', '↓ 27%'], ['4,8x', 'ROAS estimado', '↑ 35%']],
      chart: 'Rendimiento de campañas', legend: 'Conversaciones', growth: '+43%', growthLabel: 'más conversaciones que el período anterior',
      creatives: 'Ejemplos de creatividades', status: 'Activa',
      intro: defaultIntro, sidebar: defaultSidebar, presentation: 'creative',
      secondaryLegend: 'Inversión', scale: [300, 200, 100], secondaryLine: defaultSecondaryLine,
      line: 'M30 99 60 96 90 87 120 89 150 72 180 79 210 78 240 69 270 62 300 66 330 47 360 59 390 40 405 32'
    },
    google: {
      name: 'Google Ads', heading: 'Campañas Google Ads',
      metrics: [['24.532', 'Clics', '↑ 42%'], ['1.256', 'Conversiones', '↑ 68%'], ['$432', 'Costo por conversión', '↓ 27%'], ['6,8x', 'ROAS estimado', '↑ 35%']],
      chart: 'Rendimiento de campañas', legend: 'Clics', growth: '+43%', growthLabel: 'más conversiones que el período anterior',
      creatives: 'Ejemplos de anuncios de búsqueda', status: 'En marcha', presentation: 'search',
      intro: {
        title: ['Tu próximo', 'cliente ya está', 'buscando.'],
        lead: 'Gestionamos campañas de búsqueda y remarketing para conectar lo que vendes con lo que tus compradores buscan.',
        benefits: [
          ['search', 'Búsqueda', ['Organizamos palabras clave y anuncios según la intención de búsqueda.']],
          ['refresh', 'Remarketing', ['Preparamos campañas para volver a conectar con quienes mostraron interés.']],
          ['bars', 'Optimización', ['Revisamos campañas y ajustamos anuncios e inversión según su rendimiento.']]
        ]
      },
      sidebar: [['home', 'Resumen'], ['campaign', 'Campañas'], ['people', 'Audiencias'], ['keywords', 'Palabras clave'], ['check', 'Anuncios'], ['bars', 'Reportes'], ['settings', 'Configuración']],
      secondaryLegend: 'Conversiones', scale: [600, 400, 200],
      secondaryLine: 'M30 105 60 103 90 95 120 94 150 85 180 89 210 84 240 72 270 76 300 81 330 63 360 74 390 62 405 57',
      line: 'M30 92 60 89 90 72 120 75 150 62 180 67 210 64 240 51 270 43 300 45 330 27 360 35 390 22 405 15'
    },
    web: {
      name: 'Desarrollo Web', presentation: 'website',
      intro: {
        title: ['Tu marca, lista', 'para crecer.'],
        lead: 'Diseñamos sitios modernos, rápidos y enfocados en convertir visitantes en clientes.',
        benefits: [
          ['monitor', 'Diseño a medida', ['Sitios únicos que reflejan', 'la identidad de tu marca.']],
          ['search', 'SEO básico', ['Estructura y títulos definidos para tu sitio.']],
          ['lightning', 'Rendimiento y móvil', ['Cuidamos la carga y la navegación en escritorio y celular.']]
        ]
      },
      sidebar: [['home', 'Resumen'], ['monitor', 'Sitios Web'], ['keywords', 'Páginas'], ['palette', 'Diseño'], ['mail', 'Formularios'], ['seo', 'SEO'], ['web', 'Dominios'], ['bars', 'Reportes'], ['settings', 'Configuración']]
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
    const quoteLabel = id === 'web' ? 'Cotizar sitio web' : 'Cotizar ' + service.name;
    section.querySelectorAll('[data-ms-quote-label]').forEach(label => { label.textContent = quoteLabel; });
    const included = id === 'web'
      ? ['Diseño a medida', 'Sitio adaptable a celulares', 'Alcance y entregables acordados']
      : ['Estrategia personalizada', 'Reportes mensuales', 'Acompañamiento de principio a fin'];
    const includeList = section.querySelector('[data-ms-includes]');
    if (includeList) includeList.querySelectorAll('li').forEach((item, i) => {
      const icon = item.querySelector('svg');
      item.replaceChildren(icon, document.createTextNode(included[i]));
    });
    if (announce) document.dispatchEvent(new CustomEvent('orbita:marketing-service', {detail: {service:id}}));
    const isWebsite = service.presentation === 'website';
    section.querySelector('[data-ms-campaign-view]').hidden = isWebsite;
    section.querySelector('[data-ms-web-view]').hidden = !isWebsite;
    const previewLabel = section.querySelector('[data-ms-preview-label]');
    if (previewLabel) previewLabel.textContent = isWebsite ? 'Vista ilustrativa · Sitio y estados de ejemplo' : 'Vista ilustrativa · Cifras y estados de ejemplo';
    section.querySelector('[data-ms-caption]').textContent = isWebsite
      ? 'Interfaz ilustrativa · Sitio y estados de ejemplo'
      : 'Interfaz ilustrativa · Cifras de ejemplo';
    if (announce) section.querySelector('.ms-selection-status').textContent = `Servicio seleccionado: ${service.name}. El panel muestra ${isWebsite ? 'un sitio de ejemplo en escritorio y móvil' : 'datos de ejemplo'}.`;
    if (isWebsite) return;
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
  section.addEventListener('orbita:marketing-auto-select', event => selectService(event.detail, false));
  plans.forEach(plan => plan.addEventListener('click', () => {
    selectService(plan.dataset.msPlan);
    if (!mobileLayout.matches) return;
    panel.focus({ preventScroll: true });
    panel.scrollIntoView({
      behavior: reducedMotion.matches ? 'auto' : 'smooth',
      block: 'start'
    });
  }));
  selectService('meta', false);
})();
