// Mide el borde inferior de cada bloque del hero y el ancho útil (QA de primer pliegue).
const { chromium } = require('C:/Users/shermii/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async () => {
  const [url, w, h] = process.argv.slice(2);
  const b = await chromium.launch({ channel: 'msedge' });
  const p = await b.newPage({ viewport: { width: +w, height: +h } });
  await p.goto(url, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  console.log(JSON.stringify(await p.evaluate(() => Object.fromEntries(['.ph-hero', '.ph-copy', '.ph-main', '.ph-addon', '.ph-web', '.ph-desc'].map(s => { const r = document.querySelector(s).getBoundingClientRect(); return [s, [Math.round(r.left), Math.round(r.top), Math.round(r.right), Math.round(r.bottom)]]; })))));
  await b.close();
})();
