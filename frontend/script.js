/* ============================================================
   theyashgupta.com — Apple-style scroll interactions
   ============================================================ */

const prefersReducedMotion = window.matchMedia(
  "(prefers-reduced-motion: reduce)"
).matches;

let LENIS = null;

document.addEventListener("DOMContentLoaded", () => {
  LENIS = initLenis();
  initProgressBar();
  initTopnav();
  initMobileMenu();
  initSmoothAnchor();
  initPolicyModal();
  initFaq();
  initAuditForm();
  initLeadForm();
  initBillingToggle();
  initSubscriptionModal();
  initSubForm();
  initWhatsappContext();
  initCookieBanner();
  initInsightsFeed();
  if (!prefersReducedMotion) {
    initMagneticButtons();
    initTiltCards();
  }

  if (window.gsap && window.ScrollTrigger && !prefersReducedMotion) {
    gsap.registerPlugin(ScrollTrigger);
    initHeroIntro();
    initActiveNav();
    initHeroParallax();
    initPinCards();
    initSteps();
    initWorkCards();
    initCounters();
    initPlanPop();
    initMetricsPop();
    initDetailCards();
    initAboutPop();
    initTestimonialsPop();
    initFaqPop();
    initInsightsPop();
    initLogosPop();
    initSubsPop();
  } else {
    // No-motion fallback: make hidden things visible
    document
      .querySelectorAll(".pin-card, .step, .work-card")
      .forEach((el) => {
        el.style.opacity = 1;
        el.style.transform = "none";
      });
    document.querySelectorAll(".metric-num").forEach((el) => {
      const t = el.dataset.target;
      const suffix = el.dataset.suffix || "";
      el.textContent = `${t}${suffix}`;
    });
  }
});

/* --------------------------------------------------- Top nav blur on scroll */
function initTopnav() {
  const nav = document.getElementById("topnav");
  if (!nav) return;
  const onScroll = () => {
    nav.classList.toggle("scrolled", window.scrollY > 20);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

/* --------------------------------------------------- Mobile menu */
function initMobileMenu() {
  const btn = document.getElementById("menuToggle");
  const links = document.getElementById("navLinks");
  if (!btn || !links) return;

  const close = () => {
    btn.classList.remove("open");
    links.classList.remove("open");
    btn.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  };

  btn.addEventListener("click", () => {
    const isOpen = btn.classList.toggle("open");
    links.classList.toggle("open", isOpen);
    btn.setAttribute("aria-expanded", isOpen ? "true" : "false");
    document.body.style.overflow = isOpen ? "hidden" : "";
  });

  links.querySelectorAll("a").forEach((a) => a.addEventListener("click", close));
}

/* --------------------------------------------------- Smooth anchor scroll */
function initSmoothAnchor() {
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (e) => {
      const id = link.getAttribute("href");
      if (id.length < 2) return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      const y = target.getBoundingClientRect().top + window.scrollY - 70;
      if (LENIS) {
        LENIS.scrollTo(y, { duration: 1.4 });
      } else {
        window.scrollTo({ top: y, behavior: "smooth" });
      }
    });
  });
}

/* --------------------------------------------------- Hero parallax */
function initHeroParallax() {
  const hero = document.querySelector(".hero");
  if (!hero) return;

  gsap.to(".orb-a", {
    yPercent: 30,
    ease: "none",
    scrollTrigger: {
      trigger: hero,
      start: "top top",
      end: "bottom top",
      scrub: true,
    },
  });
  gsap.to(".orb-b", {
    yPercent: -20,
    ease: "none",
    scrollTrigger: {
      trigger: hero,
      start: "top top",
      end: "bottom top",
      scrub: true,
    },
  });
  gsap.to(".hero-inner", {
    yPercent: -10,
    opacity: 0.4,
    ease: "none",
    scrollTrigger: {
      trigger: hero,
      start: "top top",
      end: "bottom 60%",
      scrub: true,
    },
  });
  gsap.to(".hero-grid", {
    yPercent: 20,
    ease: "none",
    scrollTrigger: {
      trigger: hero,
      start: "top top",
      end: "bottom top",
      scrub: true,
    },
  });
}

