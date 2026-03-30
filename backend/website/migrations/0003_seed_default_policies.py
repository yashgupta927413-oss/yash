from django.db import migrations


def seed_policies(apps, schema_editor):
    Policy = apps.get_model('website', 'Policy')
    if Policy.objects.exists():
        return

    defaults = [
        ('privacy', 'Privacy Policy', 'We collect only business-contact information needed to deliver services. Data is stored securely and never sold to third parties.'),
        ('terms', 'Terms of Service', 'Work begins after scope, timeline, and deliverables are approved in writing. Third-party platform outages or policy bans are outside guaranteed control.'),
        ('refund', 'Refund & Lead Replacement Policy', 'Retainer fees are non-refundable once deliverables are provided. For pay-per-lead campaigns, duplicate/invalid leads are replaced according to agreed qualification rules.'),
        ('cookie', 'Cookie Policy', 'Analytics and performance cookies may be used to measure traffic and campaign behavior. Users can disable cookies in browser settings.'),
        ('disclaimer', 'Performance Disclaimer', 'Marketing outcomes vary by niche, budget, competition, and offer quality. We do not guarantee rankings, exact lead volume, or fixed revenue outcomes.'),
    ]

    for index, (policy_type, title, content) in enumerate(defaults, start=1):
        Policy.objects.create(
            policy_type=policy_type,
            title=title,
            content=content,
            sort_order=index,
            is_active=True,
        )


def noop(apps, schema_editor):
    return


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0002_expand_editable_site_content'),
    ]

    operations = [
        migrations.RunPython(seed_policies, reverse_code=noop),
    ]
