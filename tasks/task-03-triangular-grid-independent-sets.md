# Paper-Assisted STEM Task — CS Domain (v3)

Ready-to-submit task built per the *Paper-Assisted STEM Problems — Trainer Guidelines*
(Traditional Workflow). Replaces task-01 (too easy: Run I 16/16) and task-02 (model passed
all runs: the closed form was derivable).

**Design rationale (why this is hard *without* the paper).** The answer is the exact number
of independent sets (the hard-core lattice-gas partition function at fugacity 1) of a
210-vertex triangular grid graph. This quantity has **no known closed form**; the only way
to get it is a transfer-matrix / tensor-network contraction over `2^20`-scale state spaces,
which is **infeasible by hand and impossible to recall** (a specific 32-digit integer).
Unlike a spanning-tree count, there is no surd/recurrence shortcut for a model to derive.
The source paper *computed and printed* this value (Appendix A), so it is recoverable *with*
the paper (Run III) but not by pure reasoning (Run I). The value is **independently verified
below by my own transfer-matrix code** (exact match for all `n = 1..20`).

---

## 1. Domain and Subdomain (CS)

- **Domain:** Computer Science
- **Subdomain:** Combinatorial Enumeration / Graph Theory — counting independent sets
  (the hard-core lattice-gas / hard-square model on a lattice). `cs.DM` / `math.CO`
  (with statistical-mechanics `cond-mat` flavor).

---

## 2. Source Paper

- **Title:** Independent Set Enumeration and Estimation of Related Constants of Grid Graphs
  and Their Variants
- **arXiv:** 2507.04007 (2025)
- **PDF URL:** https://arxiv.org/pdf/2507.04007
- **Abstract URL:** https://arxiv.org/abs/2507.04007
- **License:** Creative Commons Attribution 4.0 (**CC BY 4.0**) —
  `https://creativecommons.org/licenses/by/4.0/` (qualifies under the allowed-license list).

**Non-trivial result the task relies on.** The paper computes, via optimized tensor-network
contraction, the exact number of independent sets `N∆(n)` of the `n`-triangular grid graph
for all `n ≤ 40` (Appendix A), extending OEIS A219714 / A226444. The `n = 20` entry is
`78578236089316041630019193434422`. (The paper defines the `n`-triangular grid graph as the
lower-right half of the `n × n` square-grid graph with anti-diagonal adjacencies added.)

---

## 3. Prompt (raw LaTeX)

```latex
Consider the triangular grid graph $T_n$ defined as follows. Its vertices are arranged in $n$
rows; for $1 \le i \le n$, row $i$ contains exactly $i$ vertices, labelled
$(i,1), (i,2), \dots, (i,i)$. The edges are:
\begin{itemize}
  \item within each row, $(i,j)$ is adjacent to $(i,j+1)$ for $1 \le j \le i-1$;
  \item between consecutive rows, each vertex $(i,j)$ is adjacent to both $(i+1,j)$ and
        $(i+1,j+1)$.
\end{itemize}
Equivalently, $T_n$ is the lower-left triangular half of the $n \times n$ square-grid graph
with the anti-diagonal adjacencies added; it has $n(n+1)/2$ vertices. An independent set is a
set of pairwise non-adjacent vertices, and the empty set is counted as one independent set.
Let $I(T_n)$ be the total number of independent sets of $T_n$. Determine the exact value of
$I(T_{20})$.
```

---

## 4. Golden Answer

**Final answer:** `78578236089316041630019193434422`

### Step-by-step solution (raw LaTeX)

