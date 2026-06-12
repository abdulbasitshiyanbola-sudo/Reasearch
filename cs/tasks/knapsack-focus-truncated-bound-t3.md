# Task: Third-level truncated competitive-ratio bound for the Focus knapsack algorithm

## Metadata

- **Subdomain (A1 taxonomy):** Approximation & Online Algorithms
- **Difficulty tranche:** Full Difficulty (calibrate on Eval Platform)
- **Author:** _(trainer — finalize and own per §1.6.3 before submission)_
- **Date:** 2026-06-12

## Source paper (§1.3)

- **Title:** Stealing From the Dragon's Hoard: Online Unbounded Knapsack With Removal
- **Authors / Year:** M. Gehnen, M. Stocker, 2025
- **Venue / ID:** arXiv:2509.19914v2 [cs.DS], September 2025
- **License:** **CC BY 4.0** ✅ (verified on arXiv abstract page: `licenses/by/4.0/`)
- **URL:** https://arxiv.org/abs/2509.19914
- **Which result/lemma/technique helps?** The Focus algorithm (Definition 3), the
  Sylvester sequence $a_n$, the partial sums $S_{N-1}=\sum_{i=1}^{N-1}(a_i-1)^{-1}$,
  and the finite truncation bound $T_N=a_N/(a_N-1)^2+S_{N-1}$ from Theorem 2 /
  Lemma 6. The asymptotic tight ratio $S_\infty=1$ is proved, but $T_3$ is not tabulated.

## Problem prompt (what the model sees) — raw LaTeX

```latex
\textbf{Problem.}
In the Online Unbounded Knapsack Problem with Removal (pack/unpack subject to total
weight $\le 1$), the deterministic algorithm \textsc{Focus} maintains copies of a
single item of maximal \emph{cumulative value} $v^*(x)=v(x)\cdot\lfloor 1/w(x)\rfloor$;
when an item with strictly larger $v^*$ arrives, it discards the knapsack and packs as
many copies of the new item as possible.

Define Sylvester's sequence by $a_1=2$ and $a_n=a_{n-1}(a_{n-1}-1)+1$ for $n\ge 2$.
For $N\ge 1$, set
\[
S_{N-1}=\sum_{i=1}^{N-1}\frac{1}{a_i-1}\qquad(S_0=0),
\qquad
T_N=\frac{a_N}{(a_N-1)^2}+S_{N-1}.
\]
It is known that \textsc{Focus} is strictly $c$-competitive for every $c>T_N$ (i.e.,
its competitive ratio is at most $T_N$ in the finite-$N$ sense above), and that
$T_N\downarrow S_\infty$ as $N\to\infty$.

Compute $T_3$. Report your answer as an exact reduced fraction $p/q$ in lowest terms,
using a slash with no spaces (e.g.\ \texttt{61/36}).
```

## Golden answer

- **Answer:** `61/36`
- **Form:** symbolic (canonical reduced fraction `p/q`)
- **Length check:** 6 chars ≤ 60 ✅ — **Not in {-1,0,1,Yes,No}** ✅
- **Decimal:** $T_3 = 61/36 = 1.694\overline{4}$

## Full solution (verifiable) — raw LaTeX

```latex
\textbf{Step 1: First three Sylvester numbers.}
$a_1=2$, $a_2=3$, $a_3=7$.

\textbf{Step 2: Partial sum.}
$S_2=\dfrac{1}{a_1-1}+\dfrac{1}{a_2-1}=1+\dfrac{1}{2}=\dfrac{3}{2}$.

\textbf{Step 3: Truncation term.}
$\dfrac{a_3}{(a_3-1)^2}=\dfrac{7}{6^2}=\dfrac{7}{36}$.

\textbf{Step 4: Combine.}
\[
T_3=\frac{7}{36}+\frac{3}{2}=\frac{7}{36}+\frac{54}{36}=\boxed{\frac{61}{36}}.
\]
```

## Why the paper helps (Run III > Run I rationale)

Deriving the Focus analysis from scratch requires inventing the Sylvester sequence,
the threshold sequence $T_N$, and the depacking argument of Theorem 2. The paper
provides the algorithm and the closed form for $T_N$; the solver must still compute
$a_3$ and evaluate the sum — the numeric value $61/36$ does not appear in the paper.

## Novelty check (A2)

- **Perplexity results URL:** _TODO — run novelty check and paste URL before submission._
- **Confirmed not a known/online question and not AI-generated:** _TODO_

## Pass-rate results (Eval Platform — Opus 4.8 or latest)

| Run | Paper? | Web? | Passes / attempts | Pass rate | Gate (Full) | Gate (Easier) |
| --- | --- | --- | --- | --- | --- | --- |
| I   | No  | No  | _TODO_ | _TODO_ | ≤ 12.5% (0–2) | ≤ 50% (0–8) |
| II  | No  | Yes | _TODO_ | _TODO_ | no restriction | no restriction |
| III | Yes | No  | _TODO_ | _TODO_ | ≤ 50% (1–8) | ≤ 80% (1–12) |

- **Run I OR Run II has ≥ 1 pass:** _TODO_
- **Run III passes > Run I passes:** _TODO_
- **Prompt + answer consistent across run1/run2/run3 (Taiga):** _TODO_

## Difficulty knobs

- **Easier:** ask for $T_2=7/4$ (only two Sylvester terms).
- **Harder:** ask for $T_4$ as a decimal to 4 d.p. ($\approx 1.6910$).
