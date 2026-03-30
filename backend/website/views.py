from django.http import JsonResponse
from .models import FAQ, Policy, SiteSetting


def homepage_data(request):
    settings = SiteSetting.objects.first()
    faqs = list(FAQ.objects.filter(is_active=True).values('question', 'answer'))
    policies = list(
        Policy.objects.filter(is_active=True).values('policy_type', 'title', 'content')
    )

    data = {
        'brand': settings.business_name if settings else 'Yash Gupta',
        'headline': 'Digital Marketing That Turns Traffic Into Revenue',
        'subheadline': 'SEO, Google Ads, Meta Ads, SEM, and growth-focused web experiences.',
        'services': [
            'Search Engine Optimization (SEO)',
            'Google Ads & SEM Campaigns',
            'Facebook & Instagram Ads',
            'Conversion-Focused Landing Pages',
            'Web Development & App Development Support',
        ],
        'contact_email': settings.support_email if settings else 'yash@theyashgupta.com',
        'contact_phone': settings.support_phone if settings else '+91 96963 45822',
        'whatsapp_number': settings.whatsapp_number if settings else '919696345822',
        'faqs': faqs,
        'policies': policies,
    }
    return JsonResponse(data)
