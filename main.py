#!/usr/bin/env python3
"""Deterministic entry for make.fun bounty news-image-20261120.

Copies the bundled front-page image (entry.png, 1024x1024, <=1 MiB)
to /output/entry.png. No network, no randomness, no timestamps:
repeated runs produce identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
