# Task <ID> — <short title>

> Copy this file into `tasks/` and fill in every field. Delete the parenthetical
> hints. Keep all math in LaTeX.

## Metadata

- **Task ID:** <CS-0XX>
- **Domain / Subdomain:** Computer Science / <taxonomy subdomain — see A1: Taxonomy>
- **Workflow used:** <Traditional | Alternative>
- **Author:** <name>
- **Date:** <YYYY-MM-DD>

## Source paper

- **Title:** <title>
- **Author(s):** <authors>
- **Venue / Location:** <journal / arXiv id / book>
- **URL:** <url>
- **License:** <Apache | MIT | CC BY | CC BY-SA | CC0 | BSD> (must be one of these)
- **Which result the paper supplies:** <the specific lemma/theorem/method that makes
  the problem easier once the paper is in hand>

## Problem statement (self-contained, single question, LaTeX)

<The full prompt exactly as the solver sees it. State every constant, assumption,
boundary/initial condition. Specify rounding or canonical form. Do not use the words
"in the paper". One question only.>

## Golden answer

- **Answer (≤ 60 chars):** `<value>`
- **Character count:** <n>
- **Form / rounding convention:** <e.g. decimal rounded to 4 significant figures>

## Verifiable final solution

<A short, checkable statement of how the answer is obtained — ideally reproducible by
the code in `verify/verify_answers.py`.>

## Full solution

<Complete step-by-step derivation an expert would accept.>

## Why this fits the difficulty profile

- **Hard without the paper (Run I):** <why a model's *reasoning* tends to fail>
- **Solvable / search-helped (Run II):** <why it is genuinely self-contained>
- **Easier with the paper (Run III):** <the specific lift the paper provides>
- **Self-containment justification:** <why an expert needs no paper>

## Difficulty knobs (to tune pass rates on the Eval Platform)

- <knob 1 — e.g. increase instance size>
- <knob 2 — e.g. make a constant less standard>

## Constraints checklist

- [ ] Single unambiguous answer, ≤ 60 chars
- [ ] Answer ∉ {-1, 0, 1, Yes, No}; not MCQ; not fill-in-the-blank
- [ ] Single question only
- [ ] Rounding / canonical form specified
- [ ] Self-contained; no "in the paper" phrasing
- [ ] Requires reasoning beyond lookup
- [ ] All math in LaTeX, renders correctly
- [ ] Source license is allowed
- [ ] Golden answer verified (code)

## Novelty check

- **Perplexity / search URL:** <paste URL of the novelty-check results>
- **Result:** <novel — not found online / not AI-generated from an existing item>

## Pass-rate results (fill from Eval Platform; 3 runs × 16 attempts)

| Run | Source paper? | Web search? | Passes / 16 | Pass rate | Within target? |
|-----|---------------|-------------|-------------|-----------|----------------|
| I   | No            | No          |             |           |                |
| II  | No            | Yes         |             |           |                |
| III | Yes           | No          |             |           |                |

- [ ] Run I or Run II has ≥ 1 pass
- [ ] Run III passes > Run I passes
- [ ] Prompt + answer consistent across run1/run2/run3 (checked on Taiga)
