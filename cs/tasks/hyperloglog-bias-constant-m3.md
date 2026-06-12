# Task: Exact bias-correction constant of HyperLogLog with 3 registers

## Metadata

- **Subdomain (A1 taxonomy):** Randomized & Streaming Algorithms (analysis of cardinality estimators)
- **Difficulty tranche:** Full Difficulty (calibrate on Eval Platform; see notes)
- **Author:** _(trainer — finalize and own per §1.6.3 before submission)_
- **Date:** 2026-06-11

## Source paper (§1.3)

- **Title:** HyperLogLog: the analysis of a near-optimal cardinality estimation algorithm
- **Authors / Year:** P. Flajolet, É. Fusy, O. Gandouet, F. Meunier, 2007
- **Venue / ID:** AofA 2007, DMTCS Proceedings vol. AH, pp. 127–146; DOI 10.46298/dmtcs.3545
- **License:** **CC BY 4.0** ✅ (DMTCS distributes all articles under CC BY 4.0; confirmed via
  DOAJ and the journal's open-access policy page. Trainer: re-confirm the specific volume's
  license string on the article page before submitting.)
- **URL:** https://doi.org/10.46298/dmtcs.3545
- **Which result/lemma/technique helps?** The paper's Poisson–Mellin "average-case" analysis
  yields the integral representation of the bias-correction constant,
  \(\alpha_m = \dfrac{1}{m\,J_0(m)}\) with \(J_0(m)=\int_0^\infty\!\big(\log_2\tfrac{2+u}{1+u}\big)^m\,du\),
  and even gives the closed form \(J_0(3)=\tfrac{3\zeta(3)}{4(\ln 2)^3}-2\). With the paper, the
  solver is handed the integral framework and the \(J_0(3)\) closed form, so only an arithmetic
  evaluation remains. The number \(\alpha_3\) itself is **not stated anywhere** in the paper (it
  tabulates only the deployed constants \(\alpha_{16}=0.673,\ \alpha_{32}=0.697,\ \alpha_{64}=0.709\)
  and the limit \(1/(2\ln 2)\)), so it is not a lookup.

## Problem prompt (what the model sees) — raw LaTeX

```latex
\textbf{Problem.}
Consider the following cardinality (distinct-count) estimator over a stream. Fix an
integer $m \ge 3$ of registers. A hash maps each stream item to an i.i.d.\ uniform real
in $[0,1]$, written in binary as $0.b_1 b_2 b_3\cdots$. The first $\lceil \log_2 m\rceil$
bits select one of the $m$ registers (assume the substream assignment is i.i.d.\ uniform
over the $m$ registers), and for the remaining bit-string $w=w_1 w_2\cdots$ define
$\rho(w)$ to be the position of its leftmost $1$ (so $\rho(1\cdots)=1$, $\rho(001\cdots)=3$).
Each register $M[j]$ stores the maximum value of $\rho$ seen among the items routed to it.
After processing a stream of $n$ distinct items, the estimator outputs
\[
E \;=\; \alpha_m \, m^2 \Big/ \sum_{j=1}^{m} 2^{-M[j]} .
\]
Work in the idealized Poisson model in which the number of items is $\mathrm{Poisson}(n)$
and, conditionally, each is routed independently and uniformly to one of the $m$ registers;
let $n\to\infty$. The constant $\alpha_m$ is defined as the unique value that makes $E$
asymptotically unbiased, i.e.\ $\mathbb{E}[E]/n \to 1$ as $n\to\infty$.

Compute the exact value of $\alpha_m$ for $m = 3$. Report a decimal rounded to exactly
$4$ decimal places.
```

## Golden answer

- **Answer:** `0.4714`
- **Form:** numeric, rounded to exactly 4 decimal places
- **Length check:** 6 chars ≤ 60 ✅ — **Not in {-1,0,1,Yes,No}** ✅
- **Exact closed form:** \(\alpha_3 = \dfrac{4(\ln 2)^3}{\,9\,\zeta(3) - 24(\ln 2)^3\,}\)
- **Full-precision value:** \(\alpha_3 = 0.471385736808\ldots\)

## Full solution (verifiable) — raw LaTeX

```latex
\textbf{Step 1: Poisson expectation of a single register's contribution.}
Each register receives a $\mathrm{Poisson}(\lambda)$ number of items with $\lambda=n/m$.
A register's value is $M=\max \rho$ over its items, and $\Pr[\rho = k] = 2^{-k}$. Hence
$\Pr[M \le k] = \exp(-\lambda 2^{-k})$ (no item has $\rho>k$), so $M$ is the maximum of a
Poisson number of geometric variables.

\textbf{Step 2: The harmonic-sum indicator and Mellin analysis.}
Let $Z=\sum_{j} 2^{-M[j]}$. By register independence, $\mathbb{E}[E]=\alpha_m m^2\,
\mathbb{E}[1/Z]$. Following the Poisson--Mellin ("analytic depoissonization") analysis,
the relevant Poisson average admits the integral representation: as $\lambda\to\infty$,
\[
\mathbb{E}\!\Big[\tfrac{1}{Z}\Big] \sim \frac{1}{m\,\lambda}\cdot \frac{1}{m\,J_0(m)} \cdot m ,
\qquad
J_0(m) \;=\; \int_0^\infty \Big(\log_2\tfrac{2+u}{1+u}\Big)^{m}\,du ,
\]
so that imposing $\mathbb{E}[E]/n\to1$ forces
\[
\boxed{\;\alpha_m=\frac{1}{m\,J_0(m)}\;}.
\]
(The integral arises because the leftmost-one statistic makes $2^{-M}$ behave, in the
Mellin domain, like the kernel $\log_2\frac{2+u}{1+u}$ raised to the power $m$.)

\textbf{Step 3: Evaluate $J_0(3)$ in closed form.}
The integrand's Mellin transform has poles producing values of $\zeta$ at integers; for the
cube one obtains the closed form
\[
J_0(3)=\frac{3\,\zeta(3)}{4(\ln 2)^3}-2 = 0.707134958\ldots
\]

\textbf{Step 4: Assemble.}
\[
\alpha_3=\frac{1}{3\,J_0(3)}
=\frac{1}{3\big(\tfrac{3\zeta(3)}{4(\ln 2)^3}-2\big)}
=\frac{4(\ln 2)^3}{9\,\zeta(3)-24(\ln 2)^3}
=0.4713857\ldots
\]
Rounded to $4$ decimal places:
\[
\boxed{\alpha_3 = 0.4714}.
\]
```

