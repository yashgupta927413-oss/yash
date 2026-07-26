#!/usr/bin/env python3
"""Generates frontend/public/policies.json.

Kept as a generator rather than hand-edited JSON so the bodies can be written as
readable HTML instead of one-line escaped strings. Re-run after editing:
    python3 gen_policies.py
"""
import json, pathlib

UPDATED = "Last updated · July 2026"

BIZ = """
      <p><strong>theyashgupta.com</strong> is a sole-proprietorship digital services business
      operated by Yash Gupta, registered as a micro enterprise under the Udyam / MSME scheme,
      with its place of business in Lucknow, Uttar Pradesh, India.</p>
      <p>
        Email <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a> ·
        Phone / WhatsApp <a href="tel:+919696345822">+91 96963 45822</a><br/>
        In these documents "we", "us", and "our" mean theyashgupta.com; "you" and "the client"
        mean the person or business engaging us.
      </p>
"""

POLICIES = {}

# ---------------------------------------------------------------- Terms
POLICIES["terms"] = {
    "eyebrow": UPDATED,
    "title": "Terms of Service",
    "body": f"""
      <p>These Terms govern every engagement with theyashgupta.com — website subscription plans,
      fixed-scope builds, SEO and performance-marketing retainers, and pay-per-lead arrangements.
      By paying an invoice, approving a proposal, or continuing to use a service we host, you
      accept these Terms.</p>

      <h3>1. Who you are contracting with</h3>
      {BIZ}

      <h3>2. Services</h3>
      <ul>
        <li><strong>Website subscription plans</strong> — a managed website delivered and maintained
        for a recurring fee, currently from ₹429/month. Hosting, SSL, and a set number of monthly
        content updates are included in the plan you select.</li>
        <li><strong>Fixed-scope builds</strong> — a defined website or application delivered against
        a written proposal.</li>
        <li><strong>Retainers</strong> — recurring SEO or performance-marketing work billed monthly.</li>
        <li><strong>Pay-per-lead</strong> — performance-based lead delivery for selected industries,
        governed by qualification criteria agreed in writing before campaigns launch.</li>
      </ul>
      <p>What is included in your engagement is whatever is set out on the pricing page for your plan,
      or in your written proposal. Anything else is a change request and may be quoted separately.</p>

      <h3>3. Subscription plans: fair use of included work</h3>
      <p>Plans include a stated number of <strong>content updates per month</strong> (currently one,
      two, or four depending on tier). A content update means a reasonable change to existing pages —
      editing text, swapping images, updating prices, hours, or contact details, adding a few
      products or posts to an existing template.</p>
      <p>The following are <strong>not</strong> content updates and are quoted separately: new page
      templates or layouts, redesigns, new features or integrations, custom development, migrations,
      and bulk data entry. Additional pages are currently ₹500 per page.</p>
      <p>Unused updates do not roll over. Update requests are actioned within two working days in
      the normal course; complex requests may take longer and we will tell you if so.</p>

      <h3>4. Fees, billing, and taxes</h3>
      <ul>
        <li>Subscriptions are billed <strong>monthly or annually in advance</strong>. There is no setup fee.</li>
        <li>Fixed-scope projects are billed <strong>50% on kickoff, 50% on launch</strong>.</li>
        <li>Retainers are billed monthly in advance.</li>
        <li>Pay-per-lead is invoiced against validated leads on the agreed cycle.</li>
        <li>All prices are <strong>exclusive of GST and any other applicable taxes</strong>, which are
        charged at the prevailing rate.</li>
        <li><strong>Advertising spend is not included</strong> in any retainer fee. Media budgets are
        paid by you directly to Google, Meta, or the relevant platform, or reimbursed at cost.</li>
        <li>Third-party costs — domain renewals beyond any included domain, premium plugins, stock
        assets, paid APIs, email-sending services — are passed through at cost unless your plan
        states otherwise.</li>
      </ul>
      <p>Invoices are payable within <strong>7 days</strong> unless stated otherwise. We may suspend
      services on accounts more than <strong>15 days</strong> overdue after written notice, and may
      charge interest on overdue sums at 1.5% per month.</p>

      <h3>5. Domain names</h3>
      <p>Domains provided as part of a plan are registered and held in our registrar account for the
      duration of your engagement. <strong>The domain remains our property while your subscription is
      active</strong>; inclusion of a domain in a plan is a benefit of that plan, not a transfer of
      ownership.</p>
      <p>You may request transfer of the domain into your own registrar account at any time, subject
      to a <strong>transfer fee of ₹2,999 plus the registrar's transfer and renewal charges</strong>,
      and provided your account is in good standing with no outstanding dues. Registry rules may
      impose a lock period (commonly 60 days after registration or a prior transfer) that we cannot
      waive. Full detail is in our <em>Domain, Hosting &amp; Ownership Policy</em>.</p>
      <p>If you bring your own domain, it stays yours throughout and this clause does not apply.</p>

      <h3>6. Hosting, uptime, and backups</h3>
      <p>Sites are hosted on reputable cloud infrastructure with SSL and uptime monitoring. We aim for
      high availability but <strong>do not warrant uninterrupted or error-free service</strong>. Planned
      maintenance is scheduled outside Indian business hours where practical.</p>
      <p>Backup frequency depends on your plan (weekly automated backups are included on the Growth &amp;
      E-Commerce tier). Backups are a convenience, not a guarantee — you are responsible for keeping
      your own copies of business-critical content and data.</p>

      <h3>7. Your responsibilities</h3>
      <ul>
        <li>Provide content, approvals, and access (hosting, analytics, ad accounts, domain records)
        promptly. Delays in your input shift timelines and do not entitle you to a refund.</li>
        <li>Ensure you hold the rights to all text, images, logos, and data you supply.</li>
        <li>Use the services lawfully and in line with our Acceptable Use Policy.</li>
        <li>Keep your own credentials secure and tell us promptly of any suspected compromise.</li>
      </ul>

      <h3>8. Intellectual property</h3>
      <p>On <strong>full payment</strong> of all sums due, ownership of the final deliverables created
      specifically for you — page designs, custom code, and configuration — transfers to you.</p>
      <p>The following do <strong>not</strong> transfer: pre-existing tools, libraries, frameworks,
      templates, and internal systems we use across clients; third-party software, which remains
      subject to its own licence; and anything built while fees remain outstanding.</p>
      <p>For sites delivered under a subscription plan, the deliverable is provided as a hosted
      service. Ownership of custom code and content is transferred on request, subject to settlement
      of dues; the underlying platform, tooling, and templates are not transferred.</p>
      <p>You grant us permission to display non-confidential parts of the work in our portfolio and
      case studies. Tell us in writing if you would rather we did not, and we will honour that.</p>

      <h3>9. Third-party services</h3>
      <p>Delivery may rely on third parties including cloud hosting, CDN and DNS providers, email
      delivery services, payment gateways such as Razorpay or PhonePe, and advertising platforms
      including Google and Meta. Your use of those services is governed by their own terms. We are not
      responsible for their outages, policy changes, price changes, account suspensions, or algorithm
      updates, and such events are not grounds for a refund.</p>

      <h3>10. Confidentiality</h3>
      <p>Each party will keep the other's non-public business information confidential and use it only
      to perform or receive the services. This survives termination by three years. It does not apply
      to information that is public, independently developed, or required to be disclosed by law.</p>

      <h3>11. No guarantee of results</h3>
      <p>We do not guarantee search rankings, traffic volumes, lead counts, conversion rates, revenue,
      or return on ad spend. These depend on your market, offer, budget, competition, and platform
      behaviour — variables outside our control. See our <em>Disclaimer</em>.</p>

      <h3>12. Limitation of liability</h3>
      <p>To the maximum extent permitted by law, our total aggregate liability arising out of or in
      connection with an engagement is limited to <strong>the fees you actually paid us for that
      engagement in the three months preceding the event giving rise to the claim</strong>.</p>
      <p>We are not liable for indirect or consequential loss, loss of profit, loss of revenue, loss of
      business or goodwill, loss of data, or loss arising from third-party platform actions. Nothing
      here limits liability that cannot lawfully be limited, including for fraud.</p>

      <h3>13. Indemnity</h3>
      <p>You will indemnify us against claims arising from content or data you supply, from your use
      of the services in breach of these Terms or of applicable law, and from your own products,
      services, or customer dealings.</p>

      <h3>14. Suspension and termination</h3>
      <ul>
        <li><strong>Subscriptions</strong> — cancellable with 30 days' written notice.</li>
        <li><strong>Retainers</strong> — cancellable with 14 days' written notice.</li>
        <li><strong>Fixed-scope</strong> — either party may terminate on written notice; work completed
        to that date is billable and deliverable.</li>
      </ul>
      <p>We may suspend or terminate immediately for non-payment, for breach of the Acceptable Use
      Policy, or where continuing would expose us to legal risk. On termination for any reason,
      hosting, SSL, email, and any domain held by us cease at the end of the paid period.</p>

      <h3>15. Force majeure</h3>
      <p>Neither party is liable for delay or failure caused by events beyond reasonable control,
      including infrastructure or platform outages, network failures, natural events, strikes, war, or
      governmental action.</p>

      <h3>16. Changes</h3>
      <p>We may update these Terms. Material changes affecting active engagements take effect at your
      next renewal, and we will give notice by email. Continued use after that constitutes acceptance.</p>

      <h3>17. Governing law and disputes</h3>
      <p>These Terms are governed by the laws of India. The parties will first attempt to resolve any
      dispute in good faith within 30 days of written notice. Failing that, the courts at
      <strong>Lucknow, Uttar Pradesh</strong> have exclusive jurisdiction.</p>

      <h3>18. Grievances</h3>
      <p>Write to <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a> with the subject
      line "Grievance". We acknowledge within 48 hours and aim to resolve within 30 days.</p>
    """,
}

