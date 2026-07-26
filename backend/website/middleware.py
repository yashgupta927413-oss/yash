"""Custom middleware for theyashgupta.com."""

from django.http import HttpResponsePermanentRedirect


class WwwRedirectMiddleware:
    """301 www.theyashgupta.com → theyashgupta.com.

    Both hosts serve identical content otherwise, which splits link equity and
    creates duplicate-content ambiguity for search engines. Must sit at the top
    of MIDDLEWARE so it fires before WhiteNoise serves static files.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().partition(":")[0]
        if host.startswith("www."):
            return HttpResponsePermanentRedirect(
                f"https://{host[4:]}{request.get_full_path()}"
            )
        return self.get_response(request)
