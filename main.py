#!/usr/bin/env python3
"""The One-Line Laugh.

Writes a single original funny line (1-200 chars, UTF-8) to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

MAX_CHARS = 200

ENTRY = (
    "My plants died even though I bought them a self-watering pot, "
    "which turns out just means they drown on a schedule."
)


def _validate(text: str) -> bytes:
    """Gate: the entry must be a single non-blank line of 1-200 UTF-8 chars.

    Returns the entry encoded as UTF-8 so the writer below uses exactly
    the bytes that were checked.
    """
    problems = []
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        problems.append("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry must be one line")
    if not 1 <= len(text) <= MAX_CHARS:
        problems.append(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if text != text.strip():
        problems.append("entry must not start or end with whitespace")
    if problems:
        raise ValueError("; ".join(problems))
    encoded = text.encode("utf-8")  # raises if not encodable as UTF-8
    if encoded.decode("utf-8") != text:
        raise ValueError("entry is not valid UTF-8 round-trip")
    return encoded


def main() -> None:
    encoded = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "wb") as f:
        f.write(encoded + b"\n")
    # Verify the written file round-trips exactly.
    with open(path, "rb") as f:
        written = f.read()
    assert written == encoded + b"\n", "written file does not match entry"
    print(
        f"Wrote {len(ENTRY)}-character "
        f"({len(encoded)}-byte) entry to {path}"
    )


if __name__ == "__main__":
    main()