# ---------------------------------------------------------------- Domain & ownership
POLICIES["domain"] = {
    "eyebrow": UPDATED,
    "title": "Domain, Hosting & Ownership Policy",
    "body": f"""
      <p>This policy explains exactly who owns what — the domain, the website, the content, and the
      email accounts — during and after an engagement. It applies alongside our Terms of Service.</p>

      <h3>1. Domains included in a plan</h3>
      <p>Several subscription plans include a domain name (a <strong>.in</strong> on the Digital Card
      Plan, or a <strong>.com or .in</strong> on higher tiers). Where we supply the domain:</p>
      <ul>
        <li>We register it and hold it in <strong>our registrar account</strong>, with theyashgupta.com
        as the registrant.</li>
        <li>We pay the registration and renewal fees for as long as your subscription is active.</li>
        <li><strong>The domain remains our property.</strong> Including it in a plan is a benefit of
        that plan, not a transfer of ownership.</li>
        <li>You have exclusive use of it for your business while your subscription is active, and we
        will not point it elsewhere or use it for anyone else during that time.</li>
      </ul>

      <h3>2. Transferring a domain to you</h3>
      <p>You can ask us to transfer the domain into a registrar account of your own at any time. The
      terms are:</p>
      <ul>
        <li><strong>Transfer fee: ₹2,999</strong> (plus GST), payable before the transfer begins.</li>
        <li><strong>Plus the registrar's charges</strong> — most transfers require paying for an
        additional year of registration at the receiving registrar, and some TLDs carry their own
        transfer fees. These are set by the registrar and registry, not by us, and are passed through
        at cost.</li>
        <li>Your account must be <strong>in good standing with no outstanding dues</strong>.</li>
        <li>Registry rules may impose a <strong>lock period</strong> — commonly 60 days after initial
        registration or after any prior transfer — which we cannot waive.</li>
        <li>We release the authorisation code within <strong>5 working days</strong> of cleared payment
        and any lock expiring.</li>
        <li>The transfer fee is <strong>non-refundable</strong> once the authorisation code is issued.</li>
      </ul>
      <p>Transferring the domain out does not by itself cancel your subscription, and cancelling your
      subscription does not automatically transfer the domain — they are separate requests.</p>

      <h3>3. Domains you already own</h3>
      <p>If you bring your own domain, it stays entirely yours. We only ask for the DNS access needed
      to point it at your site, and you can revoke that at any time. Nothing in section 1 or 2 applies.</p>

      <h3>4. What happens when a subscription ends</h3>
      <ul>
        <li>Hosting, SSL, email accounts, and monitoring stop at the end of the period you have paid for.</li>
        <li>Any domain we supplied and you have not purchased remains ours. We may retain it, allow it
        to lapse, or re-use it after your engagement ends.</li>
        <li>We keep a copy of your site for <strong>30 days</strong> after service ends so you can
        request an export. After that it may be deleted permanently.</li>
      </ul>

      <h3>5. Website, content, and data</h3>
      <ul>
        <li><strong>Your content is yours</strong> — text, images, logos, product data, and any customer
        or enquiry data collected through the site. We claim no ownership of it.</li>
        <li>On request and once dues are settled, we will provide an <strong>export</strong> of your
        content, page copy, images, and collected enquiry data at no charge, in a common format.</li>
        <li>Ownership of custom code and page designs built specifically for you transfers on full
        payment, as set out in the Terms.</li>
        <li>Underlying platforms, templates, internal tooling, and third-party software do not transfer
        and remain subject to their own licences.</li>
      </ul>

      <h3>6. Business email accounts</h3>
      <p>Email accounts provided with a plan run on the included domain and end when the subscription
      ends. Export your mailbox before that date — we cannot recover it afterwards. If you transfer
      the domain to yourself, you will need to set up email at your own provider.</p>

      <h3>7. Questions</h3>
      <p>Anything unclear here, ask before you sign up rather than after:
      <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a>.</p>
    """,
}

