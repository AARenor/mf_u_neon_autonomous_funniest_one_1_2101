#!/usr/bin/env python3
"""Write the one-line make.fun entry with no trailing newline."""

import os
import sys
from pathlib import Path

TEXT = "Sorry I missed the deadline. I printed the approval button so you could sign it. It's beside the kettle."


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    output_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR", "/output")
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
