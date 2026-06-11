# Task CS-003 — Expected number of flips until a pattern appears (biased coin)

## Metadata

- **Task ID:** CS-003
- **Domain / Subdomain:** Computer Science / Discrete Probability →
  Expectation & Markov state machines (pattern waiting times)
- **Workflow used:** Alternative (problem designed first, then matched to a source)
- **Author:** (trainer)
- **Date:** 2026-06-11

## Source paper

- **Title:** *Mathematics for Computer Science*
- **Author(s):** Eric Lehman, F. Thomson Leighton, Albert R. Meyer
- **Venue / Location:** Open textbook (MIT 6.042), revised 2015/2017
- **URL:** <https://people.csail.mit.edu/meyer/mcs.pdf>
- **License:** CC BY-SA 3.0
- **Which result the paper supplies:** The Expectation / "mean time to failure"
  material plus the state-machine framework, which together give the first-step
  (one-step) analysis on the absorbing chain whose states are "length of the longest
  current suffix that is a prefix of the target pattern." This is exactly the setup
  that makes the overlap correction tractable.

## Problem statement (self-contained, single question, LaTeX)

A biased coin comes up heads with probability $0.6$ and tails with probability $0.4$
on each flip, independently of all other flips. The coin is flipped repeatedly until
the three most recent outcomes are, in order, a head, then a tail, then a head — that
is, until the contiguous pattern $\mathrm{H},\mathrm{T},\mathrm{H}$ first occurs in
the sequence of flips. Let the random variable $T$ be the total number of flips
performed at the moment this pattern first appears. Compute the expected value
$\mathbb{E}[T]$, rounded to four significant figures.

## Golden answer

- **Answer (≤ 60 chars):** `8.611`
- **Character count:** 5
- **Form / rounding convention:** decimal, rounded to 4 significant figures

## Verifiable final solution

With $p=\Pr[\mathrm H]=0.6$, $q=0.4$, the overlap structure of $\mathrm{HTH}$ gives
$$\mathbb{E}[T] = \frac{1}{p^2 q} + \frac{1}{p} = \frac{125}{18} + \frac{30}{18}
= \frac{155}{18} = 8.6111\ldots \Rightarrow 8.611.$$
Reproduced by `verify/verify_answers.py` (`check_task3`), which also solves the exact
absorbing-Markov-chain expected-hitting-time linear system (no overlap formula
assumed) and confirms the match for several patterns.

## Full solution

**First-step / state-machine analysis.** Track progress toward $\mathrm{HTH}$ by the
length of the longest current suffix of the flip sequence that is a prefix of
$\mathrm{HTH}$. States are $0,1,2$ and the absorbing state $3$ (pattern complete).
Let $E_j$ be the expected number of further flips from state $j$; we want $E_0$.

Transitions (with $p=0.6$, $q=0.4$, and using $1-q=p$, $1-p=q$):

- State $0$: flip H $\to$ state $1$; flip T $\to$ state $0$.
  $E_0 = 1 + pE_1 + qE_0 \Rightarrow E_0 = \tfrac1p + E_1$.
- State $1$ (suffix …H): flip H $\to$ state $1$ (longest suffix-prefix is still "H");
  flip T $\to$ state $2$.
  $E_1 = 1 + pE_1 + qE_2 \Rightarrow E_1 = \tfrac1q + E_2$.
- State $2$ (suffix …HT): flip H $\to$ absorbed; flip T $\to$ state $0$
  (the suffix "T" is not a prefix of HTH).
  $E_2 = 1 + p\cdot 0 + qE_0 = 1 + qE_0$.

Substituting back, $E_0 = \tfrac1p + E_1 = \tfrac1p + \tfrac1q + E_2
= \tfrac1p + \tfrac1q + 1 + qE_0$. Since $1-q = p$,
$$E_0 = \frac{1}{p}\left(1 + \frac1p + \frac1q\right)
= \frac{1}{p^2} + \frac{1}{pq} + \frac1p
= \frac{1}{p^2 q} + \frac1p,$$
where the last step uses $p+q=1$ so that $\tfrac1{p^2}+\tfrac1{pq}=\tfrac{q+p}{p^2q}
=\tfrac1{p^2q}$. This matches the correlation method below.