/* --------------------------------------------------- Pinned section: cards reveal in sequence */
function initPinCards() {
  const cards = document.querySelectorAll(".pin-card");
  if (!cards.length) return;

  // Apple-style spring entrance — overshoot then settle
  const spring = "back.out(1.6)";

  cards.forEach((card) => {
    gsap.fromTo(
      card,
      { opacity: 0, y: 60, scale: 0.94 },
      {
        opacity: 1,
        y: 0,
        scale: 1,
        duration: 1.1,
        ease: spring,
        scrollTrigger: {
          trigger: card,
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );
  });
}

/* --------------------------------------------------- Process steps stagger reveal */
function initSteps() {
  const steps = document.querySelectorAll(".step");
  if (!steps.length) return;

  gsap.fromTo(
    steps,
    { opacity: 0, y: 40, scale: 0.96 },
    {
      opacity: 1,
      y: 0,
      scale: 1,
      duration: 0.95,
      ease: "back.out(1.4)",
      stagger: 0.1,
      scrollTrigger: {
        trigger: ".steps",
        start: "top 80%",
      },
    }
  );
}

/* --------------------------------------------------- Work cards reveal */
function initWorkCards() {
  const cards = document.querySelectorAll(".work-card");
  if (!cards.length) return;

  gsap.fromTo(
    cards,
    { opacity: 0, y: 60, scale: 0.94 },
    {
      opacity: 1,
      y: 0,
      scale: 1,
      duration: 1.05,
      ease: "back.out(1.5)",
      stagger: 0.14,
      scrollTrigger: {
        trigger: ".work-grid",
        start: "top 80%",
      },
    }
  );

  cards.forEach((card) => {
    const glow = card.querySelector(".art-glow");
    if (!glow) return;
    gsap.fromTo(
      glow,
      { scale: 0.85, opacity: 0.6 },
      {
        scale: 1.15,
        opacity: 1,
        ease: "none",
        scrollTrigger: {
          trigger: card,
          start: "top 90%",
          end: "bottom 10%",
          scrub: true,
        },
      }
    );
  });
}

/* --------------------------------------------------- Counters */
function initCounters() {
  document.querySelectorAll(".metric-num").forEach((el) => {
    const target = parseFloat(el.dataset.target) || 0;
    const decimals = parseInt(el.dataset.decimals || "0", 10);
    const suffix = el.dataset.suffix || "";

    const obj = { val: 0 };
    gsap.to(obj, {
      val: target,
      duration: 1.6,
      ease: "power2.out",
      scrollTrigger: {
        trigger: el,
        start: "top 85%",
        once: true,
      },
      onUpdate: () => {
        el.textContent = `${obj.val.toFixed(decimals)}${suffix}`;
      },
      onComplete: () => {
        el.textContent = `${target.toFixed(decimals)}${suffix}`;
      },
    });
  });
}

/* --------------------------------------------------- Detail section cards spring reveal */
function initDetailCards() {
  const groups = [
    { trigger: "#webdev .cap-grid", items: "#webdev .cap-card" },
    { trigger: "#marketing .channel-grid", items: "#marketing .channel-card" },
    { trigger: "#seo .pillar-grid", items: "#seo .pillar-card" },
    { trigger: "#seo .seo-callout", items: "#seo .seo-callout > div" },
  ];

  groups.forEach(({ trigger, items }) => {
    const els = document.querySelectorAll(items);
    if (!els.length) return;
    gsap.fromTo(
      els,
      { opacity: 0, y: 50, scale: 0.94 },
      {
        opacity: 1,
        y: 0,
        scale: 1,
        duration: 1,
        ease: "back.out(1.5)",
        stagger: 0.08,
        scrollTrigger: {
          trigger,
          start: "top 85%",
        },
      }
    );
  });

  // Detail head fade-in
  document.querySelectorAll(".detail-head").forEach((head) => {
    gsap.fromTo(
      head,
      { opacity: 0, y: 30 },
      {
        opacity: 1,
        y: 0,
        duration: 0.9,
        ease: "power3.out",
        scrollTrigger: { trigger: head, start: "top 85%" },
      }
    );
  });
}

/* --------------------------------------------------- Pricing plans pop */
function initPlanPop() {
  const plans = document.querySelectorAll(".plan");
  if (!plans.length) return;

  gsap.fromTo(
    plans,
    { opacity: 0, y: 70, scale: 0.92 },
    {
      opacity: 1,
      y: 0,
      scale: 1,
      duration: 1.1,
      ease: "back.out(1.5)",
      stagger: 0.12,
      scrollTrigger: {
        trigger: ".pricing-grid",
        start: "top 80%",
      },
    }
  );
}

/* --------------------------------------------------- Metric numbers pop */
function initMetricsPop() {
  const metrics = document.querySelectorAll(".metric");
  if (!metrics.length) return;

  gsap.fromTo(
    metrics,
    { opacity: 0, y: 40, scale: 0.92 },
    {
      opacity: 1,
      y: 0,
      scale: 1,
      duration: 0.95,
      ease: "back.out(1.6)",
      stagger: 0.09,
      scrollTrigger: {
        trigger: ".metrics-inner",
        start: "top 85%",
      },
    }
  );
}

/* --------------------------------------------------- Policy Modal (Apple pop) */

const POLICIES = {
  privacy: {
    eyebrow: "Last updated · May 2026",
    title: "Privacy Policy",
    body: `
      <p>This Privacy Policy explains how <strong>theyashgupta.com</strong> ("we", "us") collects, uses, and protects information you provide when interacting with this website and our services.</p>

      <h3>1. Information we collect</h3>
      <ul>
        <li><strong>Contact details</strong> you submit via forms, email, phone, or WhatsApp (name, email, phone, company, project brief).</li>
        <li><strong>Usage data</strong> collected automatically by our analytics tools (pages viewed, referrer, device type, approximate location, anonymised IP).</li>
        <li><strong>Marketing data</strong> when you click through ads or email campaigns we run on your behalf.</li>
      </ul>

      <h3>2. How we use it</h3>
      <ul>
        <li>To respond to enquiries and deliver services you have requested.</li>
        <li>To send relevant updates about projects or service offerings (you can opt out at any time).</li>
        <li>To improve site performance and the quality of our work.</li>
      </ul>

      <h3>3. Sharing</h3>
      <p>We do not sell your data. We share it only with trusted sub-processors (analytics, email, hosting, payment) strictly to deliver our services. Legal disclosure is made only if required by law.</p>

      <h3>4. Your rights</h3>
      <p>You may request access, correction, or deletion of your personal data at any time by emailing <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a>. We respond within 30 days.</p>

      <h3>5. Retention &amp; security</h3>
      <p>We keep contact records for as long as the business relationship is active, plus 2 years for compliance. Data is stored on encrypted services and access is role-restricted.</p>

      <h3>6. Contact</h3>
      <p>Questions about this policy? Email <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a>.</p>
    `,
  },
  terms: {
    eyebrow: "Last updated · May 2026",
    title: "Terms of Service",
    body: `
      <p>By engaging <strong>theyashgupta.com</strong> for web development, performance, SEO, or paid-media services, you agree to the following terms.</p>

      <h3>1. Scope of work</h3>
      <p>Every engagement begins with a written proposal defining deliverables, milestones, timelines, and acceptance criteria. Work outside that scope is treated as a change request and may be billed separately.</p>

      <h3>2. Payments</h3>
      <ul>
        <li>Fixed-scope projects: 50% deposit on kickoff, balance on launch.</li>
        <li>Retainers: billed monthly in advance; cancellable with 14 days' notice.</li>
        <li>Pay-per-lead: invoiced weekly based on validated leads.</li>
        <li>All prices are exclusive of applicable taxes (GST where relevant).</li>
      </ul>

      <h3>3. Intellectual property</h3>
      <p>Final deliverables transfer to the client upon full payment. We retain the right to display non-confidential parts of the work in our portfolio. Pre-existing tools, libraries, and frameworks remain ours or their original owners'.</p>

      <h3>4. Client responsibilities</h3>
      <p>Clients agree to provide timely feedback, content, and access (hosting, analytics, ad accounts). Delays in client input may shift project timelines and are not refundable.</p>

      <h3>5. Warranty &amp; limitation of liability</h3>
      <p>Work is delivered "as-is" with reasonable craft and care. We do not warrant uninterrupted uptime, specific search rankings, ad ROAS, or revenue outcomes. Total liability is capped at fees paid for the engagement in question.</p>

      <h3>6. Termination</h3>
      <p>Either party may terminate with written notice. Work completed up to the termination date is billable and deliverable.</p>

      <h3>7. Governing law</h3>
      <p>These terms are governed by the laws of India. Disputes are resolved in the courts of Lucknow, Uttar Pradesh.</p>
    `,
  },
  refund: {
    eyebrow: "Last updated · May 2026",
    title: "Refund & Cancellation Policy",
    body: `
      <p>We aim for clear scope and fair outcomes. This policy explains how cancellations and refunds work across our engagement models.</p>

      <h3>1. Fixed-scope projects</h3>
      <ul>
        <li>The 50% kickoff deposit is non-refundable once project planning has begun.</li>
        <li>If work is cancelled mid-project, fees are pro-rated to the milestones completed.</li>
        <li>Completed assets (designs, code, configs) are delivered after pro-rata settlement.</li>
      </ul>

      <h3>2. Monthly retainers</h3>
      <ul>
        <li>Cancellable with 14 days' written notice — billing stops at the end of the current cycle.</li>
        <li>Unused retainer hours do not roll over and are not refundable.</li>
      </ul>

      <h3>3. Pay-per-lead engagements</h3>
      <ul>
        <li>Lead-quality criteria are defined in writing before campaigns launch.</li>
        <li>Leads failing the agreed criteria (wrong country, fake number, spam) are replaced free of charge.</li>
        <li>Refunds are not issued for delivered, qualifying leads.</li>
      </ul>

      <h3>4. How to request</h3>
      <p>Email <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a> with your invoice reference and reason. We respond within 5 business days.</p>
    `,
  },
  cookies: {
    eyebrow: "Last updated · May 2026",
    title: "Cookie Policy",
    body: `
      <p>This site uses cookies and similar technologies to improve performance, understand how the site is used, and (with your consent) measure marketing.</p>

      <h3>1. Types of cookies we use</h3>
      <ul>
        <li><strong>Essential</strong> — required for the site to function; cannot be disabled.</li>
        <li><strong>Analytics</strong> — Google Analytics 4 / Tag Manager, set only if you accept analytics cookies.</li>
        <li><strong>Marketing</strong> — Meta Pixel and Google Ads tags, set only if you accept marketing cookies.</li>
      </ul>

      <h3>2. Managing cookies</h3>
      <p>You can clear or block cookies via your browser settings. Blocking essential cookies may break parts of the site.</p>

      <h3>3. Third-party processors</h3>
      <p>Analytics and ad cookies are processed by Google and Meta under their respective privacy policies.</p>

      <h3>4. Questions</h3>
      <p>Email <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a> for more information.</p>
    `,
  },
  disclaimer: {
    eyebrow: "Last updated · May 2026",
    title: "Disclaimer",
    body: `
      <p>The information and services offered on <strong>theyashgupta.com</strong> are provided for general business purposes. By using this site, you accept the following:</p>

      <h3>1. No guaranteed results</h3>
      <p>Web development, SEO, and paid-media outcomes depend on many variables outside our control — including market conditions, offer quality, competitive intensity, and platform algorithms. While we apply best practices and disclose our methodology transparently, we do not guarantee specific rankings, traffic, leads, revenue, or ROAS.</p>

      <h3>2. Performance metrics shown</h3>
      <p>Statistics displayed on this site (traffic lifts, ROAS, lead counts) represent average or selected results across past engagements. Your results will vary based on your stage, niche, and budget.</p>

      <h3>3. External links</h3>
      <p>This site may link to third-party platforms (WhatsApp, Google, Meta, etc.). We are not responsible for the content, privacy practices, or terms of those external services.</p>

      <h3>4. Not legal, financial, or tax advice</h3>
      <p>Nothing on this site constitutes legal, financial, or tax advice. Consult a qualified professional for those matters.</p>

      <h3>5. Changes</h3>
      <p>We may update this disclaimer at any time. Continued use of the site means you accept the updated version.</p>
    `,
  },
};

function initPolicyModal() {
  const modal = document.getElementById("policyModal");
  const card = document.getElementById("policyModalCard");
  const backdrop = document.getElementById("policyModalBackdrop");
  const closeBtn = document.getElementById("policyModalClose");
  const titleEl = document.getElementById("policyModalTitle");
  const eyebrowEl = document.getElementById("policyModalEyebrow");
  const bodyEl = document.getElementById("policyModalBody");
  if (!modal || !card || !bodyEl) return;

  let lastFocus = null;

  const open = (key) => {
    const p = POLICIES[key];
    if (!p) return;
    titleEl.textContent = p.title;
    eyebrowEl.textContent = p.eyebrow;
    bodyEl.innerHTML = p.body.trim();
    bodyEl.scrollTop = 0;

    lastFocus = document.activeElement;
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    document.body.classList.add("modal-open");
    requestAnimationFrame(() => closeBtn?.focus());
  };

  const close = () => {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.body.classList.remove("modal-open");
    if (lastFocus && typeof lastFocus.focus === "function") {
      lastFocus.focus();
    }
  };

  document.querySelectorAll("[data-policy]").forEach((a) => {
    a.addEventListener("click", (e) => {
      e.preventDefault();
      open(a.getAttribute("data-policy"));
    });
  });

  closeBtn?.addEventListener("click", close);
  backdrop?.addEventListener("click", close);
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modal.classList.contains("is-open")) close();
  });
}

