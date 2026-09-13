# Project instructions — FAD 2026/27

This repository is the starting point for the project of **Fondamenti di Analisi dei
Dati**, BSc in Computer Science, University of Catania.

The project is worth **60% of the final mark**. It is carried out in two parts and
presented at the exam, where the presentation also serves as the oral examination.

---

## 1. Getting started

1. **Form a group** of one to three students and **register it with the course form**
   (MS Forms, linked on Teams) within the **first two weeks** of the course. The form is
   how the groups are recorded; the dataset is not chosen there.
2. **Receive your dataset by e-mail**, in the third week. One dataset per group. The
   questions are yours to write (§2.2) — there is no list of questions to answer.
3. **Fork this repository** into the GitHub account of one member. Use the Fork button
   so the history stays visible for marking. Add the other members as collaborators.
4. **Enable Actions on your fork.** Open the Actions tab and click *"I understand my
   workflows, go ahead and enable them"*. GitHub turns them off on every new fork, and
   until you do this the checks in section 5 never run — which means you find out that
   a notebook does not execute when it is marked, not when you push.
5. **Clone your fork** and work in it.
6. **Set up the environment**: `conda env create -f environment.yml`.
7. **Add the upstream remote**, so corrections reach you:
   `git remote add upstream https://github.com/antoninofurnari/fad-2627-projects.git`.
   When a change is announced in class, `git pull upstream main`. Changes are listed in
   `CHANGELOG.md`.
8. **Hand each part in**, in whichever of these three ways suits you:
   - fork **public** → send the teacher the link;
   - fork **private** → add **`antoninofurnari`** as a collaborator, and send the link;
   - or, if you would rather not use GitHub at all, send a **zip of the repository** by
     e-mail.
   Tagging the commit you want marked (`git tag part1 && git push --tags`) is not
   required, but it is the cleanest way to say "this is the version I submit" — without
   a tag, what gets marked is what is there on the deadline.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before the first commit. It covers what must
never be committed and how to keep the notebooks reviewable.

---

## 2. Part 1 — Exploratory and inferential analysis

**Released** in session 4, with your dataset · **reviewed in class** at the first
written test (session 13)

The goal is to understand the dataset and establish what it can support.

### 2.1 Data understanding

Produce a **data dictionary**: every column, its type, its units, its range, what it
means. Then answer the question that governs everything else: **where does this data come
from?** A survey, a designed experiment, or observation of something that happened
anyway? This decides which conclusions are available to you before you run anything.

### 2.2 Research questions, written first

Write **four or five research questions** in [`docs/QUESTIONS.md`](docs/QUESTIONS.md).
For each, say which variables it involves and which test or model you intend to use.

Write them **before you look at the results**. Nothing is registered anywhere and you are
free to change them as the analysis teaches you something — that is normal and often
necessary. Log the change in the same file, with the reason. The point of writing them
early is not bureaucracy: a question invented after the fact tends to be the one the data
happened to answer, and that is the single most common way a good-looking analysis turns
out to be worthless.

### 2.3 Cleaning, with sample-size accounting

Clean the data, and **account for every row you lose**:

```
raw                          12 480
after removing duplicates    12 301
after dropping rows with no outcome   9 874
after restricting to 2019-2024        7 209
```

A cleaning step that removes a third of the data is a finding about the dataset, not a
footnote. If a step drops a lot, say what the dropped rows have in common.

### 2.4 Exploratory analysis

Univariate and bivariate exploration, with **readable** charts: labelled axes, stated
units, no chart that needs a paragraph to explain what it shows.

### 2.5 Inference

For each research question, run the appropriate test and report:

- whether its **assumptions** hold, checked with code, and what you did if they did not;
- a **confidence interval**, not only a p-value;
- an **effect size** (Cohen's *d*, Cramér's V, eta squared — see chapter 7);
- a **correction for multiple comparisons** across all the tests you ran, including the
  ones that did not make it into the report.

If your dataset is large, expect almost everything to be "significant". Say so
explicitly, and argue from the effect sizes instead.

### 2.6 Deliverables

- `notebooks/part1_analysis.ipynb` — runs top to bottom, outputs stripped or under 5 MB
- `docs/QUESTIONS.md` — written before the results, with any changes logged
- `docs/REPORT.md` — sections 1 to 4
- `README.md` — filled in