**Cleaner closed form (Conway's leading-numbers / correlation method).** For a fair
or biased coin, $\mathbb{E}[T] = \sum_{k} \frac{1}{\Pr[\text{length-}k\text{ prefix}]}$,
summed over every $k$ for which the length-$k$ prefix of the pattern equals its
length-$k$ suffix. For $\mathrm{HTH}$:

- $k=3$: prefix $\mathrm{HTH}$ = suffix $\mathrm{HTH}$ ✓, contributing
  $1/(p\,q\,p)=1/(p^2q)$.
- $k=2$: prefix $\mathrm{HT}$ vs suffix $\mathrm{TH}$ ✗.
- $k=1$: prefix $\mathrm{H}$ = suffix $\mathrm{H}$ ✓, contributing $1/p$.

Hence
$$\mathbb{E}[T] = \frac{1}{p^2 q} + \frac{1}{p}
= \frac{1}{(0.6)^2(0.4)} + \frac{1}{0.6}
= \frac{125}{18} + \frac{30}{18} = \frac{155}{18} \approx \boxed{8.611}.$$

Both routes agree, and the code in `verify/` confirms the absorbing-chain solution
equals $155/18$.

## Why this fits the difficulty profile

- **Hard without the paper (Run I):** the dominant failure mode is ignoring the
  pattern's **self-overlap**. Treating $\mathrm{HTH}$ as a generic 3-pattern gives
  $1/(p^2q)=6.944$, missing the $+1/p$ overlap term; assuming "all length-3 patterns
  have equal waiting time" is also a frequent wrong belief. The bias ($p\neq q$)
  compounds the error.
- **Run II (search helped):** the methods (first-step analysis, Conway correlation)
  are standard, so the answer is reachable with careful work or search.
- **Easier with the paper (Run III):** the source supplies the expectation /
  state-machine machinery to set up the absorbing chain correctly, where the overlap
  is handled automatically.
- **Self-containment:** the bias, the exact target pattern, and the stopping rule are
  all given; a probability expert can derive the answer unaided.

## Difficulty knobs (to tune pass rates on the Eval Platform)

- Use a longer, more self-overlapping pattern (e.g. $\mathrm{HTHTH}$ or
  $\mathrm{HHTHH}$) to add overlap terms and widen the gap from the naive answer.
- Shift the bias (e.g. $p=0.55$) so the wrong "uniform pattern" intuition is closer
  to right and harder to reject by eye.
- Ask for a Penney's-game quantity (probability one pattern beats another) to require
  a second, comparative reasoning step.

## Constraints checklist

- [x] Single unambiguous answer, ≤ 60 chars
- [x] Answer ∉ {-1, 0, 1, Yes, No}; not MCQ; not fill-in-the-blank
- [x] Single question only
- [x] Rounding / canonical form specified
- [x] Self-contained; no "in the paper" phrasing
- [x] Requires reasoning beyond lookup
- [x] All math in LaTeX, renders correctly
- [x] Source license is allowed (CC BY-SA 3.0)
- [x] Golden answer verified (code: `verify/verify_answers.py`)

## Novelty check

- **Perplexity / search URL:** _(to fill: paste novelty-check URL)_
- **Result:** _(to fill)_

## Pass-rate results (fill from Eval Platform; 3 runs × 16 attempts)

| Run | Source paper? | Web search? | Passes / 16 | Pass rate | Within target? |
|-----|---------------|-------------|-------------|-----------|----------------|
| I   | No            | No          |             |           |                |
| II  | No            | Yes         |             |           |                |
| III | Yes           | No          |             |           |                |

- [ ] Run I or Run II has ≥ 1 pass
- [ ] Run III passes > Run I passes
- [ ] Prompt + answer consistent across run1/run2/run3 (checked on Taiga)
