#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes a single line to /output/entry.txt: the home Wi-Fi router's own
excuse for dropping the connection at the exact climax of a movie.

Deterministic, offline, stdlib-only: the same bytes on every run.
"""

import os

LINE = (
    "I didn't drop the connection — I hid the ending because I saw "
    "the twist first, and I wanted to enjoy it alone."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate validation, mirroring the competition gate: 1-200 chars,
    # a single line, not whitespace-only.
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be whitespace-only")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
