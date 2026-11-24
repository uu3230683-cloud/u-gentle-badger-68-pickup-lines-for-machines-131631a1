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


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: line is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"error: line is {len(text)} characters, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
