"""Resolves Vite's content-hashed asset filenames for server-rendered templates.

The Vite build emits `/assets/index-<hash>.css` and `/assets/index-<hash>.js`.
The server-rendered pages (blog index, blog posts, service pages) used to
hard-code `/styles.css`, which has never existed in the build output — those
pages were served with the main stylesheet 404ing, so they rendered nearly
unstyled in production.

This reads Vite's manifest once per process and hands the real paths to the
templates. In local dev, where the Vite dev server serves `/styles.css`
directly and no manifest exists, it falls back to that path.
"""

import functools
import json
from pathlib import Path

from django.conf import settings

# Used when no build manifest is present (i.e. running against `vite dev`).
DEV_FALLBACK_CSS = ["/styles.css"]


@functools.lru_cache(maxsize=1)
def _manifest() -> dict:
    root = Path(getattr(settings, "WHITENOISE_ROOT", "") or "")
    if not root:
        return {}
    # Vite 5 writes to .vite/manifest.json; older versions used the root.
    for candidate in (root / ".vite" / "manifest.json", root / "manifest.json"):
        try:
            if candidate.is_file():
                return json.loads(candidate.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
    return {}


def _entry(manifest: dict) -> dict:
    if not manifest:
        return {}
    if "index.html" in manifest:
        return manifest["index.html"]
    return next((v for v in manifest.values() if v.get("isEntry")), {})


def vite_assets() -> dict:
    """Return {'vite_css': [...urls], 'vite_js': url|None} for templates."""
    entry = _entry(_manifest())
    css = [f"/{href}" for href in entry.get("css", [])]
    js = f"/{entry['file']}" if entry.get("file") else None
    return {"vite_css": css or DEV_FALLBACK_CSS, "vite_js": js}


def vite_context(request) -> dict:
    """Template context processor — makes vite_css / vite_js globally available."""
    return vite_assets()
