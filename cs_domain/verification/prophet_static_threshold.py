"""Verification for the k-unit prophet inequality static-threshold guarantee.

Source result (CC BY 4.0): Jiang, Ma, Zhang, "Tightness without Counterexamples:
A New Approach and New Results for Prophet Inequalities", arXiv:2205.00588
(recovering Chawla, Devanur, Lykouris 2020). The optimal static (oblivious)
threshold guarantee for k units, against the prophet, equals phi_k, where the
worst-case distribution is Poisson and phi_k is the common value of

    mu_k(X)    = (1/k) * E[min(X, k)]            (expected fraction of units sold)
    delta_k(X) = P[X <= k - 1]                   (prob. supply does not sell out)

evaluated at the unique rate lambda_k with mu_k(X^lambda) = delta_k(X^lambda),
X^lambda ~ Poisson(lambda).

This script solves for lambda_k by bisection and reports phi_k, with no external
dependencies (pure `math`), so the golden answers can be checked independently.
"""

import math


def poisson_pmf(i: int, lam: float) -> float:
    return math.exp(-lam) * lam**i / math.factorial(i)


def delta_k(lam: float, k: int) -> float:
    """P[X <= k-1] for X ~ Poisson(lam)."""
    return sum(poisson_pmf(i, lam) for i in range(k))


def mu_k(lam: float, k: int) -> float:
    """(1/k) * E[min(X, k)] for X ~ Poisson(lam).

    E[min(X,k)] = sum_{i=0}^{k-1} i*P[X=i] + k*P[X>=k].
    """
    head = sum(i * poisson_pmf(i, lam) for i in range(k))
    tail = k * (1.0 - delta_k(lam, k))
    return (head + tail) / k


def solve_lambda(k: int, lo: float = 1e-9, hi: float = 1e6, iters: int = 200) -> float:
    """Bisection: g(lam) = mu_k - delta_k is increasing, negative near 0, positive at infinity."""
    def g(lam: float) -> float:
        return mu_k(lam, k) - delta_k(lam, k)

    assert g(lo) < 0 < g(hi)
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if g(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main() -> None:
    paper_table = {1: 0.5, 2: 0.585, 3: 0.630, 4: 0.660, 5: 0.682, 6: 0.698}
    print(f"{'k':>2}  {'lambda_k':>12}  {'phi_k':>12}  {'phi_k(3sf)':>10}  {'paper':>7}")
    for k in range(1, 13):
        lam = solve_lambda(k)
        phi = delta_k(lam, k)
        # sanity: both sides agree at the root
        assert abs(phi - mu_k(lam, k)) < 1e-9
        paper = f"{paper_table[k]:.3f}" if k in paper_table else "-"
        sf3 = float(f"{phi:.3g}")  # 3 significant figures
        print(f"{k:>2}  {lam:>12.6f}  {phi:>12.6f}  {sf3:>10.3f}  {paper:>7}")


if __name__ == "__main__":
    main()
