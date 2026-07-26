from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, reverse
from django.shortcuts import redirect, render
from django.utils.html import format_html
import json
from .models import (
    BlogPost,
    FAQ,
    GoogleReview,
    Lead,
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


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "tag", "is_published", "published_at", "read_minutes")
    list_filter = ("is_published", "tag", "published_at")
    search_fields = ("title", "subtitle", "excerpt", "body")
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    ordering = ("-published_at",)
    fieldsets = (
        ("Visibility", {"fields": ("is_published", "published_at")}),
        ("Content", {"fields": ("title", "subtitle", "tag", "slug", "excerpt", "body")}),
        ("Display", {"fields": ("cover_emoji", "read_minutes", "author_name")}),
        ("Meta", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "kind",
        "status",
        "name",
        "email",
        "phone",
        "company",
        "project_type",
        "budget",
    )
    list_filter = ("kind", "status", "project_type", "budget", "created_at")
    search_fields = (
        "name",
        "email",
        "phone",
        "company",
        "brief",
        "site_url",
    )
    list_editable = ("status",)
    readonly_fields = (
        "created_at",
        "updated_at",
        "ip_address",
        "user_agent",
        "referrer",
    )
    fieldsets = (
        ("Submission", {
            "fields": ("kind", "status", "created_at", "updated_at"),
        }),
        ("Contact details", {
            "fields": ("name", "email", "phone", "company"),
        }),
        ("Project brief", {
            "fields": ("project_type", "budget", "brief", "site_url"),
        }),
        ("Internal", {
            "fields": ("notes", "ip_address", "user_agent", "referrer"),
            "classes": ("collapse",),
        }),
    )
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

admin.site.site_header = "theyashgupta.com Admin"
admin.site.site_title = "Yash Admin"
admin.site.index_title = "Website Content Controls"


class GraphicAdmin(admin.ModelAdmin):
    list_per_page = 20

    class Media:
        css = {"all": ("admin/custom_admin.css",)}


class DragDropSortableAdmin(GraphicAdmin):
    sortable_field = "sort_order"
    drag_column_label = "Drag"

    class Media:
        css = {"all": ("admin/custom_admin.css", "admin/drag_sort.css")}
        js = ("admin/drag_sort.js",)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "reorder/",
                self.admin_site.admin_view(self.reorder_view),
                name=f"{self.model._meta.app_label}_{self.model._meta.model_name}_reorder",
            ),
        ]
        return custom_urls + urls

    @admin.display(description=drag_column_label)
    def drag_handle(self, obj):
        reorder_url = reverse(
            f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_reorder"
        )
        return format_html(
            '<span class="drag-handle" title="Drag to reorder" data-reorder-url="{}">⋮⋮</span>',
            reorder_url,
        )

    def reorder_view(self, request):
        if request.method != "POST":
            return JsonResponse({"detail": "Method not allowed"}, status=405)
        try:
            payload = json.loads(request.body.decode("utf-8"))
            ids = payload.get("ids", [])
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse({"detail": "Invalid payload"}, status=400)

        queryset = self.model.objects.filter(pk__in=ids)
        objects_by_id = {obj.pk: obj for obj in queryset}
        for index, obj_id in enumerate(ids):
            obj = objects_by_id.get(obj_id)
            if obj is None:
                continue
            setattr(obj, self.sortable_field, index)
            obj.save(update_fields=[self.sortable_field])
        return JsonResponse({"ok": True})


@admin.register(FAQ)
class FAQAdmin(DragDropSortableAdmin):
    list_display = ("drag_handle", "question", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("question", "answer")


@admin.register(Policy)
class PolicyAdmin(DragDropSortableAdmin):
    list_display = ("drag_handle", "title", "policy_type", "sort_order", "is_active")
    list_filter = ("policy_type", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("title", "content")


@admin.register(SiteSetting)
class SiteSettingAdmin(GraphicAdmin):
    list_display = ("business_name", "support_email", "support_phone", "layout_editor_link", "updated_at")
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
            {"fields": ("support_email", "support_phone", "whatsapp_number", "section_order")},
        ),
        ("Meta", {"fields": ("updated_at",)}),
    )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "layout-editor/",
                self.admin_site.admin_view(self.layout_editor_view),
                name="website_sitesetting_layout_editor",
            )
        ]
        return custom_urls + urls

    @admin.display(description="Layout")
    def layout_editor_link(self, obj):
        url = reverse("admin:website_sitesetting_layout_editor")
        return format_html('<a class="button" href="{}">Open drag editor</a>', url)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["layout_editor_url"] = reverse(
            "admin:website_sitesetting_layout_editor"
        )
        return super().changelist_view(request, extra_context=extra_context)

    def layout_editor_view(self, request):
        settings = SiteSetting.objects.first()
        if not settings:
            settings = SiteSetting.objects.create()
        default_sections = [
            "showcase",
            "results",
            "services",
            "specialized-services",
            "pricing",
            "reviews",
            "google-reviews",
            "process",
            "contact",
            "policies",
        ]
        section_order = settings.section_order or default_sections
        if request.method == "POST":
            ids = request.POST.get("section_order", "")
            parsed = [item.strip() for item in ids.split(",") if item.strip()]
            settings.section_order = parsed or default_sections
            settings.save(update_fields=["section_order"])
            self.message_user(request, "Layout order updated successfully.")
            return redirect("admin:website_sitesetting_layout_editor")

        context = {
            **self.admin_site.each_context(request),
            "title": "Drag-and-Drop Website Layout Editor",
            "section_order": section_order,
        }
        return render(request, "admin/website/layout_editor.html", context)


@admin.register(Statistic)
class StatisticAdmin(DragDropSortableAdmin):
    list_display = ("drag_handle", "label", "value", "suffix", "sort_order", "is_active")
    list_editable = ("value", "suffix", "sort_order", "is_active")
    search_fields = ("label",)


@admin.register(Tool)
class ToolAdmin(DragDropSortableAdmin):
    list_display = ("drag_handle", "name", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("name",)


@admin.register(Service)
class ServiceAdmin(DragDropSortableAdmin):
    list_display = ("drag_handle", "title", "preview_image", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("title", "description")

    @admin.display(description="Image")
    def preview_image(self, obj):
        return format_html('<img src="{}" style="width:72px;height:44px;object-fit:cover;border-radius:8px;" />', obj.image_url)


@admin.register(Module)
class ModuleAdmin(DragDropSortableAdmin):
    list_display = ("drag_handle", "title", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("title", "item_1", "item_2", "item_3", "item_4")


@admin.register(PricingPlan)
class PricingPlanAdmin(DragDropSortableAdmin):
    list_display = ("drag_handle", "title", "price", "is_featured", "sort_order", "is_active")
    list_editable = ("price", "is_featured", "sort_order", "is_active")
    search_fields = ("title", "description")


@admin.register(Review)
class ReviewAdmin(DragDropSortableAdmin):
    list_display = ("drag_handle", "customer_name", "customer_title", "source", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("customer_name", "customer_title", "quote")


@admin.register(GoogleReview)
class GoogleReviewAdmin(DragDropSortableAdmin):
    list_display = ("drag_handle", "rating", "source_label", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("quote", "source_label")


@admin.register(ProcessStep)
class ProcessStepAdmin(DragDropSortableAdmin):
    list_display = ("drag_handle", "step_number", "title", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("step_number", "title", "description")
