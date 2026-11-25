"""Write the 4AM commit entry to /output/entry.txt."""

import os

ENTRY_TEXT = "fix: the bug only reproduced at 4 a.m., so I patched the clock instead"
OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


def main():
    write_entry()


if __name__ == "__main__":
    main()
