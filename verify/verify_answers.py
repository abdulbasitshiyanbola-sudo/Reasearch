"""
Independent verification of golden answers for the CS paper-assisted tasks.

For each task we compute the answer two ways:
  (1) the closed-form / formula a solver would use, and
  (2) a brute-force or exact-linear-algebra computation that does NOT rely on
      the formula being correct.
If (1) and (2) agree, the golden answer is trustworthy.
"""

from fractions import Fraction
from itertools import permutations
from sympy import Rational, nsimplify, Float


# ---------------------------------------------------------------------------
# TASK CS-001 : Expected depth of a key in a random binary search tree
# ---------------------------------------------------------------------------
# Keys 1..n inserted in uniformly random order into an (unbalanced) BST.
# D = depth of the node holding key k (root has depth 0).
# Claimed closed form:  E[D] = H_k + H_{n-k+1} - 2.
# ---------------------------------------------------------------------------

def H(m):
    """Exact m-th harmonic number as a Fraction."""
    s = Fraction(0)
    for i in range(1, m + 1):
        s += Fraction(1, i)
    return s

def bst_depth_closed_form(n, k):
    return H(k) + H(n - k + 1) - 2

def bst_depth_bruteforce(n, k):
    """Average depth of key k over ALL n! insertion orders (exact)."""
    total = Fraction(0)
    count = 0
    for perm in permutations(range(1, n + 1)):
        # build BST by inserting perm in order; track depth of key k
        # node -> (key, left, right); store depths in a dict
        depth = {}
        root = None
        tree = {}  # key -> [left_key, right_key]
        for key in perm:
            if root is None:
                root = key
                tree[key] = [None, None]
                depth[key] = 0
                continue
            cur = root
            d = 0
            while True:
                d += 1
                if key < cur:
                    if tree[cur][0] is None:
                        tree[cur][0] = key
                        tree[key] = [None, None]
                        depth[key] = d
                        break
                    cur = tree[cur][0]
                else:
                    if tree[cur][1] is None:
                        tree[cur][1] = key
                        tree[key] = [None, None]
                        depth[key] = d
                        break
                    cur = tree[cur][1]
        total += depth[k]
        count += 1
    return total / count

def check_task1():
    print("=" * 70)
    print("TASK CS-001: expected depth of key k in a random BST on n keys")
    print("=" * 70)
    # brute-force validation of the closed form on several small cases
    for n in range(2, 8):
        for k in range(1, n + 1):
            cf = bst_depth_closed_form(n, k)
            bf = bst_depth_bruteforce(n, k)
            assert cf == bf, f"MISMATCH n={n} k={k}: cf={cf} bf={bf}"
    print("closed form  E[D] = H_k + H_{n-k+1} - 2  verified by brute force "
          "for all 2<=n<=7, all k. OK")
    # the actual task instance
    n, k = 25, 9
    val = bst_depth_closed_form(n, k)
    f = float(val)
    print(f"\nInstance n={n}, k={k}:")
    print(f"  exact   E[D] = {val}  =  H_9 + H_17 - 2")
    print(f"  decimal E[D] = {f:.10f}")
    print(f"  rounded to 4 significant figures = {round(f, 4 - 1 - 0):.4g}")
    print(f"  GOLDEN ANSWER (4 s.f.) = {float(f'{f:.4g}')}")


# ---------------------------------------------------------------------------
# TASK CS-002 : Expected duration of a biased gambler's ruin
# ---------------------------------------------------------------------------
# Start with i dollars, target N, each round +1 w.p. p, -1 w.p. q=1-p.
# Stop at 0 or N. D_i = expected number of rounds.
# Claimed closed form (p != q):
#   D_i = i/(q-p) - (N/(q-p)) * (1-(q/p)^i)/(1-(q/p)^N)
# ---------------------------------------------------------------------------

def ruin_duration_closed_form(i, N, p):
    p = Rational(p)
    q = 1 - p
    r = q / p
    return i / (q - p) - (N / (q - p)) * (1 - r**i) / (1 - r**N)

def ruin_duration_linear_system(i, N, p):
    """Solve D_x = 1 + p*D_{x+1} + q*D_{x-1}, D_0=D_N=0 exactly (no formula)."""
    from sympy import symbols, linsolve, Eq, Matrix
    p = Rational(p)
    q = 1 - p
    # unknowns D_1..D_{N-1}
    n = N - 1
    A = [[Rational(0)] * n for _ in range(n)]
    b = [Rational(0)] * n
    for idx in range(n):       # equation for state x = idx+1
        x = idx + 1
        A[idx][idx] = Rational(1)
        b[idx] = Rational(1)
        # + p*D_{x+1}
        if x + 1 <= N - 1:
            A[idx][x + 1 - 1] -= p
        # + q*D_{x-1}
        if x - 1 >= 1:
            A[idx][x - 1 - 1] -= q
    sol = Matrix(A).solve(Matrix(b))
    return sol[i - 1]

