"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

A single-line roast of a smart fridge, written to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: no network,
no randomness, no clock.
"""

import os

# The entry: one line, 140 characters, aimed at the firmware-update
# terms-and-conditions shakedown.
ENTRY_TEXT = (
    "My smart fridge updated its firmware at 3 a.m. and now it won't open "
    "until I accept the new terms \u2014 my leftovers are held hostage by a EULA."
)

def write_entry(output_dir):
    """Write ENTRY_TEXT to entry.txt inside output_dir; return the path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    return path


if __name__ == "__main__":
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir)
    print(ENTRY_TEXT)
