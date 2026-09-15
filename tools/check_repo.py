#!/usr/bin/env python3
"""Check the things `README.md` says decide whether the work is marked at all.

Run it yourself before you tag a submission:

    python tools/check_repo.py

It is also what the `Check the submission` workflow runs on every push, so a red tick on
your fork means one of these failed. Nothing here is a judgement about your analysis —
this only checks the rules that would otherwise have the work handed back unread.

**Fails** on data committed to the repository, a notebook above 5 MB, an absolute path
inside a notebook, or oversized figures. **Warns** on placeholders left unfilled. It
never inspects your results, never runs `data/download.py`, and needs no credentials: a
fresh fork with an empty `data/` must pass.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DATA_SUFFIXES = {".csv", ".tsv", ".xlsx", ".xls", ".parquet", ".zip", ".db",
                 ".sqlite", ".json.gz", ".pkl", ".feather"}
DATA_ALLOWED = {"README.md", ".gitignore", "download.py"}
NOTEBOOK_MAX = 5 * 1024 * 1024
FIGURE_MAX = 1 * 1024 * 1024
FIGURES_TOTAL_MAX = 10 * 1024 * 1024
# Paths that only exist on the machine they were written on. The 2025/26 submissions
# were full of the first one.
ABSOLUTE_HINTS = ("/content/drive", "/content/", "C:\\\\", "C:/Users", "/Users/", "/home/")


def tracked() -> list[Path]:
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files"],
                         capture_output=True, text=True)
    if out.returncode:                      # not a git checkout: fall back to the tree
        return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
    return [ROOT / line for line in out.stdout.splitlines() if line]


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []
    files = tracked()

    for path in files:
        try:
            rel = path.relative_to(ROOT)
        except ValueError:
            continue

        if rel.parts and rel.parts[0] == "data" and path.name not in DATA_ALLOWED:
            failures.append(f"{rel}: data must not be committed")

        if path.suffix.lower() in DATA_SUFFIXES and rel.parts[0] != "docs":
            failures.append(f"{rel}: a data file is committed; say in data/README.md how to obtain it")

        if path.suffix == ".ipynb" and path.exists():
            size = path.stat().st_size
            if size > NOTEBOOK_MAX:
                failures.append(f"{rel}: {size/1e6:.1f} MB — strip the outputs "
                                f"(nbstripout) or shrink the figures; the limit is 5 MB")
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                text = ""
            for hint in ABSOLUTE_HINTS:
                if hint in text:
                    failures.append(f"{rel}: contains the absolute path {hint!r} — "
                                    f"nobody else can run that cell")
                    break

        # figures/ is optional now — the notebook carries its own charts — but if a
        # group exports them, the size cap still applies.
        if rel.parts and rel.parts[0] == "figures" and path.exists():
            if path.stat().st_size > FIGURE_MAX:
                failures.append(f"{rel}: {path.stat().st_size/1e6:.1f} MB — export the "
                                f"chart smaller; the limit is 1 MB per figure")

    figures = ROOT / "figures"
    if figures.is_dir():
        total = sum(f.stat().st_size for f in figures.rglob("*") if f.is_file())
        if total > FIGURES_TOTAL_MAX:
            failures.append(f"figures/: {total/1e6:.1f} MB in total; the limit is 10 MB")

    licence = ROOT / "LICENSE"
    if licence.exists() and "[Group members]" in licence.read_text(encoding="utf-8"):
        warnings.append("LICENSE: still says [Group members]")
    readme = ROOT / "README.md"
    if readme.exists() and "*(name and ID)*" in readme.read_text(encoding="utf-8"):
        warnings.append("README.md: the group placeholders are still there")

    for nb in sorted((ROOT / "notebooks").glob("*.ipynb")):
        try:
            doc = json.loads(nb.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            failures.append(f"notebooks/{nb.name}: not valid JSON — is it corrupted?")
            continue
        if not doc.get("cells"):
            failures.append(f"notebooks/{nb.name}: has no cells")

    for line in warnings:
        print(f"WARN  {line}")
    for line in failures:
        print(f"FAIL  {line}")

    if failures:
        print(f"\ncheck_repo: {len(failures)} failure(s), {len(warnings)} warning(s)")
        return 1
    print(f"\ncheck_repo: PASS ({len(files)} tracked files, {len(warnings)} warning(s))")
    print("This says the repository is markable, not that the analysis is good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
