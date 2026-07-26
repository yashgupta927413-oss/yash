from datetime import timedelta

from django.db import migrations
from django.utils import timezone


POSTS = [
    {
        "slug": "website-cost-india-2026",
        "title": "How much does a website cost in India in 2026? Real numbers, no surprises",
        "subtitle": "From ₹5,000 templates to ₹15L builds — what you actually get at each price point.",
        "tag": "Buying Guide",
        "excerpt": "Quotes for the 'same' website range from ₹5,000 to ₹5,00,000. Here's what each price band actually buys, where the hidden costs hide, and how to scope yours.",
        "cover_emoji": "💰",
        "read_minutes": 7,
        "body": """
<p>Ask five vendors for a website quote in India and you'll get numbers spanning two orders of magnitude — ₹5,000 from a template reseller, ₹5,00,000 from a mid-size agency, for what sounds like the same deliverable. Neither is lying. They're selling different things. Here's the honest breakdown.</p>

<h2>The price bands and what they really buy</h2>

<h3>₹5,000–₹15,000 — template installs</h3>
<p>A WordPress or Wix theme with your logo and text swapped in. Fine for a digital visiting card. The hidden costs arrive later: plugin licenses, slow load times that hurt ads and rankings, and a rebuild within 18 months when you outgrow it. If your website needs to <em>produce customers</em>, this band usually costs more than it saves.</p>

<h3>₹20,000–₹60,000 — custom professional sites</h3>
<p>This is the sweet spot for most startups and service businesses: custom design, conversion-focused copy structure, mobile-first build, basic SEO foundations, and analytics wired in. My own <a href="/services/web-development/">Launchpad builds start at ₹19,999</a> in this band — up to 8 pages on a modern stack (Next.js), Core Web Vitals in the green, shipped in 2–3 weeks.</p>

<h3>₹60,000–₹2,00,000 — e-commerce and content systems</h3>
<p>Product catalogs, payment integration, CMS workflows for a content team, multi-language. The cost driver isn't pages — it's <strong>states</strong>: carts, accounts, orders, refunds, inventory sync. Scope these by user flows, not page count.</p>

<h3>₹2,00,000+ — SaaS dashboards and platforms</h3>
<p>Authenticated apps, real-time data, role-based access, third-party API orchestration. Here you're paying for engineering, not design. Anyone quoting this band without a written technical spec is guessing — and you'll pay for the guess later.</p>

<h2>The five hidden costs nobody quotes</h2>
<ul>
<li><strong>Hosting & domain</strong> — ₹0–₹500/month for most sites if architected sensibly (static-first, CDN-served). Agencies often resell ₹2,000/month hosting on ₹200 infrastructure.</li>
<li><strong>Maintenance</strong> — security patches, dependency updates, backups. Ask: is the first year included?</li>
<li><strong>Content</strong> — copywriting and photography are rarely in the quote. Budget for them or the project stalls at 90%.</li>
<li><strong>Revisions</strong> — get the included revision rounds in writing before kickoff.</li>
<li><strong>Ownership</strong> — confirm full IP and repository transfer on final payment. If the vendor keeps the code, you're renting, not buying.</li>
</ul>

<h2>How to compare quotes properly</h2>
<p>Don't compare prices — compare <strong>what moves your metric</strong>. A ₹20,000 site that loads in under a second and converts 3% of visitors beats a ₹80,000 site that loads in four seconds and converts 1%. Ask every vendor: what Lighthouse score do you guarantee? What's the conversion path? Who owns the code? The answers separate engineers from resellers in about thirty seconds.</p>

<p>Want a fixed, written quote for your project? <a href="/#contact">Send me the brief</a> — I respond within 24 hours with scope, timeline, and a number that won't change mid-project.</p>
""",
    },
    {
        "slug": "freelancer-vs-agency-vs-inhouse",
        "title": "Freelancer vs agency vs in-house: who should build your website?",
        "subtitle": "The honest decision matrix — including when NOT to hire someone like me.",
        "tag": "Buying Guide",
        "excerpt": "Each option wins in a specific situation and burns money in the others. A decision matrix from someone who has been the freelancer, worked with the agencies, and built for in-house teams.",
        "cover_emoji": "⚖️",
        "read_minutes": 6,
        "body": """
<p>I'm a freelance operator, so discount this accordingly — but I'll argue against my own interest where it's true, including the cases where you shouldn't hire someone like me.</p>

<h2>Hire an agency when…</h2>
<ul>
<li><strong>You need volume and parallel workstreams</strong> — a 60-page multilingual site, brand identity, video, and a launch campaign all due in eight weeks. One person physically cannot parallelize that.</li>
<li><strong>You need continuity insurance</strong> — if one person quits, the project survives. With a freelancer, the bus factor is one.</li>
<li><strong>Procurement requires it</strong> — enterprise compliance, contracts, SLAs, indemnity. Agencies have the paperwork muscle.</li>
</ul>
<p>The cost: 2–4× the price for the same output, account managers between you and the people doing the work, and ticket-cycle latency on every change. You're paying for coordination overhead — sometimes that's exactly what you need.</p>

<h2>Hire in-house when…</h2>
<ul>
<li><strong>The website IS the product</strong> — SaaS, marketplaces, anything with daily iteration. You need someone who lives in the codebase.</li>
<li><strong>You ship weekly experiments</strong> — at high iteration speed, external loops become the bottleneck.</li>
</ul>
<p>The math: a good full-stack developer in India costs ₹8–25L/year plus management time. That's justified at product-company iteration speed, and wildly unjustified for a marketing site that changes quarterly.</p>

<h2>Hire a freelance operator when…</h2>
<ul>
<li><strong>Scope is well-defined</strong> — a marketing site, a storefront, a growth retainer with clear metrics.</li>
<li><strong>Speed matters more than headcount</strong> — no coordination tax means a 2–3 week ship for what agencies quote 8 weeks on.</li>
<li><strong>You want the engineer in the room</strong> — questions get answered by the person writing the code, not relayed through an account manager.</li>
</ul>
<p>The honest risks: bus factor of one (mitigate with full IP and repo transfer — <a href="/services/web-development/">how I handle it</a>), and capacity ceilings (a good freelancer will tell you when your project needs a team instead — I've referred projects out for exactly this reason).</p>

<h2>The decision in one line</h2>
<p><strong>Parallel workstreams → agency. Daily product iteration → in-house. Defined scope + speed + budget efficiency → freelance operator.</strong></p>

<p>Not sure which bucket your project falls in? <a href="/#contact">Describe it to me</a> — if it's not a fit for one operator, I'll say so and point you at the right setup. A wrong-fit project costs me more in reputation than the invoice is worth.</p>
""",
    },
    {
        "slug": "slow-website-costing-you-sales",
        "title": "Your website loads in 4 seconds. Here's what that costs you in actual sales",
        "subtitle": "The compounding math of slow pages — ads, rankings, and conversions all bleed together.",
        "tag": "Performance",
        "excerpt": "Speed isn't a vanity metric — it taxes every rupee you spend on ads, every ranking you earn, and every visitor who lands. The math, with real client numbers.",
        "cover_emoji": "🐌",
        "read_minutes": 6,
        "body": """
<p>"The site feels fine on my phone" is the most expensive sentence in small-business marketing. Your phone has the site cached, sits on fast WiFi, and runs flagship hardware. Your customer is on a mid-range Android, on patchy 4G, seeing your site cold. For them, your 'fine' site takes 4+ seconds — and they behave accordingly.</p>

<h2>The three taxes a slow site charges</h2>

<h3>Tax 1: Your ads cost more</h3>
<p>Google Ads factors landing-page experience into Quality Score, and Quality Score directly prices your clicks. Worse: users who click an ad and wait four seconds bounce before the pixel even fires — you paid for a visitor your analytics never saw. On audits I run, slow landing pages routinely waste <strong>15–30% of ad spend</strong> before the page even renders.</p>

<h3>Tax 2: Your rankings cap out</h3>
<p>Core Web Vitals are a confirmed ranking signal. In competitive SERPs, a red LCP score is the tiebreaker that keeps you on page two. The traffic you never get doesn't show up in any report — which is why this tax goes unnoticed for years.</p>

<h3>Tax 3: Your conversion rate halves</h3>
<p>Google/Deloitte's research puts it bluntly: as load time goes from 1s to 3s, bounce probability rises 32%; at 5s it's 90%. On a client rebuild last year, cutting LCP from 3.2s to 0.7s took mobile conversion from 0.8% to 2.1% — <a href="/blog/cutting-lcp-from-3-to-0-7s-on-nextjs/">same design, same traffic, 2.6× the customers</a>.</p>

<h2>Run the math on your own numbers</h2>
<p>Monthly visitors × conversion rate × average order value = revenue. Now model conversion at 1.5–2× (what a sub-second site typically recovers) and look at the annual delta. For a business doing ₹2L/month online, the gap is usually ₹1–3L/year — quietly, every year.</p>

<h2>Find out where you stand in 30 seconds</h2>
<ol>
<li>Open <strong>PageSpeed Insights</strong> (free) and test your homepage on mobile.</li>
<li>Look at LCP under "field data" — that's real users, not lab conditions.</li>
<li>Under 2.5s: you're fine. Over 4s: you're paying all three taxes right now.</li>
</ol>

<p>If you're in the red zone, the fixes are usually boring and fast — image formats, render-blocking scripts, font loading, caching headers. I cover the exact checklist in <a href="/blog/core-web-vitals-checklist-2026/">the 2026 Core Web Vitals guide</a>, or if you'd rather have it done than read about it, <a href="/services/seo/">request the free 12-point audit</a> and I'll record a Loom walking through your site's specific bottlenecks.</p>
""",
    },
]


def seed(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    now = timezone.now()
    for i, post in enumerate(POSTS):
        BlogPost.objects.update_or_create(
            slug=post["slug"],
            defaults={**post, "is_published": True, "published_at": now - timedelta(days=i * 3)},
        )


def unseed(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    BlogPost.objects.filter(slug__in=[p["slug"] for p in POSTS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0007_seed_blog_posts"),
    ]

    operations = [
        migrations.RunPython(seed, reverse_code=unseed),
    ]
