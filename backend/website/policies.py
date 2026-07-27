"""Loads the policy documents shared by the modal and the /legal/ pages.

`frontend/public/policies.json` is the single source of truth — the same file
the on-page modal fetches — so the pages and the modal can never disagree.
Regenerate it with `python3 frontend/policies.build.py`.
"""

import functools
import json
from pathlib import Path
from typing import Optional

from django.conf import settings

# Order the index page and footer list them in — most-asked-for first.
POLICY_ORDER = [
    "terms",
    "privacy",
    "refund",
    "domain",
    "acceptable-use",
    "cookies",
    "disclaimer",
]

# One-line summaries for the /legal/ index; the documents themselves carry no
# short description and a wall of undifferentiated titles is hard to scan.
POLICY_BLURBS = {
    "terms": "How engagements work — scope, fees, ownership, liability, and termination.",
    "privacy": "What personal data we collect, why, how long we keep it, and your rights.",
    "refund": "Cancellation notice periods and what is refundable for each service.",
    "domain": "Who owns the domain, the website, and the data — during and after a plan.",
    "acceptable-use": "What may and may not be published on sites we host.",
    "cookies": "The cookies this site sets and how to control them.",
    "disclaimer": "Limits on performance claims and third-party platform outcomes.",
}


@functools.lru_cache(maxsize=1)
def _load() -> dict:
    """Read policies.json from the built frontend, falling back to the source tree."""
    candidates = []
    root = getattr(settings, "WHITENOISE_ROOT", "") or ""
    if root:
        candidates.append(Path(root) / "policies.json")
    # Local dev without a build: read straight from the frontend source.
    candidates.append(Path(settings.BASE_DIR).parent / "frontend" / "public" / "policies.json")

    for path in candidates:
        try:
            if path.is_file():
                return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
    return {}


def get_policy(slug: str) -> Optional[dict]:
    policy = _load().get(slug)
    if not policy:
        return None
    return {"slug": slug, **policy}


def all_policies() -> list[dict]:
    data = _load()
    ordered = [s for s in POLICY_ORDER if s in data]
    ordered += [s for s in data if s not in POLICY_ORDER]
    return [
        {"slug": s, "blurb": POLICY_BLURBS.get(s, ""), **data[s]}
        for s in ordered
    ]
