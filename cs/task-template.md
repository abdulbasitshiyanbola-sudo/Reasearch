# Task: <short title>

> Copy this file per task (e.g. `tasks/<slug>.md`). Fill in every field.
> Delete the parenthetical hints before submission.

## Metadata

- **Subdomain (A1 taxonomy):** <e.g. Randomized & Streaming Algorithms>
- **Difficulty tranche:** <Full Difficulty | Easier Difficulty>
- **Author:** <name>
- **Date:** <YYYY-MM-DD>

## Source paper (§1.3)

- **Title:** <paper title>
- **Authors / Year:** <...>
- **Venue / ID:** <e.g. arXiv:XXXX.XXXXX, JMLR vol/issue, LIPIcs DOI>
- **License:** <Apache | MIT | CC BY | CC BY-SA | CC0 | BSD>  ✅ must be one of these
- **URL:** <link>
- **Which result/lemma/technique helps?** <the specific thing in the paper that makes
  the problem easier — but is NOT a trivial copy of the answer>

## Problem prompt (what the model sees)

(Self-contained: state model, inputs, assumptions, constraints, boundary/initial
conditions. Use LaTeX for all math. Single question only. No "in the paper"/"in the
reference". Specify rounding/canonical form.)

<problem statement here>

## Golden answer

- **Answer:** `<single unambiguous value>`
- **Form:** <numeric (rounding rule) | symbolic (canonical form) | string (convention)>
- **Length check:** <≤ 60 chars?>  **Not in {-1,0,1,Yes,No}?** <yes/no>

## Full solution (verifiable)

(Complete, step-by-step derivation that an expert could follow without the paper.
Show why the answer is unique.)

<full worked solution here>

## Why the paper helps (Run III > Run I rationale)

<explain the reasoning gap: what makes this hard without the paper, and how the paper's
result shortcuts/grounds the derivation>

## Novelty check (A2)

- **Perplexity results URL:** <paste URL>
- **Confirmed not a known/online question and not AI-generated:** <yes/no>

## Pass-rate results (Eval Platform — Opus 4.8 or latest)

| Run | Paper? | Web? | Passes / attempts | Pass rate | Gate (Full) | Gate (Easier) |
| --- | --- | --- | --- | --- | --- | --- |
| I   | No  | No  | <x>/16 | <%> | ≤ 12.5% (0–2) | ≤ 50% (0–8) |
| II  | No  | Yes | <x>/16 | <%> | no restriction | no restriction |
| III | Yes | No  | <x>/16 | <%> | ≤ 50% (1–8) | ≤ 80% (1–12) |

- **Run I OR Run II has ≥ 1 pass:** <yes/no> (else extend to ≤ 32 attempts)
- **Run III passes > Run I passes:** <yes/no>
- **Prompt + answer consistent across run1/run2/run3 (Taiga):** <yes/no>
