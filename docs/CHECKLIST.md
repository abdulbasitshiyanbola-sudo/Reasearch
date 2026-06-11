# Per-task submission checklist

Run through this before submitting any CS task. It is the union of the DO/DON'T list
and the pass-rate gating rules from the Trainer Guidelines.

## Content (DO)

- [ ] Numerical precision specified when relevant (e.g. "round to N significant figures").
- [ ] Canonical form / simplification convention specified when relevant
      (e.g. two words, a percentage, a fully reduced fraction).
- [ ] Self-contained: boundary conditions, assumptions, initial conditions, and all
      constants are stated explicitly. An expert can solve it without the source.
- [ ] Challenging and requires reasoning (not lookup).
- [ ] Exactly one correct answer.
- [ ] All mathematical symbols in LaTeX, and the LaTeX renders.
- [ ] The intended failure is a *reasoning* failure of the model.
- [ ] Golden answer and the verifiable final solution are confirmed correct
      (here: by `verify/verify_answers.py`).
- [ ] Prompt and answer are consistent across run1/run2/run3 (checked on Taiga).

## Content (DON'T)

- [ ] Not trivially answerable by copying from the source.
- [ ] Not ambiguous / multiple answers possible.
- [ ] Not multiple questions in one prompt.
- [ ] No LaTeX that fails to render.
- [ ] Does not use the words "in the paper" or "in the reference".
- [ ] Answer is not one of `-1, 0, 1, Yes, No`.
- [ ] Answer is ≤ 60 characters.
- [ ] Not multiple choice.
- [ ] Not fill-in-the-blank.

## Source paper

- [ ] License is one of: Apache, MIT, CC BY, CC BY-SA, CC0, BSD.
      (arXiv's default license does NOT qualify.)
- [ ] Source link recorded.
- [ ] Paper used at most 3 times across all tasks (prefer once).

## Novelty

- [ ] Novelty check performed; Perplexity/search URL recorded.
- [ ] Not copied from any online/other source; not AI/LLM-generated from an existing item.

## Pass-rate gating (Full difficulty; Eval Platform, latest model, 3×16)

- [ ] Run I (no paper, no web): 0–2 passes (≤ 12.5%).
- [ ] Run II (no paper, web): no restriction.
- [ ] Run III (paper, no web): 1–8 passes (≤ 50%).
- [ ] Run I or Run II has ≥ 1 pass.
- [ ] Run III passes > Run I passes.
- [ ] (If both Run I and Run II are 0 but the task is believed solvable, may extend
      to ≤ 32 attempts for Run I and/or Run II to obtain ≥ 1 pass.)

## Easier difficulty (optional "Criteria 2") thresholds, for reference

- Run I (no paper, no web): 0–8 passes (≤ 50%).
- Run III (paper, no web): 1–12 passes (≤ 80%).
- Same extra rules (Run I or II ≥ 1 pass; Run III > Run I).
