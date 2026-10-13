const fs=require('node:fs'),assert=require('node:assert/strict');
const {chromium}=require('C:/Users/SEBAS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});const checks=[];
 const baseline=JSON.parse(fs.readFileSync('outputs/marketing-bruma-20261013/render-checks.json'));
 try{for(const width of [1440,390]){
  const context=await browser.newContext({viewport:{width,height:1600},isMobile:width<768,hasTouch:width<768});await context.route('**/__live.js',route=>route.abort());const page=await context.newPage();
  await page.goto('http://127.0.0.1:8767/marketing.html');await page.evaluate(()=>document.fonts.ready);await page.waitForFunction(()=>[...document.querySelectorAll('#marketing-hero img')].every(i=>i.complete&&i.naturalWidth));
  const current=await page.evaluate(()=>({width:innerWidth,removed:document.querySelector('#otros-servicios')===null,adjacent:document.querySelector('#que-gestionamos').nextElementSibling.id==='contacto',overflow:document.documentElement.scrollWidth>innerWidth,sections:[...document.querySelectorAll('.site-header,main>section,.site-footer')].map(e=>({id:e.id,class:e.className,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height,font:getComputedStyle(e).fontFamily,color:getComputedStyle(e).color,background:getComputedStyle(e).backgroundColor})),videoCount:document.querySelectorAll('#que-gestionamos video').length}));
  assert(current.removed&&current.adjacent&&!current.overflow);assert.equal(current.videoCount,1);
  const normalize=rows=>rows.filter(r=>r.id!=='otros-servicios'&&r.id!=='que-gestionamos').map(r=>({...r,class:r.class.replace(/\s+is-scrolled\b/g,'')}));assert.deepEqual(normalize(current.sections),normalize(baseline.find(r=>r.width===width).sections));
  await page.locator('#que-gestionamos').scrollIntoViewIfNeeded();await page.locator('#que-gestionamos').screenshot({path:`outputs/marketing-remove-otros-servicios-${width}.png`});checks.push(current);console.log(`VERIFICADO ${width}: sin sección, sin hueco reservado y resto conservado.`);await context.close();
 }fs.writeFileSync('outputs/marketing-remove-otros-servicios-checks.json',JSON.stringify(checks,null,2));}finally{await browser.close();}
})();
