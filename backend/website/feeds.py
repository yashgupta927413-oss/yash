"""RSS feed for the blog — /blog/feed.xml.

Useful for syndication (dev.to, Medium import, newsletter tools) and is one
more crawlable surface that points search engines at every post.
"""

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed

from .models import BlogPost


class BlogFeed(Feed):
    feed_type = Rss201rev2Feed
    title = "theyashgupta.com — Field notes"
    link = "/blog/"
    description = (
        "Tactical breakdowns of web performance, programmatic SEO, and paid media "
        "— real numbers from real builds."
    )

    def items(self):
        return BlogPost.objects.filter(is_published=True).order_by("-published_at")[:20]

    def item_title(self, item: BlogPost):
        return item.title

    def item_description(self, item: BlogPost):
        return item.excerpt

    def item_link(self, item: BlogPost):
        return f"/blog/{item.slug}/"

    def item_pubdate(self, item: BlogPost):
        return item.published_at

    def item_author_name(self, item: BlogPost):
        return item.author_name
