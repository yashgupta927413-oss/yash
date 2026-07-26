from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import RedirectView

from website.feeds import BlogFeed
from website.sitemaps import SITEMAPS
from website.views import blog_list_page, blog_post_page, robots_txt, service_page

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
    path('sitemap.xml', sitemap, {'sitemaps': SITEMAPS}, name='sitemap'),
    path('robots.txt', robots_txt, name='robots-txt'),
]
