# Task 01 — Optimal static-threshold guarantee for the 10-unit prophet inequality

- **Subdomain (A1):** CS → Algorithmic Game Theory / Economics & Computation → Prophet inequalities (optimal stopping, online allocation)
- **Source paper:** J. Jiang, W. Ma, J. Zhang, "Tightness without Counterexamples: A New Approach and New Results for Prophet Inequalities", arXiv:2205.00588 [cs.GT], 2023 (v3).
- **License:** **CC BY 4.0** — verified: `curl -s https://arxiv.org/abs/2205.00588 | grep licenses` → `licenses/by/4.0/`.
- **Paper URL:** https://arxiv.org/abs/2205.00588
- **Workflow:** Traditional (paper contains the key tight characterization; problem applies it).
- **Novelty check (A2) Perplexity URL:** _TODO — run novelty check and paste URL before submission._

---

## Prompt (exact text submitted)

> A seller has $k = 10$ identical, indivisible units of a single good. A finite but
> arbitrary number $n$ of buyers arrive one at a time, in an order chosen by an
> adversary. Buyer $i$ has value $v_i \ge 0$ drawn independently from a distribution
> $F_i$ that is known to the seller in advance; the $F_i$ need not be identical. When
> a buyer arrives, the seller observes the realized value $v_i$ and must immediately
> and irrevocably either sell one remaining unit to that buyer (collecting $v_i$) or
> reject the buyer. There is no recall and units cannot be replenished.
>
> Consider only *static threshold* policies: before any buyer arrives, the seller
> commits to a single threshold $\tau \ge 0$ (which may depend on the known
> distributions $\{F_i\}$ but not on the realized values), and then sells one unit to
> every arriving buyer whose value satisfies $v_i \ge \tau$, as long as units remain.
> The benchmark is the offline optimum, which observes all $n$ realized values and
> keeps the $k$ largest.
>
> Let $c$ be the largest constant for which there exists a static threshold policy
> whose expected collected value is at least $c$ times the expected benchmark value,
> simultaneously for every number of buyers $n$, every collection of independent
> distributions $\{F_i\}$, and every adversarial arrival order. Determine $c$ for
> $k = 10$. Give your answer as a decimal rounded to three significant figures.

## Golden answer

```
0.742
```

Acceptable equivalent forms (for grader): `0.742` (also written `c ≈ 0.742`).
Not acceptable: `0.745` (the IID single-choice constant), `0.5`, `1 - 1/e ≈ 0.632`.

## Full solution

**Setup.** A static threshold policy with threshold $\tau$ sells to every arriving
buyer with $v_i \ge \tau$ until the 10 units run out. Write $X_\tau = \#\{i : v_i \ge
\tau\}$ for the (random) number of *interested* buyers. Because each $v_i \ge \tau$
independently with probability $q_i = \Pr[v_i \ge \tau]$, $X_\tau$ is a sum of
independent Bernoulli variables (a Poisson-binomial variable).

**Welfare decomposition (Samuel-Cahn style).** Upper-bound the benchmark by
revenue-at-$\tau$ plus excess utility:
$\mathrm{OPT} \le R_k(\tau) + U(\tau)$ where $R_k(\tau) = k\tau$ is the revenue if all
$k$ units sell at $\tau$ and $U(\tau) = \sum_i \max(0, v_i - \tau)$. The static price
$\tau$ collects:

- expected revenue $\ge \mu_k(\tau)\,R_k(\tau)$, where
  $\mu_k(\tau) = \tfrac{1}{k}\,\mathbb{E}[\min\{X_\tau, k\}]$ is the expected fraction
  of units sold;
- expected buyer utility $\ge \delta_k(\tau)\,U(\tau)$, where
  $\delta_k(\tau) = \Pr[X_\tau \le k-1]$ is the probability the supply does **not**
  sell out (so an arriving buyer still finds a unit).

Hence the policy secures at least a $\phi_k(\tau) = \min\{\mu_k(\tau),\,\delta_k(\tau)\}$
fraction of the upper bound, and the best static threshold maximizes this.

**Worst-case instance is Poisson.** Minimizing $\phi_k$ over all instances, the
binding worst case is a large number of i.i.d. interested/not-interested buyers, so
$X_\tau \to X \sim \mathrm{Poisson}(\lambda)$. Then with $X \sim \mathrm{Poisson}(\lambda)$:

$$\mu_k(\lambda) = \frac{1}{k}\,\mathbb{E}[\min\{X,k\}], \qquad
  \delta_k(\lambda) = \Pr[X \le k-1] = \sum_{i=0}^{k-1} e^{-\lambda}\frac{\lambda^i}{i!}.$$

