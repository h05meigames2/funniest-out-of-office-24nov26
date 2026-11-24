#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun bounty entry.

Writes one original out-of-office auto-reply line (max 140 characters,
single line) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only, no network access.
"""

import os
import sys

LINE = "I'm out of office until Monday. My inbox is unsupervised and has already replied 'sounds good!' to a lawsuit."

MAX_CHARS = 140


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: entry line is {len(line)} characters, max is {MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} characters to {out_path}: {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
