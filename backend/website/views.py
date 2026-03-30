from django.http import JsonResponse


def homepage_data(request):
    data = {
        'brand': 'Yash Gupta',
        'headline': 'Digital Marketing That Turns Traffic Into Revenue',
        'subheadline': 'SEO, Google Ads, Meta Ads, SEM, and growth-focused web experiences.',
        'services': [
            'Search Engine Optimization (SEO)',
            'Google Ads & SEM Campaigns',
            'Facebook & Instagram Ads',
            'Conversion-Focused Landing Pages',
            'Web Development & App Development Support',
        ],
        'contact_email': 'hello@theyashgupta.com',
    }
    return JsonResponse(data)
