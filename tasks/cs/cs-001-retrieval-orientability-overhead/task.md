# CS-001 — Orientability thresholds and the memory overhead of XOR retrieval

> Paper-Assisted STEM Problem · Domain: Computer Science · Full Difficulty (Criteria 1)

---

## 1. Taxonomy / subdomain designation

| Field | Value |
|---|---|
| Domain | Computer Science |
| Primary subdomain | Data Structures & Algorithms (arXiv `cs.DS`; ACM CCS: *Theory of computation → Data structures design and analysis*) |
| Topic | Randomized hashing data structures — orientability thresholds of random `k`-uniform hypergraphs (cuckoo hashing / XOR retrieval / Bloom-filter replacements) |
| Skills exercised | Probabilistic combinatorics, numerical root-finding of a transcendental equation, quantitative reasoning / design trade-off analysis |

---

## 2. Source paper

| Field | Value |
|---|---|
| Title | *Dense Peelable Random Uniform Hypergraphs* |
| Author | Stefan Walzer |
| Venue | 27th European Symposium on Algorithms (ESA 2019), LIPIcs vol. 144, Article 38 |
| DOI | `10.4230/LIPIcs.ESA.2019.38` |
| Open-access URL | https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2019.38 |
| **License** | **Creative Commons Attribution (CC BY 3.0)** — qualifying ✅ |

**Why the paper helps (and what it provides).** The paper studies peelability and
**orientability thresholds** `c_k*` of random `k`-uniform hypergraphs, which are exactly
the constructibility thresholds of XOR-based retrieval data structures and the load
thresholds of `k`-ary cuckoo hashing. Its **Table 1** lists the orientability thresholds
to ten decimal places:

```
k        3              4              5              6              7
c_k*  0.9179352767  0.9767701649  0.9924383913  0.9973795528  0.9990637588
```

The genuinely hard step in this problem is obtaining these constants to high precision —
each is the root of a transcendental equation and must be solved numerically. The paper
removes that obstacle by tabulating the constants, so a solver **with** the paper can go
straight to the design reasoning, while a solver **without** it must re-derive and
numerically solve the threshold equation to 4–5 significant figures unaided.

> Note: the licensing applies to the LIPIcs/DROPS open-access version linked above
> (CC BY 3.0, Schloss Dagstuhl). The arXiv preprint `arXiv:1907.04749` carries the
> default arXiv non-exclusive license and must **not** be used as the cited source.

---

## 3. Problem statement (as presented to the model)

> In an **XOR-based static retrieval data structure** (a generalization of the Bloom
> filter, used to store a function on a fixed key set), a set of \(m\) keys is stored by
> mapping each key, via \(k\) independent hash functions, to a \(k\)-subset of \(n\) memory
> cells. The keys and their cells form a random \(k\)-uniform hypergraph (each of the \(m\)
> hyperedges is \(k\) cells chosen independently and uniformly at random, \(k \ge 3\)). The
> structure can be constructed successfully with high probability **if and only if** the
> load factor \(c = m/n\) is strictly below the *orientability threshold* \(c_k^{*}\) of the
> random \(k\)-uniform hypergraph. Consequently the smallest achievable memory footprint is
> \(1/c_k^{*}\) cells per stored key, and we define the **excess overhead**
> \[
> o_k \;=\; \frac{1}{c_k^{*}} - 1
> \]
> as the number of extra cells per key beyond the ideal of one cell per key.
>
> A system designer must choose the number of hash functions \(k \ge 3\). Increasing \(k\)
> decreases \(o_k\) but increases the per-query cost, so the designer adopts the following
> rule: **use the smallest \(k \ge 3\) such that increasing the number of hash functions by
> one more would reduce the excess overhead by less than \(0.01\) cells per key** (that is,
> the smallest \(k\) with \(o_k - o_{k+1} < 0.01\)). For the value of \(k\) selected by this
> rule, what is the excess overhead \(o_k\)?
>
> Express your answer as a percentage rounded to three significant figures.

---

## 4. Golden answer

```
0.762%
```

- **Canonical form:** a percentage, three significant figures (i.e. `0.762%`).
- Equivalent acceptable phrasings: `0.762 %`, `0.762 percent`. (Decimal form `0.00762`
  cells/key is the same quantity; the prompt fixes the percentage convention.)

---

## 5. Full solution

