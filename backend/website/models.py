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
    support_email = models.EmailField(default="yash@theyashgupta.com")
    support_phone = models.CharField(max_length=30, default="+91 96963 45822")
    whatsapp_number = models.CharField(max_length=20, default="919696345822")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Settings: {self.business_name}"
