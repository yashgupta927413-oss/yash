let reviewIndex = 0;
let reviewInterval;
let policyMap = new Map();
const apiBase =
  window.location.port === '5173' || window.location.hostname === 'localhost'
    ? 'http://127.0.0.1:8000'
    : 'https://api.theyashgupta.com';

function setupMenu() {
  const menuToggle = document.getElementById('menuToggle');
  const navLinks = document.querySelector('.nav-links');
  if (!menuToggle || !navLinks) return;

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

function setupFaq() {
  document.querySelectorAll('.faq-q').forEach((button) => {
    button.addEventListener('click', () => {
      const item = button.closest('.faq-item');
      if (item) item.classList.toggle('open');
    });
  });
}

function setupReviews() {
  const reviewCards = document.querySelectorAll('.review-card');
  const nextBtn = document.getElementById('nextReview');
  const prevBtn = document.getElementById('prevReview');
  if (!nextBtn || !prevBtn || reviewCards.length === 0) return;

  const showReview = (index) => {
    reviewCards.forEach((card, i) => card.classList.toggle('active', i === index));
  };

  nextBtn.onclick = () => {
    reviewIndex = (reviewIndex + 1) % reviewCards.length;
    showReview(reviewIndex);
  };

  prevBtn.onclick = () => {
    reviewIndex = (reviewIndex - 1 + reviewCards.length) % reviewCards.length;
    showReview(reviewIndex);
  };

  if (reviewInterval) clearInterval(reviewInterval);
  reviewInterval = setInterval(() => {
    reviewIndex = (reviewIndex + 1) % reviewCards.length;
    showReview(reviewIndex);
  }, 6000);

  showReview(reviewIndex);

  const reviewSlider = document.getElementById('reviewSlider');
  if (reviewSlider) {
    let touchStartX = 0;
    let touchEndX = 0;
    reviewSlider.addEventListener(
      'touchstart',
      (event) => {
        touchStartX = event.changedTouches[0].clientX;
      },
      { passive: true }
    );
    reviewSlider.addEventListener(
      'touchend',
      (event) => {
        touchEndX = event.changedTouches[0].clientX;
        const delta = touchEndX - touchStartX;
        if (Math.abs(delta) < 35) return;
        if (delta < 0) {
          reviewIndex = (reviewIndex + 1) % reviewCards.length;
        } else {
          reviewIndex = (reviewIndex - 1 + reviewCards.length) % reviewCards.length;
        }
        showReview(reviewIndex);
      },
      { passive: true }
    );
  }
}

function animateCounters() {
  const counters = document.querySelectorAll('.stat-number');
  counters.forEach((counter) => {
    const target = Number(counter.dataset.target || 0);
    const suffix = counter.dataset.suffix || '+';
    let current = 0;
    const step = Math.max(1, Math.ceil(target / 40));

    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      counter.textContent = `${current}${suffix}`;
    }, 25);
  });
}

