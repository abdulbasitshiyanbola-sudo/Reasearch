#!/usr/bin/env python3
"""Reproducible numeric verification for the CS-domain tasks.

Run:  python3 cs/verify/verify_tasks.py

Requires: mpmath (high-precision). Install with `pip install mpmath`.

Each check re-derives a task's golden answer from first principles (no value is
hard-coded as an answer; we only assert that the independent re-derivation matches
the value recorded in the task file). This lets a reviewer confirm that every
golden answer in `cs/tasks/` (and the `cs/examples/` demo) is correct.
"""

import sys

try:
    import mpmath as mp
except ImportError:  # pragma: no cover
    sys.exit("This script needs mpmath. Run: pip install mpmath")

mp.mp.dps = 40
L = mp.log(2)

PASS = "PASS"
FAIL = "FAIL"
_failures = []


def check(name, got, expected, tol=mp.mpf("1e-9")):
    ok = abs(mp.mpf(got) - mp.mpf(expected)) <= tol
    status = PASS if ok else FAIL
    if not ok:
        _failures.append(name)
    print(f"  [{status}] {name}: got {mp.nstr(got, 12)}  expected {mp.nstr(expected, 12)}")
    return ok


# ---------------------------------------------------------------------------
# Task: cuckoo-3core-fraction-at-threshold.md
# (3,2)-cuckoo hashing: 3-uniform hypergraph, bucket capacity 2.
# 3-core BP fixed point, threshold = "core edge density == capacity 2".
# ---------------------------------------------------------------------------
def verify_cuckoo():
    print("Task: cuckoo-3core-fraction-at-threshold")

    def system(x, alpha):
        mu = 3 * alpha * x**2
        f1 = x - (1 - mp.e ** (-mu) * (1 + mu))          # x = P[Po(mu) >= 2]
        nu = 1 - mp.e ** (-mu) * (1 + mu + mu**2 / 2)     # P[Po(mu) >= 3]
        f2 = alpha * x**3 - 2 * nu                         # core edge density == 2
        return [f1, f2]

    x, alpha = mp.findroot(system, [mp.mpf("0.97"), mp.mpf("1.97")])
    mu = 3 * alpha * x**2
    nu = 1 - mp.e ** (-mu) * (1 + mu + mu**2 / 2)

    # alpha*/2 must match the published (3,2) cuckoo load threshold 0.9882014140.
    check("(3,2) load threshold alpha*/2", alpha / 2, mp.mpf("0.9882014140"), tol=mp.mpf("1e-9"))
    # core edge density at the solution is exactly the capacity 2.
    check("core edge density alpha*x^3/nu", alpha * x**3 / nu, 2, tol=mp.mpf("1e-12"))
    # golden answer: 3-core vertex fraction at threshold, 4 d.p.
    check("nu* (golden 0.9208)", mp.mpf(mp.nstr(nu, 10)), mp.mpf("0.9208329878"), tol=mp.mpf("1e-7"))
    print(f"    -> nu* = {mp.nstr(nu, 12)}  =>  rounded(4dp) = {mp.nstr(nu, 7)}\n")


def verify_cuckoo_fallback():
    print("Task: cuckoo fallback variant (3,1)")
    # x solves -ln(1-x) = 3x/(3-2x); threshold c* = 1/(x(3-2x)); answer x^2/(3-2x).
    f = lambda x: -mp.log(1 - x) - 3 * x / (3 - 2 * x)
    lo, hi = mp.mpf("0.85"), mp.mpf("0.92")
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    x = (lo + hi) / 2
    c = 1 / (x * (3 - 2 * x))
    ans = x**2 / (3 - 2 * x)
    check("(3,1) threshold c*", c, mp.mpf("0.9179352767"), tol=mp.mpf("1e-9"))
    check("(3,1) fallback answer (0.6329)", mp.mpf(mp.nstr(ans, 10)), mp.mpf("0.6328559"), tol=mp.mpf("1e-6"))
    print(f"    -> answer = {mp.nstr(ans, 12)}  =>  rounded(4dp) = {mp.nstr(ans, 5)}\n")


# ---------------------------------------------------------------------------
# Task: hyperloglog-bias-constant-m3.md
# Bias-correction constant alpha_m = 1/(m * J0(m)),
#   J0(m) = int_0^inf (log2((2+u)/(1+u)))^m du.
# ---------------------------------------------------------------------------
def J(s, m):
    f = lambda u: u**s * (mp.log((2 + u) / (1 + u)) / L) ** m
    return mp.quad(f, [0, 1, 5, 20, 100, mp.inf])


def alpha(m):
    return 1 / (m * J(0, m))


def verify_hyperloglog():
    print("Task: hyperloglog-bias-constant-m3")
    # Framework sanity: reproduce the deployed constants and the limit.
    check("alpha_16 (paper 0.673)", alpha(16), mp.mpf("0.673"), tol=mp.mpf("5e-4"))
    check("alpha_32 (paper 0.697)", alpha(32), mp.mpf("0.697"), tol=mp.mpf("5e-4"))
    check("alpha_64 (paper 0.709)", alpha(64), mp.mpf("0.709"), tol=mp.mpf("5e-4"))
    check("alpha_inf = 1/(2 ln2)", 1 / (2 * L), mp.mpf("0.7213475204"))
    # Closed forms stated in the paper (independent cross-checks of J0).
    check("J0(2) = pi^2/(6 L^2) - 2", J(0, 2), mp.pi**2 / (6 * L**2) - 2, tol=mp.mpf("1e-10"))
    check("J0(3) = 3 zeta(3)/(4 L^3) - 2", J(0, 3), 3 * mp.zeta(3) / (4 * L**3) - 2, tol=mp.mpf("1e-10"))
    # Golden answer: alpha_3, also expressible as 4 L^3 / (9 zeta(3) - 24 L^3).
    a3 = alpha(3)
    a3_closed = 4 * L**3 / (9 * mp.zeta(3) - 24 * L**3)
    check("alpha_3 closed form 4L^3/(9 zeta(3)-24L^3)", a3, a3_closed, tol=mp.mpf("1e-12"))
    check("alpha_3 (golden 0.4714)", mp.mpf(mp.nstr(a3, 10)), mp.mpf("0.4713857368"), tol=mp.mpf("1e-7"))
    print(f"    -> alpha_3 = {mp.nstr(a3, 12)}  =>  rounded(4dp) = {mp.nstr(a3, 4)}\n")