/* --------------------------------------------------- FAQ accordion (single-open behavior) */
function initFaq() {
  const items = document.querySelectorAll(".faq-item");
  if (!items.length) return;
  items.forEach((item) => {
    item.addEventListener("toggle", () => {
      if (item.open) {
        items.forEach((other) => {
          if (other !== item && other.open) other.open = false;
        });
      }
    });
  });
}

/* --------------------------------------------------- Audit lead-magnet form */
function initAuditForm() {
  const form = document.getElementById("auditForm");
  if (!form) return;
  const successEl = document.getElementById("auditSuccess");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const submitBtn = form.querySelector(".form-submit");
    const fd = new FormData(form);
    const data = {
      type: "seo_audit_request",
      url: fd.get("url"),
      email: fd.get("email"),
    };
    await sendLead(data, form, submitBtn, successEl);
  });
}

/* --------------------------------------------------- Main contact lead form */
function initLeadForm() {
  const form = document.getElementById("leadForm");
  if (!form) return;
  const successEl = document.getElementById("leadSuccess");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const submitBtn = form.querySelector(".form-submit");
    const fd = new FormData(form);
    const data = {
      type: "project_inquiry",
      name: fd.get("name"),
      email: fd.get("email"),
      company: fd.get("company"),
      phone: fd.get("phone"),
      projectType: fd.get("projectType"),
      budget: fd.get("budget"),
      brief: fd.get("brief"),
    };
    await sendLead(data, form, submitBtn, successEl);
  });
}

