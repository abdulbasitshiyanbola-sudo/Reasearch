# Task NN — <short title>

- **Subdomain (A1):** CS → <area> → <subarea>
- **Source paper:** <Authors>, "<Title>", <venue/arXiv ID>, <year>
- **License:** <CC BY 4.0 / MIT / ...> — **verify and record how it was checked**
- **Paper URL:** <url>
- **Workflow:** Traditional | Alternative
- **Novelty check (A2) Perplexity URL:** <paste>

## Prompt (exact text submitted)

> <self-contained question, LaTeX for all math, single question, rounding/canonical
> form specified, no "in the paper", answer ≤ 60 chars>

## Golden answer

```
<answer>
```

Acceptable equivalent forms (for grader): <list, or "none">

## Full solution

<step-by-step derivation; show why the answer is unique; end with the value>

## Why the paper helps (and the answer is not a lookup)

<which result/equation in the paper is the key; why the asked quantity must be
*computed* from it rather than read off>

## Pass-rate plan (Full difficulty)

| Run | Paper | Web | Predicted passes /16 | Rationale |
|-----|-------|-----|----------------------|-----------|
| I   | No    | No  | 0–2  | <why hard with no tools> |
| II  | No    | Yes | ?    | <web may surface it> |
| III | Yes   | No  | 1–8  | <must apply the result; not a lookup> |

- Run III > Run I: <argument>
- Run I or Run II ≥ 1 pass: <argument>

## DOs/DONTs compliance

- [ ] Self-contained / expert-solvable without paper
- [ ] Single unambiguous answer, ≤ 60 chars, not in {-1,0,1,Yes,No}
- [ ] Precision / canonical form specified
- [ ] LaTeX renders; one question; no "in the paper"
- [ ] Not MCQ / not fill-in-the-blank
- [ ] License qualifies; paper used ≤ 3×

## Verification

Script: [`../verification/<file>.py`](../verification/) — run `python3 <file>.py`.
