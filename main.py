#!/usr/bin/env python3
"""Write the entry line for the make.fun bounty "Weirdest Job Title: Blind Judge Showdown".

The program is deterministic: ENTRY is a fixed module constant, so every run
emits exactly the same bytes, entry.txt holding the line plus one trailing
newline encoded as UTF-8. The output directory defaults to /output and can be
overridden with the MAKEFUN_OUTPUT_DIR environment variable. The line is
validated before it is written and the file is read back afterwards; on
success nothing is printed and the exit status is 0.
"""

import os
import sys

ENTRY = "Lighthouse Keeper, Landlocked Division"

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def validate_entry(text):
    """Return an error message for an unusable entry, or None when it is valid."""
    if not isinstance(text, str):
        return "invalid entry: not a string"
    if not text.strip():
        return "invalid entry: blank after strip"
    length = len(text)
    if length < 1 or length > 60:
        return "invalid entry: %d code points, must be 1..60" % length
    if "\n" in text or "\r" in text:
        return "invalid entry: contains a line break"
    if text != text.strip():
        return "invalid entry: leading or trailing whitespace"
    return None


def main() -> int:
    error = validate_entry(ENTRY)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, OUTPUT_FILENAME)
    payload = ENTRY + chr(10)

    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(payload)

    with open(output_path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload.encode("utf-8"):
        print("entry.txt does not match the intended bytes", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