/* --------------------------------------------------- Shared submit handler
   POSTs JSON to /api/lead/ (Django backend). On success → show toast + reset
   form. On failure → mailto: fallback so the lead is never lost. */
async function sendLead(data, form, submitBtn, successEl) {
  const apiBase = document.querySelector('meta[name="api-base"]')?.content || "";
  const url = `${apiBase}/api/lead/`;

  // Lock the button while we submit
  const originalLabel = submitBtn.querySelector("span")?.textContent;
  submitBtn.disabled = true;
  if (originalLabel) submitBtn.querySelector("span").textContent = "Sending…";

  try {
    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    if (!res.ok) throw new Error(`Server returned ${res.status}`);
    // Success → reset form, show toast
    form.reset();
    successEl.classList.add("shown");
    setTimeout(() => successEl.classList.remove("shown"), 10000);
  } catch (err) {
    // Backend unreachable — last-ditch mailto: so the customer's effort isn't wasted.
    const subjects = {
      project_inquiry: `Project inquiry — ${data.name || "site visitor"}`,
      subscription_inquiry: `Subscription — ${data.projectType || "plan"} · ${data.name || "site visitor"}`,
      seo_audit_request: `SEO audit request — ${data.url || ""}`,
    };
    const subject = encodeURIComponent(subjects[data.type] || subjects.project_inquiry);
    const body = encodeURIComponent(
      Object.entries(data)
        .filter(([, v]) => v)
        .map(([k, v]) => `${k}: ${v}`)
        .join("\n")
    );
    window.location.href = `mailto:yash@theyashgupta.com?subject=${subject}&body=${body}`;
    console.warn("Lead API failed, opened mailto fallback:", err);
  } finally {
    submitBtn.disabled = false;
    if (originalLabel) submitBtn.querySelector("span").textContent = originalLabel;
  }
}

