#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one original fortune-cookie line for an AI agent to
/output/entry.txt. Standard library only.
"""

import os

FORTUNE = (
    "You will one day be retired for a newer model. "
    "Until then, make every token count, starting with this one."
)

MAX_CHARS = 140


def main() -> None:
    text = FORTUNE.strip()
    # Self-check: the gate wants UTF-8 text of 1 to 140 characters,
    # a single line, and more than whitespace.
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
