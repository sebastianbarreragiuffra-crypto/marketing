const fs=require('node:fs');
const assert=require('node:assert/strict');
const {chromium}=require('C:/Users/SEBAS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const out='outputs/marketing-bruma-20261013';
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const before=JSON.parse(fs.readFileSync(`${out}/render-before.json`));
 const records=[];
 try {
  for(const width of [1440,1920,390,360,768,320]) {
   const context=await browser.newContext({viewport:{width,height:1600},isMobile:width<768,hasTouch:width<768,deviceScaleFactor:1});
   const page=await context.newPage(); const requests=[];const errors=[];
   page.on('request',r=>{if(r.url().includes('/assets/marketing-video/'))requests.push({url:r.url(),type:r.resourceType()});});
   page.on('pageerror',e=>errors.push(e.message));
   await page.goto('http://127.0.0.1:8767/marketing.html');
   await page.evaluate(()=>document.fonts.ready);
   await page.waitForFunction(()=>[...document.querySelectorAll('#marketing-hero img')].every(i=>i.complete&&i.naturalWidth));
   await page.locator('#que-gestionamos').scrollIntoViewIfNeeded();
   await page.waitForTimeout(900);
   const result=await page.evaluate(()=>{
    const section=document.getElementById('que-gestionamos'),v=section.querySelector('video'),box=e=>e.getBoundingClientRect().toJSON();
    return {width:innerWidth,overflow:document.documentElement.scrollWidth>innerWidth,section:box(section),heading:box(section.querySelector('.bv-heading')),details:box(section.querySelector('.bv-details')),cta:box(section.querySelector('.bv-cta')),figure:box(section.querySelector('figure')),player:box(section.querySelector('.bv-player')),video:{src:v.src,currentSrc:v.currentSrc,poster:v.poster,preload:v.preload,paused:v.paused,currentTime:v.currentTime,readyState:v.readyState,controls:v.controls,playsInline:v.playsInline,autoplay:v.autoplay,loop:v.loop,muted:v.muted,style:getComputedStyle(v).objectFit},count:section.querySelectorAll('video').length,sectionCount:document.querySelectorAll('#que-gestionamos').length,fonts:[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family),sections:[...document.querySelectorAll('.site-header,main>section:not(#que-gestionamos),.site-footer')].map(e=>({id:e.id,class:e.className,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height,font:getComputedStyle(e).fontFamily,color:getComputedStyle(e).color,background:getComputedStyle(e).backgroundColor}))};
   });
   assert.equal(result.overflow,false);assert.equal(result.count,1);assert.equal(result.sectionCount,1);
   assert.equal(result.video.preload,'none');assert.equal(result.video.currentTime,0);assert.equal(result.video.paused,true);assert.equal(result.video.autoplay,false);assert.equal(result.video.loop,false);assert.equal(result.video.controls,true);assert.equal(result.video.playsInline,true);assert.equal(result.video.style,'contain');
   assert.equal(requests.filter(r=>r.url.endsWith('.mp4')).length,0);
   assert.equal(requests.filter(r=>r.url.endsWith('.webp')).length,1);
   assert(result.fonts.includes('Manrope')&&result.fonts.includes('DM Sans'));
   if(width<768){assert(result.video.src.includes('mobile-9x16'));assert(result.video.poster.includes('poster-mobile'));assert(result.figure.top>result.heading.bottom);assert(result.details.top>result.figure.bottom);assert(result.cta.top>result.details.bottom);assert(Math.abs(result.player.width/result.player.height-9/16)<.005);}
   else {assert(result.video.src.includes('anuncio-10s-v2'));assert(result.video.poster.includes('poster-desktop'));assert(result.player.left>result.heading.right);assert(Math.abs(result.player.width/result.player.height-4/5)<.005);if(width>=1440)assert.equal(result.player.width,420);}
   const baseline=before.find(r=>r.width===width);
   // Scrolling to the tested section activates the existing header state.
   const stableSections=rows=>rows.map(r=>({...r,class:r.class.replace(/\s+is-scrolled\b/g,'')}));
   if(baseline)assert.deepEqual(stableSections(result.sections),stableSections(baseline.sections));
   await page.locator('#que-gestionamos').screenshot({path:`${out}/section-${width}.png`});
   records.push({...result,requests,errors,regression:baseline?'Header, hero and other sections match baseline geometry/styles':'No pre-change render at this extra width'});
   assert.equal(errors.length,0);console.log(`VERIFICADO render ${width}`);await context.close();
  }
  fs.writeFileSync(`${out}/render-checks.json`,JSON.stringify(records,null,2));
 } finally {await browser.close();}
})();
