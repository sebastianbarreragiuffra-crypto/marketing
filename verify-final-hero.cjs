const { chromium } = require('C:/Users/shermii/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const results = [];
  for (const width of [320, 390, 768, 1280, 1440]) {
    const page = await browser.newPage({ viewport: { width, height: 900 }, deviceScaleFactor: 1 });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto('http://127.0.0.1:8766/index.html', { waitUntil: 'networkidle' });
    const result = await page.evaluate(() => ({
      overflow: document.documentElement.scrollWidth > innerWidth,
      imageLoaded: [...document.querySelectorAll('.final-dashboard img')].every(img => img.complete && img.naturalWidth > 0),
      h1Count: document.querySelectorAll('h1').length,
      heroLinks: [...document.querySelectorAll('.final-hero .hero-actions a')].map(a => a.getAttribute('href')),
      heroHeight: Math.round(document.querySelector('.final-hero').getBoundingClientRect().height),
      headerHeight: Math.round(document.querySelector('.site-header').getBoundingClientRect().height),
    }));
    if ([390, 1280, 1440].includes(width)) await page.locator('.final-hero').screenshot({ path: `preview-hero-final-${width}.png` });
    results.push({ width, ...result, errors });
    await page.close();
  }
  await browser.close();
  console.log(JSON.stringify(results, null, 2));
  if (results.some(r => r.overflow || !r.imageLoaded || r.h1Count !== 1 || r.errors.length)) process.exitCode = 1;
})().catch(error => { console.error(error); process.exitCode = 1; });
