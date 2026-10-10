const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = fs.readFileSync(path.resolve(__dirname, '../../js/experience-motion.js'), 'utf8');

function setup(reduce = false, native = true) {
  const scheduled = new Map(), events = new Map(), observers = [];
  let nextId = 0;
  function element() {
    const classes = new Set();
    return {
      classList: { add: (...names) => names.forEach(n => classes.add(n)), remove: (...names) => names.forEach(n => classes.delete(n)), contains: n => classes.has(n) },
      parentElement: { closest: () => null },
      contains: other => other === this,
      offsetWidth: 100,
      classes,
      listeners: new Map(),
      addEventListener(name, listener) { this.listeners.set(name, listener); }
    };
  }
  const intro = element(), title = element(), copy = element(), work = element(), image = element(), detail = element();
  for (const node of [intro, title, copy, work, image, detail]) node.contains = other => other === node;
  image.complete = true; image.naturalWidth = 546;
  detail.open = false;
  const fields = { '[data-channel-title]': title, '[data-channel-copy]': copy, '[data-channel-work]': work, '[data-channel-image]': image };
  const doc = {
    hidden: false, activeElement: null, documentElement: element(),
    getElementById: () => intro,
    querySelector: selector => selector === '.purchase-services' ? { querySelector: s => fields[s] } : fields[selector],
    querySelectorAll: selector => selector === '.hx-tabs, .purchase-tabs' ? [] : selector === 'main details' ? [detail] : [intro],
    addEventListener(name, fn) { events.set(name, fn); }
  };
  const pref = { matches: reduce, addEventListener(name, fn) { (this.listeners ||= []).push(fn); } };
  class Observer {
    constructor(callback) { this.callback = callback; observers.push(this); }
    observe() {} unobserve() {} disconnect() { this.disconnected = true; }
  }
  const win = {
    matchMedia: () => pref, IntersectionObserver: Observer,
    setTimeout(fn) { scheduled.set(++nextId, fn); return nextId; },
    clearTimeout(id) { scheduled.delete(id); }
  };
  const context = { window: win, document: doc, IntersectionObserver: Observer, CSS: { supports: () => native } };
  win.CSS = context.CSS;
  vm.runInNewContext(source, context);
  return { intro, title, copy, work, image, detail, doc, pref, scheduled, events, observers,
    reduce(value) { pref.matches = value; pref.listeners.forEach(fn => fn({ matches: value })); },
    enter() { observers[0]?.callback([{ isIntersecting: true, target: intro }]); },
    select() { events.get('orbita:marketing-service')(); }
  };
}

test('reduced motion starts with visible static content and still permits native selection', () => {
  const app = setup(true);
  app.enter(); app.select();
  assert.equal(app.observers.length, 0);
  assert.equal(app.scheduled.size, 0);
  for (const node of [app.intro, app.title, app.copy, app.work, app.image]) assert.equal(node.classes.size, 0);
});
test('turning reduced motion on ends ongoing entrances and transitions immediately', () => {
  const app = setup();
  app.enter(); app.select();
  assert.ok(app.intro.classes.has('site-motion-enter'));
  assert.ok(app.image.classes.has('site-motion-switch'));
  app.reduce(true);
  assert.equal(app.scheduled.size, 0);
  assert.ok(app.observers[0].disconnected);
  app.select();
  for (const node of [app.intro, app.title, app.copy, app.work, app.image]) assert.equal(node.classes.size, 0);
});
test('rapid tab changes replace rather than accumulate animation work', () => {
  const app = setup();
  for (let i = 0; i < 20; i++) app.select();
  assert.equal(app.scheduled.size, 4);
  [...app.scheduled.values()].forEach(fn => fn());
  assert.equal(app.scheduled.size, 0);
  assert.equal(app.image.classes.size, 0);
});
test('keyboard focus cancels motion around the focused control', () => {
  const app = setup(); app.enter();
  app.doc.activeElement = app.intro;
  app.events.get('focusin')({ target: app.intro });
  assert.equal(app.intro.classes.size, 0);
  app.enter();
  assert.equal(app.intro.classes.size, 0);
});
test('an entrance runs once and backgrounding the document clears work', () => {
  const app = setup(); app.enter();
  [...app.scheduled.values()].forEach(fn => fn());
  app.enter(); assert.equal(app.scheduled.size, 0);
  app.select(); app.doc.hidden = true;
  app.events.get('visibilitychange')();
  assert.equal(app.scheduled.size, 0);
});
test('older-browser fallback preserves native disclosure and motion preference', () => {
  const app = setup(false, false);
  app.detail.open = true; app.detail.listeners.get('toggle')();
  assert.ok(app.detail.classes.has('site-motion-detail'));
  app.reduce(true);
  assert.equal(app.detail.open, true);
  assert.equal(app.detail.classes.size, 0);
  app.detail.open = false; app.detail.listeners.get('toggle')();
  assert.equal(app.detail.open, false);
  assert.equal(app.scheduled.size, 0);
});
test('manual Home views have finite motion controlled by the page event', () => {
  const app = setup();
  app.events.get('orbita:hero-view')({ detail: { panelId: 'hx-slide-2' } });
  assert.ok(app.intro.classes.has('site-motion-view'));
  [...app.scheduled.values()].forEach(fn => fn());
  assert.equal(app.intro.classes.size, 0);
  app.reduce(true);
  app.events.get('orbita:hero-view')({ detail: { panelId: 'hx-slide-1' } });
  assert.equal(app.scheduled.size, 0);
});