# ---------------------------------------------------------------------------
# Example demo (NOT a submission): Bloom-filter optimal FPP at m/n = 8.
# ---------------------------------------------------------------------------
def verify_bloom_demo():
    print("Example (demo only): bloom-filter-fpp")
    p = mp.e ** (-8 * L**2)  # e^{-(m/n)(ln2)^2}, m/n = 8
    check("bloom optimal FPP (0.0214)", mp.mpf(mp.nstr(p, 10)), mp.mpf("0.02141585"), tol=mp.mpf("1e-6"))
    print(f"    -> p = {mp.nstr(p, 12)}  =>  rounded(3sf) = {mp.nstr(p, 3)}\n")


# ---------------------------------------------------------------------------
# Sylvester sequence helpers (Gehnen & Stocker, arXiv:2509.19914, CC BY 4.0)
# ---------------------------------------------------------------------------
def sylvester(n):
    """Return a_1 .. a_n of Sylvester's sequence."""
    a = [mp.mpf(0)] * (n + 1)
    a[1] = mp.mpf(2)
    for i in range(2, n + 1):
        a[i] = a[i - 1] * (a[i - 1] - 1) + 1
    return a


def knapsack_cN(N):
    """Largest root > 1 of the Theorem 3 degree-N polynomial (Equation 7)."""
    a = sylvester(N)
    c = mp.mpf("1.5")
    h = mp.mpf("1e-12")
    for _ in range(80):
        f = _knapsack_poly(c, a, N)
        fp = (_knapsack_poly(c + h, a, N) - _knapsack_poly(c - h, a, N)) / (2 * h)
        c -= f / fp
    return c


def _knapsack_poly(c, a, N):
    lhs = mp.mpf(1)
    for i in range(1, N + 1):
        lhs *= c - 1 / (a[i] - 1)
    rhs = mp.mpf("0.5")
    for i in range(3, N + 1):
        rhs *= c - 1 / (a[i] - 1)
    s = mp.mpf(0)
    for i in range(3, N + 1):
        prod = mp.mpf(1)
        for j in range(i + 1, N + 1):
            prod *= c - 1 / (a[j] - 1)
        s += (1 / (a[i] - 1)) * prod
    rhs += (c - mp.mpf("0.5")) * s
    return lhs - rhs


def knapsack_TN(N):
  a = sylvester(N)
  s_nm1 = sum(1 / (a[i] - 1) for i in range(1, N))
  return a[N] / (a[N] - 1) ** 2 + s_nm1


def verify_knapsack_c3():
    print("Task: knapsack-removal-lower-bound-c3")
    a = sylvester(3)
    check("a_3 = 7", a[3], 7)
    # Closed form for N=3: 12 r^3 - 20 r^2 + r + 1 = 0
    r = mp.polyroots([12, -20, 1, 1])
    roots_gt1 = [x for x in r if mp.re(x) > 1 and abs(mp.im(x)) < mp.mpf("1e-20")]
    c3 = max(roots_gt1)
    c3_nr = knapsack_cN(3)
    check("c_3 closed form vs numeric root", c3, c3_nr, tol=mp.mpf("1e-12"))
    check("c_3 (golden 1.5806)", mp.mpf(mp.nstr(c3, 8)), mp.mpf("1.58058703"), tol=mp.mpf("1e-6"))
    print(f"    -> c_3 = {mp.nstr(c3, 12)}  =>  rounded(4dp) = {mp.nstr(c3, 5)}\n")


def verify_knapsack_t3():
    print("Task: knapsack-focus-truncated-bound-t3")
    t3 = knapsack_TN(3)
    check("T_3 = 61/36", t3, mp.mpf(61) / 36, tol=mp.mpf("1e-15"))
    check("T_2 = 7/4", knapsack_TN(2), mp.mpf(7) / 4, tol=mp.mpf("1e-15"))
    print(f"    -> T_3 = {mp.nstr(t3, 12)}  =>  fraction 61/36\n")


def verify_list_update_R():
    print("Task: list-update-uniform-competitive-ratio")
    R = (23 + mp.sqrt(17)) / 8
    check("R = (23+sqrt17)/8", R, mp.mpf("3.390388203"), tol=mp.mpf("1e-9"))
    check("R (golden 3.3904)", mp.mpf(mp.nstr(R, 8)), mp.mpf("3.39038820"), tol=mp.mpf("1e-6"))
    check("R improves prior bound 4", R < 4, True)
    print(f"    -> R = {mp.nstr(R, 12)}  =>  rounded(4dp) = {mp.nstr(R, 5)}\n")


def main():
    print(f"mpmath {mp.__version__}, dps={mp.mp.dps}\n")
    verify_cuckoo()
    verify_cuckoo_fallback()
    verify_hyperloglog()
    verify_knapsack_c3()
    verify_knapsack_t3()
    verify_list_update_R()
    verify_bloom_demo()
    if _failures:
        print("FAILURES:", ", ".join(_failures))
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