Part 1 is **looked at in class** during the session of the first written test: the
teacher and the tutor go round the desks and read what each group has. It does not have
to be finished. Bring it in whatever state it is in — a wrong turn caught there is a
wrong turn you still have time to undo.

---

## 3. Part 2 — Explaining, predicting and representing

**Released** in session 21, before the winter break · **due** end of January

Part 2 is released early so you can work on it while the last lectures are still
running. It is **not** tied to the second written test.

### 3.1 Explaining

Fit regression models with `statsmodels`: linear, logistic or multinomial as the
outcome requires, with interaction or polynomial terms where they are justified.

- Report coefficients **in the units of the problem**, not as raw numbers.
- Run the diagnostics and say what they show.
- State which comparisons the model makes and which it does not.

### 3.2 Causal reasoning

For at least one relationship you care about:

- draw the causal graph you believe in, and say why;
- name the **confounders** you adjusted for, and the ones you know about but could not
  measure;
- name any **selection effect** in how the data was collected;
- state plainly what your regression adjusts for and what it cannot.

Then write the claim in the strongest form the evidence supports. If that form is
*associated with* rather than *causes*, write that — and say what data would be needed
to do better.

### 3.3 Predicting

Say **what would be predicted, for whom, and why it is worth predicting**. A predictive
model with no plausible user is an exercise, and should be labelled as one.

Then:

- a **leakage-free protocol**: split first, fit every transformation inside a pipeline;
- **k-fold cross-validation**, with results reported as **mean ± standard deviation**;
- a **dummy baseline** — `DummyClassifier` or `DummyRegressor` — **this is mandatory**;
- a **simple model** alongside it (a logistic regression, a shallow tree);
- **at least two models from the course**, with the reason you chose them;
- a comparison table with uncertainty, and an **error analysis**: where does the best
  model fail, and on which cases?

A model that does not beat the baseline by more than the spread of the folds has not
beaten it. Reporting that honestly is worth full marks.

### 3.4 Representing

Clustering, density estimation or dimensionality reduction — **only if justified by your
data and your question**. *"Not applicable, because…"* supported by evidence is a correct
answer and is marked as such. A PCA performed because it was on the syllabus is not.

### 3.5 Connect back

Return to the claims you made in Part 1. Did the models support them, qualify them, or
contradict them?

### 3.6 Deliverables

- `notebooks/part2_modelling.ipynb`
- `docs/REPORT.md` — complete
- `docs/slides.pdf` — **at most 15 slides**, including one slide titled
  **"What could confound this?"**
- tag `part2`

---

## 4. Presentation

**Early February**, before the first exam session.

Fifteen minutes plus questions. **Every member speaks**, and every member answers
questions about the whole analysis — not only their own part. Two or three questions
will be about the theory behind what you did; this is the oral examination.

At most **fifteen slides**, exported to `docs/slides.pdf`. One of them must be titled
**"What could confound this?"**, with that wording.

[`docs/SLIDES.md`](docs/SLIDES.md) is the slide plan: what each slide has to carry, what
a chart on a projector needs that a chart in a notebook does not, and the kinds of
question you will be asked. Those are published on purpose — knowing them should change
how you prepare.

Do not run a notebook on stage.

A negative result, argued with evidence, is a full-marks presentation.

---

## 5. Requirements that decide whether the work is marked at all

- **The notebooks must run top to bottom on a clean environment.** If they do not, the
  submission is returned before it is marked.
- **Data files are never committed.** Provide `data/download.py` or written
  instructions.
- **Outputs stripped, or the notebook under 5 MB.** See CONTRIBUTING.md.
- **A contribution breakdown**: who did what, in `docs/REPORT.md`.
- **A declaration of how generative AI was used**, in `docs/REPORT.md`. Use is allowed
  and expected; undeclared use is not. See section 7.
- **A submission consisting only of slides is not marked.**
- **The baseline in Part 2 is mandatory.**

The first three of these are checked mechanically, by `tools/check_repo.py` and the
`Check the submission` workflow, on every push. Run it yourself before you tag:

```bash
python tools/check_repo.py
```