def check_task2():
    print("\n" + "=" * 70)
    print("TASK CS-002: expected duration of a biased gambler's ruin")
    print("=" * 70)
    # validate closed form against exact linear-system solve on small cases
    for (i, N, p) in [(3, 7, Rational(2, 5)), (2, 5, Rational(1, 3)),
                      (4, 9, Rational(11, 20))]:
        cf = ruin_duration_closed_form(i, N, p)
        ls = ruin_duration_linear_system(i, N, p)
        assert nsimplify(cf - ls) == 0, f"MISMATCH i={i} N={N} p={p}: {cf} vs {ls}"
    print("closed form verified against exact linear-system solution. OK")
    # the actual task instance
    i, N, p = 20, 50, Rational(9, 20)   # p = 0.45
    cf = ruin_duration_closed_form(i, N, p)
    ls = ruin_duration_linear_system(i, N, p)
    assert nsimplify(cf - ls) == 0
    f = float(cf)
    print(f"\nInstance i={i}, N={N}, p=0.45:")
    print(f"  exact (rational) D = {cf}")
    print(f"  decimal D = {f:.10f}")
    print(f"  GOLDEN ANSWER (4 s.f.) = {float(f'{f:.4g}')}")


# ---------------------------------------------------------------------------
# TASK CS-003 : Expected number of flips to first see a pattern (biased coin)
# ---------------------------------------------------------------------------
# Pattern HTH, P(H)=p=0.6. Conway: E[T] = 1/(p^2 q) + 1/p.
# ---------------------------------------------------------------------------

def pattern_wait_conway(pattern, p):
    p = Rational(p)
    q = 1 - p
    def prefix_prob(k):
        pr = Rational(1)
        for c in pattern[:k]:
            pr *= p if c == 'H' else q
        return pr
    L = len(pattern)
    total = Rational(0)
    for k in range(1, L + 1):
        if pattern[:k] == pattern[L - k:]:   # length-k prefix == length-k suffix
            total += 1 / prefix_prob(k)
    return total

def pattern_wait_markov(pattern, p):
    """Exact expected hitting time via absorbing-chain linear system (no Conway)."""
    from sympy import Matrix
    p = Rational(p)
    q = 1 - p
    L = len(pattern)
    # states = length of current matching prefix, 0..L ; L absorbing
    def next_state(j, c):
        # current matched prefix length j, read char c -> new matched length
        s = pattern[:j] + c
        # longest suffix of s that is a prefix of pattern
        for m in range(min(len(s), L), -1, -1):
            if pattern[:m] == s[len(s) - m:]:
                return m
        return 0
    n = L  # unknowns E_0..E_{L-1}
    A = [[Rational(0)] * n for _ in range(n)]
    b = [Rational(0)] * n
    for j in range(L):
        A[j][j] = Rational(1)
        b[j] = Rational(1)
        for c, pr in (('H', p), ('T', q)):
            ns = next_state(j, c)
            if ns < L:
                A[j][ns] -= pr
            # if ns == L absorbed, contributes 0
    sol = Matrix(A).solve(Matrix(b))
    return sol[0]

def check_task3():
    print("\n" + "=" * 70)
    print("TASK CS-003: expected flips until pattern HTH appears (P(H)=0.6)")
    print("=" * 70)
    for pat in ['HTH', 'HH', 'HHH', 'HTHH', 'HHT']:
        c = pattern_wait_conway(pat, Rational(3, 5))
        m = pattern_wait_markov(pat, Rational(3, 5))
        assert c == m, f"MISMATCH {pat}: conway={c} markov={m}"
    print("Conway formula verified against absorbing-Markov-chain solve. OK")
    cf = pattern_wait_conway('HTH', Rational(3, 5))
    f = float(cf)
    print(f"\nInstance pattern=HTH, p=0.6:")
    print(f"  exact (rational) E[T] = {cf}")
    print(f"  decimal E[T] = {f:.10f}")
    print(f"  GOLDEN ANSWER (4 s.f.) = {float(f'{f:.4g}')}")


if __name__ == "__main__":
    check_task1()
    check_task2()
    check_task3()
    print("\nAll checks passed.")
