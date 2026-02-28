(function () {
  const toggleBtn = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('[data-nav]');
  if (!toggleBtn || !nav) return;

  function closeMenu() {
    nav.classList.remove('is-open');
    toggleBtn.setAttribute('aria-expanded', 'false');
  }

  toggleBtn.addEventListener('click', function () {
    const isOpen = nav.classList.toggle('is-open');
    toggleBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });

  window.addEventListener('resize', function () {
    if (window.innerWidth > 992) {
      closeMenu();
    }
  });

  document.addEventListener('click', function (event) {
    if (!nav.contains(event.target) && !toggleBtn.contains(event.target)) {
      closeMenu();
    }
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
      closeMenu();
    }
  });
})();
