#!/usr/bin/env python3
"""Write one line, a single joke about office life, to /output/entry.txt.

The line is written exactly as given: 95 Unicode code points,
inside the competition gate of 1-200.
Python 3, standard library only, no network.
"""

import os

TEXT = "I need a meeting to find time for the work from the last meeting about the meeting before that."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
