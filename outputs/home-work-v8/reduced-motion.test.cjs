const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

function element(dataset = {}) {
  const listeners = {};
  const attributes = {};
  const classes = new Set();
  return {
    dataset,
    hidden: false,
    textContent: '',
    classList: { toggle(name, active) { active ? classes.add(name) : classes.delete(name); } },
    setAttribute(name, value) { attributes[name] = value; },
    getAttribute(name) { return attributes[name]; },
    addEventListener(name, handler) { listeners[name] = handler; },
    click() { listeners.click?.(); }
  };
}

const pause = element();
const counts = { creative: 2, management: 3, client: 2 };
const scenes = {};
const choices = [];
for (const [name, count] of Object.entries(counts)) {
  const buttons = Array.from({ length: count }, (_, index) => element({ workChoice: name, index: String(index) }));
  const variants = name === 'creative' ? Array.from({ length: 2 }, (_, index) => element({ workVariant: String(index) })) : [];
  scenes[name] = {
    dataset: {},
    querySelectorAll(selector) {
      return selector === '[data-work-variant]' ? variants : selector === `[data-work-choice="${name}"]` ? buttons : [];
    }
  };
  choices.push(...buttons);
}

const section = {
  querySelector(selector) {
    if (selector === '[data-work-pause]') return pause;
    const match = selector.match(/^\[data-work-scene="([^"]+)"\]$/);
    return match ? scenes[match[1]] : null;
  },
  querySelectorAll(selector) { return selector === '[data-work-choice]' ? choices : []; }
};
const media = { matches: true, addEventListener() {} };
const document = { hidden: false, querySelector() { return section; }, addEventListener() {} };
let scheduled = 0;
class IntersectionObserver {
  constructor(callback) { this.callback = callback; }
  observe() { this.callback([{ isIntersecting: true }]); }
}
const window = {
  matchMedia() { return media; },
  setTimeout() { scheduled += 1; return scheduled; },
  clearTimeout() {},
  IntersectionObserver
};
vm.runInNewContext(fs.readFileSync('js/home-work-v8.js', 'utf8'), { window, document, IntersectionObserver });

assert.equal(pause.hidden, true, 'reduced motion hides the irrelevant playback control');
assert.equal(scheduled, 0, 'reduced motion schedules no animation');
assert.deepEqual(Object.values(scenes).map(scene => scene.dataset.workState), ['0', '0', '0']);
choices.find(button => button.dataset.workChoice === 'management' && button.dataset.index === '2').click();
assert.equal(scenes.management.dataset.workState, '2', 'manual selection remains available');
assert.equal(scheduled, 0, 'manual selection does not start animation');
console.log('Reduced motion: static, manual selection available, no timers.');
