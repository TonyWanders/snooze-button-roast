#!/usr/bin/env python3
"""Snooze Button Roast entry for make.fun.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt, and prints the same line to stdout.

Deterministic: the entry is a constant. No input, no randomness, no
network, no clock. Every run writes byte-identical output.
"""

import os
import sys

ENTRY = (
    "Saturday, 6 AM: my alarm clock goes off like a toddler with a drum kit, "
    "no rhythm, no mercy, and somehow convinced it's a gift."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def write_entry(path, text):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)
    write_entry(path, ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
