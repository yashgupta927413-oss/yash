from django.contrib import admin
from .models import FAQ, Policy, SiteSetting


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("question", "answer")


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ("title", "policy_type", "sort_order", "is_active")
    list_filter = ("policy_type", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("title", "content")


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("business_name", "support_email", "support_phone", "updated_at")
