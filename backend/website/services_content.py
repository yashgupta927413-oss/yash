"""Content for the server-rendered service landing pages (/services/<slug>/).

Each page targets one commercial-intent keyword cluster so Google has a
dedicated, fully-rendered URL to rank per service. Edit copy here; no
template changes needed.
"""

SERVICES = {
    "web-development": {
        "nav_label": "Web Development",
        "title": "Web Development Services in India | Next.js & React Developer",
        "meta_description": (
            "Conversion-focused web development services — marketing sites, SaaS dashboards, "
            "and e-commerce built on Next.js and React. Sub-second loads, SEO-ready, from ₹19,999. "
            "Based in India, working globally."
        ),
        "eyebrow": "Service · Web Development",
        "h1": "Web Development Services",
        "intro": (
            "I design, engineer, and ship fast, conversion-first websites for startups and growing "
            "businesses — marketing sites, SaaS dashboards, and e-commerce storefronts. Every build "
            "targets sub-second loads, accessible HTML, and a measurable conversion path. No plugin "
            "soup, no agency overhead, no tech debt handed back to you."
        ),
        "sections": [
            {
                "h2": "What I build",
                "body": (
                    "<ul>"
                    "<li><strong>Marketing & landing sites</strong> — high-converting pages designed around a single metric, shipped in 2–3 weeks.</li>"
                    "<li><strong>SaaS dashboards & web apps</strong> — type-safe React/TypeScript builds with real-time data and clean auth.</li>"
                    "<li><strong>E-commerce storefronts</strong> — Shopify, Hydrogen, and headless builds optimized for AOV and ad-traffic conversion.</li>"
                    "<li><strong>Custom CMS & content systems</strong> — editor experiences your team actually likes (Sanity, Payload, Django).</li>"
                    "<li><strong>API integrations & automations</strong> — CRM hookups, payment flows, lead routing, WhatsApp automation.</li>"
                    "</ul>"
                ),
            },
            {
                "h2": "Why teams hire me instead of an agency",
                "body": (
                    "<p>One operator, full ownership. I write the code myself — no subcontracting, no offshore "
                    "handoffs, no account managers between you and the person building your site. You get "
                    "agency-grade output at freelancer economics, with a direct line to the engineer.</p>"
                    "<p>Every site ships with Lighthouse scores above 95, Core Web Vitals in the green, "
                    "structured data, and analytics wired in — because I also run <a href='/services/seo/'>SEO</a> "
                    "and <a href='/services/digital-marketing/'>paid campaigns</a>, I build sites that are ready "
                    "to rank and convert from day one.</p>"
                ),
            },
            {
                "h2": "Pricing",
                "body": (
                    "<ul>"
                    "<li><strong>Launchpad</strong> — complete marketing site, from ₹19,999. Up to 8 pages, custom design, CMS-ready, 2 weeks.</li>"
                    "<li><strong>E-commerce build</strong> — from ₹29,999 with catalog, payments, and conversion-focused layout.</li>"
                    "<li><strong>Growth retainer</strong> — ₹59,999/month for rolling engineering + marketing sprints.</li>"
                    "</ul>"
                    "<p>Fixed scope, milestone billing (50% kickoff / 50% launch), full IP transfer on final payment.</p>"
                ),
            },
        ],
        "faqs": [
            {
                "q": "How much does a website cost in India?",
                "a": "A professional marketing site starts at ₹19,999. E-commerce builds start at ₹29,999. Complex SaaS dashboards are scoped individually — most land between ₹1L and ₹5L. You get a fixed written quote before any work starts.",
            },
            {
                "q": "How long does a website take to build?",
                "a": "Marketing sites ship in 2–3 weeks. E-commerce and SaaS builds typically run 4–8 weeks depending on scope and content readiness.",
            },
            {
                "q": "Do you work with clients outside India?",
                "a": "Yes — I currently serve clients in the US, UK, UAE, and Singapore. Communication is async-first with weekly calls in your timezone.",
            },
            {
                "q": "Who owns the code after delivery?",
                "a": "You do. Full intellectual property, the GitHub repository, deploy credentials, and documentation transfer to you once the final invoice clears.",
            },
        ],
        "cta_heading": "Get a fixed quote for your build",
        "related_tag": "Performance",
    },
    "digital-marketing": {
        "nav_label": "Digital Marketing",
        "title": "Digital Marketing Services in India | Google Ads & Meta Ads Management",
        "meta_description": (
            "Performance marketing that pays for itself — Google Ads, Meta Ads, email, and WhatsApp "
            "campaigns with transparent reporting and conversion tracking. Pay-per-lead options "
            "available. Managed by the same engineer who builds your landing pages."
        ),
        "eyebrow": "Service · Digital Marketing",
        "h1": "Digital Marketing Services",
        "intro": (
            "Four channels, one operator, one dashboard. I architect Google Ads, Meta Ads, email, and "
            "WhatsApp campaigns end to end — audience research, creative testing, landing-page "
            "iteration, and conversion tracking that ties every rupee spent to a measurable outcome."
        ),
        "sections": [
            {
                "h2": "Channels I manage",
                "body": (
                    "<ul>"
                    "<li><strong>Google Ads</strong> — Search, Performance Max, and Shopping with conversion-API tracking and tight account structure.</li>"
                    "<li><strong>Meta Ads</strong> — Facebook and Instagram full-funnel campaigns: lead-gen forms, click-to-WhatsApp, retargeting pools.</li>"
                    "<li><strong>Email & lifecycle</strong> — welcome flows, cart recovery, win-back sequences in Klaviyo or Mailchimp.</li>"
                    "<li><strong>WhatsApp Business</strong> — the fastest-converting channel in India: broadcast offers, bot flows, CRM-routed follow-ups.</li>"
                    "</ul>"
                ),
            },
            {
                "h2": "Why ads + engineering in one place wins",
                "body": (
                    "<p>Most agencies run ads into landing pages they can't change. I build the page <em>and</em> run "
                    "the traffic — so when the data says the headline or the form is leaking conversions, it gets "
                    "fixed the same day, not after a three-week ticket cycle. See "
                    "<a href='/services/web-development/'>web development services</a> for what's under the hood.</p>"
                    "<p>Every engagement includes a shared live dashboard, weekly Loom walkthroughs, and honest "
                    "reporting — if a channel isn't working, you'll hear it from me first.</p>"
                ),
            },
            {
                "h2": "Pay-per-lead option",
                "body": (
                    "<p>For select industries and geographies I work on a pure performance model: "
                    "<strong>₹99–₹1,999 per qualified lead</strong>, with lead criteria agreed in writing before "
                    "launch, a shared real-time dashboard, and a replacement policy for leads that don't meet "
                    "the bar. You pay for outcomes, not activity.</p>"
                ),
            },
        ],
        "faqs": [
            {
                "q": "What budget do I need to start with Google or Meta Ads?",
                "a": "For most Indian service businesses, ₹30,000–₹50,000/month in ad spend is enough to gather meaningful data and produce leads. Below that, I'll usually recommend starting with one channel only.",
            },
            {
                "q": "How fast will I see leads?",
                "a": "Paid campaigns generate first leads within days of launch. Expect 2–4 weeks of optimization before cost-per-lead stabilizes at its real level.",
            },
            {
                "q": "Do you guarantee ROAS or lead volume?",
                "a": "No — and you should be skeptical of anyone who does. I commit to transparent reporting, weekly optimization, and honest kill-calls on what isn't working.",
            },
            {
                "q": "What is the pay-per-lead model?",
                "a": "Instead of a monthly fee, you pay a fixed price per qualified lead (₹99–₹1,999 depending on industry and qualification depth). Criteria are agreed before launch and invalid leads are replaced.",
            },
        ],
        "cta_heading": "Plan a campaign with me",
        "related_tag": "Paid Media",
    },
    "seo": {
        "nav_label": "SEO Services",
        "title": "SEO Services in India | Technical, Content & Programmatic SEO",
        "meta_description": (
            "SEO done as engineering — technical audits, content systems, and programmatic pages that "
            "compound organic traffic month over month. Core Web Vitals, schema, and crawl-clean "
            "foundations on every project. Free 12-point audit available."
        ),
        "eyebrow": "Service · SEO",
        "h1": "SEO Services",
        "intro": (
            "SEO done as engineering — not blog spam. I work across three pillars: a crawl-clean "
            "technical foundation, content mapped to buyer intent, and programmatic scale for sites "
            "that should rank for hundreds of long-tail queries. Real results: 0 to 12,000 organic "
            "visits/month in 4 months on a brand-new services domain."
        ),
        "sections": [
            {
                "h2": "The three pillars",
                "body": (
                    "<ul>"
                    "<li><strong>Technical SEO</strong> — Core Web Vitals tuning, crawl-budget hygiene, schema markup, JS rendering strategy, migration planning.</li>"
                    "<li><strong>Content & on-page</strong> — keyword research clustered by intent, pillar pages, internal-linking architecture, content refreshes.</li>"
                    "<li><strong>Programmatic SEO</strong> — data-driven page templates that rank for thousands of location/service/comparison queries, released in index-safe waves.</li>"
                    "</ul>"
                ),
            },
            {
                "h2": "Why technical foundations come first",
                "body": (
                    "<p>If Google can't crawl, render, or trust your site, content won't save it. Every engagement "
                    "starts with a full technical audit — and because I'm also a "
                    "<a href='/services/web-development/'>web developer</a>, fixes get implemented, not just "
                    "listed in a PDF you have to hand to someone else.</p>"
                    "<p>Sites I ship hold Lighthouse SEO scores of 95+ and green Core Web Vitals — ranking "
                    "signals most agencies treat as someone else's problem.</p>"
                ),
            },
            {
                "h2": "Free 12-point SEO audit",
                "body": (
                    "<p>Not sure where your site stands? I'll record a personal Loom walkthrough covering your "
                    "Core Web Vitals, indexation, on-page issues, and the top 3 wins you can ship this week. "
                    "No bots, no generic PDF, no obligation — <a href='/#audit'>request it here</a>.</p>"
                ),
            },
        ],
        "faqs": [
            {
                "q": "How long does SEO take to show results?",
                "a": "Technical fixes can lift rankings within 2–6 weeks. Content and authority building compound over 3–6 months. Anyone promising page-one rankings in days is selling something dangerous.",
            },
            {
                "q": "Do you guarantee #1 rankings on Google?",
                "a": "No — nobody can, and Google itself warns against anyone who claims to. I commit to engineering-grade execution, transparent rank tracking, and monthly strategy reviews.",
            },
            {
                "q": "What is programmatic SEO?",
                "a": "Generating hundreds or thousands of genuinely useful pages from structured data — e.g. every service × city combination — with real research behind each page, structural variation, and index throttling so Google trusts the rollout.",
            },
            {
                "q": "Do you do local SEO?",
                "a": "Yes — Google Business Profile optimization, local schema, citation building, and review strategy for businesses targeting city-level searches.",
            },
        ],
        "cta_heading": "Request your free SEO audit",
        "related_tag": "Programmatic SEO",
    },
}
