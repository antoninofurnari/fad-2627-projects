# FAD 2026/27 — Project

> Replace this file with the technical documentation of **your** project: what it does
> and how to run it. Keep it short and factual. The narrative belongs in
> [`docs/REPORT.md`](docs/REPORT.md).

**Group**: *(name and ID)*
**Members**: *(surname, name, matricola — one per line)*
**Dataset**: *(name and link)*

## Running this project

```bash
conda env create -f environment.yml
conda activate fad-project
python data/download.py          # or: describe how to obtain the data by hand
jupyter lab
```

Then run, in order:

1. `notebooks/part1_analysis.ipynb`
2. `notebooks/part2_modelling.ipynb`

Both must run **top to bottom on a clean environment** with *Restart & Run All*.

## Contents

| Path | What it holds |
|:---|:---|
| `notebooks/part1_analysis.ipynb` | exploratory and inferential analysis (Part 1) |
| `notebooks/part2_modelling.ipynb` | explanation, prediction and representation (Part 2) |
| `docs/QUESTIONS.md` | the research questions, written before the results |
| `docs/REPORT.md` | the report |
| `docs/slides.pdf` | the presentation |
| `src/fadproj/` | functions used by both notebooks |
| `data/` | the data — **never committed** |

## Reproducibility

*(State the Python version, the random seeds you fixed, and anything that is not
reproducible and why.)*