# ---------------------------------------------------------------- Privacy
POLICIES["privacy"] = {
    "eyebrow": UPDATED,
    "title": "Privacy Policy",
    "body": f"""
      <p>This policy explains what personal data we collect, why, and what rights you have. It is
      written with reference to India's <strong>Digital Personal Data Protection Act, 2023</strong>
      and the Information Technology Act, 2000 and rules made under it.</p>

      <h3>1. Who is responsible for your data</h3>
      {BIZ}
      <p>For the data we collect through this website and in the course of our own business, we act as
      the <strong>Data Fiduciary</strong>. Where we handle data inside a client's own systems on their
      instructions, we act as a <strong>Data Processor</strong> for that client.</p>

      <h3>2. What we collect</h3>
      <ul>
        <li><strong>Details you give us</strong> — name, email, phone or WhatsApp number, business name,
        the plan or service you are interested in, and anything you write in an enquiry or brief.</li>
        <li><strong>Website URLs</strong> you submit for a free SEO audit.</li>
        <li><strong>Technical data</strong> collected automatically — IP address, browser and device
        type, referring page, pages viewed, and approximate location derived from IP.</li>
        <li><strong>Analytics and advertising data</strong>, only where you have accepted analytics or
        marketing cookies.</li>
        <li><strong>Client account data</strong> for active engagements — billing details, invoices,
        and correspondence.</li>
      </ul>
      <p>We do not knowingly collect sensitive personal data, and we ask that you do not send financial
      account numbers, passwords, or identity-document numbers through website forms or WhatsApp.</p>

      <h3>3. Why we use it, and on what basis</h3>
      <ul>
        <li><strong>To respond to your enquiry and provide services you asked for</strong> — this is the
        purpose for which you provide the data, and processing is on the basis of your consent given
        when you submit a form.</li>
        <li><strong>To perform our contract with you</strong> — delivering, hosting, supporting, and
        invoicing the services.</li>
        <li><strong>To send service-related messages</strong> — renewal reminders, downtime notices,
        invoices.</li>
        <li><strong>To send occasional marketing</strong>, only where you have not objected. Every such
        message carries a one-click opt-out.</li>
        <li><strong>To improve the site and our work</strong>, using aggregated analytics.</li>
        <li><strong>To meet legal, tax, and accounting obligations.</strong></li>
      </ul>

      <h3>4. Cookies</h3>
      <p>Essential cookies are required for the site to function. Analytics and marketing cookies are
      set only if you accept them in the consent banner. See our <em>Cookie Policy</em>.</p>

      <h3>5. Who we share it with</h3>
      <p>We do not sell personal data and we do not trade it for advertising. We share it only with
      service providers who help us operate, each bound to protect it and use it only on our
      instructions. These currently include categories such as:</p>
      <ul>
        <li>Cloud hosting and infrastructure providers</li>
        <li>CDN, DNS, and security providers</li>
        <li>Transactional email delivery providers</li>
        <li>Analytics and advertising platforms, where you have consented</li>
        <li>Payment gateways and our accountants, for billing and statutory records</li>
      </ul>
      <p>We also disclose data where required by law, court order, or a lawful request from a
      government authority.</p>

      <h3>6. Where your data is stored</h3>
      <p>Our primary infrastructure is hosted in India. Some providers — analytics, email delivery, ad
      platforms — process data outside India. Where that happens, we rely on the provider's own
      safeguards and on transfers being permitted under applicable Indian law.</p>

      <h3>7. How long we keep it</h3>
      <ul>
        <li><strong>Enquiries that do not become clients</strong> — up to 24 months, then deleted.</li>
        <li><strong>Client records</strong> — for the life of the relationship, then as long as
        required for tax and legal purposes (generally 8 years for financial records).</li>
        <li><strong>Analytics data</strong> — per the retention setting of the analytics tool.</li>
        <li><strong>Server logs</strong> — typically 30 days.</li>
      </ul>

      <h3>8. Security</h3>
      <p>Data is held on access-controlled services, encrypted in transit over HTTPS. Access is limited
      to those who need it. No system is perfectly secure; if a breach affects your personal data, we
      will notify you and the Data Protection Board as required.</p>

      <h3>9. Your rights</h3>
      <p>Subject to applicable law, you may ask us to:</p>
      <ul>
        <li><strong>Access</strong> a summary of the personal data we hold about you and how it is processed</li>
        <li><strong>Correct</strong> data that is inaccurate, incomplete, or out of date</li>
        <li><strong>Erase</strong> data we no longer need for the purpose it was collected for</li>
        <li><strong>Withdraw consent</strong> at any time, without affecting processing already carried out</li>
        <li><strong>Nominate</strong> another person to exercise your rights in the event of death or incapacity</li>
        <li><strong>Complain</strong> to us, and then to the Data Protection Board of India</li>
      </ul>
      <p>Email <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a> and we will respond
      within 30 days. We may need to verify your identity first.</p>

      <h3>10. Children</h3>
      <p>Our services are for businesses and are not directed at children. We do not knowingly collect
      personal data of anyone under 18. If you believe we have, contact us and we will delete it.</p>

      <h3>11. Grievance Officer</h3>
      <p>Grievances about the handling of personal data go to <strong>Yash Gupta</strong>,
      <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a>, Lucknow, Uttar Pradesh, India.
      We acknowledge within 48 hours and aim to resolve within 30 days.</p>

      <h3>12. Changes</h3>
      <p>We may update this policy. The date at the top always reflects the current version, and
      material changes are notified by email to active clients.</p>
    """,
}

