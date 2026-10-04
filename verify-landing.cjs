const {chromium}=require('C:/Users/shermii/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');
(async()=>{
 const browser=await chromium.launch({headless:true,channel:"msedge"});const page=await browser.newPage();const errors=[];const results=[];
 page.on('pageerror',e=>errors.push(e.message));
 for(const width of [390,768,1440]){
  await page.setViewportSize({width,height:1000});
  for(const file of ['index.html','marketing.html','software.html','automatizaciones.html']){
   await page.goto('http://127.0.0.1:4175/'+file);await page.waitForTimeout(400);
   await page.evaluate(async()=>{for(const i of document.images){i.loading='eager';await i.decode()}});
   const check=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,h1:document.querySelectorAll('h1').length,images:[...document.images].every(i=>i.complete&&i.naturalWidth>0),anchors:[...document.querySelectorAll('a[href^="#"]')].every(a=>document.querySelector(a.getAttribute('href'))),active:document.querySelectorAll('[aria-current="page"]').length}));
   results.push({width,file,...check});
   if(file==='index.html'&&width!==768){await page.screenshot({path:`preview-home-${width}.png`,fullPage:true});}
  }
 }
 await page.setViewportSize({width:390,height:844});await page.goto('http://127.0.0.1:4175/index.html');
 await page.getByRole('button',{name:'Abrir menú'}).click();await page.getByRole('navigation').getByRole('link',{name:'Software',exact:true}).click();
 const mobileNavigation=page.url().endsWith('/software.html');
 await page.goto('http://127.0.0.1:4175/index.html');const firstFaq=page.locator('details').first();const initiallyOpen=await firstFaq.getAttribute('open')!==null;await firstFaq.locator('summary').click();const closed=await firstFaq.getAttribute('open')===null;await firstFaq.locator('summary').click();const reopened=await firstFaq.getAttribute('open')!==null;const faq=initiallyOpen&&closed&&reopened;
 const report={results,errors,mobileNavigation,faq};fs.writeFileSync('landing-validation.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report));await browser.close();
 if(errors.length||!mobileNavigation||!faq||results.some(r=>r.overflow||r.h1!==1||!r.images||!r.anchors||r.active!==1))process.exitCode=1;
})();

