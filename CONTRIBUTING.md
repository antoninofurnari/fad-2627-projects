# Working in this repository

Conventions for keeping the project reviewable. They exist because the repository is
what gets marked — a good analysis in an unreadable repository loses marks it earned.

## 1. What must never be committed

**Data.** Not the raw file, not the cleaned one, not "just the small sample".
`.gitignore` already excludes `data/`, but check `git status` before every commit. A
dataset in the history cannot be removed by deleting the file later.

Instead, make the data reproducible: a `data/download.py` that fetches it, or a
paragraph in `data/README.md` saying exactly where it comes from and what to do with it.

**Large notebook outputs.** A notebook full of embedded images grows to tens of
megabytes, becomes impossible to review as a diff, and is slow to open. Either:

```bash
pip install nbstripout
nbstripout --install          # run once in the repository
```

which strips the outputs on every commit, or keep the notebook under **5 MB** by
limiting how many large figures you leave in it.

**Anything private**: credentials, API keys, personal data about identifiable people.

## 2. Notebooks

- The notebook must run **top to bottom after *Restart & Run All***, on a machine that
  has only `environment.yml` installed. This is checked.
- No cell may depend on a cell below it, or on something you ran once and deleted.
- Keep the cells in the order of the argument, not in the order you happened to write
  them.
- Fix the random seeds and say where you fixed them.
- Anything reused by both notebooks goes in `src/fadproj/`, imported — not
  copy-pasted.

## 3. Prose

`README.md` is technical: what this is, how to run it.
`docs/REPORT.md` is the argument: what you asked, what you found, what it means, what
you could not establish.

Write for a reader who knows the course but not your dataset.

## 4. Git for a group

- Commit often, with messages saying what changed and why.
- Work on branches and merge, or agree who touches which notebook when. Two people
  editing one notebook produces a conflict that is painful to resolve, because the file
  is JSON.
- **Say which version you are submitting.** A tag is the cleanest way —
  `git tag part1 && git push --tags` — and without one, what is marked is whatever is
  there on the deadline. If you are handing in a zip by e-mail instead, the zip *is* the
  version.
- Everyone commits under their own account. The history is the evidence for the
  contribution breakdown.

## 5. Structure

```
notebooks/     part1_analysis.ipynb, part2_modelling.ipynb
src/fadproj/   functions used by both notebooks
data/          the data (never committed) and how to obtain it
docs/          QUESTIONS.md, REPORT.md, slides.pdf
figures/       exported charts, if you need them outside the notebooks
```

Add directories if your project needs them. Do not rename the ones above.
