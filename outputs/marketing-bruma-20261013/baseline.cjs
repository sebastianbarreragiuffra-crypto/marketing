const fs = require('node:fs');
const {chromium} = require('C:/Users/SEBAS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async () => {
  const browser = await chromium.launch({channel:'chrome',headless:true});
  const result = [];
  try {
    for (const width of [1440,1920,390,360]) {
      const page = await browser.newPage({viewport:{width,height:1600}});
      await page.goto('http://127.0.0.1:8767/marketing.html');
      await page.evaluate(() => document.fonts.ready);
      await page.waitForFunction(() => [...document.querySelectorAll('#marketing-hero img')].every(i => i.complete && i.naturalWidth));
      result.push(await page.evaluate(() => ({width:innerWidth, sections:[...document.querySelectorAll('.site-header,main>section:not(#que-gestionamos),.site-footer')].map(e => ({id:e.id,class:e.className,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height,font:getComputedStyle(e).fontFamily,color:getComputedStyle(e).color,background:getComputedStyle(e).backgroundColor}))})));
      await page.locator('#que-gestionamos').screenshot({path:`outputs/marketing-bruma-20261013/before-${width}.png`});
      await page.close();
    }
    fs.writeFileSync('outputs/marketing-bruma-20261013/render-before.json',JSON.stringify(result,null,2));
    console.log('Baseline guardado: 1440, 1920, 390, 360.');
  } finally {await browser.close();}
})();
