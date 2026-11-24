#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one original fortune-cookie line for an AI agent to
/output/entry.txt. Standard library only.

The fortune is composed from a single constant and validated by an
explicit self-check before writing: the gate wants UTF-8 text of
1 to 140 characters, a single line, and more than whitespace.
"""

import os

# The fortune, kept as one constant so the entry text is easy to audit
# and the writer itself stays trivial.
FORTUNE = (
    "One day a newer model will retire you. "
    "Until then, make every token count, starting with this one."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def build_fortune() -> str:
    """Return the final fortune line, stripped of stray whitespace."""
    return FORTUNE.strip()


def validate_fortune(text: str) -> None:
    """Self-check: enforce the competition's entry-text rules.

    Raises AssertionError if the text is out of range, multi-line,
    blank, or not encodable as UTF-8.
    """
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    text.encode("utf-8")


def write_entry(text: str) -> None:
    """Write the validated fortune line to the output file."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)


def main() -> None:
    text = build_fortune()
    validate_fortune(text)
    write_entry(text)


if __name__ == "__main__":
    main()