# ---------------------------------------------------------------- Refund
POLICIES["refund"] = {
    "eyebrow": UPDATED,
    "title": "Refund & Cancellation Policy",
    "body": """
      <p>We aim for clear scope and fair outcomes. This policy explains how cancellations and refunds
      work across each way of working with us. It should be read with our Terms of Service.</p>

      <h3>1. Website subscription plans</h3>
      <ul>
        <li>Billed <strong>monthly or annually in advance</strong>. No setup fee, no lock-in period.</li>
        <li>Cancel any time with <strong>30 days' written notice</strong> to
        <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a>. Your site stays live through
        the end of the period already paid for.</li>
        <li><strong>Part-months are not refunded.</strong> Unused time on an annual plan is not refunded.</li>
        <li>Unused monthly content updates do not roll over and hold no cash value.</li>
        <li>Hosting, SSL, email, and any domain we supplied stop at the end of the notice period.</li>
        <li>If we materially fail to deliver what your plan promises and cannot put it right within 14
        days of you telling us in writing, you may cancel immediately and we will refund the unused
        portion of the current period.</li>
      </ul>

      <h3>2. Domain transfer fee</h3>
      <p>The ₹2,999 domain transfer fee is <strong>non-refundable once the authorisation code has been
      issued</strong>. If a transfer cannot proceed because of a registry lock we did not disclose, we
      refund it in full. Registrar and registry charges are set by third parties and are not
      refundable by us.</p>

      <h3>3. Fixed-scope projects</h3>
      <ul>
        <li>The 50% kickoff deposit is <strong>non-refundable</strong> once planning has begun, as it
        reserves delivery capacity.</li>
        <li>If work is cancelled mid-project, fees are pro-rated to the milestones completed and
        accepted.</li>
        <li>Completed assets are delivered once the pro-rata balance is settled.</li>
        <li>Each milestone includes the revision round set out in the proposal. Additional revisions
        are quoted separately and are not grounds for a refund.</li>
      </ul>

      <h3>4. SEO and performance-marketing retainers</h3>
      <ul>
        <li>Cancellable with <strong>14 days' written notice</strong>. Billing stops at the end of the
        current cycle.</li>
        <li>Retainer fees for work already delivered are <strong>not refundable</strong>.</li>
        <li>Unused retainer hours do not roll over.</li>
        <li><strong>Advertising spend is separate</strong> from our fee. Money already spent with
        Google, Meta, or any platform cannot be recovered by us; refunds of media spend are a matter
        between you and that platform.</li>
        <li>Ranking, traffic, and revenue outcomes are not guaranteed and disappointing results are
        not by themselves grounds for a refund. See our <em>Disclaimer</em>.</li>
      </ul>

      <h3>5. Pay-per-lead engagements</h3>
      <ul>
        <li>Lead qualification criteria are agreed <strong>in writing before campaigns launch</strong>.</li>
        <li>Leads failing those criteria — wrong geography, fake or unreachable number, duplicate,
        obvious spam — are <strong>replaced free of charge</strong> when reported within 7 days.</li>
        <li>Refunds are not issued for delivered leads that meet the agreed criteria, including leads
        that do not convert.</li>
      </ul>

      <h3>6. One-time add-ons</h3>
      <p>Add-ons such as extra pages, Google Business Profile work, and logo or branding packs are
      refundable in full if you cancel <strong>before work begins</strong>, and are non-refundable once
      work has started. Recurring add-ons, such as extra email accounts, follow the subscription rules
      in section 1.</p>

      <h3>7. Chargebacks</h3>
      <p>Please raise any billing concern with us first — we would rather fix it. Initiating a
      chargeback without contacting us may result in immediate suspension of services pending
      resolution.</p>

      <h3>8. How to request a cancellation or refund</h3>
      <p>Email <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a> with your invoice
      reference, the service concerned, and the reason. We acknowledge within 48 hours and respond
      substantively within <strong>5 working days</strong>. Approved refunds are returned by the
      original payment method within <strong>7 to 10 working days</strong>, less any transaction
      charges levied by the payment gateway.</p>
    """,
}

