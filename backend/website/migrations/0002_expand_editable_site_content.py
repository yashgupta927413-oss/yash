from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesetting",
            name="hero_eyebrow",
            field=models.CharField(default="Performance Marketing for Serious Growth", max_length=140),
        ),
        migrations.AddField(
            model_name="sitesetting",
            name="hero_title",
            field=models.CharField(default="Scale Leads & Sales with SEO, Ads, and Conversion-Focused Execution", max_length=220),
        ),
        migrations.AddField(
            model_name="sitesetting",
            name="hero_description",
            field=models.TextField(default="I'm Yash Gupta. I help businesses grow with SEO, SEM, Google Ads, Facebook/Instagram Ads, and digital funnels built for measurable ROI."),
        ),
        migrations.AddField(
            model_name="sitesetting",
            name="trust_badge_1",
            field=models.CharField(default="MSME Registered Business: theyashgupta.com", max_length=180),
        ),
        migrations.AddField(
            model_name="sitesetting",
            name="trust_badge_2",
            field=models.CharField(default="Performance-Focused Digital Marketing", max_length=180),
        ),
        migrations.AddField(
            model_name="sitesetting",
            name="trust_badge_3",
            field=models.CharField(default="Transparent Reporting & Lead Tracking", max_length=180),
        ),
        migrations.AddField(
            model_name="sitesetting",
            name="show_default_admin_note",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="sitesetting",
            name="primary_cta_text",
            field=models.CharField(default="Get Free Audit", max_length=80),
        ),
        migrations.AddField(
            model_name="sitesetting",
            name="secondary_cta_text",
            field=models.CharField(default="See Client Reviews", max_length=80),
        ),
        migrations.CreateModel(
            name="GoogleReview",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("rating", models.CharField(default="★★★★★", max_length=10)),
                ("quote", models.TextField()),
                ("source_label", models.CharField(default="Google Review", max_length=80)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["sort_order", "id"]},
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("item_1", models.CharField(max_length=220)),
                ("item_2", models.CharField(max_length=220)),
                ("item_3", models.CharField(max_length=220)),
                ("item_4", models.CharField(max_length=220)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["sort_order", "id"]},
        ),
        migrations.CreateModel(
            name="PricingPlan",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("price", models.CharField(max_length=80)),
                ("description", models.TextField()),
                ("is_featured", models.BooleanField(default=False)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["sort_order", "id"]},
        ),
        migrations.CreateModel(
            name="ProcessStep",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("step_number", models.CharField(default="01", max_length=10)),
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField()),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["sort_order", "id"]},
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quote", models.TextField()),
                ("customer_name", models.CharField(max_length=120)),
                ("customer_title", models.CharField(max_length=120)),
                ("source", models.CharField(default="Client Review", max_length=60)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["sort_order", "id"]},
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField()),
                ("image_url", models.URLField()),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["sort_order", "id"]},
        ),
        migrations.CreateModel(
            name="Statistic",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("label", models.CharField(max_length=120)),
                ("value", models.PositiveIntegerField(default=0)),
                ("suffix", models.CharField(default="+", max_length=8)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["sort_order", "id"]},
        ),
        migrations.CreateModel(
            name="Tool",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80)),
                ("sort_order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["sort_order", "id"]},
        ),
    ]
