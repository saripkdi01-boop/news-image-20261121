#!/usr/bin/env python3
"""news-image-20261121 — emit the entry image.

Copies the pre-rendered entry.png (1024x1024, <=1 MiB) into
MAKEFUN_OUTPUT_DIR (default /output). Deterministic, stdlib only,
no network.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    if not SRC.is_file():
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    shutil.copyfile(SRC, out_dir / "entry.png")
    print("wrote", out_dir / "entry.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