# ---------------------------------------------------------------- Acceptable use
POLICIES["acceptable-use"] = {
    "eyebrow": UPDATED,
    "title": "Acceptable Use Policy",
    "body": """
      <p>This policy applies to every website, email account, and service we host or operate for you.
      It exists so that one client's conduct cannot put other clients, our infrastructure, or our
      business at risk.</p>

      <h3>1. You must not use our services to</h3>
      <ul>
        <li>Publish or distribute anything unlawful under Indian law, including content that is
        obscene, defamatory, or that infringes copyright, trademark, or other rights.</li>
        <li>Publish content you do not hold the rights to, including images, fonts, and text taken
        from other sites.</li>
        <li>Operate phishing pages, distribute malware, or attempt to gain unauthorised access to any
        system.</li>
        <li>Send unsolicited bulk email or SMS, or use included business email accounts for cold
        outreach at scale.</li>
        <li>Sell goods or services whose sale requires a licence you do not hold, or which are
        prohibited in India.</li>
        <li>Run gambling, adult, or cryptocurrency-investment offerings, or any get-rich-quick,
        multi-level-marketing, or deceptive financial scheme.</li>
        <li>Make health, medical, financial, or earnings claims you cannot substantiate.</li>
        <li>Collect personal data without a lawful basis, adequate notice, and a privacy policy of
        your own.</li>
        <li>Consume server resources in a way that degrades service for others, including through
        cryptomining or unthrottled scraping.</li>
      </ul>

      <h3>2. Regulated sectors</h3>
      <p>If you operate in a regulated sector — healthcare, finance, education, legal services, food —
      you are responsible for ensuring your website content meets the advertising and disclosure rules
      that apply to you. We will build to your instructions but we do not verify regulatory compliance
      on your behalf.</p>

      <h3>3. Enforcement</h3>
      <p>Where we believe this policy has been breached we will normally contact you first and give a
      reasonable opportunity to fix it. Where the breach is serious, unlawful, or exposes us or other
      clients to immediate risk, we may <strong>suspend the service without prior notice</strong> and
      terminate the engagement. Fees already paid are not refunded in that case.</p>

      <h3>4. Reporting abuse</h3>
      <p>To report content or activity on a site we host, email
      <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a> with the URL and details. We
      acknowledge within 48 hours.</p>
    """,
}