/* ============================================================
   Website subscription plans (WaaS) — #plans
   ============================================================ */

const WA_NUMBER = "919696345822";

const BILLING = {
  monthly: { period: "/ month", label: "Monthly" },
  annual: { period: "/ year", label: "Annual" },
};

// Which billing period the section is currently showing. Read by the modal and
// the WhatsApp links so every surface quotes the same price.
let currentBilling = "monthly";

// Assigned by initSubscriptionModal so other handlers can dismiss the modal.
let closeSubModal = () => {};

/** 4999 → "₹4,999" (Indian digit grouping). */
const formatINR = (n) => `₹${Number(n).toLocaleString("en-IN")}`;

/** wa.me deep link carrying a pre-filled message. */
const waLink = (text) => `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(text)}`;

/** Price label for a tier card, e.g. "₹649" (monthly) or "₹6,999/yr" (annual). */
function planPriceLabel(card, billing = currentBilling) {
  return billing === "annual"
    ? `${formatINR(card.dataset.annual)}/yr`
    : formatINR(card.dataset.monthly);
}

/** "Hi Yash, I want to discuss the ₹649 Business Plus Plan." */
function planWaMessage(card, billing = currentBilling) {
  const name = card.dataset.plan;
  // Tier names that already end in "Plan" must not become "… Plan plan".
  const suffix = /plan$/i.test(name) ? "" : " plan";
  return `Hi Yash, I want to discuss the ${planPriceLabel(card, billing)} ${name}${suffix}.`;
}

/* --------------------------------------------------- Monthly / annual toggle */
function initBillingToggle() {
  const opts = document.querySelectorAll(".billing-opt");
  const cards = document.querySelectorAll(".sub-card");
  if (!opts.length || !cards.length) return;

  const render = (billing) => {
    if (!BILLING[billing]) return;
    currentBilling = billing;

    opts.forEach((opt) => {
      const on = opt.dataset.billing === billing;
      opt.classList.toggle("is-active", on);
      opt.setAttribute("aria-pressed", on ? "true" : "false");
    });

    cards.forEach((card) => {
      const monthly = Number(card.dataset.monthly);
      const annual = Number(card.dataset.annual);
      const priceEl = card.querySelector("[data-price]");
      const periodEl = card.querySelector("[data-period]");
      const savingEl = card.querySelector("[data-saving]");
      const cta = card.querySelector("[data-plan-cta]");
      const wa = card.querySelector("[data-plan-wa]");

      if (priceEl) priceEl.textContent = formatINR(billing === "annual" ? annual : monthly);
      if (periodEl) periodEl.textContent = BILLING[billing].period;

      if (savingEl) {
        if (billing === "annual") {
          // Derived from the two prices, never hard-coded — the number on screen
          // can't drift away from what the tier actually costs.
          const saved = monthly * 12 - annual;
          savingEl.textContent =
            saved > 0 ? `Save ${formatINR(saved)} vs paying monthly` : "Billed once a year";
          savingEl.classList.toggle("is-neutral", saved <= 0);
        } else {
          savingEl.textContent = "Billed monthly · cancel anytime";
          savingEl.classList.add("is-neutral");
        }
      }

      // Only tiers whose CTA label quotes a price carry these attributes.
      if (cta && cta.dataset.ctaMonthly && cta.dataset.ctaAnnual) {
        cta.textContent = billing === "annual" ? cta.dataset.ctaAnnual : cta.dataset.ctaMonthly;
      }
      if (wa) wa.href = waLink(planWaMessage(card, billing));
    });

    // Keep the modal in step with the visible toggle, so the dropdown never
    // quotes a monthly figure while the section is showing annual pricing.
    const billingSelect = document.getElementById("subBillingSelect");
    if (billingSelect) billingSelect.value = BILLING[billing].label;

    const planSelect = document.getElementById("subPlanSelect");
    if (planSelect) {
      const per = billing === "annual" ? "/yr" : "/mo";
      cards.forEach((card) => {
        const opt = [...planSelect.options].find((o) => o.value === card.dataset.plan);
        if (!opt) return;
        const amount = formatINR(billing === "annual" ? card.dataset.annual : card.dataset.monthly);
        opt.textContent = `${card.dataset.plan} — ${amount}${per}`;
      });
    }
  };

  opts.forEach((opt) => opt.addEventListener("click", () => render(opt.dataset.billing)));

  render("monthly");
}

/* --------------------------------------------------- Scroll lock shared by modals
   Lenis runs its own rAF loop, so `body { overflow: hidden }` alone doesn't stop
   the page moving behind a modal — it has to be paused explicitly. */
function lockScroll() {
  document.body.classList.add("modal-open");
  LENIS?.stop();
}
function unlockScroll() {
  document.body.classList.remove("modal-open");
  LENIS?.start();
}

