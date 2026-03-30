const counters = document.querySelectorAll('.stat-number');
const reviews = document.querySelectorAll('.review-card');
const nextBtn = document.getElementById('nextReview');
const prevBtn = document.getElementById('prevReview');
const menuToggle = document.getElementById('menuToggle');
const navLinks = document.querySelector('.nav-links');
const faqQuestions = document.querySelectorAll('.faq-q');
const serviceCardsFallback = document.querySelectorAll('.service-stack-3d .service-card');
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
  const depthCards = gsap.utils.toArray('.depth-card');
  const orbs = gsap.utils.toArray('.glow-orb');
  const serviceCards = gsap.utils.toArray('.service-stack-3d .service-card');

  if (showcase && mockup && frames.length > 0) {
    gsap.fromTo(
      mockup,
      { scale: 0.84, opacity: 0.7, y: 55, rotateX: 14, rotateY: -10 },
      {
        scale: 1,
        opacity: 1,
        y: 0,
        rotateX: 0,
        rotateY: 0,
        duration: 1,
        ease: 'power3.out',
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
        end: '+=1800',
        scrub: true,
        pin: true,
      },
    });

    storyTl
      .to(mockup, { rotateY: 10, rotateX: -8, z: 120, duration: 1.2, ease: 'none' }, 0)
      .to(mockup, { rotateY: -10, rotateX: 8, z: -60, duration: 1.2, ease: 'none' }, 1.25)
      .to(mockup, { rotateY: 0, rotateX: 0, z: 0, duration: 1, ease: 'none' }, 2.5);

    depthCards.forEach((card, i) => {
      storyTl.fromTo(
        card,
        { y: 30 + i * 10, opacity: 0, rotate: -10 + i * 5 },
        { y: -20 - i * 12, opacity: 1, rotate: 8 - i * 4, duration: 1.6, ease: 'none' },
        0.2 + i * 0.25
      );
    });

    orbs.forEach((orb, i) => {
      storyTl.to(
        orb,
        { y: i % 2 === 0 ? -60 : 80, x: i % 2 === 0 ? 40 : -30, scale: 1.2, duration: 2, ease: 'none' },
        0
      );
    });

    frames.forEach((frame, index) => {
      storyTl.add(() => {
        frames.forEach((item) => item.classList.remove('active'));
        frame.classList.add('active');
      }, index * 0.8);
    });
  }

  if (serviceCards.length > 0) {
    gsap.fromTo(
      serviceCards,
      { opacity: 0, y: 70, rotateX: -18, rotateY: 8, scale: 0.88 },
      {
        opacity: 1,
        y: 0,
        rotateX: 0,
        rotateY: 0,
        scale: 1,
        ease: 'back.out(1.35)',
        stagger: 0.12,
        duration: 1.1,
        scrollTrigger: {
          trigger: '.service-stack-3d',
          start: 'top 78%',
          end: 'top 35%',
          scrub: false,
        },
      }
    );

    serviceCards.forEach((card) => {
      const image = card.querySelector('img');
      if (!image) return;

      card.addEventListener('mouseenter', () => {
        gsap.to(image, { scale: 1.12, duration: 0.45, ease: 'power2.out' });
      });

      card.addEventListener('mouseleave', () => {
        gsap.to(image, { scale: 1, duration: 0.45, ease: 'power2.out' });
      });
    });
  }
}

faqQuestions.forEach((button) => {
  button.addEventListener('click', () => {
    const item = button.closest('.faq-item');
    if (item) {
      item.classList.toggle('open');
    }
  });
});

if (serviceCardsFallback.length > 0) {
  serviceCardsFallback.forEach((card, index) => {
    card.classList.add('animate-ready');
    card.style.setProperty('--card-delay', `${index * 90}ms`);
  });

  const serviceObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          serviceObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.18 }
  );

  serviceCardsFallback.forEach((card) => serviceObserver.observe(card));
}

async function loadAdminManagedContent() {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/homepage/');
    if (!response.ok) return;
    const data = await response.json();

    if (Array.isArray(data.faqs) && data.faqs.length > 0) {
      const faqContainer = document.getElementById('faqContainer');
      if (faqContainer) {
        faqContainer.innerHTML = `<h2>Frequently Asked Questions</h2>${data.faqs
          .map(
            (faq) => `\n<div class=\"faq-item\">\n<button class=\"faq-q\">${faq.question}</button>\n<p class=\"faq-a\">${faq.answer}</p>\n</div>`
          )
          .join('')}`;

        faqContainer.querySelectorAll('.faq-q').forEach((button) => {
          button.addEventListener('click', () => {
            const item = button.closest('.faq-item');
            if (item) item.classList.toggle('open');
          });
        });
      }
    }

    if (Array.isArray(data.policies) && data.policies.length > 0) {
      const policyCards = document.getElementById('policyCards');
      if (policyCards) {
        policyCards.innerHTML = data.policies
          .map(
            (policy) =>
              `<article class=\"policy-card\"><h3>${policy.title}</h3><p>${policy.content}</p></article>`
          )
          .join('');
      }

      const footerPolicyLinks = document.getElementById('footerPolicyLinks');
      if (footerPolicyLinks) {
        footerPolicyLinks.innerHTML = data.policies
          .map((policy) => `<a href=\"#\">${policy.title}</a>`)
          .join('');
      }
    }
  } catch (_error) {
    // keep static content if API is unavailable
  }
}

loadAdminManagedContent();
