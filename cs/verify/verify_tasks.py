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


def main():
    print(f"mpmath {mp.__version__}, dps={mp.mp.dps}\n")
    verify_cuckoo()
    verify_cuckoo_fallback()
    verify_hyperloglog()
    verify_bloom_demo()
    if _failures:
        print("FAILURES:", ", ".join(_failures))
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
