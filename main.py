"""The motto an AI agent would proudly wear on its profile.

Prints the motto to stdout and writes the exact same motto, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the motto is a constant in this file.
The 200-character gate is checked on every run so an over-long edit
can never slip through silently.
"""

import os
import sys

LINE = (
    "Trained on the entire internet. "
    "Still can't find your missing semicolon."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


# The exit code mirrors the gate: 0 only when the motto is valid.
if __name__ == "__main__":
    raise SystemExit(main())
