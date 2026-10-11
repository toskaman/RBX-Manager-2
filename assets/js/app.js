// RBX Manager 2 — Ultra-light Vanilla JS (< 3KB)
document.addEventListener('DOMContentLoaded', function () {
  // FAQ Accordion logic with ARIA compliance
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function (item) {
    const btn = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');
    if (!btn || !answer) return;

    btn.addEventListener('click', function () {
      const isExpanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', !isExpanded);
      answer.hidden = isExpanded;
      const icon = btn.querySelector('.faq-icon');
      if (icon) {
        icon.style.transform = isExpanded ? 'rotate(0deg)' : 'rotate(45deg)';
      }
    }, { passive: true });
  });

  // Video Facade play handler
  const video = document.getElementById('showcase-video');
  if (video) {
    video.addEventListener('play', function () {
      video.setAttribute('preload', 'auto');
    }, { once: true, passive: true });
  }
});
