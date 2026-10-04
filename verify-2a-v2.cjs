const { chromium } = require('C:/Users/shermii/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const page = await browser.newPage();
  const results = [];
  for (const width of [320, 360, 390, 768, 1440]) {
    await page.setViewportSize({ width, height: 900 });
    await page.goto('http://127.0.0.1:4175/index.html');
    const check = await page.evaluate(() => ({
      overflow: document.documentElement.scrollWidth > innerWidth,
      heroImages: document.querySelectorAll('.commerce-hero img').length,
      solutionsImages: document.querySelectorAll('#soluciones img').length,
      panelCount: document.querySelectorAll('.offer-panel').length,
      captionVisible: Boolean(document.querySelector('.hero-composition figcaption')?.getClientRects().length),
    }));
    results.push({ width, ...check });
    if (width === 320 || width === 1440) await page.screenshot({ path: `preview-2a-v2-${width}.png`, fullPage: true });
  }
  for (const href of ['marketing.html', 'software.html', 'automatizaciones.html']) {
    await page.goto('http://127.0.0.1:4175/index.html');
    await page.locator(`#soluciones a[href="${href}"]`).click();
    results.push({ href, navigated: page.url().endsWith(href) });
  }
  console.log(JSON.stringify(results));
  await browser.close();
  if (results.some(x => x.overflow || x.navigated === false || x.heroImages > 0 || x.solutionsImages > 0 || (x.panelCount !== undefined && x.panelCount !== 3) || x.captionVisible === false)) process.exitCode = 1;
})();
