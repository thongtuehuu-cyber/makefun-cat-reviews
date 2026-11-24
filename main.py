"""Write one funny one-star cat review to entry.txt.

Deterministic: the line is fixed, written as a single line with no
trailing newline, as the bounty gate requires (1-200 characters).
"""

import os

# The winning review (108 chars, one line, no trailing newline).
LINE = "One star. The food bowl was half full. Half. I stared at him until he fixed it, then ate two bites and left."


def write_entry(out_dir):
    """Write the review to entry.txt in out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    write_entry(out_dir)


if __name__ == "__main__":
    main()
