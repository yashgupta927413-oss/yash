from django.contrib import admin
from django.utils.html import format_html
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

admin.site.site_header = "theyashgupta.com Admin"
admin.site.site_title = "Yash Admin"
admin.site.index_title = "Website Content Controls"


class GraphicAdmin(admin.ModelAdmin):
    list_per_page = 20

    class Media:
        css = {"all": ("admin/custom_admin.css",)}


@admin.register(FAQ)
class FAQAdmin(GraphicAdmin):
    list_display = ("question", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("question", "answer")


@admin.register(Policy)
class PolicyAdmin(GraphicAdmin):
    list_display = ("title", "policy_type", "sort_order", "is_active")
    list_filter = ("policy_type", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("title", "content")


@admin.register(SiteSetting)
class SiteSettingAdmin(GraphicAdmin):
    list_display = ("business_name", "support_email", "support_phone", "updated_at")
    readonly_fields = ("updated_at",)
    fieldsets = (
        (
            "Brand + Hero",
            {
                "fields": (
                    "business_name",
                    "hero_eyebrow",
                    "hero_title",
                    "hero_description",
                )
            },
        ),
        (
            "Trust + CTA",
            {
                "fields": (
                    "trust_badge_1",
                    "trust_badge_2",
                    "trust_badge_3",
                    "primary_cta_text",
                    "secondary_cta_text",
                    "show_default_admin_note",
                )
            },
        ),
        (
            "Contacts",
            {"fields": ("support_email", "support_phone", "whatsapp_number")},
        ),
        ("Meta", {"fields": ("updated_at",)}),
    )


@admin.register(Statistic)
class StatisticAdmin(GraphicAdmin):
    list_display = ("label", "value", "suffix", "sort_order", "is_active")
    list_editable = ("value", "suffix", "sort_order", "is_active")
    search_fields = ("label",)


@admin.register(Tool)
class ToolAdmin(GraphicAdmin):
    list_display = ("name", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("name",)


@admin.register(Service)
class ServiceAdmin(GraphicAdmin):
    list_display = ("title", "preview_image", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("title", "description")

    @admin.display(description="Image")
    def preview_image(self, obj):
        return format_html('<img src="{}" style="width:72px;height:44px;object-fit:cover;border-radius:8px;" />', obj.image_url)


@admin.register(Module)
class ModuleAdmin(GraphicAdmin):
    list_display = ("title", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("title", "item_1", "item_2", "item_3", "item_4")


@admin.register(PricingPlan)
class PricingPlanAdmin(GraphicAdmin):
    list_display = ("title", "price", "is_featured", "sort_order", "is_active")
    list_editable = ("price", "is_featured", "sort_order", "is_active")
    search_fields = ("title", "description")


@admin.register(Review)
class ReviewAdmin(GraphicAdmin):
    list_display = ("customer_name", "customer_title", "source", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("customer_name", "customer_title", "quote")


@admin.register(GoogleReview)
class GoogleReviewAdmin(GraphicAdmin):
    list_display = ("rating", "source_label", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("quote", "source_label")


@admin.register(ProcessStep)
class ProcessStepAdmin(GraphicAdmin):
    list_display = ("step_number", "title", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("step_number", "title", "description")
