# Task: Closed-form competitive ratio for uniform-cost list update (Fpm)

## Metadata

- **Subdomain (A1 taxonomy):** Approximation & Online Algorithms
- **Difficulty tranche:** Full Difficulty (calibrate on Eval Platform)
- **Author:** _(trainer — finalize and own per §1.6.3 before submission)_
- **Date:** 2026-06-12

## Source paper (§1.3)

- **Title:** A 3.3904-Competitive Online Algorithm for List Update with Uniform Costs
- **Authors / Year:** M. Basiak, M. Bienkowski, M. Böhm, M. Chrobak, Ł. Jeż, J. Sgall, A. Tatarczuk, 2025
- **Venue / ID:** ESA 2025 (LIPIcs vol. 351, article 74); arXiv:2503.17264v3 [cs.DS]
- **License:** **CC BY 4.0** ✅ (LIPIcs + arXiv `licenses/by/4.0/`)
- **URL:** https://arxiv.org/abs/2503.17264
- **Which result/lemma/technique helps?** Theorem 14 and the non-linear potential
  optimization (Section 4.5): setting $R$ as the target ratio and solving for the
  six pair-state potentials under Assumption 4.11 yields
  $R=\tfrac{1}{8}(23+\sqrt{17})$. The decimal $3.3904$ appears in the abstract, but
  the exact radical form must be extracted from the proof.

## Problem prompt (what the model sees) — raw LaTeX

```latex
\textbf{Problem.}
In \emph{List Update with uniform costs} ($\mathsf{LUP}_1$), each access to list
position $\ell$ costs $\ell$, and each adjacent swap costs $1$. The online algorithm
\textsc{Fpm} (Full-Or-Partial-Move) is analyzed via a pair-state potential function
on item pairs with six active states
$\alpha^d,\beta^d,\alpha^{oe},\beta^o,\beta^{ne},\gamma^{ne}$, subject to
$\alpha^d=0$ and non-negativity constraints linking the potentials to a target
competitive ratio $R$.

It is known that \textsc{Fpm} achieves competitive ratio exactly $R$, and that $R$
can be written in the form
\[
R \;=\; \frac{a + b\sqrt{c}}{d},
\]
where $a,b,c,d$ are positive integers, $c$ is squarefree, and $\gcd(a,b,d)=1$.

Determine $R$ as a decimal rounded to exactly $4$ decimal places.
```

## Golden answer

- **Answer:** `3.3904`
- **Form:** numeric, rounded to exactly 4 decimal places
- **Length check:** 6 chars ≤ 60 ✅ — **Not in {-1,0,1,Yes,No}** ✅
- **Exact closed form:** $R=(23+\sqrt{17})/8=3.390388\ldots$

## Full solution (verifiable) — raw LaTeX

```latex
\textbf{Step 1: Target ratio from the potential program.}
The amortized-analysis constraints (Assumption 4.11 and Theorem 14) force
\[
R \;=\; \frac{23+\sqrt{17}}{8}.
\]

\textbf{Step 2: Numerical evaluation.}
$\sqrt{17}=4.1231056256\ldots$, so
\[
R=\frac{23+4.1231056256\ldots}{8}=\frac{27.1231056256\ldots}{8}
=3.3903882032\ldots
\]

\textbf{Step 3: Round.}
To four decimal places: $R=\boxed{3.3904}$.
```

## Why the paper helps (Run III > Run I rationale)

Deriving $R$ from scratch requires the full Fpm state-transition analysis and the
non-linear program over six potentials. The paper proves
$R=\tfrac{1}{8}(23+\sqrt{17})$; a solver still must evaluate the radical expression.
The abstract's ``3.3904'' alone does not certify the answer without the derivation —
models often mis-round or confuse this with the previous bound of $4$.

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

- **Easier:** give $R=(23+\sqrt{17})/8$ explicitly and ask only for 4 d.p.
- **Harder:** ask for the radical form integers $a,b,c,d$ (answer `23,1,17,8`).
