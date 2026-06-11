"""
Verification script for task CS-001.

Computes the l=1 orientability thresholds c_k* of fully random k-uniform
hypergraphs (equivalently, the load thresholds of k-ary cuckoo hashing /
the constructibility thresholds of k-XOR retrieval data structures) and
re-derives the golden answer.

The threshold is characterized (Fountoulakis & Panagiotou; see also the
source paper's Table 1) by:

    xi*  is the unique positive root of   k = xi*(e^{xi*} - 1) / (e^{xi*} - 1 - xi*)
    c_k* = xi* / ( k * (1 - e^{-xi*})^{k-1} )

No third-party dependencies are required (pure standard library).
"""

from math import exp


def _bisect(f, a, b, iters=300):
    fa = f(a)
    for _ in range(iters):
        m = 0.5 * (a + b)
        fm = f(m)
        if fa * fm <= 0.0:
            b = m
        else:
            a, fa = m, fm
    return 0.5 * (a + b)


def xi_star(k):
    """Unique positive root of k = xi*(e^xi - 1)/(e^xi - 1 - xi)."""
    g = lambda x: x * (exp(x) - 1.0) / (exp(x) - 1.0 - x) - k
    return _bisect(g, 1e-12, 300.0)


def c_star(k):
    """l=1 orientability threshold of the random k-uniform hypergraph."""
    x = xi_star(k)
    return x / (k * (1.0 - exp(-x)) ** (k - 1))


def excess_overhead(k):
    """Excess memory overhead o_k = 1/c_k* - 1 (extra cells per stored key)."""
    return 1.0 / c_star(k) - 1.0


def solve():
    # Values published in the source paper's Table 1 (rounded to 10 dp),
    # used here purely as an independent cross-check.
    paper_table = {
        3: 0.9179352767,
        4: 0.9767701649,
        5: 0.9924383913,
        6: 0.9973795528,
        7: 0.9990637588,
    }

    print("k   c_k* (computed)   c_k* (paper)     |diff|        o_k=1/c_k*-1")
    for k in range(3, 8):
        ck = c_star(k)
        print(
            f"{k}   {ck:.10f}    {paper_table[k]:.10f}   "
            f"{abs(ck - paper_table[k]):.2e}    {excess_overhead(k)*100:.4f}%"
        )

    o = {k: excess_overhead(k) for k in range(3, 8)}

    print("\nIncremental absolute saving from k -> k+1 (cells/key):")
    for k in range(3, 7):
        d = o[k] - o[k + 1]
        print(f"  Delta_{k} = o_{k} - o_{k+1} = {d:.6f}   (< 0.01 ? {d < 0.01})")

    # Designer's rule: smallest k >= 3 such that going to k+1 saves
    # less than 0.01 cells per key.
    chosen_k = min(k for k in range(3, 7) if (o[k] - o[k + 1]) < 0.01)
    answer_pct = o[chosen_k] * 100.0

    print(f"\nChosen k = {chosen_k}")
    print(f"Excess overhead o_{chosen_k} = {answer_pct:.6f}%")
    print(f"GOLDEN ANSWER (3 significant figures) = {answer_pct:.3g}%")
    return round(answer_pct, 3)


if __name__ == "__main__":
    ans = solve()
    assert abs(ans - 0.762) < 1e-9, f"unexpected answer: {ans}"
    print("\nOK: golden answer reproduced -> 0.762%")
