#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing today.

Writes a single line (<= 200 chars) to /output/entry.txt.
The line is fixed and deterministic: the same bytes every run.

Line chosen from 6 candidates by in-session pairwise judging against the
published brief (on-subject, warmth, surprise, concreteness, fresh wording);
the relay pairwise judge was unavailable (HTTP 400), so selection fell back
to in-session judging as the checklist directs.
"""

import os
from pathlib import Path

ENTRY = (
    'Today my three-year-old taught me her new word for rain \u2014 '
    '"sky juice" \u2014 and now I can\'t hear a downpour any other way.'
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
