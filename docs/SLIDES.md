# Presentation — slide plan

Fill this in as you build the deck, then export to `docs/slides.pdf`. Fifteen slides at
most, fifteen minutes, plus questions. Every member speaks, and every member answers
questions about the **whole** analysis — not only their own part.

A negative result, argued with evidence, is a full-marks presentation. So is "we could
not establish this, and here is why". What does not work is a finding that the data does
not support, and the questions are where that shows.

Do not run a notebook on stage. If something is worth showing, it is worth exporting to
`figures/` first.

---

## The slides

Fill in the one-line takeaway for each. If you cannot write the takeaway, the slide is
not ready.

### 1. Title
Group, members, dataset.

*Takeaway:*

### 2. The question
What you set out to answer, in one sentence a person outside this course would
understand. No jargon, no variable names.

*Takeaway:*

### 3. The data, and where it came from
One line of provenance: was it a survey, an experiment, or observation? This is not
bookkeeping — it is what licenses everything you say later. Observational data does not
support a causal claim however good the model is.

*Takeaway:*

### 4. What we had to throw away
The sample-size accounting in one number, and **what the dropped rows had in common**.
If they had nothing in common, say that too: it is the stronger result.

*Takeaway:*

### 5–7. The evidence
One chart per claim. Each carries its **effect size and confidence interval on the
slide**, not only a p-value. Three slides is the budget; if you have more claims than
that, you have not chosen yet.

*Takeaways:*

### 8. The model
Two or three coefficients, read aloud **in the units of the problem** — "each extra hour
of study is worth 0.4 grade points", not "beta one is 0.4".

*Takeaway:*

### 9. What could confound this?
**This slide is mandatory and its title is fixed.** Name at least three things:

- a confounder you **adjusted for**, and what adjusting bought you;
- a confounder you **could not measure** from your data;
- a **selection effect** — who or what never made it into the dataset.

"Further research is needed" is not an answer to any of the three.

*Takeaway:*

### 10. Prediction
The dummy baseline and your best model, on the same axis, each with mean ± standard
deviation across folds. If the intervals overlap, you do not have a winner, and saying
so is worth more than claiming one.

*Takeaway:*

### 11. Where the model fails
A concrete case it gets wrong, and what that kind of case has in common. An accuracy
figure is not error analysis.

*Takeaway:*

### 12. What we could not establish
Specific, not ritual. "We cannot separate the effect of age from the effect of
experience, because in this dataset they correlate at 0.9."

*Takeaway:*

### 13. Conclusion
In the language of the problem, not of the method.

*Takeaway:*

### 14–15. Spare
Backup charts for the questions you expect.

---

## Charts

- Axis labels carry **units**. A number with no unit cannot be interpreted aloud.
- The slide **title states the takeaway**, not the chart type. "Prices rise with floor
  area" beats "Scatter plot of price and area".
- No screenshots of notebook output. Export from `figures/`, at 150 dpi or better, with
  the label fonts enlarged — what is readable on your laptop is not readable projected.
- No table with more than about six rows. If it needs more, it is a chart.

## The questions

Each member is asked two or three, about any part of the work. These are the kinds that
get asked — they are published because knowing them should change how you prepare, not
because knowing them lets you avoid them:

- Why that test and not the other one?
- What does this coefficient mean, in the units of the problem?
- Why is your baseline *that* baseline?
- What changes if the groups are unbalanced?
- Which of your results is statistically significant but too small to matter?
- What would you need to measure to turn this correlation into a causal claim?
- Which decision in your cleaning would most change the answer if you reversed it?

"The AI wrote it" is not an answer to any of them. See `INSTRUCTIONS.md` §7.