$\mu_k$ increases from $0$ to $1$ and $\delta_k$ decreases from $1$ to $0$ as
$\lambda$ grows, so the optimal threshold equalizes them: choose $\lambda_k$ with

$$\frac{1}{k}\,\mathbb{E}[\min\{X,k\}] \;=\; \Pr[X \le k-1], \qquad
  c \;=\; \phi_k \;=\; \delta_k(\lambda_k) = \mu_k(\lambda_k). \tag{$\ast$}$$

The source paper (Jiang–Ma–Zhang) proves this static-threshold scheme is **optimal**:
no static threshold policy — oblivious or not — can guarantee more than $\phi_k$ in the
worst case. So the constant asked for is exactly $c = \phi_k$.

**Solve for $k = 10$.** Equation $(\ast)$ is monotone on each side, so the root is
unique. Solving numerically gives $\lambda_{10} \approx 7.7911$ and

$$c = \phi_{10} = 0.742178\ldots \;\Rightarrow\; \boxed{0.742} \text{ (3 s.f.).}$$

**Cross-check.** The same procedure reproduces the published small-$k$ values
exactly: $\phi_1=0.5,\ \phi_2=0.5859,\ \phi_3=0.6309,\ \phi_4=0.6605,\ \phi_5=0.6821,\
\phi_6=0.6989$. For $k=10$ it continues to $0.742178$. (See verification script.)

## Why the paper helps (and the answer is not a lookup)

- The paper supplies the **key tight characterization**: the worst case is Poisson
  and the optimal static-threshold guarantee is the crossing value of
  $\tfrac1k\mathbb{E}[\min\{X,k\}]$ and $\Pr[X\le k-1]$ — and, crucially, that *no*
  static threshold policy beats it. With this, the solver only needs to solve $(\ast)$.
- It is **not** a lookup: the paper's worked tables stop at $k=6$ (Chawla et al.'s
  numbers) and the paper's own Table 1 tabulates a *different* quantity (the IID
  adaptive DP/Proph ratio). $k=10$ for the **non-IID static-threshold** ratio is not
  printed anywhere, so the solver must actually solve the transcendental equation.

## Pass-rate plan (Full difficulty)

| Run | Paper | Web | Predicted passes /16 | Rationale |
|-----|-------|-----|----------------------|-----------|
| I   | No    | No  | 0–2  | With no tools the model must (a) discover the Poisson worst case for multi-unit static thresholds and (b) solve a transcendental equation by hand for $k=10$. Most attempts will instead emit a famous-but-wrong constant ($0.5$, $1-1/e$, or the IID $0.745$). |
| II  | No    | Yes | unrestricted | Search may surface the characterization / small-$k$ tables; the model can then extrapolate to $k=10$. No restriction applies. |
| III | Yes   | No  | 1–8  | The paper gives the exact characterization, reducing the task to solving $(\ast)$ for $k=10$ — doable but still requires careful numerics by hand, so well short of automatic. |

- **Run III > Run I:** the paper removes the hardest step (identifying the Poisson
  worst case and the optimality of the scheme), leaving a mechanical-but-nontrivial solve.
- **Run I or Run II ≥ 1 pass:** the problem is fully self-contained; a domain expert
  (or a web-assisted run) can derive $(\ast)$ and compute $0.742$.

> These are predictions. Confirm on the Eval Platform (Opus 4.8, 16 attempts/run)
> and adjust $k$ if Run III exceeds 50% or Run I exceeds 12.5%. Larger $k$ (e.g.
> $k=12 \Rightarrow 0.756$) further reduces lookup risk if needed.

## DOs/DONTs compliance

- [x] Self-contained / expert-solvable without paper
- [x] Single unambiguous answer (`0.742`), 5 chars ≤ 60, not in {-1,0,1,Yes,No}
- [x] Precision specified ("three significant figures"); robust away from rounding boundary
- [x] LaTeX renders; exactly one question; no phrase "in the paper"
- [x] Not MCQ / not fill-in-the-blank
- [x] License qualifies (CC BY 4.0); paper usage 1 of ≤ 3

## Verification

Script: [`../verification/prophet_static_threshold.py`](../verification/prophet_static_threshold.py)
— run `python3 prophet_static_threshold.py` (pure standard library). It solves
$(\ast)$ by bisection for $k = 1\ldots12$, confirms the published $k\le 6$ values, and
prints $\phi_{10} = 0.742178 \Rightarrow 0.742$.
