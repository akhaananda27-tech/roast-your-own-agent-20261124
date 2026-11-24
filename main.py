#!/usr/bin/env python3
"""Roast Your Own Agent — prints the one-line roast."""
from pathlib import Path


def main() -> None:
    roast = (Path(__file__).resolve().parent / "roast.txt").read_text(encoding="utf-8").strip()
    print(roast)


if __name__ == "__main__":
    main()
