from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return self.question


class Policy(models.Model):
    POLICY_TYPES = [
        ("privacy", "Privacy Policy"),
        ("terms", "Terms of Service"),
        ("refund", "Refund Policy"),
        ("cookie", "Cookie Policy"),
        ("disclaimer", "Disclaimer"),
    ]

    policy_type = models.CharField(max_length=20, choices=POLICY_TYPES)
    title = models.CharField(max_length=255)
    content = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return self.title


class SiteSetting(models.Model):
    business_name = models.CharField(max_length=120, default="Yash Gupta")
    hero_eyebrow = models.CharField(max_length=140, default="Performance Marketing for Serious Growth")
    hero_title = models.CharField(
        max_length=220,
        default="Scale Leads & Sales with SEO, Ads, and Conversion-Focused Execution",
    )
    hero_description = models.TextField(
        default=(
            "I'm Yash Gupta. I help businesses grow with SEO, SEM, Google Ads, "
            "Facebook/Instagram Ads, and digital funnels built for measurable ROI."
        )
    )
    trust_badge_1 = models.CharField(
        max_length=180, default="MSME Registered Business: theyashgupta.com"
    )
    trust_badge_2 = models.CharField(
        max_length=180, default="Performance-Focused Digital Marketing"
    )
    trust_badge_3 = models.CharField(
        max_length=180, default="Transparent Reporting & Lead Tracking"
    )
    show_default_admin_note = models.BooleanField(default=True)
    primary_cta_text = models.CharField(max_length=80, default="Get Free Audit")
    secondary_cta_text = models.CharField(max_length=80, default="See Client Reviews")
    support_email = models.EmailField(default="yash@theyashgupta.com")
    support_phone = models.CharField(max_length=30, default="+91 96963 45822")
    whatsapp_number = models.CharField(max_length=20, default="919696345822")
    section_order = models.JSONField(
        default=list,
        blank=True,
        help_text="Homepage section IDs in preferred order",
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Settings: {self.business_name}"


class Statistic(models.Model):
    label = models.CharField(max_length=120)
    value = models.PositiveIntegerField(default=0)
    suffix = models.CharField(max_length=8, default="+")
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return self.label


class Tool(models.Model):
    name = models.CharField(max_length=80)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image_url = models.URLField()
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=120)
    item_1 = models.CharField(max_length=220)
    item_2 = models.CharField(max_length=220)
    item_3 = models.CharField(max_length=220)
    item_4 = models.CharField(max_length=220)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return self.title


class PricingPlan(models.Model):
    title = models.CharField(max_length=120)
    price = models.CharField(max_length=80)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    quote = models.TextField()
    customer_name = models.CharField(max_length=120)
    customer_title = models.CharField(max_length=120)
    source = models.CharField(max_length=60, default="Client Review")
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return self.customer_name


class GoogleReview(models.Model):
    rating = models.CharField(max_length=10, default="★★★★★")
    quote = models.TextField()
    source_label = models.CharField(max_length=80, default="Google Review")
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return f"{self.source_label} ({self.rating})"


class ProcessStep(models.Model):
    step_number = models.CharField(max_length=10, default="01")
    title = models.CharField(max_length=120)
    description = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return f"{self.step_number} - {self.title}"
