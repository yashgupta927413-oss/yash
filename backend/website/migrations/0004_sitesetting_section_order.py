from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0003_seed_default_policies'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='section_order',
            field=models.JSONField(blank=True, default=list, help_text='Homepage section IDs in preferred order'),
        ),
    ]
