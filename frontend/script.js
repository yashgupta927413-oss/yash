const counters = document.querySelectorAll('.stat-number');
const reviews = document.querySelectorAll('.review-card');
const nextBtn = document.getElementById('nextReview');
const prevBtn = document.getElementById('prevReview');
let reviewIndex = 0;

function animateCounters() {
  counters.forEach((counter) => {
    const target = Number(counter.dataset.target || 0);
    let current = 0;
    const step = Math.max(1, Math.ceil(target / 40));

    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      counter.textContent = `${current}${target >= 100 ? '+' : 'x'}`;
    }, 25);
  });
}

function showReview(index) {
  reviews.forEach((card, i) => {
    card.classList.toggle('active', i === index);
  });
}

if (nextBtn && prevBtn && reviews.length > 0) {
  nextBtn.addEventListener('click', () => {
    reviewIndex = (reviewIndex + 1) % reviews.length;
    showReview(reviewIndex);
  });

  prevBtn.addEventListener('click', () => {
    reviewIndex = (reviewIndex - 1 + reviews.length) % reviews.length;
    showReview(reviewIndex);
  });

  setInterval(() => {
    reviewIndex = (reviewIndex + 1) % reviews.length;
    showReview(reviewIndex);
  }, 6000);
}

const statsSection = document.getElementById('results');
if (statsSection) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCounters();
          observer.disconnect();
        }
      });
    },
    { threshold: 0.35 }
  );

  observer.observe(statsSection);
}
