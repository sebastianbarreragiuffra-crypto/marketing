const {chromium}=require('C:/Users/SEBAS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('node:fs/promises');const path=require('node:path');
(async()=>{
 const before=process.argv.includes('--before');
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const results=[];
 for(const width of before?[1440,390]:[1440,1920,390,320,768,1024,900,901]){
  const page=await browser.newPage({viewport:{width,height:960}});const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto('http://127.0.0.1:8767/index.html',{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);
  const selector=before?'.work-section':'.omd-section';
  await page.locator(selector).scrollIntoViewIfNeeded();
  await page.locator(selector+' img').first().waitFor({state:'visible'});
  await page.waitForFunction(s=>[...document.querySelectorAll(s+' img')].every(i=>i.complete&&i.naturalWidth>0),selector);
  const data=await page.evaluate(s=>{
   const el=document.querySelector(s),box=e=>{const r=e.getBoundingClientRect();return{x:r.x+scrollX,y:r.y+scrollY,w:r.width,h:r.height}};
   return{width:innerWidth,overflow:document.documentElement.scrollWidth>innerWidth,section:box(el),h1Count:document.querySelectorAll('h1').length,h1:document.querySelector('h1').textContent.replace(/\s+/g,' ').trim(),text:el.innerText,images:[...el.querySelectorAll('img')].map(i=>({src:i.currentSrc,loaded:i.complete&&i.naturalWidth>0,render:[i.clientWidth,i.clientHeight]})),clipped:[...el.querySelectorAll('h2,h3,p,figcaption,li,strong,span')].filter(e=>e.clientWidth>0&&e.scrollWidth>e.clientWidth+1).map(e=>({class:e.className,text:e.textContent})),adBoxes:[...el.querySelectorAll('.omd-ad')].map(box),tasks:[...el.querySelectorAll('.omd-management li')].map(box),layout:Object.fromEntries([...el.querySelectorAll('[data-omd-layout]')].map(e=>[e.dataset.omdLayout,box(e)])),actions:[...el.querySelectorAll('a,button,input')].map(e=>({tag:e.tagName,text:e.innerText,href:e.getAttribute('href')}))};
  },selector);data.errors=errors;results.push(data);
  await page.evaluate(()=>window.scrollTo({top:0,behavior:'instant'}));
  if([1440,390,320,1920].includes(width))await page.screenshot({path:path.join(__dirname,(before?'before-':'section-')+width+'.png'),fullPage:true,clip:{x:0,y:data.section.y,width,height:Math.ceil(data.section.h)}});
  if(!before&&width===390){
   await page.locator('.omd-cta').focus();data.focus=await page.locator('.omd-cta').evaluate(e=>({outline:getComputedStyle(e).outlineWidth,minHeight:e.clientHeight}));
   await page.locator('.omd-cta').press('Enter');await page.waitForURL('**/hablemos.html');data.contact={url:page.url(),preview:await page.getByText('Vista previa · Tu consulta no se enviará.',{exact:true}).count()>0};
  }
  await page.close();
 }
 await fs.writeFile(path.join(__dirname,before?'before.json':'browser-checks.json'),JSON.stringify(results,null,2));
 await browser.close();console.log(JSON.stringify(results.map(r=>({width:r.width,overflow:r.overflow,clipped:r.clipped,errors:r.errors,images:r.images.every(i=>i.loaded),focus:r.focus,contact:r.contact})),null,2));
})().catch(e=>{console.error(e);process.exitCode=1});
