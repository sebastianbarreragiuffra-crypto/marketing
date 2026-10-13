const { chromium } = require('C:/Users/SEBAS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('node:fs/promises');
const path = require('node:path');
(async () => {
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: true });
  const out = __dirname;
  const result = [];
  for (const width of [1440, 390]) {
    const page = await browser.newPage({ viewport: { width, height: 900 } });
    await page.goto('http://127.0.0.1:8767/index.html', { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(out, `before-${width}.png`), fullPage: false });
    result.push(await page.evaluate(() => ({ width: innerWidth, title: document.querySelector('h1').innerText, heroClass: document.querySelector('main > section').className, overflow: document.documentElement.scrollWidth > innerWidth })));
    await page.close();
  }
  await fs.writeFile(path.join(out, 'before-render.json'), JSON.stringify(result, null, 2));
  await browser.close();
  console.log(JSON.stringify(result));
})().catch(error => { console.error(error); process.exitCode = 1; });
