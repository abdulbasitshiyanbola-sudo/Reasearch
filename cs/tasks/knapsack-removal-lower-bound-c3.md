# Task: Adversarial lower-bound constant for 3-round unbounded knapsack with removal

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
- **Which result/lemma/technique helps?** Theorem 3 and Equation (7): the adversarial
  lower-bound construction parameterized by Sylvester's sequence, together with the
  reduction of the tight ratio $c_N$ to a degree-$N$ polynomial in $c_N$. The paper
  reports only $c_5 > 1.5877$ numerically; it does **not** state $c_3$.

## Problem prompt (what the model sees) — raw LaTeX

```latex
\textbf{Problem.}
Consider the \emph{Online Unbounded Knapsack Problem with Removal}. Items
$x=(w,v)$ with weight $w\in(0,1]$ and value $v>0$ arrive one at a time. An online
algorithm may pack any number of copies of the current item, and may remove arbitrary
subsets of packed items at any time (at zero cost), subject to total packed weight
$\le 1$. The goal is to maximize total packed value. A deterministic algorithm is
$c$-competitive if $c\cdot v(\mathrm{Alg}(I))\ge v(\mathrm{Opt}(I))$ for every instance
$I$.

Define Sylvester's sequence by $a_1=2$ and, for $n\ge 2$,
\[
a_n \;=\; 1 + \prod_{i=1}^{n-1} a_i \;=\; a_{n-1}(a_{n-1}-1)+1 .
\]
For an integer $N\ge 3$, an adversary may present the following $2N-1$ items in order
(using a sufficiently small $\varepsilon>0$):
\begin{itemize}
\item for $i=N,N-1,\ldots,3$: first $x_i=\bigl(\tfrac{1}{a_i}+2\varepsilon,\;
  v_i/(a_i-1)\bigr)$, then $y_i=\bigl(1-\tfrac{1}{a_i}-\varepsilon,\;v_{i-1}\bigr)$;
\item then $x_2=\bigl(\tfrac{1}{3}+2\varepsilon,\;v_1/2\bigr)$ and
  $y_2=\bigl(\tfrac{2}{3}-\varepsilon,\;v_2\bigr)$;
\item finally $z=\bigl(\tfrac{1}{2}+\varepsilon,\;v_2\bigr)$.
\end{itemize}
The values $v_1,\ldots,v_N$ and the constant $c_N>1$ satisfy the system
\begin{align*}
v_N &= 1,\\
c_N &= \frac{v_{i-1}+v_i/(a_i-1)}{v_i}\quad(3\le i\le N),\\
c_N &= \frac{v_2+v_1/2}{v_1},\\
c_N &= \frac{v_2+v_1/2+\sum_{i=3}^{N} v_i/(a_i-1)}{v_2},
\end{align*}
and the single-variable polynomial obtained by eliminating $v_1,\ldots,v_{N-1}$:
\[
\prod_{i=1}^{N}\!\Bigl(c_N-\frac{1}{a_i-1}\Bigr)
= \frac{1}{2}\prod_{i=3}^{N}\!\Bigl(c_N-\frac{1}{a_i-1}\Bigr)
+ \Bigl(c_N-\frac{1}{2}\Bigr)\sum_{i=3}^{N}\frac{1}{a_i-1}
  \prod_{j=i+1}^{N}\!\Bigl(c_N-\frac{1}{a_j-1}\Bigr).
\]
For $N=3$, let $c_3$ be the \emph{largest} real root $>1$ of this polynomial. Any
deterministic online algorithm has competitive ratio at least $c_3$ on some instance.

Determine $c_3$. Report a decimal rounded to exactly $4$ decimal places.
```

## Golden answer

- **Answer:** `1.5806`
- **Form:** numeric, rounded to exactly 4 decimal places
- **Length check:** 6 chars ≤ 60 ✅ — **Not in {-1,0,1,Yes,No}** ✅
- **Full-precision value:** $c_3 = 1.580587027606\ldots$

## Full solution (verifiable) — raw LaTeX

```latex
\textbf{Step 1: Sylvester numbers for $N=3$.}
$a_1=2$, $a_2=3$, $a_3=7$.

\textbf{Step 2: Build the degree-$3$ polynomial.}
Write $r=c_3$. For $N=3$ the elimination identity (only the $i=3$ term survives in
the sum) is
\[
(r-1)\Bigl(r-\tfrac{1}{2}\Bigr)\Bigl(r-\tfrac{1}{6}\Bigr)
= \frac{1}{2}\Bigl(r-\tfrac{1}{6}\Bigr)
+ \Bigl(r-\tfrac{1}{2}\Bigr)\cdot\frac{1}{6}.
\]
Multiply both sides by $12$:
\[
(r-1)(2r-1)(6r-1)=6\Bigl(r-\tfrac{1}{6}\Bigr)+2\Bigl(r-\tfrac{1}{2}\Bigr)=8r-2.
\]
Expanding the left side gives $12r^3-20r^2+9r-1=8r-2$, hence
\[
12r^3-20r^2+r+1=0
\qquad\Longleftrightarrow\qquad
r^3-\tfrac{5}{3}r^2+\tfrac{1}{12}r+\tfrac{1}{12}=0.
\]

\textbf{Step 3: Largest root $>1$.}
This cubic has one real root greater than $1$. Numerically,
$r\approx 1.5805870276$, so rounded to four decimal places $c_3=\boxed{1.5806}$.
```

## Why the paper helps (Run III > Run I rationale)

Without the paper, a solver must independently discover Sylvester's sequence, the
multi-phase adversarial item schedule, and the value-recurrence system that collapses
to Equation (7). The paper supplies the construction template and the elimination
identity; the solver still must instantiate $N=3$, expand the polynomial, and
identify the correct root — none of which is a direct lookup (the paper only reports
$c_5>1.5877$).

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

- **Easier:** ask for $c_2$ (degree-$2$ polynomial; answer $1.75$).
- **Harder:** ask for $c_4$ (answer $1.5877$ to 4 d.p.).
