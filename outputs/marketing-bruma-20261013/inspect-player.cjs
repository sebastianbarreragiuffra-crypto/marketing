const fs=require('node:fs');
const {chromium}=require('C:/Users/SEBAS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1200}});
  await page.goto('http://127.0.0.1:8767/marketing.html');
  const b=page.getByRole('button',{name:'Reproducir anuncio de ejemplo',exact:true});await b.focus();await page.keyboard.press('Enter');
  await page.waitForFunction(()=>document.querySelector('#bruma-example-video').currentTime>1);
  console.log(await page.locator('video').evaluate(v=>({time:v.currentTime,paused:v.paused,focus:document.activeElement===v,audioBytes:v.webkitAudioDecodedByteCount,dim:[v.videoWidth,v.videoHeight]})));
  await page.keyboard.press('Space');await page.waitForTimeout(200);console.log('Space',await page.locator('video').evaluate(v=>({paused:v.paused,time:v.currentTime,muted:v.muted})));
  const cdp=await page.context().newCDPSession(page);await cdp.send('Accessibility.enable');
  const ax=await cdp.send('Accessibility.getFullAXTree');
  const controls=ax.nodes.filter(n=>n.role&&/button|slider|Video/.test(n.role.value));
  console.log(controls.map(n=>({role:n.role.value,name:n.name&&n.name.value,backend:n.backendDOMNodeId,ignored:n.ignored,props:n.properties})).filter(n=>!n.ignored).slice(-25));
  fs.writeFileSync('outputs/marketing-bruma-20261013/native-controls.json',JSON.stringify(controls,null,2));
 }finally{await browser.close();}
})();
