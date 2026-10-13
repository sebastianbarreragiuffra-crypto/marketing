const fs=require('node:fs');
const assert=require('node:assert/strict');
const {chromium}=require('C:/Users/SEBAS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 try{
  const context=await browser.newContext({viewport:{width:360,height:844},isMobile:true,hasTouch:true,reducedMotion:'reduce'});
  // Isolate the tested page from automatic preview reloads during unrelated edits.
  await context.route('**/__live.js',route=>route.abort());
  const page=await context.newPage();await page.goto('http://127.0.0.1:8767/marketing.html');await page.evaluate(()=>document.fonts.ready);
  await page.locator('#que-gestionamos').scrollIntoViewIfNeeded();
  const before=await page.locator('video').evaluate(v=>({time:v.currentTime,paused:v.paused,motion:matchMedia('(prefers-reduced-motion: reduce)').matches}));assert.equal(before.time,0);assert.equal(before.paused,true);assert.equal(before.motion,true);
  const button=page.getByRole('button',{name:'Reproducir anuncio de ejemplo',exact:true});await button.focus();await page.keyboard.press('Enter');await page.waitForFunction(()=>document.querySelector('video').currentTime>.3);
  const focused=await page.locator('video').evaluate(v=>({focus:v===document.activeElement,visible:v.matches(':focus-visible'),outline:getComputedStyle(v).outlineWidth}));assert.equal(focused.focus,true);assert.equal(focused.visible,true);assert.equal(focused.outline,'3px');
  await page.keyboard.press('Space');await page.waitForFunction(()=>document.querySelector('video').paused);
  const cta=page.locator('#que-gestionamos .bv-cta');await cta.focus();await page.keyboard.press('Tab');await page.keyboard.press('Shift+Tab');const ctaFocus=await cta.evaluate(e=>({visible:e.matches(':focus-visible'),outline:getComputedStyle(e).outlineWidth,href:e.getAttribute('href')}));assert.equal(ctaFocus.visible,true);assert.equal(ctaFocus.outline,'3px');assert.equal(ctaFocus.href,'#contacto');
  await page.keyboard.press('Enter');await page.waitForURL('**/marketing.html#contacto');
  const contactPreview=await page.locator('.cp-action-note').textContent();assert(contactPreview.includes('Tu consulta no se enviará'));
  const contactControlsDisabled=await page.locator('.cp-controls').isDisabled();
  await page.locator('#que-gestionamos').scrollIntoViewIfNeeded();const scrollBefore=await page.evaluate(()=>scrollY);const client=await context.newCDPSession(page);await client.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:180,y:500,id:1}]});for(let i=1;i<=8;i++){await client.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:180,y:500-i*25,id:1}]});await page.waitForTimeout(20);}await client.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});await page.waitForTimeout(200);assert((await page.evaluate(()=>scrollY))>scrollBefore);
  fs.writeFileSync('outputs/marketing-bruma-20261013/accessibility-checks.json',JSON.stringify({width:360,height:844,reducedMotion:before,keyboardPlayPause:true,focusTransfer:focused,ctaFocus,contactAnchor:true,contactPreview,contactControlsDisabled,verticalTouchScroll:true},null,2));
  console.log('VERIFICADO teclado, foco, movimiento reducido, contacto y scroll vertical a 360 × 844.');await context.close();
 }finally{await browser.close();}
})();
