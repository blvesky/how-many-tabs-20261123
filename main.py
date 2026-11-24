#!/usr/bin/env python3
"""Entry writer for How Many Tabs Do You Have Open? (make.fun program/v1).

Writes the single entry number to /output/entry.txt (or to the path
given as the first argument, for local checks).
"""

import os
import sys

ENTRY = "247"


MAX_CHARS = 5


def render() -> bytes:
    """Encode the entry once, checking the gate limits before any write."""
    if not ENTRY.isdigit() or not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} digits, got {ENTRY!r}")
    return ENTRY.encode("utf-8")


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    tmp = out + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(render())
    os.replace(tmp, out)


if __name__ == "__main__":
    main()