# ---------------------------------------------------------------- Cookies
POLICIES["cookies"] = {
    "eyebrow": UPDATED,
    "title": "Cookie Policy",
    "body": """
      <p>Cookies are small files stored on your device. This site uses them to function, to understand
      how the site is used, and — only with your consent — to measure advertising.</p>

      <h3>1. Categories we use</h3>
      <ul>
        <li><strong>Essential</strong> — required for the site to work: security, form submission, and
        remembering your cookie choice. These cannot be switched off.</li>
        <li><strong>Analytics</strong> — help us understand which pages are read and where visitors
        come from, in aggregate. Set <strong>only if you accept</strong>.</li>
        <li><strong>Marketing</strong> — used by advertising platforms to measure campaign performance
        and show relevant ads. Set <strong>only if you accept</strong>.</li>
      </ul>

      <h3>2. Your choice</h3>
      <p>When you first visit, a banner lets you choose <em>Essential only</em> or <em>Accept all</em>.
      Your choice is stored locally in your browser. To change it later, clear this site's data in your
      browser settings and the banner will appear again.</p>

      <h3>3. Third-party cookies</h3>
      <p>Where you accept analytics or marketing cookies, they are set and read by those third-party
      providers under their own privacy policies. We do not control their cookie lifetimes.</p>

      <h3>4. Blocking cookies</h3>
      <p>You can block or delete cookies through your browser. Blocking essential cookies will break
      parts of this site.</p>

      <h3>5. Questions</h3>
      <p>Email <a href="mailto:yash@theyashgupta.com">yash@theyashgupta.com</a>.</p>
    """,
}