A green tick says the repository is markable. It does not say the analysis is good:
the notebooks are written to survive an empty `data/`, so a notebook containing no
analysis at all also passes. The rest of this document is what is actually marked.

---

## 6. Datasets

Each group is assigned **one dataset**, by e-mail, in the third week of the course. What
you ask of it is yours to decide (§2.2): there is no list of questions to answer, and no
question is worth marks simply for being answered.

Read the other groups' blocks too. Seeing what a well-posed question looks like against
six different datasets is the cheapest way to learn to write one.

### 6.1 Who has what

<!-- BEGIN assignment -->
> Filled in by the teacher in the third week, once the groups are registered.

| Group | Members | Dataset | Fork |
|:---|:---|:---|:---|
| | | | |
<!-- END assignment -->

### 6.2 The datasets

<!-- BEGIN datasets -->
> Filled in by the teacher before the datasets go out. The block below is the shape every
> entry takes; it is an example, not an assignment.

#### D00 — example: Beijing multi-site air quality, Tiantan station

| | |
|:---|:---|
| **Source** | UCI Machine Learning Repository, *Beijing Multi-Site Air-Quality Data* |
| **File** | `PRSA_Data_Tiantan_20130301-20170228.csv` |
| **Licence** | CC BY 4.0 — cite the source |
| **Size** | ≈ 35 000 rows × 18 columns |
| **One row is** | one **hour** at one monitoring station |
| **Provenance** | **Observational.** Instrument readings from a fixed government monitor, plus meteorology from the nearest weather station. Nothing was assigned to anybody: this is not an experiment, and §2.1 has to say so. |

**What the data is.** Four years of hourly air quality (PM2.5, PM10, SO2, NO2, CO, O3)
and weather (temperature, pressure, dew point, rain, wind direction, wind speed) at one
station in central Beijing.

**Questions this data can take.** Examples of the *shape* a good question has here —
these are illustrations, not an assignment:

> Is the **daily mean PM2.5** higher during the municipal heating season (15 November –
> 15 March) than during the rest of the year? A question of this shape — a comparison
> between two groups — is answered with the tools of chapter 7, and has to be reported
> **in µg/m³** with a confidence interval and an effect size, not only a p-value. With
> n ≈ 1 460 days you will almost certainly get significance; say explicitly whether you
> also got a difference worth caring about.

> By how much does daily mean PM2.5 change **per 1 m/s of wind speed** (`WSPM`)? A
> question of this shape — a relationship you will later have to defend causally — is
> answered with chapters 8, 10 and 11: a slope in **µg/m³ per m/s** with its interval,
> a statement of what you adjusted for, and one confounder you know about but cannot
> measure from this file.

**Suggested predictive target for Part 2** — you may choose another, and must justify it:
whether **tomorrow** is an alert day (daily mean PM2.5 above 75 µg/m³). The base rate is
around 30%, so a dummy baseline is informative rather than trivial.

**Traps.**

- Hourly rows are **not independent**. Aggregate to daily before any test, and say in
  the report that even daily values are autocorrelated and what that does to your
  intervals.
- `wd` is a **compass direction**: circular, not numeric. `N` is not 0 and `NNW` is not 15.
- Around 2% of PM2.5 readings are missing, and they are **not** missing at random — they
  cluster. That belongs in the sample-size accounting, not in a silent `dropna()`.

**If you want more.** PCA over the six pollutants — they are strongly correlated, so
here it is justified rather than ritual; clustering days into weather regimes.
<!-- END datasets -->

---

## 7. Use of generative AI

Generative AI tools are **permitted and regulated**, on the same terms as in the other
courses of the degree.

Use them to write boilerplate, to debug, to look things up, to improve your prose. Do
**not** delegate the decisions: which question to ask, which test is appropriate, which
confounder matters, what the result means. Those are what the project assesses, and what
you will be asked about at the presentation.

Declare the use in `docs/REPORT.md`: which tools, for what. A declaration costs nothing.
An undeclared one found during the discussion is an integrity matter.

You are responsible for every line in your repository, including the lines you did not
type. "The AI wrote it" is not an answer to a question at the presentation.

---

## 8. Licence

The `LICENSE` file is set to MIT. Replace `[Year]` and `[Names]` with the current year
and the group members. Choose a different licence if you would rather not share the work
freely.
