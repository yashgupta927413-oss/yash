import json
import logging
import os

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import (
    BlogPost,
    FAQ,
    GoogleReview,
    Lead,
    Module,
    Policy,
    PricingPlan,
    ProcessStep,
    Review,
    Service,
    SiteSetting,
    Statistic,
    Tool,
)


logger = logging.getLogger(__name__)


DEFAULT_POLICIES = [
    {
        "policy_type": "privacy",
        "title": "Privacy Policy",
        "content": (
            "We collect only business-contact information needed to provide digital marketing services, "
            "store it securely, and never sell personal data to third parties."
        ),
    },
    {
        "policy_type": "terms",
        "title": "Terms of Service",
        "content": (
            "Project scope, timeline, approvals, and deliverables are documented before work starts. "
            "Platform policy violations, ad account suspensions, and third-party outages are outside direct control."
        ),
    },
    {
        "policy_type": "refund",
        "title": "Refund & Lead Replacement Policy",
        "content": (
            "Retainer services are non-refundable once work is delivered. For pay-per-lead campaigns, "
            "invalid or duplicate leads are replaced based on mutually agreed qualification rules."
        ),
    },
    {
        "policy_type": "cookie",
        "title": "Cookie Policy",
        "content": (
            "This site may use analytics cookies for traffic and conversion measurement. "
            "Visitors can disable cookies in browser settings, which may limit tracking features."
        ),
    },
    {
        "policy_type": "disclaimer",
        "title": "Performance Disclaimer",
        "content": (
            "Marketing results vary by niche, budget, offer quality, website readiness, and competition. "
            "No guaranteed ranking or revenue claim is made."
        ),
    },
]


def homepage_data(request):
    settings = SiteSetting.objects.first()
    faqs = list(FAQ.objects.filter(is_active=True).values("question", "answer"))
    policies = list(
        Policy.objects.filter(is_active=True).values("policy_type", "title", "content")
    ) or DEFAULT_POLICIES
    stats = list(
        Statistic.objects.filter(is_active=True).values("label", "value", "suffix")
    )
    tools = list(Tool.objects.filter(is_active=True).values_list("name", flat=True))
    services = list(
        Service.objects.filter(is_active=True).values("title", "description", "image_url")
    )
    modules = list(
        Module.objects.filter(is_active=True).values(
            "title", "item_1", "item_2", "item_3", "item_4"
        )
    )
    pricing = list(
        PricingPlan.objects.filter(is_active=True).values(
            "title", "price", "description", "is_featured"
        )
    )
    reviews = list(
        Review.objects.filter(is_active=True).values(
            "quote", "customer_name", "customer_title", "source"
        )
    )
    google_reviews = list(
        GoogleReview.objects.filter(is_active=True).values(
            "rating", "quote", "source_label"
        )
    )
    process_steps = list(
        ProcessStep.objects.filter(is_active=True).values(
            "step_number", "title", "description"
        )
    )

    data = {
        "brand": settings.business_name if settings else "Yash Gupta",
        "hero_eyebrow": (
            settings.hero_eyebrow
            if settings
            else "Performance Marketing for Serious Growth"
        ),
        "hero_title": (
            settings.hero_title
            if settings
            else "Scale Leads & Sales with SEO, Ads, and Conversion-Focused Execution"
        ),
        "hero_description": (
            settings.hero_description
            if settings
            else "Result-driven digital growth systems for businesses."
        ),
        "trust_badges": [
            settings.trust_badge_1 if settings else "MSME Registered Business: theyashgupta.com",
            settings.trust_badge_2 if settings else "Performance-Focused Digital Marketing",
            settings.trust_badge_3 if settings else "Transparent Reporting & Lead Tracking",
        ],
        "primary_cta_text": settings.primary_cta_text if settings else "Get Free Audit",
        "secondary_cta_text": (
            settings.secondary_cta_text if settings else "See Client Reviews"
        ),
        "contact_email": settings.support_email if settings else "yash@theyashgupta.com",
        "contact_phone": settings.support_phone if settings else "+91 96963 45822",
        "whatsapp_number": settings.whatsapp_number if settings else "919696345822",
        "show_default_admin_note": settings.show_default_admin_note if settings else True,
        "section_order": settings.section_order if settings else [],
        "faqs": faqs,
        "policies": policies,
        "stats": stats,
        "tools": tools,
        "service_cards": services,
        "modules": modules,
        "pricing_plans": pricing,
        "reviews": reviews,
        "google_reviews": google_reviews,
        "process_steps": process_steps,
    }
    return JsonResponse(data)


# ---------------------------------------------------------------------------
# Blog endpoints
# GET /api/blog/         → list of published posts (light payload)
# GET /api/blog/<slug>/  → full post body
# ---------------------------------------------------------------------------


