# Task: 3-core fraction at the (3,2)-cuckoo-hashing orientability threshold

## Metadata

- **Subdomain (A1 taxonomy):** Algorithms & Data Structures (randomized data structures / hashing)
- **Difficulty tranche:** Full Difficulty
- **Author:** _(trainer — finalize and own per §1.6.3 before submission)_
- **Date:** 2026-06-11

## Source paper (§1.3)

- **Title:** Load Thresholds for Cuckoo Hashing with Overlapping Blocks
- **Authors / Year:** Stefan Walzer, 2018
- **Venue / ID:** ICALP 2018, LIPIcs Vol. 107, pp. 102:1–102:10
- **License:** **CC BY 3.0 Unported** ✅ (verified on the Dagstuhl page)
- **URL:** https://doi.org/10.4230/LIPIcs.ICALP.2018.102
- **Which result/lemma/technique helps?** Table 1 lists the exact load threshold
  \(c_{3,2} = 0.9882014140\) for 3-ary cuckoo hashing with blocks (buckets) of size 2 —
  equivalently \(\alpha^* = 2c_{3,2} = 1.9764028280\) keys per bucket — and the paper
  explains that these thresholds are governed by belief-propagation fixed points for
  hypergraph orientability (Lelarge's framework; Leconte–Lelarge–Massoulié). With the
  paper, the solver can skip deriving the threshold and only needs the 3-core BP fixed
  point and core-composition formulas. The answer itself (the core fraction) appears
  nowhere in the paper, so it is not a lookup.

## Problem prompt (what the model sees) — raw LaTeX

```latex
\textbf{Problem.}
A hash table consists of $N$ buckets, each with capacity $2$ (a bucket can store at
most $2$ keys). There are $n = \lfloor \alpha N \rfloor$ keys; each key independently
draws a set of $3$ distinct buckets uniformly at random from all $\binom{N}{3}$ such
sets, and the key may only ever be stored in one of its $3$ drawn buckets. A
\emph{valid placement} assigns every key to one of its $3$ buckets such that no bucket
stores more than $2$ keys.

Let $\alpha^{*}$ denote the sharp threshold for this scheme: for every fixed
$\varepsilon > 0$, if $\alpha \le \alpha^{*} - \varepsilon$ then a valid placement
exists with probability tending to $1$ as $N \to \infty$, while if
$\alpha \ge \alpha^{*} + \varepsilon$ then with probability tending to $1$ no valid
placement exists.

Model the system as a $3$-uniform hypergraph $H$ whose vertices are the $N$ buckets
and whose hyperedges are the $n$ keys (each key is the set of its $3$ buckets). The
\emph{$3$-core} of $H$ is the maximal subset $E'$ of hyperedges such that every vertex
incident to at least one hyperedge of $E'$ is incident to at least $3$ hyperedges of
$E'$; the vertices of the $3$-core are exactly the vertices incident to $E'$.

At $\alpha = \alpha^{*}$, the fraction of the $N$ buckets that belong to the $3$-core
of $H$ converges in probability, as $N \to \infty$, to a constant
$\nu^{*} \in (0,1)$. Compute $\nu^{*}$. Report your answer as a decimal rounded to
exactly $4$ decimal places.
```

## Golden answer

- **Answer:** `0.9208`
- **Form:** numeric, rounded to exactly 4 decimal places
- **Length check:** 6 chars ≤ 60 ✅ — **Not in {-1,0,1,Yes,No}** ✅
- **Full-precision value:** \(\nu^* = 0.920832987787\ldots\)

## Full solution (verifiable) — raw LaTeX

```latex
\textbf{Step 1: Local structure.}
Vertex degrees: each of the $n=\alpha N$ hyperedges contains a given bucket with
probability $\tbinom{N-1}{2}/\tbinom{N}{3} = 3/N$, so the degree of a fixed vertex is
$\mathrm{Bin}(\alpha N,\,3/N) \to \mathrm{Po}(3\alpha)$. Locally, $H$ converges to a
Galton--Watson hypertree: since the degree distribution is Poisson, the size-biased
offspring law equals the original, and each hyperedge leads to $2$ fresh child vertices.

\textbf{Step 2: Fixed point for the $3$-core.}
Run the standard peeling/message-passing characterization of the $3$-core on the limit
tree. Say an incidence $(v,e)$ is \emph{supportive} if vertex $v$ has at least $2$
incident hyperedges other than $e$ that are \emph{live toward} $v$, where a hyperedge
$f$ is live toward $v$ if both incidences of $f$ at its other two endpoints are
supportive. Let $x$ denote the probability that a uniformly random incidence is
supportive. A hyperedge other than $e$ at $v$ is live toward $v$ with probability
$x^{2}$, and the number of such hyperedges is $\mathrm{Po}(3\alpha)$ thinned by
$x^{2}$, i.e.\ $\mathrm{Po}(\mu)$ with
\[
\mu = 3\alpha x^{2}.
\]
Hence the fixed-point equation
\[
x \;=\; \Pr[\mathrm{Po}(\mu)\ge 2] \;=\; 1-e^{-\mu}(1+\mu),
\qquad \mu = 3\alpha x^{2},
\]
where (as is standard for cores) $x$ is the \emph{largest} root in $[0,1]$.

\textbf{Step 3: Composition of the $3$-core.}
A hyperedge survives into the $3$-core iff all $3$ of its incidences are supportive:
\[
\Pr[e \in \text{core}] = x^{3}.
\]
A vertex lies in the $3$-core iff it has at least $3$ incident live hyperedges:
\[
\nu(\alpha) \;=\; \Pr[\mathrm{Po}(\mu)\ge 3] \;=\; 1-e^{-\mu}\Bigl(1+\mu+\tfrac{\mu^{2}}{2}\Bigr).
\]
Thus the $3$-core contains $\sim \alpha x^{3} N$ hyperedges and $\sim \nu N$ vertices.

\textbf{Step 4: Characterization of the threshold.}
A valid placement is a $2$-orientation of $H$ (each hyperedge assigned to an incident
vertex, each vertex assigned at most $2$ hyperedges). By Hall's theorem (deficiency
form), a $2$-orientation exists iff every sub-hypergraph $(V',E')$ satisfies
$|E'| \le 2|V'|$. In the random setting the asymptotically densest sub-hypergraph is
the $3$-core, so the sharp threshold $\alpha^{*}$ occurs exactly when the $3$-core
reaches edge density $2$ (edges per vertex):
\[
\alpha\, x^{3} \;=\; 2\,\nu(\alpha).
\]

\textbf{Step 5: Solve the system.}
Solve simultaneously
\[
x = 1-e^{-\mu}(1+\mu), \qquad \mu = 3\alpha x^{2}, \qquad
\alpha x^{3} = 2\Bigl(1-e^{-\mu}\bigl(1+\mu+\tfrac{\mu^{2}}{2}\bigr)\Bigr),
\]
taking the largest root $x$. Numerically,
\[
x^{*} = 0.9767388585\ldots,\quad
\mu^{*} = 5.6565763494\ldots,\quad
\alpha^{*} = 1.9764028280\ldots
\]
(equivalently $\alpha^{*}/2 = 0.9882014140$ keys per slot, matching the known
$(k,\ell)=(3,2)$ cuckoo-hashing load threshold, which validates the system).

\textbf{Step 6: Evaluate the core fraction.}
\[
\nu^{*} \;=\; 1-e^{-\mu^{*}}\Bigl(1+\mu^{*}+\tfrac{(\mu^{*})^{2}}{2}\Bigr)
\;=\; 0.9208329878\ldots
\]
Rounded to $4$ decimal places:
\[
\boxed{\nu^{*} = 0.9208}
\]
```

## Why the paper helps (Run III > Run I rationale)

Without the paper the model must (1) derive the Poisson local limit, (2) set up the
3-core BP fixed point, (3) derive the core-composition formulas, (4) discover the
"core density = capacity" threshold characterization, and (5) solve a coupled
transcendental system numerically — five independent failure points. With the paper,
Table 1 hands it \(\alpha^* = 2 \times 0.9882014140\) and frames the BP/orientability
machinery, collapsing steps (4)–(5) into a one-dimensional fixed-point solve; only
steps (2)–(3) plus a single numeric solve remain. The final quantity \(\nu^*\) is
tabulated nowhere (papers tabulate thresholds, never core fractions at threshold), so
neither memorization nor paper-lookup yields the answer directly.

## Verification performed

- Framework reproduces the published thresholds to 10 decimal places for **both**
  \((k,\ell)=(3,1)\): \(0.9179352767\) and \((3,2)\): \(0.9882014140\) (paper Table 1).
- High-precision values (mpmath, 30 digits): \(x^*=0.976738858529\),
  \(\mu^*=5.65657634943\), \(\alpha^*=1.97640282795\), \(\nu^*=0.920832987787\).
- Core density check at solution: \(\alpha^* x^{*3}/\nu^* = 2.000000000000\).

## Novelty check (A2)

- **Perplexity results URL:** _(trainer to run and paste)_
- **Confirmed not a known/online question:** _(trainer to confirm)_

## Pass-rate results (Eval Platform — Opus 4.8 or latest)

| Run | Paper? | Web? | Passes / attempts | Pass rate | Gate (Full) |
| --- | --- | --- | --- | --- | --- |
| I   | No  | No  | _(run)_ /16 | — | ≤ 12.5% (0–2) |
| II  | No  | Yes | _(run)_ /16 | — | no restriction |
| III | Yes | No  | _(run)_ /16 | — | ≤ 50% (1–8) |

- Expected: Run I very low (must reconstruct research-level theory + numerics
  end-to-end); Run III materially higher (threshold given, framework given).
- **Fallback if Run III = 0:** use the easier \((k,\ell)=(3,1)\) variant of the same
  construction — "fraction of cells in the 2-core at the plain 3-ary cuckoo threshold"
  — whose answer is \(x^{*2}/(3-2x^{*}) = 0.6329\) (4 d.p.), with
  \(x^*\) solving \(-\ln(1-x) = 3x/(3-2x)\), \(c^* = 1/(x^*(3-2x^*)) = 0.9179352767\).