function setupCounterObserver() {
  const statsSection = document.getElementById('results');
  if (!statsSection) return;

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

function setupGsap() {
  const serviceCardsFallback = document.querySelectorAll('.service-stack-3d .service-card');
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

  if (!(window.gsap && window.ScrollTrigger)) return;

  gsap.registerPlugin(ScrollTrigger);

  const showcase = document.querySelector('.showcase-section');
  const mockup = document.querySelector('.device-mockup');
  const frames = gsap.utils.toArray('.frame');
  const depthCards = gsap.utils.toArray('.depth-card');
  const orbs = gsap.utils.toArray('.glow-orb');
  const serviceCards = gsap.utils.toArray('.service-stack-3d .service-card');

  if (showcase && mockup && frames.length > 0) {
    const mm = gsap.matchMedia();

    mm.add('(min-width: 1025px)', () => {
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
            start: 'top 75%',
            end: 'top 35%',
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
          invalidateOnRefresh: true,
        },
      });

      storyTl
        .to(mockup, { rotateY: 10, rotateX: -8, z: 110, duration: 1.2, ease: 'none' }, 0)
        .to(mockup, { rotateY: -10, rotateX: 8, z: -50, duration: 1.2, ease: 'none' }, 1.1)
        .to(mockup, { rotateY: 0, rotateX: 0, z: 0, duration: 1, ease: 'none' }, 2.2);

      depthCards.forEach((card, i) => {
        storyTl.fromTo(
          card,
          { y: 25 + i * 8, opacity: 0, rotate: -8 + i * 4 },
          { y: -18 - i * 10, opacity: 1, rotate: 6 - i * 3, duration: 1.4, ease: 'none' },
          0.2 + i * 0.25
        );
      });

      orbs.forEach((orb, i) => {
        storyTl.to(
          orb,
          { y: i % 2 === 0 ? -50 : 70, x: i % 2 === 0 ? 35 : -25, scale: 1.18, duration: 2, ease: 'none' },
          0
        );
      });

      frames.forEach((frame, index) => {
        storyTl.add(() => {
          frames.forEach((item) => item.classList.remove('active'));
          frame.classList.add('active');
        }, index * 0.8);
      });
    });

    mm.add('(max-width: 1024px)', () => {
      gsap.fromTo(
        mockup,
        { opacity: 0, y: 35, scale: 0.95 },
        {
          opacity: 1,
          y: 0,
          scale: 1,
          duration: 0.8,
          ease: 'power2.out',
          scrollTrigger: {
            trigger: showcase,
            start: 'top 78%',
            end: 'top 45%',
            scrub: true,
            invalidateOnRefresh: true,
          },
        }
      );

      const mobileFrames = document.querySelectorAll('.frame');
      if (mobileFrames.length > 1) {
        const setActiveFrame = (index) => {
          mobileFrames.forEach((frame, idx) => frame.classList.toggle('active', idx === index));
        };

        setActiveFrame(0);

        ScrollTrigger.create({
          trigger: showcase,
          start: 'top 72%',
          end: 'bottom 28%',
          scrub: 1,
          invalidateOnRefresh: true,
          onUpdate: (self) => {
            const progress = self.progress;
            let index = 0;

            if (progress < 0.34) {
              index = 0;
            } else if (progress < 0.67) {
              index = 1;
            } else {
              index = 2;
            }

            setActiveFrame(index);
          },
        });

        const screen = document.querySelector('.device-screen');
        if (screen) {
          let startX = 0;
          screen.addEventListener(
            'touchstart',
            (event) => {
              startX = event.changedTouches[0].clientX;
            },
            { passive: true }
          );
          screen.addEventListener(
            'touchend',
            (event) => {
              const endX = event.changedTouches[0].clientX;
              const delta = endX - startX;
              if (Math.abs(delta) < 30) return;

              const activeIndex = [...mobileFrames].findIndex((frame) => frame.classList.contains('active'));
              let nextIndex = activeIndex < 0 ? 0 : activeIndex;

              if (delta < 0) {
                nextIndex = Math.min(mobileFrames.length - 1, nextIndex + 1);
              } else {
                nextIndex = Math.max(0, nextIndex - 1);
              }

              setActiveFrame(nextIndex);
            },
            { passive: true }
          );
        }
      }
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
      card.addEventListener('mouseenter', () => gsap.to(image, { scale: 1.12, duration: 0.45, ease: 'power2.out' }));
      card.addEventListener('mouseleave', () => gsap.to(image, { scale: 1, duration: 0.45, ease: 'power2.out' }));
    });
  }
}

function setupShowcaseFallback() {
  const showcase = document.querySelector('.showcase-section');
  const mockup = document.querySelector('.device-mockup');
  const frames = Array.from(document.querySelectorAll('.frame'));
  if (!showcase || !mockup || frames.length === 0) return;

  const updateShowcase = () => {
    const rect = showcase.getBoundingClientRect();
    const viewport = window.innerHeight || 1;
    const start = viewport * 0.2;
    const end = viewport * -0.9;
    const distance = start - end;
    const progress = Math.min(1, Math.max(0, (start - rect.top) / distance));
    const frameIndex = Math.min(frames.length - 1, Math.floor(progress * frames.length));

    frames.forEach((frame, index) => frame.classList.toggle('active', index === frameIndex));
    const rotateY = (progress - 0.5) * 20;
    const rotateX = (0.5 - progress) * 12;
    const scale = 0.94 + progress * 0.06;
    mockup.style.transform = `perspective(1200px) rotateY(${rotateY}deg) rotateX(${rotateX}deg) scale(${scale})`;
  };

  window.addEventListener('scroll', updateShowcase, { passive: true });
  window.addEventListener('resize', updateShowcase);
  updateShowcase();
}