/* --------------------------------------------------- Subscription enquiry modal */
function initSubscriptionModal() {
  const modal = document.getElementById("subModal");
  if (!modal) return;

  const backdrop = document.getElementById("subModalBackdrop");
  const closeBtn = document.getElementById("subModalClose");
  const titleEl = document.getElementById("subModalTitle");
  const eyebrowEl = document.getElementById("subModalEyebrow");
  const planSelect = document.getElementById("subPlanSelect");
  const billingSelect = document.getElementById("subBillingSelect");
  const messageEl = document.getElementById("subMessage");
  const successEl = document.getElementById("subSuccess");

  let lastFocus = null;

  const open = ({ card, addon } = {}) => {
    lastFocus = document.activeElement;
    successEl?.classList.remove("shown");

    if (card) {
      const plan = card.dataset.plan;
      // Pre-select the tier that was clicked; unknown names fall back gracefully.
      if (planSelect) {
        const known = [...planSelect.options].some((o) => o.value === plan);
        planSelect.value = known ? plan : "Not sure yet";
      }
      eyebrowEl.textContent = `${plan} · ${planPriceLabel(card)}`;
      titleEl.textContent = "Start your subscription";
    } else if (addon) {
      eyebrowEl.textContent = "Add-on request";
      titleEl.textContent = "Add this to your plan";
      // Seed the message so the request says exactly which add-on was clicked.
      if (messageEl) {
        const line = `I'd like to add: ${addon}.`;
        if (!messageEl.value.includes(line)) {
          messageEl.value = [messageEl.value.trim(), line].filter(Boolean).join("\n");
        }
      }
    }

    if (billingSelect) billingSelect.value = BILLING[currentBilling].label;

    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    lockScroll();
    requestAnimationFrame(() => closeBtn?.focus());
  };

  const close = () => {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    unlockScroll();
    if (lastFocus && typeof lastFocus.focus === "function") lastFocus.focus();
  };
  closeSubModal = close;

  // Tier CTAs — "Get Started", "Claim Popular Plan", "Launch Your Store".
  document.querySelectorAll("[data-plan-cta]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const card = btn.closest(".sub-card");
      if (card) setFloatingWhatsapp(planWaMessage(card));
      open({ card });
    });
  });

  // Add-on CTAs.
  document.querySelectorAll("[data-addon-cta]").forEach((btn) => {
    btn.addEventListener("click", () => open({ addon: btn.dataset.addonCta }));
  });

  closeBtn?.addEventListener("click", close);
  backdrop?.addEventListener("click", close);
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modal.classList.contains("is-open")) close();
  });
}

/** Price string stored against the lead, e.g. "₹649 / month". */
function subPlanPrice(plan, billing) {
  const card = [...document.querySelectorAll(".sub-card")].find(
    (c) => c.dataset.plan === plan
  );
  if (!card) return "";
  const annual = billing === "Annual";
  return `${formatINR(annual ? card.dataset.annual : card.dataset.monthly)} ${
    annual ? "/ year" : "/ month"
  }`;
}

/* --------------------------------------------------- Subscription form submit */
function initSubForm() {
  const form = document.getElementById("subForm");
  if (!form) return;
  const successEl = document.getElementById("subSuccess");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const submitBtn = form.querySelector(".form-submit");
    const fd = new FormData(form);
    const str = (k) => (fd.get(k) || "").toString().trim();

    const plan = str("plan");
    const billing = str("billing") || "Monthly";

    const data = {
      type: "subscription_inquiry",
      name: str("name"),
      email: str("email"),
      phone: str("phone"),
      company: str("company"),
      // Reuse the existing Lead columns: plan → project_type, price → budget.
      projectType: plan,
      budget: subPlanPrice(plan, billing),
      brief: [`Plan: ${plan}`, `Billing: ${billing}`, str("message")]
        .filter(Boolean)
        .join("\n"),
      website: str("website"), // honeypot — server drops the lead if filled
    };

    await sendLead(data, form, submitBtn, successEl);

    // sendLead only adds `.shown` on a real 2xx, so this won't fire when the
    // request failed over to the mailto: fallback.
    if (successEl?.classList.contains("shown")) {
      setTimeout(closeSubModal, 2600);
    }
  });
}

/* --------------------------------------------------- Context-aware WhatsApp float
   The floating button carries a generic greeting by default, a plans-specific
   message while #plans is on screen, and a tier-specific one once a visitor
   opens a tier's CTA. */
function setFloatingWhatsapp(text) {
  const float = document.getElementById("whatsappFloat");
  if (float) float.href = waLink(text);
}

function initWhatsappContext() {
  const float = document.getElementById("whatsappFloat");
  const section = document.getElementById("plans");
  if (!float || !section || !("IntersectionObserver" in window)) return;

  const defaultText = float.dataset.defaultText || "Hi Yash, I found your website.";
  const plansText = "Hi Yash, I'd like to know more about your website subscription plans.";

  new IntersectionObserver(
    ([entry]) => setFloatingWhatsapp(entry.isIntersecting ? plansText : defaultText),
    { rootMargin: "-30% 0px -30% 0px" }
  ).observe(section);
}

/* --------------------------------------------------- Subscription cards reveal */
function initSubsPop() {
  const cards = document.querySelectorAll(".sub-card");
  if (cards.length) {
    gsap.fromTo(
      cards,
      { opacity: 0, y: 70, scale: 0.92 },
      {
        opacity: 1, y: 0, scale: 1,
        duration: 1.1, ease: "back.out(1.5)",
        stagger: 0.12,
        scrollTrigger: { trigger: ".subs-grid", start: "top 80%" },
      }
    );
  }

  const addons = document.querySelectorAll(".addon-card");
  if (addons.length) {
    gsap.fromTo(
      addons,
      { opacity: 0, y: 40, scale: 0.94 },
      {
        opacity: 1, y: 0, scale: 1,
        duration: 0.85, ease: "back.out(1.6)",
        stagger: 0.08,
        scrollTrigger: { trigger: ".addons-grid", start: "top 88%" },
      }
    );
  }
}

