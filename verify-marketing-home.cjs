const { chromium } = require('C:/Users/shermii/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const page = await browser.newPage();
  const results = [];
  for (const width of [320, 390, 768, 1440]) {
    await page.setViewportSize({ width, height: 1000 });
    await page.goto('http://127.0.0.1:4175/index.html');
    const section = page.locator('.marketing-method');
    if (width === 390 || width === 1440) await section.screenshot({ path: `preview-marketing-home-${width}.png` });
    const check = await page.evaluate(() => ({
      overflow: document.documentElement.scrollWidth > innerWidth,
      sectionImages: document.querySelectorAll('.marketing-method img').length,
      caption: Boolean(document.querySelector('.campaign-map figcaption')?.getClientRects().length),
      steps: document.querySelectorAll('.method-responsibilities > div').length,
    }));
    results.push({ width, ...check });
  }
  await page.locator('.marketing-method a[href="marketing.html"]').click();
  results.push({ marketingLink: page.url().endsWith('/marketing.html') });
  console.log(JSON.stringify(results));
  await browser.close();
  if (results.some(x => x.overflow || x.sectionImages > 0 || x.caption === false || (x.steps !== undefined && x.steps !== 3) || x.marketingLink === false)) process.exitCode = 1;
})();