function openPolicyModal(title, content) {
  const modal = document.getElementById('policyModal');
  const modalTitle = document.getElementById('policyModalTitle');
  const modalBody = document.getElementById('policyModalBody');
  if (!modal || !modalTitle || !modalBody) return;

  modalTitle.textContent = title;
  modalBody.textContent = content;
  modal.setAttribute('aria-hidden', 'false');
  document.body.classList.add('modal-open');
}

function closePolicyModal() {
  const modal = document.getElementById('policyModal');
  if (!modal) return;
  modal.setAttribute('aria-hidden', 'true');
  document.body.classList.remove('modal-open');
}

function setupPolicyLinks() {
  const closeBtn = document.getElementById('policyModalClose');
  const backdrop = document.getElementById('policyModalBackdrop');
  if (closeBtn) closeBtn.onclick = closePolicyModal;
  if (backdrop) backdrop.onclick = closePolicyModal;
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closePolicyModal();
  });

  document.querySelectorAll('#footerPolicyLinks a').forEach((link) => {
    link.addEventListener('click', (event) => {
      const href = link.getAttribute('href');
      if (!href || !href.startsWith('#policy-')) return;
      const key = href.replace('#policy-', '');
      const policy = policyMap.get(key);
      if (!policy) return;
      event.preventDefault();
      const target = document.getElementById(`policy-${key}`);
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'center' });
      openPolicyModal(policy.title, policy.content);
    });
  });

  document.querySelectorAll('#policyCards .policy-card').forEach((card) => {
    card.addEventListener('click', () => {
      const id = card.id.replace('policy-', '');
      const policy = policyMap.get(id);
      if (!policy) return;
      openPolicyModal(policy.title, policy.content);
    });
  });
}

function setupBackToTop() {
  const backToTop = document.getElementById('backToTop');
  if (!backToTop) return;
  const toggle = () => {
    if (window.scrollY > 420) {
      backToTop.classList.add('visible');
    } else {
      backToTop.classList.remove('visible');
    }
  };
  window.addEventListener('scroll', toggle, { passive: true });
  toggle();
}

function setupImagePopup() {
  const modal = document.getElementById('imageModal');
  const modalPreview = document.getElementById('imageModalPreview');
  const closeBtn = document.getElementById('imageModalClose');
  const backdrop = document.getElementById('imageModalBackdrop');
  if (!modal || !modalPreview) return;

  const close = () => {
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('modal-open');
    modalPreview.src = '';
  };

  closeBtn?.addEventListener('click', close);
  backdrop?.addEventListener('click', close);
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') close();
  });

  document.querySelectorAll('.service-card img').forEach((img) => {
    img.style.cursor = 'zoom-in';
    img.addEventListener('click', () => {
      modalPreview.src = img.src;
      modalPreview.alt = img.alt || 'Service preview';
      modal.setAttribute('aria-hidden', 'false');
      document.body.classList.add('modal-open');
    });
  });
}

function applySectionOrder(sectionOrder) {
  if (!Array.isArray(sectionOrder) || sectionOrder.length === 0) return;
  const main = document.getElementById('mainContent');
  if (!main) return;

  sectionOrder.forEach((sectionId) => {
    if (sectionId === 'policies') {
      const policiesSection = document.getElementById('policies');
      const footer = document.querySelector('footer.footer');
      if (policiesSection && footer && footer.parentNode) {
        footer.parentNode.insertBefore(policiesSection, footer);
      }
      return;
    }
    const section = document.getElementById(sectionId);
    if (section && section.parentNode === main) {
      main.appendChild(section);
    }
  });
}

function setText(id, value) {
  const el = document.getElementById(id);
  if (el && value) el.textContent = value;
}

