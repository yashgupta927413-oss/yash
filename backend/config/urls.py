from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import RedirectView

from website.feeds import BlogFeed
from website.sitemaps import SITEMAPS
from website.views import (
    blog_list_page,
    blog_post_page,
    legal_index,
    legal_page,
    robots_txt,
    service_page,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('website.urls')),
    # Shareable short URL for the subscription tiers. Kept as a 302 (not 301) so
    # a standalone /pricing/ page can replace it later without fighting browser
    # redirect caches. /pricing resolves here too via APPEND_SLASH.
    path('pricing/', RedirectView.as_view(url='/#plans', permanent=False), name='pricing-redirect'),
    path('blog/feed.xml', BlogFeed(), name='blog-feed'),
    path('blog/', blog_list_page, name='blog-list-page'),
    path('blog/<slug:slug>/', blog_post_page, name='blog-post-page'),
    path('services/<slug:slug>/', service_page, name='service-page'),
    # Real, crawlable legal pages. Meta Lead Ads fetches the privacy policy URL
    # and checks the document is present in the HTML — a JS modal doesn't pass.
    path('legal/', legal_index, name='legal-index'),
    path('legal/<slug:slug>/', legal_page, name='legal-page'),
    # Conventional short URLs people (and reviewers) type by hand.
    path('privacy/', RedirectView.as_view(url='/legal/privacy/', permanent=True)),
    path('terms/', RedirectView.as_view(url='/legal/terms/', permanent=True)),
    path('refund/', RedirectView.as_view(url='/legal/refund/', permanent=True)),
    path('sitemap.xml', sitemap, {'sitemaps': SITEMAPS}, name='sitemap'),
    path('robots.txt', robots_txt, name='robots-txt'),
]
