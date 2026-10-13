const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');

const script = fs.readFileSync(path.join(__dirname, 'hero.js'), 'utf8');

function element(dataset = {}) {
  const attrs = new Map();
  const events = new Map();
  const classes = new Set();
  return {
    dataset,
    attrs,
    events,
    classes,
    classList: { toggle(name, on) { if (on) classes.add(name); else classes.delete(name); } },
    setAttribute(name, value) { attrs.set(name, value); },
    getAttribute(name) { return attrs.get(name); },
    removeAttribute(name) { attrs.delete(name); },
    addEventListener(name, callback) { events.set(name, callback); },
    click() { events.get('click')?.(); },
    textContent: '',
    title: '',
    disabled: false,
    inert: false,
  };
}

function setup({ reduced = false, mobile = true } = {}) {
  const cards = ['google', 'meta', 'tiktok'].map((name) => element({ ad: name }));
  const buttons = ['google', 'meta', 'tiktok'].map((name) => element({ channel: name }));
  const play = element();
  const status = element();
  const deck = element();
  const rotator = element();
  rotator.querySelector = (selector) => ({ '.v6-showcase__deck': deck, '[data-play-toggle]': play, '[data-rotator-status]': status })[selector];
  rotator.querySelectorAll = (selector) => selector === '[data-ad]' ? cards : buttons;
  const media = {
    mobile: { matches: mobile, addEventListener(_event, listener) { this.listener = listener; } },
    reduced: { matches: reduced, addEventListener(_event, listener) { this.listener = listener; } },
  };
  const documentEvents = new Map();
  const doc = {
    hidden: false,
    querySelector: () => rotator,
    addEventListener(name, callback) { documentEvents.set(name, callback); },
  };
  let callback = null;
  let delay = null;
  const win = {
    matchMedia: (query) => query.includes('reduced-motion') ? media.reduced : media.mobile,
    setTimeout(fn, ms) { callback = fn; delay = ms; return 1; },
    clearTimeout() { callback = null; },
    addEventListener() {},
  };
  let observed = null;
  class Observer {
    constructor(fn) { observed = fn; }
    observe() {}
  }
  vm.runInNewContext(script, { window: win, document: doc, IntersectionObserver: Observer });
  return {
    cards, buttons, play, rotator, doc, media,
    get timer() { return callback; },
    get delay() { return delay; },
    visible(ratio) { observed([{ intersectionRatio: ratio }]); },
    tick() { const fn = callback; callback = null; fn?.(); },
    visibilityChanged() { documentEvents.get('visibilitychange')(); },
  };
}

const normal = setup();
assert.equal(normal.rotator.dataset.activeChannel, 'meta');
assert.equal(normal.timer, null, 'Must wait for at least 50% visibility');
normal.visible(0.49);
assert.equal(normal.timer, null);
normal.visible(0.5);
assert.equal(normal.delay, 3000);
normal.tick();
assert.equal(normal.rotator.dataset.activeChannel, 'google');
normal.tick();
assert.equal(normal.rotator.dataset.activeChannel, 'tiktok');
normal.tick();
assert.equal(normal.rotator.dataset.activeChannel, 'meta');
normal.doc.hidden = true;
normal.visibilityChanged();
assert.equal(normal.timer, null, 'Hidden tab must stop the timer');
normal.doc.hidden = false;
normal.visibilityChanged();
assert.notEqual(normal.timer, null);
normal.buttons[0].click();
assert.equal(normal.rotator.dataset.activeChannel, 'google');
assert.equal(normal.timer, null, 'Manual selection must pause');
assert.equal(normal.play.getAttribute('aria-label'), 'Reproducir cambio automático');
normal.play.click();
assert.equal(normal.delay, 3000);

const reduced = setup({ reduced: true });
reduced.visible(1);
assert.equal(reduced.timer, null, 'Reduced motion must stay static');
assert.equal(reduced.play.disabled, true);
reduced.buttons[2].click();
assert.equal(reduced.rotator.dataset.activeChannel, 'tiktok', 'Manual selection must remain available');
assert.equal(reduced.timer, null);

const desktop = setup({ mobile: false });
assert.equal(desktop.cards.every((card) => !card.attrs.has('aria-hidden')), true);
desktop.visible(1);
assert.equal(desktop.timer, null, 'Desktop shows all cards without rotation');

console.log('Hero rotator: 3-second order, visibility, hidden tab, manual pause, reduced motion, desktop OK');