function escapeHtml(value) {
  return String(value || '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

async function loadAdminManagedContent() {
  try {
    const response = await fetch(`${apiBase}/api/homepage/`);
    if (!response.ok) return;
    const data = await response.json();

    setText('brandName', data.brand);
    setText('footerBrandName', data.brand);
    setText('heroEyebrow', data.hero_eyebrow);
    setText('heroTitle', data.hero_title);
    setText('heroDescription', data.hero_description);
    setText('primaryCtaText', data.primary_cta_text);
    setText('secondaryCtaText', data.secondary_cta_text);

    if (Array.isArray(data.trust_badges) && data.trust_badges.length >= 3) {
      setText('trustBadge1', `✅ ${data.trust_badges[0]}`);
      setText('trustBadge2', `✅ ${data.trust_badges[1]}`);
      setText('trustBadge3', `✅ ${data.trust_badges[2]}`);
    }

    if (Array.isArray(data.stats) && data.stats.length > 0) {
      const statsGrid = document.getElementById('statsGrid');
      if (statsGrid) {
        statsGrid.innerHTML = data.stats
          .map(
            (item) => `<article class="stat-card"><p class="stat-number" data-target="${item.value}" data-suffix="${escapeHtml(item.suffix || '+')}">0</p><p class="stat-label">${escapeHtml(item.label)}</p></article>`
          )
          .join('');
      }
    }

    if (Array.isArray(data.tools) && data.tools.length > 0) {
      const brandStrip = document.getElementById('brandStrip');
      if (brandStrip) {
        brandStrip.innerHTML = data.tools.map((tool) => `<span>${escapeHtml(tool)}</span>`).join('');
      }
    }

    if (Array.isArray(data.service_cards) && data.service_cards.length > 0) {
      const serviceGrid = document.getElementById('serviceGrid');
      if (serviceGrid) {
        serviceGrid.innerHTML = data.service_cards
          .map(
            (service) => `<article class="service-card"><img src="${escapeHtml(service.image_url)}" alt="${escapeHtml(service.title)}" /><h3>${escapeHtml(service.title)}</h3><p>${escapeHtml(service.description)}</p></article>`
          )
          .join('');
      }
    }

    if (Array.isArray(data.modules) && data.modules.length > 0) {
      const moduleGrid = document.getElementById('moduleGrid');
      if (moduleGrid) {
        moduleGrid.innerHTML = data.modules
          .map(
            (item) => `<article class="module-card"><h3>${escapeHtml(item.title)}</h3><ul><li>${escapeHtml(item.item_1)}</li><li>${escapeHtml(item.item_2)}</li><li>${escapeHtml(item.item_3)}</li><li>${escapeHtml(item.item_4)}</li></ul></article>`
          )
          .join('');
      }
    }

    if (Array.isArray(data.pricing_plans) && data.pricing_plans.length > 0) {
      const planGrid = document.getElementById('planGrid');
      if (planGrid) {
        planGrid.innerHTML = data.pricing_plans
          .map(
            (plan) => `<article class="plan-card ${plan.is_featured ? 'featured-plan' : ''}"><h3>${escapeHtml(plan.title)}</h3><p class="plan-price">${escapeHtml(plan.price)}</p><p>${escapeHtml(plan.description)}</p></article>`
          )
          .join('');
      }
    }

    if (Array.isArray(data.reviews) && data.reviews.length > 0) {
      const reviewSlider = document.getElementById('reviewSlider');
      if (reviewSlider) {
        reviewSlider.innerHTML = data.reviews
          .map(
            (review, index) => `<article class="review-card ${index === 0 ? 'active' : ''}"><p>“${escapeHtml(review.quote)}”</p><h4>${escapeHtml(review.customer_name)}</h4><span>${escapeHtml(review.customer_title)}</span></article>`
          )
          .join('');
      }
    }

    if (Array.isArray(data.google_reviews) && data.google_reviews.length > 0) {
      const googleReviewGrid = document.getElementById('googleReviewGrid');
      if (googleReviewGrid) {
        googleReviewGrid.innerHTML = data.google_reviews
          .map(
            (item) => `<article class="google-card"><p class="rating">${escapeHtml(item.rating)}</p><p>“${escapeHtml(item.quote)}”</p><span>${escapeHtml(item.source_label)}</span></article>`
          )
          .join('');
      }
    }

    if (Array.isArray(data.process_steps) && data.process_steps.length > 0) {
      const timelineGrid = document.getElementById('timelineGrid');
      if (timelineGrid) {
        timelineGrid.innerHTML = data.process_steps
          .map(
            (step) => `<article class="timeline-card"><span>${escapeHtml(step.step_number)}</span><h3>${escapeHtml(step.title)}</h3><p>${escapeHtml(step.description)}</p></article>`
          )
          .join('');
      }
    }

    if (Array.isArray(data.faqs) && data.faqs.length > 0) {
      const faqContainer = document.getElementById('faqContainer');
      if (faqContainer) {
        faqContainer.innerHTML = `<h2>Frequently Asked Questions</h2>${data.faqs
          .map((faq) => `<div class="faq-item"><button class="faq-q">${escapeHtml(faq.question)}</button><p class="faq-a">${escapeHtml(faq.answer)}</p></div>`)
          .join('')}`;
      }
    }

    if (Array.isArray(data.policies) && data.policies.length > 0) {
      policyMap = new Map();
      data.policies.forEach((policy) => policyMap.set(policy.policy_type, policy));
      const policyCards = document.getElementById('policyCards');
      if (policyCards) {
        policyCards.innerHTML = data.policies
          .map((policy) => `<article class="policy-card" id="policy-${escapeHtml(policy.policy_type)}" data-policy-title="${escapeHtml(policy.title)}" data-policy-content="${escapeHtml(policy.content)}"><h3>${escapeHtml(policy.title)}</h3><p>${escapeHtml(policy.content)}</p></article>`)
          .join('');
      }

      const footerPolicyLinks = document.getElementById('footerPolicyLinks');
      if (footerPolicyLinks) {
        footerPolicyLinks.innerHTML = data.policies
          .map((policy) => `<a href="#policy-${escapeHtml(policy.policy_type)}">${escapeHtml(policy.title)}</a>`)
          .join('');
      }
    }

    applySectionOrder(data.section_order);

    if (data.contact_email) {
      const emailBtn = document.getElementById('emailBtn');
      if (emailBtn) {
        emailBtn.href = `mailto:${data.contact_email}`;
        emailBtn.textContent = data.contact_email;
      }
    }

    if (data.contact_phone) {
      const digits = String(data.contact_phone).replace(/[^\d+]/g, '');
      const phoneBtn = document.getElementById('phoneBtn');
      if (phoneBtn) {
        phoneBtn.href = `tel:${digits}`;
        phoneBtn.textContent = `Call: ${data.contact_phone}`;
      }
    }

    if (data.whatsapp_number) {
      const message = encodeURIComponent('Hi Yash, I want digital marketing help for my business.');
      const floatMessage = encodeURIComponent('Hi Yash, I found your website and need digital marketing support.');
      const waBtn = document.getElementById('waBtn');
      const waFloat = document.getElementById('waFloat');
      if (waBtn) waBtn.href = `https://wa.me/${data.whatsapp_number}?text=${message}`;
      if (waFloat) waFloat.href = `https://wa.me/${data.whatsapp_number}?text=${floatMessage}`;
    }
  } catch (_error) {
    // keep static content if API is unavailable
  }
}

function boot() {
  document.querySelectorAll('#policyCards .policy-card').forEach((card) => {
    const id = card.id.replace('policy-', '');
    policyMap.set(id, {
      title: card.dataset.policyTitle || card.querySelector('h3')?.textContent || 'Policy',
      content: card.dataset.policyContent || card.querySelector('p')?.textContent || '',
    });
  });
  setupMenu();
  setupFaq();
  setupReviews();
  setupPolicyLinks();
  setupBackToTop();
  setupImagePopup();
  setupCounterObserver();
  setupGsap();
  if (!(window.gsap && window.ScrollTrigger)) {
    setupShowcaseFallback();
  }
}

loadAdminManagedContent().finally(() => {
  boot();
});
