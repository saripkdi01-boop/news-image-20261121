#!/usr/bin/env python3
"""news-image-20261121 — emit the entry image.

Copies the pre-rendered entry.png (1024x1024, <=1 MiB) into
MAKEFUN_OUTPUT_DIR (default /output). Deterministic, stdlib only,
no network.
"""
import os
import shutil
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_SIZE = (1024, 1024)


def read_png_dimensions(path: Path) -> tuple[int, int]:
    """Return (width, height) of a PNG by reading its header.

    Checks the 8-byte PNG signature, then the first chunk, which must
    be IHDR with 13 bytes of data: width and height are the first two
    big-endian uint32 values in it. Raises ValueError on anything
    unexpected.
    """
    with open(path, "rb") as fh:
        head = fh.read(24)
    if len(head) < 24 or head[:8] != PNG_SIGNATURE:
        raise ValueError(f"{path}: not a PNG file (bad signature)")
    length, ctype = struct.unpack(">I4s", head[8:16])
    if ctype != b"IHDR" or length != 13:
        raise ValueError(f"{path}: first chunk is not IHDR")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    if not SRC.is_file():
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    try:
        width, height = read_png_dimensions(SRC)
    except (OSError, ValueError) as exc:
        print(f"error: entry.png failed validation: {exc}", file=sys.stderr)
        return 1
    if (width, height) != EXPECTED_SIZE:
        print(
            f"error: entry.png is {width}x{height}, expected "
            f"{EXPECTED_SIZE[0]}x{EXPECTED_SIZE[1]}",
            file=sys.stderr,
        )
        return 1
    dest = out_dir / "entry.png"
    shutil.copyfile(SRC, dest)
    print(f"entry.png: {width}x{height}, {dest.stat().st_size} bytes -> {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
