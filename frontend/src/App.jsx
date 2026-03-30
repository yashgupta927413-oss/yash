const services = [
  {
    title: 'SEO Growth Engine',
    description:
      'Technical SEO, topical content strategy, and authority building to rank your business where buyers are searching.',
    image:
      'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80',
  },
  {
    title: 'Google Ads & SEM',
    description:
      'Conversion-focused campaign architecture, high-intent keywords, ad copy testing, and budget optimization.',
    image:
      'https://images.unsplash.com/photo-1551281044-8b9a4c4b7139?auto=format&fit=crop&w=1200&q=80',
  },
  {
    title: 'Meta / Facebook Ads',
    description:
      'Creative-first paid social strategy for lead generation, remarketing, and scalable ROAS growth.',
    image:
      'https://images.unsplash.com/photo-1611926653458-09294b3142bf?auto=format&fit=crop&w=1200&q=80',
  },
];

const proof = [
  'Performance-driven dashboards and transparent reporting',
  'Full-funnel campaigns from traffic to conversion',
  'Tech + marketing execution in one place',
  'Fast communication and hands-on optimization',
];

export default function App() {
  return (
    <>
      <header className="hero">
        <nav className="nav container">
          <p className="brand">Yash Gupta</p>
          <a className="btn btn-outline" href="#contact">
            Start a Project
          </a>
        </nav>

        <div className="container hero-content">
          <p className="eyebrow">Digital Marketing Specialist</p>
          <h1>Professional Growth Marketing for Modern Businesses</h1>
          <p className="lead">
            I help founders and brands scale revenue using SEO, SEM, Google Ads, Meta Ads,
            and conversion-focused web execution.
          </p>
          <div className="hero-actions">
            <a className="btn btn-primary" href="#contact">
              Book Free Consultation
            </a>
            <a className="btn btn-outline" href="#services">
              View Services
            </a>
          </div>
        </div>
      </header>

      <main>
        <section id="services" className="section container">
          <h2>Digital Marketing Services</h2>
          <p className="section-text">
            High-quality strategy and execution built to increase qualified leads, lower acquisition cost, and improve ROI.
          </p>
          <div className="service-grid">
            {services.map((service) => (
              <article className="service-card" key={service.title}>
                <img src={service.image} alt={service.title} loading="lazy" />
                <div className="service-card-content">
                  <h3>{service.title}</h3>
                  <p>{service.description}</p>
                </div>
              </article>
            ))}
          </div>
        </section>

        <section className="section section-alt">
          <div className="container two-col">
            <div>
              <h2>Why Clients Choose Yash</h2>
              <p className="section-text">
                You get a strategic partner who understands both paid growth and technical implementation.
              </p>
              <ul className="proof-list">
                {proof.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </div>
            <div className="featured-image-wrap">
              <img
                className="featured-image"
                src="https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?auto=format&fit=crop&w=1200&q=80"
                alt="Digital marketing analytics dashboard"
              />
            </div>
          </div>
        </section>

        <section id="contact" className="section container contact">
          <h2>Let’s Build Your Growth Plan</h2>
          <p className="section-text">
            Tell me your goals, current marketing challenges, and budget range. I’ll propose a practical action plan.
          </p>
          <a className="btn btn-primary" href="mailto:hello@theyashgupta.com">
            hello@theyashgupta.com
          </a>
        </section>
      </main>

      <footer className="footer">
        <div className="container">
          <p>© {new Date().getFullYear()} Yash Gupta · Digital Marketing & IT Services</p>
        </div>
      </footer>
    </>
  );
}
