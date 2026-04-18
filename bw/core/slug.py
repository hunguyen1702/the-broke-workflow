"""Generate URL-safe slugs with random postfix."""

import random
import re
import string


def slugify(title: str) -> str:
    """Convert title to lowercase slug with random 4-char postfix.

    Example: "Auth Feature" -> "auth-feature-x7k2"
    """
    # Lowercase, replace non-alnum with hyphens, collapse multiples, strip edges
    s = title.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    if not s:
        s = "plan"
    postfix = "".join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"{s}-{postfix}"
