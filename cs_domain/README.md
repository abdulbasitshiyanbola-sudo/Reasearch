# CS Domain — Paper-Assisted STEM Problems

Working area for authoring **Computer Science** tasks under the
*Paper-Assisted STEM Problems* trainer guidelines (Part 2: Task Creation).

This folder holds:

- This guide: requirements checklist, CS taxonomy, paper-vetting notes, pass-rate
  strategy, and a reusable problem template.
- [`problems/`](problems/) — one Markdown file per task (statement, golden answer,
  full solution, pass-rate plan, novelty check).
- [`verification/`](verification/) — small, dependency-light scripts that
  independently recompute each golden answer so it can be trusted.

---

## 1. Requirements checklist (per task)

Distilled from the guidelines (DOs/DONTs + Source Paper + Pass-rate sections).

**Problem design**

- [ ] Challenging and requires reasoning (not a paper lookup). `[2.1.1.1]`
- [ ] Self-contained: an expert could solve it **without** the paper. Boundary
      conditions, assumptions, initial conditions, constraints stated explicitly. `[2.1.1.2.3]`
- [ ] Does **not** use the words "in the paper" / "in the reference".
- [ ] Single, unambiguous correct answer (string / numeric / symbolic). `[2.2.1.2]`
- [ ] Numerical precision specified (e.g. "round to 3 significant figures"). `[2.1.1.2.1]`
- [ ] Canonical form specified when symbolic. `[2.1.1.2.2]`
- [ ] All math in LaTeX, and it renders. `[2.2.1.4.5]`

**Answer constraints**

- [ ] Answer length ≤ 60 characters. `[2.2.1.1]`
- [ ] Answer is **not** one of `-1, 0, 1, Yes, No`. `[2.1.1.15]`
- [ ] Not multiple choice. `[2.1.1.6]`  Not fill-in-the-blank. `[2.1.1.8]`
- [ ] Exactly one question in the prompt.

**Source paper**

- [ ] License is one of: **Apache, MIT, CC BY, CC BY-SA, CC0, BSD**. `(§1.3)`
- [ ] The paper genuinely makes the problem *easier* (it is the key result).
- [ ] Paper reused ≤ 3 times across all tasks; prefer once. `(§1.6)`

**Pass-rate plan (Full difficulty — primary)** `(§1.4)`

- [ ] Run I  (no paper, no web): target 0–2 / 16 passes (≤ 12.5%).
- [ ] Run II (no paper, web):    no restriction.
- [ ] Run III (paper, no web):   target 1–8 / 16 passes (≤ 50%).
- [ ] Run III passes **> ** Run I passes (paper makes it easier).
- [ ] Run I **or** Run II has ≥ 1 pass (self-contained & solvable).

**Submission hygiene**

- [ ] Prompt + answer consistent across run1/run2/run3 (check on Taiga).
- [ ] Novelty check done (A2) and Perplexity URL recorded.
- [ ] Subdomain tagged per taxonomy (A1).
- [ ] Not copied from any source and not AI/LLM-generated. `(§1.6.3)`

> ⚠️ The guidelines reference **A1: Taxonomy** and **A2: Novelty Check** appendices
> that were not included in the uploaded PDF. Treat the taxonomy below as a working
> placeholder and replace the subdomain tags with the official ones once provided.

---

## 2. Working CS taxonomy (placeholder)

Use to keep topics diverse — aim to spread tasks across subdomains rather than
clustering. Replace with the official A1 taxonomy when available.

- **Theory of Computation**: complexity, algorithms & data structures, online
  algorithms, streaming/sketching, randomized algorithms, approximation.
- **Algorithmic Game Theory / Economics & Computation**: mechanism design,
  prophet inequalities, online matching, auctions, price of anarchy.
- **Cryptography & Security**: provable security bounds, hardness assumptions.
- **Information & Coding Theory**: capacity, rate–distortion, code bounds.
- **Machine Learning Theory**: generalization/PAC bounds, optimization rates,
  sample complexity.
- **Systems / Networking / Databases**: scheduling, caching, query complexity.
- **Programming Languages / Formal Methods / Logic**.

Each task file records its subdomain in the front-matter block.

---

## 3. Paper-vetting notes (licensing reality check)

The license requirement is the most common reason a candidate paper is unusable.
Findings while sourcing CS papers:

**Reliably qualifying (CC BY 4.0):**

- **LIPIcs / Dagstuhl** proceedings — every paper is CC BY 4.0
  (ICALP, ESA, ITCS, CCC, STACS, SoCG, MFCS, APPROX/RANDOM, FSTTCS, DISC, ...).
- **TheoretiCS**, **Logical Methods in Computer Science (LMCS)** — CC BY.
- **Transactions on Machine Learning Research (TMLR)** — CC BY 4.0.
- **Quantum** journal — CC BY.
- **PLOS** (e.g. PLOS Comp. Bio.) — CC BY.
- **arXiv** papers **only if** the author selected a CC license — verify per paper.

**Usually NOT qualifying (do not assume):**

- Default **arXiv** license is `arXiv perpetual non-exclusive` — **not** CC BY.
  Always check the abstract page license line.
- **ACM**, **IEEE**, **Springer LNCS**, **INFORMS**, **Elsevier** — default
  copyright is the publisher's, not CC BY (even for "open access" PDFs).

**How to verify an arXiv license from the terminal:**

```bash
curl -s https://arxiv.org/abs/<ID> | grep -i -o -E 'licenses/[a-z0-9./-]+' | sort -u
# qualifying examples:   licenses/by/4.0/   licenses/by-sa/4.0/   licenses/zero/1.0/
# NOT qualifying:        licenses/nonexclusive-distrib/1.0/
```

---

## 4. Pass-rate design strategy

The hard part is making a problem that is *hard without the paper* yet *easier
with it*, while the answer remains a clean single value. Patterns that work:

1. **Apply, don't recall.** Ask for a quantity that requires *running* the
   paper's theorem/equation, **not** a value printed in the paper. If the number
   is in the paper's own table, Run III collapses to a lookup (pass-rate → ~100%,
   breaking the ≤50% rule). Choose parameters *outside* the paper's tables.
2. **Specialized key result.** Anchor on a characterization a generalist model is
   unlikely to reconstruct from scratch with no tools (drives Run I low) but that
   an expert — or a reader of the paper — can apply (keeps Run III > Run I).
3. **Lure with a famous-but-wrong constant.** If the setting sits near a
   well-known constant that does *not* apply, no-paper runs tend to answer the
   famous one and fail — as long as the statement pins the answer unambiguously.
4. **Robust rounding.** Pick parameters whose answer is far from a rounding
   boundary, and state the rounding rule explicitly. Verify with code. Note that
   papers often *truncate*; recompute and round properly yourself.

These are predictions; actual pass-rates must be confirmed on the Eval Platform
(Opus 4.8, 16 attempts/run) before submission.

---

## 5. Task template

Copy [`problems/_TEMPLATE.md`](problems/_TEMPLATE.md) for each new task.

## 6. Index of tasks

| # | Subdomain | Source paper (license) | Answer | Status |
|---|-----------|------------------------|--------|--------|
| 1 | AGT / Prophet inequalities | arXiv:2205.00588 (CC BY 4.0) | `0.742` | Drafted, golden answer verified; pass-rates pending Eval Platform |