**Step 1 — Identify the governing constants.** The constructibility threshold of the
described structure is the \(\ell=1\) orientability threshold \(c_k^{*}\) of the random
\(k\)-uniform hypergraph. For \(k \ge 3\) it is characterized by
\[
k \;=\; \frac{\xi^{*}\,(e^{\xi^{*}}-1)}{e^{\xi^{*}}-1-\xi^{*}},
\qquad
c_k^{*} \;=\; \frac{\xi^{*}}{k\,\bigl(1-e^{-\xi^{*}}\bigr)^{k-1}},
\]
where \(\xi^{*}\) is the unique positive root of the first equation. Solving numerically
(or reading the constants from the source paper's Table 1):

| \(k\) | \(c_k^{*}\) | \(o_k = 1/c_k^{*}-1\) |
|---|---|---|
| 3 | 0.9179352767 | 8.9401 % |
| 4 | 0.9767701649 | 2.3782 % |
| 5 | 0.9924383913 | 0.7619 % |
| 6 | 0.9973795528 | 0.2627 % |
| 7 | 0.9990637588 | 0.0937 % |

**Step 2 — Apply the designer's stopping rule.** Compute the incremental absolute saving
\(\Delta_k = o_k - o_{k+1}\) (cells per key):
\[
\Delta_3 = 0.0656,\quad \Delta_4 = 0.0162,\quad \Delta_5 = 0.00499,\quad \Delta_6 = 0.00169.
\]
We need the smallest \(k\) with \(\Delta_k < 0.01\). Since \(\Delta_4 = 0.0162 \ge 0.01\) but
\(\Delta_5 = 0.00499 < 0.01\), the rule selects \(k = 5\).

**Step 3 — Report the overhead for the chosen \(k\).**
\[
o_5 = \frac{1}{0.9924383913} - 1 = 0.0076192 = 0.76192\% \;\xrightarrow{\text{3 s.f.}}\; \boxed{0.762\%}.
\]

**Verifiable final solution.** See [`solve.py`](./solve.py) (pure standard library). It
re-derives every \(c_k^{*}\) from the transcendental equation, cross-checks them against the
paper's Table 1 to within \(5\times10^{-11}\), applies the rule, and asserts the result
equals `0.762%`.

```
$ python3 solve.py
...
Chosen k = 5
Excess overhead o_5 = 0.761922%
GOLDEN ANSWER (3 significant figures) = 0.762%
OK: golden answer reproduced -> 0.762%
```

---

## 6. Why this should hit the target pass-rate profile (Full Difficulty)

The hardness is concentrated in obtaining \(c_4^{*}, c_5^{*}, c_6^{*}\) to ~4–5 significant
figures and then chaining several exact arithmetic/selection steps. The orientability
threshold (≈0.918, 0.977, 0.992, …) is frequently **confused with the peelability /
2-core threshold** (≈0.818, 0.772, 0.702, …); a solver who uses the wrong family of
constants lands far from `0.762%`. Each constant is a root of a transcendental equation,
which is very hard to evaluate to the required precision by hand (no tools), so unaided
attempts tend to fail at the precision bar even when the high-level method is right.

| Run | Source paper | Web search | Target passes / 16 | Expectation & rationale |
|---|---|---|---|---|
| **I** | No | No | 0–2 (≤ 12.5%) | Must recall the exact orientability-threshold equation **and** solve it to 5 s.f. for three values of `k` with no tools — expected to fail / mis-round / use peelability constants. |
| **II** | No | Yes | no limit | Web can surface the threshold table; allowed to pass freely. Satisfies the "≥1 pass in Run I or II" self-containedness signal. |
| **III** | Yes | No | 1–8 (≤ 50%), and **> Run I** | Paper's Table 1 supplies all `c_k*` directly; remaining work is the (still non-trivial) selection rule + reciprocal arithmetic + rounding. Should pass more often than Run I. |

> ⚠️ These are *design expectations*. The actual Run I/II/III pass rates must be measured on
> the Eval Platform with Opus 4.8 (16 attempts each), and the task confirmed consistent
> across run1/run2/run3 on Taiga before submission. See the checklist in
> [`../README.md`](../README.md).

---

## 7. DOs / DON'Ts self-check

DOs:
- [x] Numerical precision specified ("three significant figures").
- [x] Canonical form specified (a percentage).
- [x] Self-contained: all definitions (random `k`-uniform hypergraph, orientability
      threshold, excess overhead, the selection rule, `k ≥ 3`) are given explicitly; an
      expert can solve it without the paper.
- [x] Challenging, requires multi-step reasoning (not a lookup).
- [x] Single correct answer.
- [x] LaTeX used for all math.
- [x] Targets model reasoning failure (orientability-vs-peelability confusion + precision).
- [x] Golden answer verified by an independent script.

DON'Ts:
- [x] Not trivially answerable by lookup — the answer (`0.762%`) is a derived quantity, not a
      number printed in the paper.
- [x] Exactly one possible answer.
- [x] Single question only.
- [x] LaTeX is simple and renders.
- [x] Phrases "in the paper"/"in the reference" are **not** used in the prompt.
- [x] Answer is not −1, 0, 1, "Yes", or "No".
- [x] Answer length ≤ 60 characters.
- [x] Not multiple choice; not fill-in-the-blank.

---

## 8. Novelty / uniqueness

- Novelty check (A2): run the problem statement through Perplexity and record the result URL
  here before submission → **TODO (must be done on the trainer account):** `__________`
- Not copied from any online source; constructed for this project. The numeric answer is a
  composed design quantity, not a published value.
- Source-paper reuse: this is the first task using *Dense Peelable Random Uniform
  Hypergraphs* (uses remaining: up to 2 more allowed).
