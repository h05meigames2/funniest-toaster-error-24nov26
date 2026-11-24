#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (<=120 chars) to /output/entry.txt: the error message
a kitchen toaster shows its owner when the bread refuses to cooperate.
"""

import os

ENTRY = "TOASTING ABORTED: YOUR BREAD HAS UNIONISED AND DEMANDS BUTTER UP FRONT."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