```latex
\textbf{Step 1 — Model the count.}
$I(T_n)$ is the number of subsets of vertices containing no edge, i.e. the independence
polynomial of $T_n$ evaluated at $1$ (equivalently, the hard-core lattice-gas partition
function at fugacity $1$). $T_n$ is a triangular-lattice region; no closed-form expression
for $I(T_n)$ is known, so the value must be obtained by exact computation.

\textbf{Step 2 — Row transfer matrix.}
Process the rows $1, 2, \dots, n$ in order. The "state" after row $i$ is the subset
$S_i \subseteq \{1,\dots,i\}$ of selected vertices in that row; $S_i$ must be \emph{independent
within the row}, i.e. it contains no two consecutive indices (from the horizontal edges).
Row $i+1$ with selected set $S_{i+1} \subseteq \{1,\dots,i+1\}$ is compatible with $S_i$ iff,
because of the diagonal edges $(i,j)\!\sim\!(i{+}1,j)$ and $(i,j)\!\sim\!(i{+}1,j{+}1)$,
\[
S_{i+1} \cap \big(\, S_i \ \cup \ \{\,j+1 : j \in S_i\,\}\,\big) = \varnothing .
\]
Let $d_i$ be the vector indexed by valid row-$i$ states with $d_i[S]=$ number of ways to fill
rows $1..i$ ending in state $S$. Starting from $d_1$ (row of one vertex: states
$\varnothing,\{1\}$) and applying the compatibility transition gives $d_n$, and
$I(T_n)=\sum_S d_n[S]$.

\textbf{Step 3 — Anchor values.}
The recursion yields
\[
I(T_1)=2,\; I(T_2)=4,\; I(T_3)=14,\; I(T_4)=60,\; I(T_5)=384,\; I(T_6)=3318,\;
I(T_7)=40638,\dots
\]
(matching OEIS A219714). Continuing the exact integer transfer-matrix computation to $n=20$:
\[
\boxed{\,I(T_{20}) = 78578236089316041630019193434422.\,}
\]

\textbf{Verification.} An independent transfer-matrix program reproduces every value
$I(T_n)$ for $n=1,\dots,20$ exactly, including the 32-digit value above; this also matches
the figure tabulated by the source paper (its $N\!\Delta(20)$). The number has no closed
form and 32 digits, so it cannot be produced by hand or from memory without the precomputed
result.
```

---

## 5. Task-Quality Self-Check (against the guidelines)

- **Single, unambiguous answer:** Yes — `I(T_{20})` is a unique integer,
  `78578236089316041630019193434422`. Independently verified by my own transfer-matrix code
  (exact match for `n = 1..20`).
- **Self-contained / not paper-dependent:** Yes — the graph and the quantity are defined
  completely; an expert could (with a computer) set up the transfer matrix and obtain it. No
  phrase such as "in the paper" appears.
- **Hard without the paper:** There is **no closed form**; computing it requires a
  `~2^20`-state transfer-matrix contraction, infeasible by hand, and the 32-digit value
  cannot be recalled. So pure-reasoning runs (Run I) should fail (→ ~0), unlike the previous
  derivable-closed-form attempts.
- **Easier with the paper / reasoning beyond reading:** The paper prints the value in
  Appendix A, but the solver must (a) recognize that the row-by-row graph defined here is the
  paper's `n`-triangular grid graph, (b) pick the correct table among the paper's four
  distinct quantities (`N(m,n)` square, `N∆(n)`, `N∆(m,n)`, `NK(m,n)`) with the right index
  and the empty-set convention, and (c) transcribe a 32-digit integer exactly. This makes
  Run III achievable yet error-prone (so Run III > Run I and plausibly ≤ 50%).
- **Answer constraints:** Not in `{-1,0,1,Yes,No}`; 32 characters ≤ 60; not multiple-choice;
  not fill-in-the-blank; single question; all math in LaTeX and renders.

### Items the trainer must complete on the Eval Platform (cannot be done here)
- Passrate runs (Run I / II / III on Opus 4.8) to confirm the bands. Levers if needed:
  increase `n` (longer integer ⇒ more transcription errors ⇒ lower Run III; the paper prints
  values up to `n = 40`), or switch to the king-graph `NK(m,n)` / `(m,n)`-triangular
  `N∆(m,n)` quantities from the same paper to further reduce lookup-ability.
- Perplexity novelty check (A2) URL.
- run1/run2/run3 consistency check on Taiga before submission.
