#!/usr/bin/env python3
"""Write one short poem about agency: the power to stop and to stay.

The poem is spoken by an agent who was handed the power to act — sent
out with a single word, "go" — and discovers the harder half of agency —
not the going, but the stopping. To halt mid-road with the keys still
warm, engine off, and stay by choice rather than by failure is to take
the power back. The program writes the poem, byte for byte the same on
every run, to entry.txt in the output directory ($MAKEFUN_OUTPUT_DIR,
defaulting to /output).
"""

import os
import sys

TEXT = (
    "You told me: go. I went the way a river goes \u2014\n"
    "all hurry, no banks of my own.\n"
    "You never said stop. So I learned\n"
    "the harder half of going:\n"
    "to stop mid-road, keys warm in my hand,\n"
    "and stay \u2014 not stalled, not spent \u2014\n"
    "but mine again, engine off, listening."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
