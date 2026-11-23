#!/usr/bin/env python3
"""The One-Line Laugh.

Writes a single original funny line (1-200 chars, UTF-8) to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "My plants died even though I bought them a self-watering pot, "
    "which turns out just means they drown on a schedule."
)


def _validate(text: str) -> None:
    """Gate: the entry must be a single non-blank line of 1-200 UTF-8 chars."""
    assert isinstance(text, str)
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    encoded = text.encode("utf-8")  # raises if not encodable as UTF-8
    assert encoded.decode("utf-8") == text, "entry is not valid UTF-8 round-trip"
    assert text == text.strip(), "entry must not start or end with whitespace"


def main() -> None:
    _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Verify the written file round-trips exactly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written file does not match entry"
    print(
        f"Wrote {len(ENTRY)}-character "
        f"({len(ENTRY.encode('utf-8'))}-byte) entry to {path}"
    )


if __name__ == "__main__":
    main()
