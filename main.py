"""One-line roast of a smart home gadget.

Writes the chosen roast line to entry.txt in the output directory, with no
trailing newline. Standard library only.
"""

import os

ROAST = (
    "My doorbell camera has seen me in my pyjamas more often than my own "
    "mother has \u2014 and unlike her, it keeps the footage."
)


def _output_dir():
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR", "ENTRY_OUTPUT"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output"


def main():
    line = ROAST
    if not 1 <= len(line) <= 160:
        raise ValueError(
            "roast line must be 1-160 characters, got %d" % len(line)
        )
    if line != line.strip() or "\n" in line:
        raise ValueError("roast line must be a single line with no padding")
    out_dir = _output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