## Why the paper helps (Run III > Run I rationale)

Without the paper the model must (1) set up the Poisson model for the leftmost-one maximum,
(2) handle the coupling introduced by the **harmonic-style** sum \(Z=\sum 2^{-M[j]}\) (this is
exactly what makes HyperLogLog harder to analyze than LogLog), (3) carry out the Mellin /
analytic-depoissonization asymptotics to obtain the integral representation, (4) identify
\(\alpha_m = 1/(m J_0(m))\), and (5) evaluate \(J_0(3)\) — a multi-step research-level
derivation with several independent failure points. With the paper, the integral framework
and the closed form \(J_0(3)=\tfrac{3\zeta(3)}{4(\ln 2)^3}-2\) are supplied, collapsing the
task to a one-line arithmetic evaluation. The specific number \(\alpha_3\) is tabulated
nowhere (the paper lists only \(m\in\{16,32,64\}\) and the limit), so neither memorization
nor lookup yields it directly.

## Verification performed

- Reproduced the paper's deployed constants from \(\alpha_m=1/(mJ_0(m))\):
  \(\alpha_{16}=0.67310,\ \alpha_{32}=0.69712,\ \alpha_{64}=0.70921\), and
  \(\alpha_\infty=1/(2\ln 2)=0.72135\).
- Cross-checked the paper's stated closed forms: \(J_0(2)=\pi^2/(6L^2)-2\) and
  \(J_0(3)=3\zeta(3)/(4L^3)-2\) (\(L=\ln 2\)) match numerical integration to ≥10 digits.
- Golden value: \(\alpha_3 = 1/(3 J_0(3)) = 4L^3/(9\zeta(3)-24L^3) = 0.471385736808\),
  rounds to \(0.4714\). (See `cs/verify/verify_tasks.py`.)

## Difficulty notes & fallback (read before calibrating)

- **Run-I risk:** the relation \(\alpha_m=1/(m\int_0^\infty(\log_2\frac{2+u}{1+u})^m du)\) is
  documented (paper + some expository sources), so a strong model *might* reconstruct it
  without the paper. Calibrate Run I on the Eval Platform; if Run I exceeds the Full gate
  (≤ 12.5%), either (a) submit under the **Easier Difficulty** tranche, or (b) switch to the
  harder target below.
- **Harder fallback (better Run-I separation):** ask instead for the **standard-error
  constant** \(\beta_m\) at a small \(m\). The paper supplies the *method* and the limit
  \(\beta_\infty=\sqrt{3\ln 2-1}=1.03896\) but does **not** tabulate finite-\(m\) values nor the
  closed form of the variance integral \(J_1(m)=\int_0^\infty u\,(\log_2\frac{2+u}{1+u})^m du\),
  so \(\beta_m\) for small \(m\) is much less memorizable.
  > Caveat: reproduce the exact \(\beta_m\) formula against the paper's stated
  > \(\beta_{16}=1.046\) **before** using this fallback — a naive
  > \(\beta_m=\sqrt{m(J_1/J_0^2-1)}\) reproduces the correct limit but did **not** match the
  > paper's \(\beta_{16}\) in our check, indicating the finite-\(m\) variance expression needs
  > the paper's Section 3 derivation to be transcribed carefully. Do not ship a \(\beta_m\)
  > golden answer until it matches the paper's \(\beta_{16}=1.046\).

## Novelty check (A2)

- **Perplexity results URL:** _(trainer to run and paste)_
- **Confirmed not a known/online question and not AI-generated:** _(trainer to confirm and own per §1.6.3)_

## Pass-rate results (Eval Platform — Opus 4.8 or latest)

| Run | Paper? | Web? | Passes / attempts | Pass rate | Gate (Full) | Gate (Easier) |
| --- | --- | --- | --- | --- | --- | --- |
| I   | No  | No  | _(run)_ /16 | — | ≤ 12.5% (0–2) | ≤ 50% (0–8) |
| II  | No  | Yes | _(run)_ /16 | — | no restriction | no restriction |
| III | Yes | No  | _(run)_ /16 | — | ≤ 50% (1–8) | ≤ 80% (1–12) |

- **Run I OR Run II has ≥ 1 pass:** _(confirm; else extend to ≤ 32 attempts)_
- **Run III passes > Run I passes:** _(confirm)_
- **Prompt + answer consistent across run1/run2/run3 (Taiga):** _(confirm)_
