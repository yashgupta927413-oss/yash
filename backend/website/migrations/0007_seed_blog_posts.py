from django.db import migrations
from django.utils import timezone
from datetime import timedelta


SEED_POSTS = [
    {
        "slug": "cutting-lcp-from-3-to-0-7s-on-nextjs",
        "title": "Cutting LCP from 3.2s to 0.7s on a Next.js marketing site",
        "subtitle": "The audit and the 8 changes that moved the needle.",
        "tag": "Performance",
        "excerpt": "Real numbers from a real rebuild — what the Lighthouse panel hid, the four bottlenecks we found, and why most marketing sites are 60% slower than they need to be.",
        "cover_emoji": "⚡",
        "read_minutes": 8,
        "body": """
<p>A B2B SaaS client came to us with a marketing site that "felt fine" — Lighthouse mobile score in the low 70s, no obvious complaints from users. The catch: paid traffic was converting <strong>2.3% on desktop and 0.8% on mobile</strong>. The desktop number was OK; the mobile number was lighting money on fire.</p>

<p>The first instinct in this situation is to redesign the page. Don't. Before touching the design, audit how the page <em>delivers</em>. Here's what we found, and what fixed it.</p>

<h2>The audit: where the seconds were going</h2>

<p>We ran a synthetic test on a throttled 4G connection (the closest analogue to a real Indian / SE-Asia mobile visitor) and got these numbers from WebPageTest:</p>

<ul>
  <li><strong>LCP:</strong> 3.2s (poor — Google's threshold is 2.5s)</li>
  <li><strong>INP:</strong> 410ms (poor — threshold is 200ms)</li>
  <li><strong>CLS:</strong> 0.21 (poor — threshold is 0.1)</li>
  <li><strong>Total blocking time:</strong> 1.8s</li>
</ul>

<p>The page <em>looked</em> done in about 1.5 seconds. But the LCP element — the hero image — wasn't visible until 3.2s because the browser was busy parsing 480KB of JavaScript before it could even fetch it. The interactive controls were locked for another 410ms after that, because a third-party chat widget kept blocking the main thread.</p>

<h2>The 8 changes that fixed it</h2>

<h3>1. Preload the LCP image, prefer AVIF</h3>
<p>The single largest win. We added a <code>&lt;link rel="preload" as="image" href="/hero.avif"&gt;</code> in <code>&lt;head&gt;</code>, and re-encoded the hero from a 320KB JPEG to a 48KB AVIF. LCP dropped by 1.1 seconds immediately.</p>

<h3>2. Self-host the font, drop <code>font-display: swap</code> for <code>optional</code></h3>
<p>Google Fonts was injecting two render-blocking stylesheets plus a CSP-blocked WOFF2. We downloaded the WOFF2 directly, served it from <code>/public/fonts/</code>, and used <code>font-display: optional</code> — which tells the browser "if the font isn't already cached, just use the system fallback." On a return visit, the real font appears. On the first visit, the user sees text instantly.</p>

<h3>3. Move the chat widget to <code>requestIdleCallback</code></h3>
<p>The chat script was loading synchronously and blocked the main thread for 410ms. Wrapping it in <code>requestIdleCallback(() =&gt; loadChat())</code> kept the button visible (rendered as plain HTML) but delayed the heavy JS until the browser had nothing better to do.</p>

<h3>4. Lazy-mount below-the-fold sections</h3>
<p>Next.js bundles every React component on the route — even the testimonials carousel sitting 4000px below the hero. We swapped to <code>next/dynamic</code> imports with <code>{ ssr: false }</code> on the components users wouldn't see for 6+ seconds. The initial JS payload dropped from 480KB to 220KB.</p>

<h3>5. Reserve space for everything</h3>
<p>CLS of 0.21 was almost entirely caused by the testimonials section, which loaded fonts late and shifted the page by 60px on font swap. Setting explicit <code>min-height</code> on every async section took CLS to 0.02.</p>

<h3>6. Cache static assets at the edge</h3>
<p>The host was returning <code>Cache-Control: no-cache</code> on the bundled JS. Configuring <code>immutable</code> caching on Vercel's edge meant repeat visitors loaded zero JS over the network.</p>

<h3>7. Inline critical CSS, defer the rest</h3>
<p>Next.js does this by default for App Router routes but the client was on the Pages Router. We extracted the above-the-fold styles (~3KB) into a <code>&lt;style&gt;</code> tag in <code>&lt;Head&gt;</code> and deferred the rest with <code>media="print"</code> trick.</p>

<h3>8. Drop the heaviest third-party script</h3>
<p>An analytics-stacked pixel was adding 110KB and 800ms of script evaluation. The client agreed to consolidate to GA4 + a single conversion API call.</p>

<h2>The final numbers</h2>

<ul>
  <li><strong>LCP:</strong> 0.7s (from 3.2s)</li>
  <li><strong>INP:</strong> 90ms (from 410ms)</li>
  <li><strong>CLS:</strong> 0.02 (from 0.21)</li>
  <li><strong>Mobile conversion:</strong> 2.1% (from 0.8%)</li>
</ul>

<p>The kicker: we changed zero design elements. Same hero, same copy, same testimonials. Just delivered them honestly. <strong>2.6× the mobile conversion rate</strong> with zero ad-budget increase.</p>

<h2>The lesson</h2>

<p>Most marketing sites today aren't slow because the design is heavy. They're slow because the build pipeline ships everything everywhere, regardless of whether the user has scrolled to it yet. Audit, measure, then ship only what's actually visible. Performance is a designable surface — start treating it like one.</p>
""",
    },
    {
        "slug": "programmatic-seo-playbook-zero-to-12k",
        "title": "The 4-month playbook that took a services site from 0 to 12k organic / mo",
        "subtitle": "Programmatic SEO for local services, step by step.",
        "tag": "Programmatic SEO",
        "excerpt": "How we built 1,800 indexed pages, ranked 60% of them, and turned a brand-new domain into a steady lead engine in 16 weeks.",
        "cover_emoji": "📈",
        "read_minutes": 12,
        "body": """
<p>The brief was straightforward: a local services business (think dental, real estate, home services — I'll keep the name out of it) wanted to stop relying on Google Ads. They had a single homepage, a contact form, and a phone number. Domain age: 11 days.</p>

<p>Four months later, they were getting ~12,000 organic visits per month and 400+ qualified phone inquiries — without spending another rupee on ads. Here's the playbook, step by step.</p>

<h2>1. Map the search intent in your category</h2>

<p>Most "programmatic SEO" advice tells you to combine two lists (e.g. <em>{city}</em> × <em>{service}</em>) and call it a day. That generates a lot of pages, but Google has gotten very good at recognizing those pages as templated thin content. So we started somewhere different: <strong>what does someone in this category actually type into Google?</strong></p>

<p>We pulled six months of Google Search Console data from three competitors using the Ahrefs Content Gap report. The patterns we found:</p>
<ul>
  <li><strong>Local + service + price intent:</strong> "root canal cost mumbai", "dental implant price near me" (high commercial value)</li>
  <li><strong>Local + service + question intent:</strong> "is teeth whitening safe", "how long does invisalign take" (top-funnel education)</li>
  <li><strong>Local + service + provider intent:</strong> "best dentist in andheri east", "dentist near {neighborhood}" (bottom-funnel, high-intent)</li>
  <li><strong>Comparison:</strong> "{brand x} vs {brand y}"</li>
</ul>

<p>Result: four distinct page templates, each engineered to answer one buyer-intent type — not one giant matrix of duplicates.</p>

<h2>2. Build the data layer first</h2>

<p>We modelled the content in a Postgres table — one row per page — with fields like <code>service_slug</code>, <code>area_slug</code>, <code>price_range</code>, <code>duration</code>, <code>top_3_questions</code>, <code>local_signals</code> (nearby landmarks, transit stations).</p>

<p>Crucial: the data was researched, not generated. We hired one freelancer for two weeks to interview the client's existing patients and document real prices, real questions, real procedures. That gave us ~80 service rows × ~22 neighbourhood rows = 1,760 page combinations, each with <em>actual</em> data behind it.</p>

<h2>3. Templates that aren't templated</h2>

<p>Each page used a Next.js dynamic route — <code>/[service]/[area]/page.tsx</code> — that pulled from Postgres at build time. But here's the part most people skip: <strong>we generated structural variation</strong>.</p>

<ul>
  <li>Page intro: 3 different opening paragraph styles, chosen by a hash of the slug. Google sees variety, not duplicates.</li>
  <li>FAQ order: shuffled per page based on local search volume.</li>
  <li>Internal links: top 5 most-similar pages, calculated by service category + geographic proximity.</li>
  <li>Schema markup: <code>LocalBusiness</code> + <code>FAQPage</code> + <code>Service</code>, generated from the same data.</li>
</ul>

<h2>4. Index throttling — release in waves</h2>

<p>This is the step nobody talks about. Dumping 1,800 pages into Google's index in one day is the fastest way to trigger a quality review. We released in waves:</p>

<ol>
  <li><strong>Week 1:</strong> 50 highest-priority pages (top-volume keywords in the highest-margin services).</li>
  <li><strong>Week 2:</strong> +200 pages, gated behind sitemap re-submission.</li>
  <li><strong>Week 4:</strong> +500 pages once Search Console showed the first wave indexing.</li>
  <li><strong>Week 6:</strong> Remaining 1,050 pages.</li>
</ol>

<p>This gave Google time to crawl, render, and trust each batch before more arrived. By week 8, ~80% of pages were indexed. By week 16, ~60% were ranking in the top 30.</p>

<h2>5. The "first cohort to convert" trick</h2>

<p>Don't write 1,800 pages and hope. Pick the 20 most likely to convert in your highest-margin service, ship them, get traffic, measure conversion. <em>Then</em> scale.</p>

<p>For us, this was the 20 highest-volume "{service} cost {area}" pages. Those went live in week 1 with custom lead forms. Within 30 days, conversion rate was 4.1% — high enough to justify scaling the model to the full inventory.</p>

<h2>6. Add a content engine, not just a build pipeline</h2>

<p>After launch, we built a CMS layer so the client's team could update prices, add new services, and write neighborhood-specific announcements without touching code. Each update auto-redeployed the affected pages via ISR (incremental static regeneration) on Vercel.</p>

<h2>What it cost</h2>

<ul>
  <li>One full-time freelancer for 2 weeks (data collection): ~₹40k</li>
  <li>Engineering (us, 16 weeks part-time): ~₹2.5L</li>
  <li>Hosting (Vercel Pro + Postgres): ₹3k/mo</li>
</ul>

<p>By month 4, the site was generating an estimated ₹6L+ in revenue per month from organic alone, replacing roughly ₹1.8L/month of Google Ads spend.</p>

<h2>What I'd do differently</h2>

<p>Two things. First: start with even fewer pages — 200 instead of 1,800 — and measure rank velocity before scaling. Second: invest more in editorial review on the first cohort. The first 50 pages set the trust tone for everything Google indexes after.</p>

<p>Programmatic SEO works. But "programmatic" doesn't mean "lazy." The brands winning at it are doing real research, real differentiation, and treating it as a content product — not a script.</p>
""",
    },
    {
        "slug": "meta-ads-leaking-spend-pixel-fix",
        "title": "Why your Meta Ads are leaking 30%+ of spend (and the fix is in your pixel)",
        "subtitle": "iOS 14.5, server-side events, and the modern attribution stack.",
        "tag": "Paid Media",
        "excerpt": "If your Meta Ads dashboard is still showing the same CPL it did in 2022, the platform isn't lying — it just can't see most of your conversions anymore. Here's how to fix attribution properly.",
        "cover_emoji": "🎯",
        "read_minutes": 6,
        "body": """
<p>Quick question: when's the last time you compared Meta's reported conversions to what actually showed up in your CRM?</p>

<p>If you haven't done it in the past 6 months, do this exercise. Most accounts I audit are missing somewhere between 28% and 41% of conversions in Meta's reporting. That's not a Meta bug. That's iOS 14.5, ad-blockers, and 18 months of Apple's privacy push doing exactly what they were designed to do.</p>

<p>If the platform can't see those conversions, three things break:</p>
<ol>
  <li>The bid algorithm optimizes against incomplete data.</li>
  <li>Lookalike audiences shrink (fewer seed conversions).</li>
  <li>Your reported ROAS looks worse than reality, so you scale back when you should be scaling up.</li>
</ol>

<h2>The diagnosis: are you actually losing data?</h2>

<p>Open Events Manager → your pixel → Diagnostics tab. Look for:</p>

<ul>
  <li><strong>Match rate</strong> below 65% — your pixel is failing to attribute events to real users.</li>
  <li><strong>Event Match Quality</strong> below "Good" on Purchase or Lead — Meta isn't getting enough first-party data.</li>
  <li><strong>"Browser only" events</strong> — these are the ones being killed by iOS / ad-blockers. The fix is server-side.</li>
</ul>

<h2>The fix: Conversions API (CAPI), done right</h2>

<p>CAPI sends events from <em>your server</em> to Meta, bypassing the browser entirely. iOS can't block it, ad-blockers can't see it, and the data is richer because you control what you send.</p>

<p>Most implementations are wrong in one of three ways:</p>

<h3>Mistake 1: Only sending the conversion, not the path</h3>
<p>If you only fire CAPI on the final purchase, Meta has no view of PageView, ViewContent, InitiateCheckout. The algorithm needs the full funnel signal. Fire all 6 standard events server-side.</p>

<h3>Mistake 2: Forgetting <code>event_id</code> deduplication</h3>
<p>If both your browser pixel <em>and</em> your CAPI server send a Purchase event without a shared <code>event_id</code>, Meta counts it twice. Always generate a UUID per conversion and pass it to both layers.</p>

<h3>Mistake 3: Skipping the user-data hash</h3>
<p>CAPI's power comes from sending hashed user info (email, phone, FBP cookie, IP, user agent). Skip these and your match rate collapses. Send everything you can — Meta hashes it client-side before storing.</p>

<h2>The "set it up in an afternoon" stack</h2>

<p>For 90% of e-commerce / lead-gen sites:</p>

<ul>
  <li><strong>Browser layer:</strong> Standard Meta Pixel with <code>event_id</code>.</li>
  <li><strong>Server layer:</strong> Either Shopify's native CAPI app, Stape's Server GTM container, or a Next.js API route that fires events on your backend webhooks.</li>
  <li><strong>Identity:</strong> Always pass <code>em</code> (hashed email), <code>ph</code> (hashed phone), <code>fbp</code> (cookie), <code>client_user_agent</code>, <code>client_ip_address</code>.</li>
  <li><strong>Deduplication:</strong> Same <code>event_id</code> on browser + server within 24 hours.</li>
</ul>

<h2>What changed for the brands I audited</h2>

<p>After proper CAPI + deduplication on three accounts I worked on in 2025:</p>
<ul>
  <li>Reported CPL dropped 28–34% (because Meta finally saw conversions it was already producing).</li>
  <li>Lookalike audiences re-expanded by 2.5–4× their previous size.</li>
  <li>Bid algorithm started picking better audiences within ~10 days.</li>
  <li>Cumulative spend efficiency improved by ~38% over the following quarter.</li>
</ul>

<p>The ad creative didn't change. The targeting didn't change. The budget didn't change. The platform just started seeing what it was already doing.</p>

<h2>One more thing</h2>

<p>If you're running both Google and Meta and only have CAPI for Meta, do enhanced conversions on Google next. Same principle, different stack. The platforms that win in 2026 are the ones with the best first-party data infrastructure, not the best creative.</p>
""",
    },
    {
        "slug": "core-web-vitals-checklist-2026",
        "title": "The 2026 Core Web Vitals checklist that actually moves the needle",
        "subtitle": "INP replaced FID. Here's the new ranked priority order.",
        "tag": "Performance",
        "excerpt": "Most performance guides are still written for FID. Here's what to optimize now that INP is the metric — ranked by which fixes Google rewards the hardest in 2026.",
        "cover_emoji": "📊",
        "read_minutes": 7,
        "body": """
<p>Google quietly replaced FID with INP (Interaction to Next Paint) as a Core Web Vital in March 2024. Most articles online still describe the old metric. Here's the 2026 checklist, ranked by impact-per-hour-of-work.</p>

<h2>What changed: INP vs FID</h2>

<p>FID measured the delay between a user's <em>first</em> interaction and the browser's ability to start handling it. INP measures the worst case across <em>all</em> interactions during the page visit. In practice: if any button click feels janky, INP catches it. FID didn't.</p>

<p>This matters for ranking. INP is in the top three signals Google uses for page experience. A poor INP score (above 500ms) can drop a page's ranking position by 1–3 spots in competitive SERPs.</p>

<h2>The 2026 priority order</h2>

<h3>1. Audit long tasks first (45 min, biggest win)</h3>
<p>Open DevTools → Performance → record a normal user flow. Anything over 50ms on the main thread is a long task. Common culprits:</p>
<ul>
  <li>Third-party tags loading synchronously (chat widgets, analytics, AB testing).</li>
  <li>Hydration of large client components on Next.js / React.</li>
  <li>Heavy synchronous JavaScript in scroll/click handlers.</li>
</ul>
<p>Move them to <code>requestIdleCallback</code> or break them up with <code>setTimeout</code> chunks.</p>

<h3>2. Use the right rendering strategy (1–2 days)</h3>
<p>If your route is mostly static, ship it static. Most marketing pages don't need to be SPAs. Static generation + selective client islands gets you INP under 100ms by default. Next.js App Router server components are tailor-made for this.</p>

<h3>3. Defer non-critical CSS (15 min)</h3>
<p>Above-the-fold CSS inlined into <code>&lt;head&gt;</code>. Everything else loaded with <code>media="print"</code> then swapped to <code>media="all"</code> on load. This frees up render thread for interactivity.</p>

<h3>4. Self-host fonts, use <code>font-display: optional</code></h3>
<p>Reduces both LCP and INP. Optional avoids the layout shift that swap causes, and removes a network roundtrip blocking interactivity.</p>

<h3>5. Image strategy: AVIF + sizes + lazy below the fold</h3>
<p>Hero images: AVIF, preloaded, with explicit <code>width</code>/<code>height</code> attributes. Everything below: lazy-load with <code>loading="lazy"</code>. Set <code>fetchpriority="high"</code> on the LCP element.</p>

<h3>6. Reserve space for everything async (30 min)</h3>
<p>CLS killer. Any element that loads after first paint needs a fixed dimension. Iframes need <code>height</code>. Images need <code>aspect-ratio</code>. Carousels need a defined container.</p>

<h3>7. Service worker for repeat visitors</h3>
<p>If your site has significant returning traffic, a service worker that caches the shell can take repeat-visit LCP to under 200ms. Workbox handles this in ~30 lines of config.</p>

<h2>What I'd skip</h2>

<ul>
  <li>Obsessing over TTFB if you're already under 800ms on a CDN.</li>
  <li>Micro-optimizing bundle size if your route is already under 200KB JS.</li>
  <li>Anything related to FID — that metric no longer affects ranking.</li>
</ul>

<h2>How to verify it worked</h2>

<p>Wait two weeks after deploying changes. Google's CrUX dataset uses real user data and updates on a 28-day rolling window. Your synthetic Lighthouse scores can be perfect while CrUX still shows red — and CrUX is what affects rankings.</p>

<p>Performance is a competitive advantage that compounds. Most of your competition isn't doing this work. Be the one who is.</p>
""",
    },
    {
        "slug": "google-ads-account-structure-2026",
        "title": "The Google Ads account structure I run for clients in 2026",
        "subtitle": "Performance Max, Smart Bidding, and what to keep manual.",
        "tag": "Paid Media",
        "excerpt": "Google's automation is finally good enough to trust — but only if you set it up with the right signals. Here's the exact structure I deploy for new accounts.",
        "cover_emoji": "🔧",
        "read_minutes": 9,
        "body": """
<p>The biggest mindset shift in Google Ads over the past two years: <strong>your job stopped being to pick keywords and write headlines, and started being to feed the algorithm clean signals.</strong> Get the inputs right and Smart Bidding outperforms manual every time. Get them wrong and Performance Max is the fastest way to set your budget on fire.</p>

<p>Here's the account structure I deploy when I take over a new account in 2026.</p>

<h2>The 4-campaign baseline</h2>

<h3>1. Brand search (manual CPC)</h3>
<p>One campaign, one ad group, exact + phrase match of your brand name. Manual CPC at a low ceiling (₹15-30 in India). Why manual: smart bidding will overspend here because brand traffic converts by default. Cap it.</p>

<h3>2. Non-brand search (Maximize conversions, target CPA)</h3>
<p>This is where 60% of your budget goes. Organized by intent cluster, not by keyword. Typical ad groups:</p>
<ul>
  <li><em>Buyer-intent commercial:</em> "{service} cost", "{service} near me", "best {service}"</li>
  <li><em>Problem-aware educational:</em> "how to fix {problem}", "why does {symptom} happen"</li>
  <li><em>Comparison:</em> "{competitor} vs", "alternatives to {competitor}"</li>
</ul>
<p>One responsive search ad per ad group. Pin headline 1 to your brand promise. Let Google rotate the rest. Bidding strategy: Maximize conversions with target CPA once you have ~30 conversions in a 30-day window.</p>

<h3>3. Performance Max (one campaign, audience signals + asset groups by buyer)</h3>
<p>PMax is no longer optional in 2026 — it's where the algorithm finds incremental volume your search campaigns miss. But it only works with structured signals:</p>
<ul>
  <li><strong>Audience signals:</strong> Upload your customer email list (CRM customer match), recent purchasers, and 1% lookalikes. PMax uses these as starting points.</li>
  <li><strong>Asset groups:</strong> One per buyer segment. Different headlines, descriptions, and images per segment.</li>
  <li><strong>Account-level negative list:</strong> Brand terms, irrelevant queries. Otherwise PMax will cannibalize search.</li>
  <li><strong>Conversion goal weighting:</strong> Tell Google a Purchase is worth 10× a Lead. Otherwise it optimizes for whatever's easier.</li>
</ul>

<h3>4. Retargeting (manual CPM display)</h3>
<p>Standard display campaign, cap at 1-2 impressions per user per day, audiences segmented by funnel stage. Critical: exclude converted users at the account level so you don't waste impressions.</p>

<h2>The non-negotiable conversion stack</h2>

<p>If your conversion tracking is wrong, none of this works. The 2026 stack:</p>
<ul>
  <li><strong>Server-side GTM</strong> (Stape or self-hosted). Browser-only pixels are losing 25-30% of conversions to ad-blockers and privacy modes.</li>
  <li><strong>Enhanced conversions</strong> turned on. Send hashed email at minimum; phone if you have it.</li>
  <li><strong>Offline conversion imports</strong> for any lead-gen account. If a lead becomes a customer, upload the conversion value back to Google within 30 days. This is how Smart Bidding learns to find higher-value leads, not just cheaper leads.</li>
  <li><strong>Single Purchase / Lead event</strong> as the only "primary" conversion. Everything else is "secondary." Don't let secondary conversions bid against primary.</li>
</ul>

<h2>What I monitor weekly (and what I ignore)</h2>

<p><strong>Watch:</strong> Search terms report, conversion volume by campaign, cost-per-conversion by ad group, asset performance ratings, search lost (rank), search lost (budget).</p>

<p><strong>Ignore:</strong> Impression share alone, CTR (it's a vanity metric in Smart Bidding), quality score (matters less than people think for non-brand).</p>

<h2>Bid strategy timing</h2>

<p>This is the part most people get wrong. New campaigns start with <em>Maximize Clicks</em> for the first 7-10 days to gather data. Once you have 30+ conversions in the last 30 days, switch to <em>Maximize Conversions</em>. Once that's stable, set a <em>Target CPA</em> 10% above the average. Then drop the CPA target by 10% every 14 days until volume starts shrinking — that's your true cost ceiling.</p>

<p>The brands beating their competition in Google Ads in 2026 aren't writing better headlines. They're feeding the algorithm cleaner signals and giving it room to optimize. Set the structure right, then get out of its way.</p>
""",
    },
]


def seed(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    now = timezone.now()
    for i, post in enumerate(SEED_POSTS):
        # Stagger published dates so the listing has natural variety
        published = now - timedelta(days=i * 9 + 2)
        BlogPost.objects.update_or_create(
            slug=post["slug"],
            defaults={
                **post,
                "is_published": True,
                "published_at": published,
            },
        )


def unseed(apps, schema_editor):
    BlogPost = apps.get_model("website", "BlogPost")
    BlogPost.objects.filter(slug__in=[p["slug"] for p in SEED_POSTS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0006_blogpost"),
    ]

    operations = [
        migrations.RunPython(seed, reverse_code=unseed),
    ]
