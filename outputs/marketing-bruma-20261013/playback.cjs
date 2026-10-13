const fs=require('node:fs');
const assert=require('node:assert/strict');
const {chromium}=require('C:/Users/SEBAS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const out='outputs/marketing-bruma-20261013';
async function nativeButton(page,client,name){
 let n;
 for(let attempt=0;attempt<10&&!n;attempt++){
  const {nodes}=await client.send('Accessibility.getFullAXTree');
  n=nodes.find(n=>!n.ignored&&n.role?.value==='button'&&name.test(n.name?.value||''));
  if(!n){if(attempt===9)console.log('Controles observados:',nodes.filter(n=>!n.ignored&&n.role?.value==='button').map(n=>n.name?.value));await page.waitForTimeout(150);}
 }
 assert(n,`Native control ${name} present`);
 const {model}=await client.send('DOM.getBoxModel',{backendNodeId:n.backendDOMNodeId});
 const q=model.content,x=(q[0]+q[2]+q[4]+q[6])/4,y=(q[1]+q[3]+q[5]+q[7])/4;
 await client.send('Input.dispatchMouseEvent',{type:'mousePressed',x,y,button:'left',clickCount:1});
 await client.send('Input.dispatchMouseEvent',{type:'mouseReleased',x,y,button:'left',clickCount:1});
 return n.name.value;
}
async function state(page){return page.locator('#bruma-example-video').evaluate(v=>({src:v.src,poster:v.poster,time:v.currentTime,duration:v.duration,paused:v.paused,ended:v.ended,muted:v.muted,volume:v.volume,dim:[v.videoWidth,v.videoHeight],audioBytes:v.webkitAudioDecodedByteCount,videoBytes:v.webkitVideoDecodedByteCount,frameCount:v.getVideoPlaybackQuality().totalVideoFrames,error:v.error&&v.error.code,focus:document.activeElement===v,focusVisible:v.matches(':focus-visible'),height:v.getBoundingClientRect().height,playerHeight:v.parentElement.getBoundingClientRect().height,overlayHidden:v.parentElement.querySelector('button').hidden,overflow:document.documentElement.scrollWidth>innerWidth}));}
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});const only=Number(process.argv[2]);const results=only?JSON.parse(fs.readFileSync(`${out}/playback-checks.json`)).filter(r=>r.width!==only):[];
 try{
  for(const width of (only?[only]:[1440,390])){
   const context=await browser.newContext({viewport:{width,height:1600},isMobile:width<768,hasTouch:width<768,deviceScaleFactor:1});
   const page=await context.newPage();const requests=[];const errors=[];
   page.on('request',r=>{if(r.url().includes('/assets/marketing-video/'))requests.push({url:r.url(),type:r.resourceType()});});page.on('pageerror',e=>errors.push(e.message));
   await page.goto('http://127.0.0.1:8767/marketing.html');await page.evaluate(()=>document.fonts.ready);await page.locator('#que-gestionamos').scrollIntoViewIfNeeded();await page.waitForTimeout(400);
   const initial=await state(page);assert.equal(requests.filter(r=>r.url.endsWith('.mp4')).length,0);
   await page.evaluate(()=>{
    const v=document.querySelector('#bruma-example-video');window.brumaEvents=[];
    for(const event of ['loadstart','loadedmetadata','play','playing','pause','ended','volumechange','seeking','seeked'])v.addEventListener(event,()=>window.brumaEvents.push({event,time:v.currentTime,muted:v.muted}));
    const audio=new AudioContext();const source=audio.createMediaElementSource(v);const analyser=audio.createAnalyser();analyser.fftSize=2048;source.connect(analyser);analyser.connect(audio.destination);window.brumaAudio={audio,analyser};
    document.querySelector('.bv-play').addEventListener('click',()=>audio.resume(),{once:true});
   });
   const button=page.getByRole('button',{name:'Reproducir anuncio de ejemplo',exact:true});
   let overlayFocus;
   if(width>=768){await button.focus();await page.keyboard.press('Tab');await page.keyboard.press('Shift+Tab');overlayFocus=await button.evaluate(e=>({visible:e.matches(':focus-visible'),outline:getComputedStyle(e).outlineWidth}));assert.equal(overlayFocus.visible,true);assert.equal(overlayFocus.outline,'3px');await page.keyboard.press('Enter');}
   else await button.tap();
   await page.waitForFunction(()=>document.querySelector('#bruma-example-video').currentTime>1);
   const playing=await state(page);assert.equal(playing.paused,false);assert.equal(playing.overlayHidden,true);assert.equal(playing.focus,true);assert.equal(playing.error,null);assert(playing.audioBytes>0);assert(playing.frameCount>0);assert.equal(playing.muted,false);assert.equal(playing.playerHeight,initial.playerHeight);assert.equal(playing.duration,10);
   let audioPeak=0;
   for(let i=0;i<5;i++){const p=await page.evaluate(()=>{const data=new Float32Array(2048);window.brumaAudio.analyser.getFloatTimeDomainData(data);return Math.max(...data.map(Math.abs));});audioPeak=Math.max(audioPeak,p);await page.waitForTimeout(100);}
   assert(audioPeak>0.00001,'Decoded sound produces a non-zero signal');
   await page.locator('video').focus();await page.keyboard.press('Space');await page.waitForFunction(()=>document.querySelector('video').paused);const paused=await state(page);await page.waitForTimeout(200);assert(Math.abs((await state(page)).time-paused.time)<.01);
   const client=await context.newCDPSession(page);await client.send('Accessibility.enable');
   const muteName=await nativeButton(page,client,/^silenciar$/i);await page.waitForFunction(()=>document.querySelector('video').muted);
   const unmuteName=await nativeButton(page,client,/^activar sonido$/i);await page.waitForFunction(()=>!document.querySelector('video').muted);
   const resumeName=await nativeButton(page,client,/^reproducir$/i);await page.waitForFunction(()=>!document.querySelector('video').paused);
   const beforeResize=await state(page);await page.setViewportSize({width:width>=768?390:1440,height:1600});await page.waitForTimeout(450);const resized=await state(page);
   assert.equal(resized.src,initial.src);assert.equal(resized.poster,initial.poster);assert(resized.time>=beforeResize.time);assert.equal(resized.paused,false);assert.equal(resized.overflow,false);
   await page.setViewportSize({width,height:1600});await page.waitForTimeout(100);
   await page.waitForFunction(()=>document.querySelector('video').currentTime>=4.8);
   await page.locator('video').focus();await page.keyboard.press('Space');await page.waitForFunction(()=>document.querySelector('video').paused);
   const middle=await state(page);await page.mouse.move(0,0);await page.locator('#que-gestionamos').screenshot({path:`${out}/playing-${width}.png`});
   assert.equal(middle.playerHeight,initial.playerHeight);
   await nativeButton(page,client,/^reproducir$/i);await page.waitForFunction(()=>document.querySelector('video').ended,null,{timeout:15000});
   const ended=await state(page);assert.equal(ended.time,10);assert.equal(ended.paused,true);assert.equal(ended.overlayHidden,true);assert(ended.frameCount>=290);assert.equal(ended.error,null);
   await page.locator('#que-gestionamos').screenshot({path:`${out}/end-${width}.png`});
   await nativeButton(page,client,/^reproducir$/i);await page.waitForFunction(()=>document.querySelector('video').currentTime>.25&&document.querySelector('video').currentTime<3);
   const replay=await state(page);assert.equal(replay.paused,false);await page.locator('video').focus();await page.keyboard.press('Space');
   const mediaUrls=[...new Set(requests.filter(r=>r.url.endsWith('.mp4')).map(r=>r.url))];assert.equal(mediaUrls.length,1);assert.equal(mediaUrls[0],initial.src);
   const posterUrls=[...new Set(requests.filter(r=>r.url.endsWith('.webp')).map(r=>r.url))];assert.equal(posterUrls.length,1);assert.equal(posterUrls[0],initial.poster);
   const events=await page.evaluate(()=>window.brumaEvents);assert.equal(events.filter(e=>e.event==='loadedmetadata').length,1);assert.equal(errors.length,0);
   results.push({width,initial,playing,audioPeak,overlayFocus,keyboardPause:true,nativeMuteControl:muteName,nativeUnmuteControl:unmuteName,nativeResumeControl:resumeName,paused,resized,middle,ended,replay,requests,events,errors,perceptualAudio:'NOT VERIFIED: headless Chrome verifies decoding and signal; no physical speaker listening'});
   fs.writeFileSync(`${out}/playback-checks.json`,JSON.stringify(results,null,2));console.log(`VERIFICADO reproducción ${width}: inicio, pausa, audio/silencio, resize sin reinicio, fin y repetición.`);await client.detach();await context.close();
  }
 }finally{await browser.close();}
})();
