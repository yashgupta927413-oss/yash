from django.http import JsonResponse
from .models import (
    FAQ,
    GoogleReview,
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
