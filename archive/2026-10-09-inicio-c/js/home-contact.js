const contactChoices = {
  marketing: {
    title: 'Cuéntanos sobre tus campañas.',
    description: 'Cuéntanos qué vendes y qué necesitas mejorar para preparar una propuesta acorde al alcance.',
    action: 'Cotizar marketing'
  },
  general: {
    title: 'Definamos juntos el siguiente paso.',
    description: 'Revisaremos tu tienda y tus prioridades para decidir si necesitas campañas, software o un proyecto.',
    action: 'Agendar reunión'
  },
  software: {
    title: 'Veamos la bandeja con tu equipo.',
    description: 'Una demo útil parte de tus consultas, responsables y próximos pasos reales.',
    action: 'Agendar demo'
  },
  automatizaciones: {
    title: 'Cuéntanos qué proceso quieres resolver.',
    description: 'Revisaremos el alcance, las herramientas y los entregables antes de cotizar el proyecto.',
    action: 'Cotizar proyecto'
  }
};

const contactTitle = document.querySelector('#contact-choice-title');
const contactDescription = document.querySelector('#contact-choice-description');
const contactSubmit = document.querySelector('#contact-submit');
const contactPicker = document.querySelectorAll('.contact-choice');

function chooseContactIntent(intent) {
  const choice = contactChoices[intent];
  if (!choice || !contactTitle || !contactDescription || !contactSubmit) return;
  contactTitle.textContent = choice.title;
  contactDescription.textContent = choice.description;
  contactSubmit.firstChild.textContent = `${choice.action} `;
  contactPicker.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.contactIntent === intent)));
}

document.querySelectorAll('[data-contact-intent]').forEach(control => {
  control.addEventListener('click', () => chooseContactIntent(control.dataset.contactIntent));
});

chooseContactIntent('marketing');
