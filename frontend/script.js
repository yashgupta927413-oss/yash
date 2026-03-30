const counters = document.querySelectorAll('.stat-number');
const reviews = document.querySelectorAll('.review-card');
const nextBtn = document.getElementById('nextReview');
const prevBtn = document.getElementById('prevReview');
const menuToggle = document.getElementById('menuToggle');
const navLinks = document.querySelector('.nav-links');
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

if (menuToggle && navLinks) {
  menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    const expanded = menuToggle.getAttribute('aria-expanded') === 'true';
    menuToggle.setAttribute('aria-expanded', String(!expanded));
  });

  navLinks.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      menuToggle.setAttribute('aria-expanded', 'false');
    });
  });
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

if (window.gsap && window.ScrollTrigger) {
  gsap.registerPlugin(ScrollTrigger);

  const showcase = document.querySelector('.showcase-section');
  const mockup = document.querySelector('.device-mockup');
  const frames = gsap.utils.toArray('.frame');

  if (showcase && mockup && frames.length > 0) {
    gsap.fromTo(
      mockup,
      { scale: 0.88, opacity: 0.75, y: 40 },
      {
        scale: 1,
        opacity: 1,
        y: 0,
        duration: 1,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: showcase,
          start: 'top 70%',
          end: 'top 30%',
          scrub: true,
        },
      }
    );

    const storyTl = gsap.timeline({
      scrollTrigger: {
        trigger: showcase,
        start: 'top top',
        end: '+=1400',
        scrub: true,
        pin: true,
      },
    });

    frames.forEach((frame, index) => {
      storyTl.add(() => {
        frames.forEach((item) => item.classList.remove('active'));
        frame.classList.add('active');
      }, index * 0.8);
    });
  }
}
