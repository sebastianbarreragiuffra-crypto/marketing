const { chromium } = require('C:/Users/SEBAS/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('node:fs/promises');
const path = require('node:path');
const out = __dirname;
const url = 'http://127.0.0.1:8767/index.html';
async function inspect(page) {
  return page.evaluate(() => {
    const hero = document.querySelector('.oh-hero');
    const box = e => { const r = e.getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height }; };
    const selectors = ['.oh-heading','.oh-terms','.oh-ad','.oh-gisba','.oh-cta','.oh-example-note'];
    const essential = hero.querySelectorAll('.oh-lead,.oh-terms p,.oh-role,.oh-ad__account strong,.oh-ad__account div span,.oh-ad__strip,.oh-channel-note,.oh-gisba__brand span,.oh-message__sender,.oh-message__bubble,.oh-quote strong,.oh-quote__state,.oh-quote div span,.oh-status,.oh-next-step p');
    const ids = [...document.querySelectorAll('[id]')].map(e=>e.id);
    return {
      width: innerWidth, pageOverflow: document.documentElement.scrollWidth > innerWidth,
      h1Count: document.querySelectorAll('h1').length,
      title: document.querySelector('h1').textContent.replace(/\s+/g,' ').trim(),
      heroText: hero.innerText, hero: box(hero),
      layout: Object.fromEntries(selectors.map(s=>[s,box(document.querySelector(s))])),
      heroActions: [...hero.querySelectorAll('a,button,input,select,textarea')].map(e=>({tag:e.tagName,text:e.innerText,href:e.getAttribute('href'),box:box(e)})),
      essentialMinFont: Math.min(...[...essential].map(e=>parseFloat(getComputedStyle(e).fontSize))),
      clippedText: [...hero.querySelectorAll('p,h1,h2,strong,span')].filter(e=>e.clientWidth>0 && e.scrollWidth>e.clientWidth+1).map(e=>({class:e.className,text:e.textContent})),
      images: [...hero.querySelectorAll('img')].map(e=>({src:e.currentSrc,loaded:e.complete&&e.naturalWidth>0,natural:[e.naturalWidth,e.naturalHeight],render:[e.clientWidth,e.clientHeight]})),
      duplicatedIds: ids.filter((v,i)=>ids.indexOf(v)!==i),
      fonts: document.fonts.status,
      motion: [...hero.querySelectorAll('*')].filter(e=>getComputedStyle(e).animationName!=='none').map(e=>({class:e.className,animation:getComputedStyle(e).animationName})),
      header: box(document.querySelector('.site-header')),
      lower: [...document.querySelectorAll('main > section:not(.oh-hero)')].map(e=>({id:e.id,class:e.className})),
      ctaTarget: document.querySelector('.oh-cta').getAttribute('href')
    };
  });
}
(async () => {
  const browser = await chromium.launch({ executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true });
  const checks = [];
  for (const width of [1440,1920,390,320,768,1100,1101,700,701]) {
    const page = await browser.newPage({viewport:{width,height:900},deviceScaleFactor:1});
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.goto(url,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);
    const check=await inspect(page);check.errors=errors;checks.push(check);
    if ([1440,1920,390,320].includes(width)) {
      await page.screenshot({path:path.join(out,`hero-${width}.png`),fullPage:true,clip:{x:0,y:0,width,height:Math.ceil(check.hero.y+check.hero.h)}});
    }
    if (width===390) {
      const button=page.locator('.menu-toggle');await button.click();
      check.menu={expanded:await button.getAttribute('aria-expanded'),prices:await page.getByRole('navigation',{name:'Navegación principal'}).getByRole('link',{name:'Precios',exact:true}).isVisible(),login:await page.getByRole('navigation',{name:'Navegación principal'}).getByRole('link',{name:'Iniciar sesión',exact:true}).isVisible()};
      await page.screenshot({path:path.join(out,'menu-390.png')});
      await page.keyboard.press('Escape');
      check.menu.closedOnEscape=await button.getAttribute('aria-expanded')==='false';
      check.menu.focusReturned=await button.evaluate(e=>document.activeElement===e);
      await page.locator('.oh-cta').focus();
      check.focus=await page.locator('.oh-cta').evaluate(e=>({visible:e.matches(':focus-visible'),outline:getComputedStyle(e).outlineWidth,minHeight:e.clientHeight}));
      await page.locator('.oh-cta').press('Enter');await page.waitForURL('**/hablemos.html');
      check.contact={url:page.url(),preview:await page.getByText('Vista previa · Tu consulta no se enviará.',{exact:true}).isVisible()};
    }
    await page.close();
  }
  for (const settings of [{javaScriptEnabled:false},{reducedMotion:'reduce'}]) {
    const context=await browser.newContext({...settings,viewport:{width:390,height:900}});
    const page=await context.newPage();await page.goto(url,{waitUntil:'networkidle'});await page.evaluate(()=>document.fonts.ready);
    checks.push({...await inspect(page),mode:settings});await context.close();
  }
  await fs.writeFile(path.join(out,'browser-checks.json'),JSON.stringify(checks,null,2));
  await browser.close();
  console.log(JSON.stringify(checks.map(c=>({width:c.width,mode:c.mode,overflow:c.pageOverflow,minFont:c.essentialMinFont,clipped:c.clippedText,images:c.images.every(i=>i.loaded),heroHeight:c.hero.h,errors:c.errors,menu:c.menu,focus:c.focus,contact:c.contact})),null,2));
})().catch(e=>{console.error(e);process.exitCode=1;});
