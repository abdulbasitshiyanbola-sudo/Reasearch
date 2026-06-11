# Task CS-002 — Expected duration of a biased gambler's ruin

## Metadata

- **Task ID:** CS-002
- **Domain / Subdomain:** Computer Science / Discrete Probability →
  Random walks (gambler's ruin, expected absorption time)
- **Workflow used:** Alternative (problem designed first, then matched to a source)
- **Author:** (trainer)
- **Date:** 2026-06-11

## Source paper

- **Title:** *Mathematics for Computer Science*
- **Author(s):** Eric Lehman, F. Thomson Leighton, Albert R. Meyer
- **Venue / Location:** Open textbook (MIT 6.042), revised 2015/2017
- **URL:** <https://people.csail.mit.edu/meyer/mcs.pdf>
- **License:** CC BY-SA 3.0
- **Which result the paper supplies:** The "Random Walks" chapter derives, for the
  biased gambler's ruin, both the ruin probability and the **expected number of
  steps** until absorption, including the $p \neq q$ closed form built from the ratio
  $(q/p)$. It also sets up the first-step (one-step) recurrence used below.

## Problem statement (self-contained, single question, LaTeX)

A gambler starts with a bankroll of $20$ dollars and repeatedly plays independent,
identical rounds. In each round the gambler gains $1$ dollar with probability $0.45$
and loses $1$ dollar with probability $0.55$. Play continues until the bankroll first
reaches either $0$ dollars (ruin) or $50$ dollars (the target), at which moment play
stops. Let the random variable $T$ be the total number of rounds played until play
stops. Compute the expected value $\mathbb{E}[T]$, rounded to four significant
figures.

## Golden answer

- **Answer (≤ 60 chars):** `198.8`
- **Character count:** 5
- **Form / rounding convention:** decimal, rounded to 4 significant figures

## Verifiable final solution

With $p=0.45$, $q=0.55$, $r=q/p=11/9$, start $i=20$, target $N=50$:
$$\mathbb{E}[T] = \frac{i}{q-p} - \frac{N}{q-p}\cdot\frac{1-r^{\,i}}{1-r^{\,N}}
= 198.8072\ldots \Rightarrow 198.8.$$
Reproduced by `verify/verify_answers.py` (`check_task2`), which also solves the exact
absorbing-chain linear system $D_x = 1 + pD_{x+1} + qD_{x-1}$ (with $D_0=D_N=0$) over
the rationals and confirms it matches the closed form.

## Full solution

Let $D_x$ denote the expected number of remaining rounds when the current bankroll is
$x$, for $0 \le x \le N=50$. Absorption gives the boundary conditions
$D_0 = D_N = 0$. Conditioning on the first round (first-step analysis), for
$1 \le x \le N-1$,
$$D_x = 1 + p\,D_{x+1} + q\,D_{x-1}, \qquad p=0.45,\ q=0.55.$$

This is a linear recurrence with constant coefficients. Its general solution is the
sum of a particular solution and the homogeneous solution. Because $p \neq q$, a
particular solution is linear, $D_x^{\text{part}} = \frac{x}{q-p}$, and the
homogeneous solution is $A + B\,r^{x}$ with $r = q/p$. Imposing $D_0 = D_N = 0$ and
solving for $A,B$ yields
$$D_x = \frac{x}{q-p} - \frac{N}{q-p}\cdot\frac{1 - r^{\,x}}{1 - r^{\,N}}.$$

Substituting $x=i=20$, $N=50$, $q-p = 0.10$, and $r = 0.55/0.45 = 11/9$:
$$\mathbb{E}[T] = D_{20} = 200 - 500\cdot\frac{1 - (11/9)^{20}}{1 - (11/9)^{50}}
= 198.8072\ldots \approx \boxed{198.8}.$$

(The exact value is the rational number
$\tfrac{20789717569770748973346250889551164400060000}{104572250999317156571202037596291497938001}$,
which equals $198.80721\ldots$)

## Why this fits the difficulty profile

- **Hard without the paper (Run I):** the expected-duration formula for the *biased*
  walk is the one models most often get wrong. Common failures: using the symmetric
  result $\mathbb{E}[T]=i(N-i)$ (valid only for $p=\tfrac12$), getting the sign of
  $q-p$ backwards, or mixing up which exponent ($i$ vs. $N$) carries the $(q/p)$
  ratio. Any of these yields a wrong number.
- **Run II (search helped):** the recurrence and its solution are standard, so the
  problem is genuinely self-contained and reachable with careful work or search.
- **Easier with the paper (Run III):** the source gives the exact biased-walk
  expected-duration formula, so the solver only has to substitute numbers correctly.
- **Self-containment:** all probabilities, the start value, both absorbing barriers,
  and the stopping rule are stated; a probability expert can derive the answer
  unaided.

## Difficulty knobs (to tune pass rates on the Eval Platform)

- Move $p$ closer to $0.5$ (e.g. $0.48$): the bias correction term shrinks, making the
  symmetric-formula shortcut *almost* right and thus a more tempting trap.
- Increase $N$ and the gap $N-i$ to enlarge the $(q/p)^N$ magnitudes and stress the
  arithmetic.
- Ask instead for the **probability of reaching the target before ruin**, or for the
  expected duration *conditioned on ruin*, to add a reasoning step.

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
