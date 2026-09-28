// Filtering enhances the static page. All projects remain available without JavaScript.
(() => {
  const controls = document.querySelector('.filters');
  if (!controls) return;

  const buttons = [...controls.querySelectorAll('button[data-filter]')];
  const cards = [...document.querySelectorAll('.card[data-category]')];
  const status = document.querySelector('.filter-status');

  function filterProjects(category, announce = true) {
    let visible = 0;
    for (const card of cards) {
      card.hidden = category !== 'all' && card.dataset.category !== category;
      if (!card.hidden) visible++;
    }
    for (const button of buttons) {
      button.setAttribute('aria-pressed', String(button.dataset.filter === category));
    }
    if (announce) status.textContent = `Visar ${visible} av ${cards.length} projekt.`;
  }

  controls.hidden = false;
  status.hidden = false;
  filterProjects('all');
  controls.addEventListener('click', (event) => {
    const button = event.target.closest('button[data-filter]');
    if (button) filterProjects(button.dataset.filter);
  });

  // Competence links and bookmarks must also reach cards hidden by a filter.
  function revealTarget() {
    const id = window.location.hash.slice(1);
    const target = document.getElementById(id);
    if (target && target.matches('.card[data-category]') && target.hidden) {
      filterProjects('all');
      target.scrollIntoView({ block: 'start' });
    }
  }
  window.addEventListener('hashchange', revealTarget);
  document.addEventListener('click', (event) => {
    const link = event.target.closest('a[href^="#"]');
    if (!link) return;
    const target = document.getElementById(link.getAttribute('href').slice(1));
    if (target && target.matches('.card[data-category]') && target.hidden) {
      filterProjects('all');
    }
  });
  revealTarget();
})();
