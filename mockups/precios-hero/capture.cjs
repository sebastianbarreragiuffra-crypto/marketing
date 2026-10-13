// Captura de mockups S: espera fuentes, imágenes y animaciones; verifica dimensiones.
// Uso: node capture.cjs <url> <salida.png> <ancho> <alto> [full]
const { chromium } = require('C:/Users/shermii/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async () => {
  const [url, out, w, h, mode] = process.argv.slice(2);
  const browser = await chromium.launch({ channel: 'msedge' });
  const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.evaluate(async () => {
    await document.fonts.ready;
    await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; })));
    document.querySelectorAll('[data-reveal],.reveal,.is-hidden-motion').forEach(e => e.classList.add('is-visible'));
  });
  await page.waitForTimeout(1200);
  if (mode === 'hero') {
    const b = await page.evaluate(() => { const s = document.querySelector('.p4-hero, .ph-hero, .pr-hero'); const r = s.getBoundingClientRect(); return Math.ceil(r.bottom + scrollY); });
    await page.screenshot({ path: out, fullPage: true, clip: { x: 0, y: 0, width: +w, height: b } });
  } else await page.screenshot({ path: out, fullPage: mode === 'full' });
  const dims = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
  console.log(out, 'overflow:', dims.sw > dims.cw ? `SI (${dims.sw})` : 'no');
  await browser.close();
})();