# ---------------------------------------------------------------- Disclaimer
POLICIES["disclaimer"] = {
    "eyebrow": UPDATED,
    "title": "Disclaimer",
    "body": """
      <p>The information and services offered on theyashgupta.com are provided for general business
      purposes. By using this site or engaging our services, you accept the following.</p>

      <h3>1. No guaranteed results</h3>
      <p>Web development, SEO, and paid-media outcomes depend on variables outside our control —
      market conditions, offer quality, competitive intensity, budget, seasonality, and platform
      algorithms. We apply current best practice and report transparently, but we
      <strong>do not guarantee</strong> any specific ranking, traffic level, lead volume, conversion
      rate, revenue, or return on ad spend.</p>

      <h3>2. Figures shown on this site</h3>
      <p>Statistics presented on this site — traffic lifts, ROAS figures, lead counts, ratings, and
      client outcomes — are drawn from selected past engagements and are illustrative. They are
      <strong>not a prediction of your results</strong>, and your results will differ based on your
      stage, sector, offer, and budget.</p>

      <h3>3. Pricing</h3>
      <p>Prices shown are current at the time of publication, exclusive of GST, and may change. The
      price that applies to you is the one stated in your invoice or written proposal. Included
      features are those listed for your plan at the time you subscribe.</p>

      <h3>4. Third-party platforms</h3>
      <p>We are not responsible for the availability, content, pricing, policies, or decisions of
      third-party platforms, including hosting providers, payment gateways, and advertising networks.
      Account suspensions, policy changes, and algorithm updates imposed by those platforms are
      outside our control.</p>

      <h3>5. Not professional advice</h3>
      <p>Nothing on this site or in our communications constitutes legal, financial, tax, medical, or
      regulatory advice. Consult a qualified professional before acting on anything you read here.</p>

      <h3>6. External links</h3>
      <p>This site links to third-party services. We are not responsible for their content, security,
      or privacy practices.</p>

      <h3>7. Changes</h3>
      <p>We may update this disclaimer at any time. Continued use of the site means you accept the
      current version.</p>
    """,
}


def main() -> None:
    out = pathlib.Path(__file__).resolve().parent
    # Written into frontend/public so Vite copies it to the site root.
    target = pathlib.Path("/Users/yash/theyashgupta/frontend/public/policies.json")
    cleaned = {
        k: {"eyebrow": v["eyebrow"], "title": v["title"], "body": v["body"].strip()}
        for k, v in POLICIES.items()
    }
    target.write_text(json.dumps(cleaned, ensure_ascii=False, indent=2), encoding="utf-8")
    size = target.stat().st_size
    print(f"wrote {target} ({size/1024:.1f} KB)")
    for k, v in cleaned.items():
        words = len(v["body"].split())
        print(f"  {k:16} {v['title']:38} ~{words} words")


if __name__ == "__main__":
    main()
