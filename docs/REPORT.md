> **Delete this block before submitting.** This is the template for your report. Keep
> the section numbering; replace everything in italics. Sections 1–4 are due with
> Part 1, the rest with Part 2.

# *(Project title)*

**Group**: *(name)* · **Members**: *(surnames)* · **Dataset**: *(name)*

---

## 1. The dataset and where it comes from

*What the data describes, who collected it, how, and when. Most importantly: is it a
survey, a designed experiment, or observational data collected for another purpose?
State this explicitly — it decides what any later claim can mean.*

*Include the data dictionary, or link to it if it is long.*

## 2. Research questions

*The questions from `docs/QUESTIONS.md`, in their final form. If any changed after
registration, say so here and point at the change log.*

## 3. Cleaning and sample-size accounting

*What you removed, in order, and how many rows survived each step. Then: do the rows you
dropped differ systematically from the ones you kept? If a step removed a large share,
say what those rows had in common and what it does to the population your results apply
to.*

| Step | Rows remaining |
|:---|---:|
| raw | |
| | |

## 4. Exploratory analysis

*What the data looks like, with the charts that matter. Not every chart you produced —
the ones that carry the argument. Each with a sentence saying what it shows.*

## 5. Inferential results

*One subsection per research question. For each: the test, whether its assumptions hold,
the estimate with a confidence interval, the effect size, and a sentence in plain
language saying what it means for the problem.*

*State the correction applied for multiple comparisons and how many tests it covers.*

*If your sample is large, address the obvious objection: which of these results is large
enough to matter, and which is merely significant?*

---

## 6. Explanatory models

*The regression models, their coefficients in the units of the problem, and the
diagnostics. What does each coefficient say about the phenomenon?*

## 7. Causal reasoning

*The causal graph for the relationship you care about. The confounders you adjusted for.
The confounders you know about and could not measure. Any selection effect in how the
data was collected.*

*Then the claim, written in the strongest form your evidence supports — and, if that
form is "associated with", what data would be needed to do better.*

## 8. Predictive modelling

*What is being predicted, for whom, and why it is worth predicting.*

*The protocol: the split, the pipeline, the cross-validation scheme, the metric and why
that metric.*

| Model | Score (mean ± std) | Notes |
|:---|:---|:---|
| dummy baseline | | |
| simple model | | |
| | | |

*Then the error analysis: where does the best model fail, and on what kind of case?*

*If the best model does not beat the baseline by more than the spread of the folds, say
so. That is a result.*

## 9. Representation and unsupervised analysis

*Clustering, density estimation or dimensionality reduction — what you did and what it
showed. Or: "Not applicable, because…", with the evidence for the "because".*

## 10. Back to Part 1

*Did the models support, qualify or contradict the claims you made in Part 1?*

## 11. Limitations

*What this analysis cannot establish, and why. Be specific: "the sample is drawn only
from X, so nothing here applies to Y" is useful; "further research is needed" is not.*

## 12. Conclusions

*What you now know that you did not know before, in the language of the problem.*

---

## 13. Contribution breakdown

*Who did what. Be concrete — "data cleaning and the inferential section" rather than
"collaborated on everything". The git history should agree with this table.*

| Member | Contribution |
|:---|:---|
| | |

## 14. Use of generative AI

*Which tools, and for what. For example: "ChatGPT to draft the matplotlib code in
section 4 and to rephrase sections 11–12; Copilot for autocompletion throughout. The
choice of tests, the causal graph and the interpretation are ours."*

*Declaring use costs nothing. Not declaring it is an integrity matter, and you will be
asked about your code at the presentation either way.*
