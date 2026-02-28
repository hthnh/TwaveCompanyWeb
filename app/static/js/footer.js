(function () {
  const yearNode = document.querySelector('[data-current-year]');
  if (yearNode) {
    yearNode.textContent = String(new Date().getFullYear());
  }

  const form = document.querySelector('[data-newsletter-form]');
  const msg = document.querySelector('[data-newsletter-msg]');
  if (!form || !msg) return;

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    const emailInput = form.querySelector('input[name="email"]');
    if (!emailInput) return;

    const email = emailInput.value.trim();
    const isValidEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

    msg.classList.remove('is-success', 'is-error');
    if (!isValidEmail) {
      msg.textContent = 'Email chưa hợp lệ. Vui lòng kiểm tra lại.';
      msg.classList.add('is-error');
      return;
    }

    msg.textContent = 'Cảm ơn bạn. Chúng tôi sẽ liên hệ sớm.';
    msg.classList.add('is-success');
    form.reset();
  });
})();
