#!/usr/bin/env python3
"""Fetch this project's dataset into `data/`.

Reproducibility starts here: anyone who clones the repository must be able to obtain
exactly the data you analysed, without asking you for it. The dataset itself is never
committed — this script is what stands in for it.

Fill in the three constants from your dataset's block in section 6 of `INSTRUCTIONS.md`.

    python data/download.py            # fetch if missing
    python data/download.py --check    # verify what is already there, fetch nothing
    python data/download.py --force    # fetch again even if the file is present

If your dataset needs credentials, or arrives as several files, or has to be assembled
from an API, write that here too and say so in `docs/REPORT.md`. The rule is not "one
urlopen call", it is "a reader can reproduce your data/ folder from this repository".
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import urllib.request
from pathlib import Path

# ----------------------------------------------------------------- fill these in
SOURCE = "https://example.org/replace-me.csv"   # from your section 6 block
TARGET = Path(__file__).parent / "your_dataset.csv"
SHA256 = ""          # from your section 6 block; leave "" only until you know it
# --------------------------------------------------------------------------------


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify(path: Path) -> bool:
    if not path.exists():
        print(f"missing: {path.name}")
        return False
    got = digest(path)
    if not SHA256:
        print(f"{path.name}: {path.stat().st_size:,} bytes, sha256 {got}")
        print("  (no SHA256 recorded yet — paste the value above into this file)")
        return True
    if got != SHA256:
        print(f"{path.name}: CHECKSUM MISMATCH\n  expected {SHA256}\n  got      {got}")
        return False
    print(f"{path.name}: {path.stat().st_size:,} bytes, checksum matches")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify only, download nothing")
    parser.add_argument("--force", action="store_true", help="download even if present")
    args = parser.parse_args()

    if args.check:
        return 0 if verify(TARGET) else 1
    if TARGET.exists() and not args.force:
        return 0 if verify(TARGET) else 1

    print(f"downloading {SOURCE}")
    try:
        urllib.request.urlretrieve(SOURCE, TARGET)
    except OSError as exc:
        print(f"could not download: {exc}", file=sys.stderr)
        return 1
    return 0 if verify(TARGET) else 1


if __name__ == "__main__":
    raise SystemExit(main())