def _serialize_post(post: BlogPost, full: bool = False) -> dict:
    data = {
        "id": post.id,
        "slug": post.slug,
        "title": post.title,
        "subtitle": post.subtitle,
        "tag": post.tag,
        "excerpt": post.excerpt,
        "cover_emoji": post.cover_emoji or "✦",
        "read_minutes": post.read_minutes,
        "author_name": post.author_name,
        "published_at": post.published_at.isoformat() if post.published_at else None,
    }
    if full:
        data["body"] = post.body
        data["updated_at"] = post.updated_at.isoformat()
    return data


def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True).order_by("-published_at")
    return JsonResponse({"posts": [_serialize_post(p) for p in posts]})


def blog_detail(request, slug: str):
    try:
        post = BlogPost.objects.get(slug=slug, is_published=True)
    except BlogPost.DoesNotExist:
        return JsonResponse({"error": "not_found"}, status=404)
    return JsonResponse({"post": _serialize_post(post, full=True)})


# ---------------------------------------------------------------------------
# Server-rendered blog pages (real HTML, indexable by Google on first crawl).
# These templates are the canonical /blog/ URLs in production.
# ---------------------------------------------------------------------------


def blog_list_page(request):
    posts = BlogPost.objects.filter(is_published=True).order_by("-published_at")
    tags = sorted({p.tag for p in posts})
    base_url = getattr(settings, "SITE_BASE_URL", "https://theyashgupta.com")
    return render(
        request,
        "website/blog_list.html",
        {
            "posts": posts,
            "tags": tags,
            "base_url": base_url,
            "page_url": f"{base_url}/blog/",
        },
    )


def blog_post_page(request, slug: str):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    related = (
        BlogPost.objects.filter(is_published=True, tag=post.tag)
        .exclude(id=post.id)
        .order_by("-published_at")[:3]
    )
    base_url = getattr(settings, "SITE_BASE_URL", "https://theyashgupta.com")
    return render(
        request,
        "website/blog_post.html",
        {
            "post": post,
            "related": related,
            "base_url": base_url,
            "canonical_url": f"{base_url}/blog/{post.slug}/",
        },
    )


def service_page(request, slug: str):
    from .services_content import SERVICES

    svc = SERVICES.get(slug)
    if svc is None:
        raise Http404("Unknown service")
    related = (
        BlogPost.objects.filter(is_published=True, tag=svc["related_tag"])
        .order_by("-published_at")[:3]
    )
    base_url = getattr(settings, "SITE_BASE_URL", "https://theyashgupta.com")
    return render(
        request,
        "website/service_page.html",
        {
            "svc": svc,
            "related": related,
            "base_url": base_url,
            "canonical_url": f"{base_url}/services/{slug}/",
        },
    )


def robots_txt(request):
    base_url = getattr(settings, "SITE_BASE_URL", "https://theyashgupta.com")
    body = "\n".join(
        [
            "User-agent: *",
            "Allow: /",
            "Disallow: /admin/",
            "Disallow: /api/",
            "",
            f"Sitemap: {base_url}/sitemap.xml",
            "",
        ]
    )
    return HttpResponse(body, content_type="text/plain")


# ---------------------------------------------------------------------------
# Lead-form endpoint  POST /api/lead/
# Accepts JSON from the marketing site's audit form and main inquiry form,
# persists the lead, emails Yash, and returns a JSON ack.
# ---------------------------------------------------------------------------


_REQUIRED_BY_KIND = {
    Lead.KIND_AUDIT: ["email", "site_url"],
    Lead.KIND_INQUIRY: ["name", "email", "brief"],
    # Subscription leads are followed up on WhatsApp, so the phone number is
    # required; the plan itself arrives in project_type.
    Lead.KIND_SUBSCRIPTION: ["name", "email", "phone"],
}


def _client_ip(request):
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


