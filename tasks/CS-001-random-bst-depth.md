# Task CS-001 — Expected depth of a key in a random binary search tree

## Metadata

- **Task ID:** CS-001
- **Domain / Subdomain:** Computer Science / Algorithms & Data Structures →
  Randomized data structures (random binary search trees)
- **Workflow used:** Alternative (problem designed first, then matched to a source)
- **Author:** (trainer)
- **Date:** 2026-06-11

## Source paper

- **Title:** *Algorithms*
- **Author(s):** Jeff Erickson
- **Venue / Location:** Open textbook (1st ed., 2019)
- **URL:** <http://jeffe.cs.illinois.edu/teaching/algorithms/book/Algorithms-JeffE.pdf>
- **License:** CC BY 4.0
- **Which result the paper supplies:** The randomized-analysis lemma that, in a tree
  built by random insertion of the keys $1,\dots,n$, key $i$ is an ancestor of key
  $j$ **iff** $i$ is the first of the keys $\{\min(i,j),\dots,\max(i,j)\}$ to be
  inserted, giving $\Pr[i \text{ is an ancestor of } j] = \frac{1}{|i-j|+1}$. The
  book develops exactly this "first key in the interval is the common ancestor"
  argument used to analyze randomized BSTs / quicksort.

## Problem statement (self-contained, single question, LaTeX)

The integer keys $1, 2, \ldots, 25$ are inserted one at a time, in an order chosen
uniformly at random from all $25!$ possible orders, into an initially empty binary
search tree. Insertions use the standard binary-search-tree rule and the tree is
**never** rebalanced: each new key starts at the root and repeatedly moves to the
left child if it is smaller than the current node's key, or to the right child if it
is larger, until it reaches an empty slot, where it is placed. Define the depth of a
node as the number of edges on the path from the root to that node, so the root has
depth $0$. Let the random variable $D$ be the depth of the node that ends up storing
the key $9$. Compute the expected value $\mathbb{E}[D]$, rounded to four significant
figures.

## Golden answer

- **Answer (≤ 60 chars):** `4.269`
- **Character count:** 5
- **Form / rounding convention:** decimal, rounded to 4 significant figures

## Verifiable final solution

$\mathbb{E}[D] = H_9 + H_{17} - 2$, where $H_m=\sum_{t=1}^{m}\frac1t$.
Exact value $= \dfrac{52298941}{12252240} = 4.26852\ldots \Rightarrow 4.269$.
Reproduced by `verify/verify_answers.py` (`check_task1`), which also confirms the
closed form against brute force over all $n!$ insertion orders for every
$2 \le n \le 7$.

## Full solution

For distinct keys $i \neq k$, node $i$ is a **proper ancestor** of node $k$ in the
final tree iff, among the contiguous block of keys
$\{\min(i,k),\dots,\max(i,k)\}$, key $i$ is the one inserted earliest. (The first key
inserted from that block becomes the lowest common ancestor of the whole block; every
other key in the block descends from it, and key $i$ in particular lies on the
root-to-$k$ path precisely when $i$ is that earliest key.) Because the insertion order
is uniformly random and the block has $|i-k|+1$ keys,
$$\Pr[i \text{ is an ancestor of } k] = \frac{1}{|i-k|+1}.$$

The depth of node $k$ equals its number of proper ancestors, so with indicator
variables and linearity of expectation,
$$\mathbb{E}[D] = \sum_{\substack{i=1\\ i\neq k}}^{n} \frac{1}{|i-k|+1}.$$

Split the sum at $k$. For $i<k$ the distance $k-i$ runs over $1,\dots,k-1$, giving
$\sum_{d=1}^{k-1}\frac1{d+1}=H_k-1$. For $i>k$ the distance $i-k$ runs over
$1,\dots,n-k$, giving $\sum_{d=1}^{n-k}\frac1{d+1}=H_{n-k+1}-1$. Hence
$$\mathbb{E}[D] = H_k + H_{n-k+1} - 2.$$

With $n=25$ and $k=9$: $\mathbb{E}[D] = H_9 + H_{17} - 2$. Numerically
$H_9 = 2.8289683\ldots$, $H_{17} = 3.4395239\ldots$, so
$\mathbb{E}[D] = 4.2685208\ldots \approx \boxed{4.269}$.

## Why this fits the difficulty profile

- **Hard without the paper (Run I):** the clean answer hinges on the exact ancestor
  probability $\frac{1}{|i-k|+1}$. The closely related *quicksort comparison* lemma
  has a factor of $2$ ($\Pr=\frac{2}{|i-j|+1}$), and models routinely conflate the
  two, or treat depth as a one-sided sum, or evaluate the harmonic sums incorrectly
  by hand — each produces a wrong final number.
- **Run II (search helped):** the underlying facts are standard, so a careful
  self-contained derivation (or search) can reach the answer; it is genuinely
  solvable without being handed the source.
- **Easier with the paper (Run III):** the source states the "first key in the
  interval is the ancestor" lemma directly, removing the main place reasoning slips.
- **Self-containment:** every rule (insertion procedure, no rebalancing, depth
  definition, uniform order) is given; an algorithms expert can derive the result
  unaided.

## Difficulty knobs (to tune pass rates on the Eval Platform)

- Increase $n$ (e.g. to 60–100) and/or pick an off-center $k$ to lengthen the
  harmonic-number computation and increase hand-arithmetic error.
- Ask instead for the **expected number of descendants** of key $k$, or the expected
  number of nodes at depth exactly $2$, which require an extra reasoning step.
- Tighten the rounding (e.g. 6 significant figures) to penalize sloppy summation.

## Constraints checklist

- [x] Single unambiguous answer, ≤ 60 chars
- [x] Answer ∉ {-1, 0, 1, Yes, No}; not MCQ; not fill-in-the-blank
- [x] Single question only
- [x] Rounding / canonical form specified
- [x] Self-contained; no "in the paper" phrasing
- [x] Requires reasoning beyond lookup
- [x] All math in LaTeX, renders correctly
- [x] Source license is allowed (CC BY 4.0)
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
