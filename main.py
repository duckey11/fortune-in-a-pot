#!/usr/bin/env python3
"""Fortune in a Pot: write one kind, funny fortune for a windowsill houseplant.

The fortune is a single fixed line of 110 characters, under the 120-character
limit, so the output is identical on every run (fully deterministic).
"""

import os

FORTUNE = (
    "The morning light on your windowsill has chosen you: "
    "a new leaf is on its way, and it will be your finest yet."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