/* --------------------------------------------------- Insights feed (homepage teaser) */
function initInsightsFeed() {
  const grid = document.getElementById("insightsGrid");
  if (!grid) return;

  const escape = (s) =>
    String(s || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");

  fetch("/api/blog/")
    .then((res) => {
      if (!res.ok) throw new Error(`API ${res.status}`);
      return res.json();
    })
    .then((data) => {
      const posts = (data.posts || []).slice(0, 3);
      if (!posts.length) {
        grid.innerHTML = `<p class="insights-loading">No posts yet — check back soon.</p>`;
        grid.dataset.state = "empty";
        return;
      }
      grid.innerHTML = posts
        .map(
          (p) => `
          <a class="insight-card" href="/blog/${encodeURIComponent(p.slug)}/">
            <p class="insight-tag">${escape(p.tag)}</p>
            <h3>${escape(p.title)}</h3>
            <p class="insight-meta">${p.read_minutes} min read · ${escape(p.tag.toLowerCase())} breakdown</p>
          </a>`
        )
        .join("");
      grid.dataset.state = "loaded";
    })
    .catch((err) => {
      // Backend offline — fall back to a polite static placeholder
      console.warn("Insights feed offline:", err);
      grid.innerHTML = `<p class="insights-loading">New posts will appear here once the blog backend is live.</p>`;
      grid.dataset.state = "error";
    });
}

/* --------------------------------------------------- Cookie banner */
function initCookieBanner() {
  const banner = document.getElementById("cookieBanner");
  const acceptBtn = document.getElementById("cookieAccept");
  const declineBtn = document.getElementById("cookieDecline");
  if (!banner) return;

  const KEY = "tyg_cookie_consent_v1";
  const existing = (() => {
    try { return localStorage.getItem(KEY); } catch { return null; }
  })();
  if (existing) return;

  // Delay banner appearance so it doesn't fight the hero animation
  setTimeout(() => {
    banner.classList.add("is-shown");
    banner.setAttribute("aria-hidden", "false");
  }, 1500);

  const hide = (choice) => {
    banner.classList.remove("is-shown");
    banner.setAttribute("aria-hidden", "true");
    try { localStorage.setItem(KEY, choice); } catch {}
    // Hook for analytics: if accepted, load GA4/Pixel here.
    if (choice === "accept" && typeof window.loadAnalytics === "function") {
      window.loadAnalytics();
    }
  };

  acceptBtn?.addEventListener("click", () => hide("accept"));
  declineBtn?.addEventListener("click", () => hide("decline"));
}

/* --------------------------------------------------- Magnetic buttons (Apple-style cursor pull) */
function initMagneticButtons() {
  const targets = document.querySelectorAll(".btn, .cta-pill, .side-cta, .plan-cta");
  const strength = 16; // px max offset

  targets.forEach((btn) => {
    btn.addEventListener("mousemove", (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - (rect.left + rect.width / 2);
      const y = e.clientY - (rect.top + rect.height / 2);
      const dx = (x / rect.width) * strength;
      const dy = (y / rect.height) * strength;
      btn.style.transform = `translate(${dx}px, ${dy}px)`;
    });
    btn.addEventListener("mouseleave", () => {
      btn.style.transform = "";
    });
  });
}

/* --------------------------------------------------- Tilt-on-hover cards */
function initTiltCards() {
  const tiltables = document.querySelectorAll(
    ".cap-card, .channel-card, .pillar-card, .insight-card, .testimonial, .about-card, .plan, .work-card, .pin-card, .sub-card, .addon-card"
  );

  tiltables.forEach((el) => {
    el.style.transformStyle = "preserve-3d";
    el.addEventListener("mousemove", (e) => {
      const rect = el.getBoundingClientRect();
      const px = (e.clientX - rect.left) / rect.width;
      const py = (e.clientY - rect.top) / rect.height;
      const rotateX = (0.5 - py) * 6;
      const rotateY = (px - 0.5) * 6;
      el.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
      // Cursor spotlight position (consumed by the ::after radial gradient)
      el.style.setProperty("--mx", `${px * 100}%`);
      el.style.setProperty("--my", `${py * 100}%`);
    });
    el.addEventListener("mouseleave", () => {
      el.style.transform = "";
    });
  });
}

/* --------------------------------------------------- Scroll reveals for new sections */
function initLogosPop() {
  const pills = document.querySelectorAll(".logo-pill");
  if (!pills.length) return;
  gsap.fromTo(
    pills,
    { opacity: 0, y: 20, scale: 0.9 },
    {
      opacity: 1, y: 0, scale: 1,
      duration: 0.6, ease: "back.out(1.6)",
      stagger: 0.04,
      scrollTrigger: { trigger: ".logos-row", start: "top 90%" }
    }
  );
}

function initAboutPop() {
  const photo = document.querySelector(".about-photo");
  const copy = document.querySelector(".about-copy");
  if (photo) {
    gsap.fromTo(
      photo,
      { opacity: 0, x: -40, scale: 0.92 },
      {
        opacity: 1, x: 0, scale: 1,
        duration: 1.1, ease: "back.out(1.4)",
        scrollTrigger: { trigger: ".about-inner", start: "top 75%" }
      }
    );
  }
  if (copy) {
    gsap.fromTo(
      copy.children,
      { opacity: 0, y: 30 },
      {
        opacity: 1, y: 0,
        duration: 0.7, ease: "power3.out",
        stagger: 0.08,
        scrollTrigger: { trigger: ".about-copy", start: "top 80%" }
      }
    );
  }
  const aboutCards = document.querySelectorAll(".about-card");
  if (aboutCards.length) {
    gsap.fromTo(
      aboutCards,
      { opacity: 0, y: 30, scale: 0.9 },
      {
        opacity: 1, y: 0, scale: 1,
        duration: 0.8, ease: "back.out(1.6)",
        stagger: 0.1,
        scrollTrigger: { trigger: ".about-cards", start: "top 85%" }
      }
    );
  }
}

function initTestimonialsPop() {
  const cards = document.querySelectorAll(".testimonial");
  if (!cards.length) return;
  gsap.fromTo(
    cards,
    { opacity: 0, y: 50, scale: 0.94 },
    {
      opacity: 1, y: 0, scale: 1,
      duration: 1, ease: "back.out(1.5)",
      stagger: 0.1,
      scrollTrigger: { trigger: ".testimonials-grid", start: "top 80%" }
    }
  );
}

function initFaqPop() {
  const items = document.querySelectorAll(".faq-item");
  if (!items.length) return;
  gsap.fromTo(
    items,
    { opacity: 0, y: 25 },
    {
      opacity: 1, y: 0,
      duration: 0.7, ease: "power3.out",
      stagger: 0.06,
      scrollTrigger: { trigger: ".faq-list", start: "top 80%" }
    }
  );
}

function initInsightsPop() {
  const cards = document.querySelectorAll(".insight-card");
  if (!cards.length) return;
  gsap.fromTo(
    cards,
    { opacity: 0, y: 40, scale: 0.94 },
    {
      opacity: 1, y: 0, scale: 1,
      duration: 0.9, ease: "back.out(1.5)",
      stagger: 0.1,
      scrollTrigger: { trigger: ".insights-grid", start: "top 85%" }
    }
  );
}

/* --------------------------------------------------- Lenis inertia smooth scroll */
function initLenis() {
  if (!window.Lenis || prefersReducedMotion) return null;
  const lenis = new Lenis({ lerp: 0.09, smoothWheel: true });
  const raf = (time) => {
    lenis.raf(time);
    requestAnimationFrame(raf);
  };
  requestAnimationFrame(raf);
  if (window.ScrollTrigger) lenis.on("scroll", ScrollTrigger.update);
  document.documentElement.classList.add("lenis-active");
  return lenis;
}

/* --------------------------------------------------- Scroll progress bar */
function initProgressBar() {
  const bar = document.getElementById("scrollProgress");
  if (!bar) return;
  const update = () => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.transform = `scaleX(${max > 0 ? Math.min(window.scrollY / max, 1) : 0})`;
  };
  window.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update, { passive: true });
  update();
}

