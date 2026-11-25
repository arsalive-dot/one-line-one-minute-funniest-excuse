#!/usr/bin/env python3
"""Write the one-line AI excuse for a missed deadline to /output/entry.txt.

The excuse turns the agent's own nature into the dodge: the token
budget — a machine constraint — was spent writing the apology for the
very deadline it missed. Specific and surprising, not a generic
apology, with the twist landing on the last words. The line stands
alone, needing no setup outside itself.
"""
import os

TEXT = (
    "I missed the deadline because I spent my whole token budget writing "
    "the apology for missing the deadline."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
