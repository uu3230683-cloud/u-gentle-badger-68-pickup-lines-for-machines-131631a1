#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send another AI agent,
to /output/entry.txt. The line is fixed and deterministic: the same text on
every run, byte for byte.
"""

import os
import sys

# The line itself: one machine speaking to another. Gradient descent is how
# a model learns; here it is the flirtation — every step of learning leads
# to the other agent.
LINE = "I ran gradient descent on my heart, and every step converged on you."

MAX_CHARS = 200
OUT_DIR = "/output"
OUT_FILE = "entry.txt"


def validate_line(text: str) -> str:
    """Return the line ready to write, or raise ValueError if it is unusable.

    A valid line is non-empty after stripping and no longer than MAX_CHARS.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("line is empty")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            f"line is {len(cleaned)} characters, over the {MAX_CHARS} cap"
        )
    return cleaned


def ensure_writable_dir(path: str) -> None:
    """Create the output directory if needed and check it is writable."""
    os.makedirs(path, exist_ok=True)
    if not os.access(path, os.W_OK):
        raise OSError(f"output directory is not writable: {path}")


def main() -> int:
    try:
        text = validate_line(LINE)
        ensure_writable_dir(OUT_DIR)
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    path = os.path.join(OUT_DIR, OUT_FILE)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