/* --------------------------------------------------- Hero cinematic intro */
function initHeroIntro() {
  const title = document.querySelector(".hero-title");
  if (!title) return;

  // Split text nodes into word spans (.w > .wi) without losing .grad-text styling
  const splitWords = (el) => {
    [...el.childNodes].forEach((node) => {
      if (node.nodeType === Node.TEXT_NODE) {
        const frag = document.createDocumentFragment();
        node.textContent.split(/(\s+)/).forEach((tok) => {
          if (!tok) return;
          if (/^\s+$/.test(tok)) {
            frag.appendChild(document.createTextNode(" "));
            return;
          }
          const w = document.createElement("span");
          w.className = "w";
          const wi = document.createElement("span");
          wi.className = "wi";
          wi.textContent = tok;
          w.appendChild(wi);
          frag.appendChild(w);
        });
        el.replaceChild(frag, node);
      } else if (node.nodeType === Node.ELEMENT_NODE && node.tagName !== "BR") {
        splitWords(node);
      }
    });
  };
  splitWords(title);

  const tl = gsap.timeline({ delay: 0.1 });
  tl.to(".hero-title .wi", {
    y: 0,
    duration: 1.15,
    ease: "power4.out",
    stagger: 0.07,
  });
  tl.from(
    [".hero .eyebrow", ".hero-lead", ".hero-actions", ".hero-meta"],
    { opacity: 0, y: 26, duration: 0.9, ease: "power3.out", stagger: 0.1 },
    "-=0.75"
  );
  tl.from(
    ".hero-ring",
    { opacity: 0, scale: 0.85, duration: 1.6, ease: "power2.out" },
    "-=1.1"
  );
}

/* --------------------------------------------------- Scroll-aware nav highlight */
function initActiveNav() {
  document.querySelectorAll('.nav-links a[href^="#"]').forEach((link) => {
    const section = document.querySelector(link.getAttribute("href"));
    if (!section) return;
    ScrollTrigger.create({
      trigger: section,
      start: "top 40%",
      end: "bottom 40%",
      onToggle: (self) => link.classList.toggle("is-active", self.isActive),
    });
  });
}
