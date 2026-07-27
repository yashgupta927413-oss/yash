"""Sitemap definitions for theyashgupta.com.

Drives /sitemap.xml. Every published BlogPost auto-appears here within seconds
of being marked published in the admin.
"""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import BlogPost
from .policies import POLICY_ORDER


class StaticSitemap(Sitemap):
    """Top-level routes that don't live in the database."""

    changefreq = "monthly"
    priority = 0.9
    protocol = "https"

    def items(self):
        return [
            ("home", "/", 1.0, "weekly"),
            ("svc-webdev", "/services/web-development/", 0.9, "monthly"),
            ("svc-marketing", "/services/digital-marketing/", 0.9, "monthly"),
            ("svc-seo", "/services/seo/", 0.9, "monthly"),
            ("webdev", "/#webdev", 0.8, "monthly"),
            ("marketing", "/#marketing", 0.8, "monthly"),
            ("seo", "/#seo", 0.8, "monthly"),
            ("about", "/#about", 0.7, "monthly"),
            ("work", "/#work", 0.7, "monthly"),
            ("plans", "/#plans", 0.9, "monthly"),
            ("pricing", "/#pricing", 0.7, "monthly"),
            ("faq", "/#faq", 0.6, "monthly"),
            ("contact", "/#contact", 0.7, "monthly"),
            ("blog", "/blog/", 0.9, "weekly"),
            ("legal", "/legal/", 0.5, "yearly"),
        ] + [
            (f"legal-{slug}", f"/legal/{slug}/", 0.4, "yearly")
            for slug in POLICY_ORDER
        ]

    def location(self, item):
        return item[1]

    def priority(self, item):  # noqa: F811
        return item[2]

    def changefreq(self, item):  # noqa: F811
        return item[3]


class BlogPostSitemap(Sitemap):
    """Every published blog post."""

    changefreq = "monthly"
    priority = 0.7
    protocol = "https"

    def items(self):
        return BlogPost.objects.filter(is_published=True).order_by("-published_at")

    def location(self, obj: BlogPost):
        return f"/blog/{obj.slug}/"

    def lastmod(self, obj: BlogPost):
        return obj.updated_at


SITEMAPS = {
    "static": StaticSitemap,
    "posts": BlogPostSitemap,
}