def _notify_owner(lead: Lead) -> None:
    """Send a notification email to the site owner. Soft-fails on SMTP errors
    so the API still returns success — the lead row is the source of truth."""
    recipient = os.getenv("LEAD_NOTIFICATION_EMAIL", "yash@theyashgupta.com")
    subject_prefix = {
        Lead.KIND_INQUIRY: "[Lead]",
        Lead.KIND_SUBSCRIPTION: "[Subscription]",
        Lead.KIND_AUDIT: "[Audit]",
    }.get(lead.kind, "[Lead]")
    subject = f"{subject_prefix} {lead.name or lead.email} — {lead.project_type or lead.site_url or 'no subject'}"

    lines = [
        f"New {lead.get_kind_display()} from theyashgupta.com",
        "",
        f"Name      : {lead.name or '—'}",
        f"Email     : {lead.email}",
        f"Phone     : {lead.phone or '—'}",
        f"Company   : {lead.company or '—'}",
        f"Project   : {lead.project_type or '—'}",
        f"Budget    : {lead.budget or '—'}",
        f"Site URL  : {lead.site_url or '—'}",
        "",
        "Brief:",
        lead.brief or "—",
        "",
        "----",
        f"Received  : {lead.created_at:%Y-%m-%d %H:%M %Z}",
        f"IP        : {lead.ip_address or '—'}",
        f"Referrer  : {lead.referrer or '—'}",
        f"User agent: {lead.user_agent or '—'}",
        "",
        f"Open in admin: /admin/website/lead/{lead.id}/change/",
    ]
    body = "\n".join(lines)

    try:
        from_addr = getattr(settings, "DEFAULT_FROM_EMAIL", "no-reply@theyashgupta.com")
        msg = EmailMultiAlternatives(
            subject=subject,
            body=body,
            from_email=from_addr,
            to=[recipient],
            reply_to=[lead.email] if lead.email else None,
        )
        msg.send(fail_silently=False)
    except Exception as exc:  # noqa: BLE001
        # Email infra problems should never lose the lead. Log and move on.
        logger.warning("Lead notification email failed: %s", exc)


@csrf_exempt
@require_POST
def create_lead(request):
    # Parse JSON body
    try:
        payload = json.loads(request.body or b"{}")
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON payload.")

    if not isinstance(payload, dict):
        return HttpResponseBadRequest("Payload must be a JSON object.")

    # Optional spam honeypot: any field named "website" filled => silently accept-but-drop
    if payload.get("website"):
        return JsonResponse({"ok": True})

    # Normalize kind. Frontend sends `type`; map to model `kind`.
    raw_kind = (payload.get("type") or payload.get("kind") or Lead.KIND_INQUIRY).strip()
    if raw_kind not in dict(Lead.KIND_CHOICES):
        raw_kind = Lead.KIND_INQUIRY

    # Field map between frontend payload keys and model fields
    field_map = {
        "name": payload.get("name", "").strip()[:120],
        "email": payload.get("email", "").strip()[:254],
        "phone": payload.get("phone", "").strip()[:40],
        "company": payload.get("company", "").strip()[:120],
        "project_type": payload.get("projectType", "").strip()[:120],
        "budget": payload.get("budget", "").strip()[:60],
        "brief": payload.get("brief", "").strip(),
        "site_url": (payload.get("url") or payload.get("site_url") or "").strip()[:400],
    }

    # Required field validation
    missing = [f for f in _REQUIRED_BY_KIND[raw_kind] if not field_map.get(f)]
    if missing:
        return JsonResponse(
            {"ok": False, "error": "missing_required_fields", "fields": missing},
            status=400,
        )

    lead = Lead.objects.create(
        kind=raw_kind,
        **field_map,
        ip_address=_client_ip(request),
        user_agent=request.META.get("HTTP_USER_AGENT", "")[:400],
        referrer=request.META.get("HTTP_REFERER", "")[:400],
    )

    _notify_owner(lead)

    return JsonResponse(
        {
            "ok": True,
            "id": lead.id,
            "kind": lead.kind,
            "message": {
                Lead.KIND_AUDIT: "Audit request received. Loom arriving within 48 hours.",
                Lead.KIND_SUBSCRIPTION: "Plan request received. I'll confirm on WhatsApp within 24 hours.",
            }.get(lead.kind, "Brief received. You'll hear back within 24 hours."),
        }
    )


# ---------------------------------------------------------------------------
# Server-rendered legal pages at /legal/ and /legal/<slug>/.
# Real crawlable URLs — required by Meta Lead Ads, which fetches the privacy
# policy URL and checks the document is actually in the HTML. The on-page modal
# reads the same policies.json, so the two can never drift apart.
# ---------------------------------------------------------------------------


def legal_index(request):
    from .policies import all_policies

    base_url = getattr(settings, "SITE_BASE_URL", "https://theyashgupta.com")
    return render(
        request,
        "website/legal_index.html",
        {
            "policies": all_policies(),
            "base_url": base_url,
            "canonical_url": f"{base_url}/legal/",
        },
    )


def legal_page(request, slug: str):
    from .policies import all_policies, get_policy

    policy = get_policy(slug)
    if policy is None:
        raise Http404("Unknown policy")
    base_url = getattr(settings, "SITE_BASE_URL", "https://theyashgupta.com")
    return render(
        request,
        "website/legal_page.html",
        {
            "policy": policy,
            "others": [p for p in all_policies() if p["slug"] != slug],
            "base_url": base_url,
            "canonical_url": f"{base_url}/legal/{slug}/",
        },
    )
