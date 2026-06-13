> **SUPERSEDED — failed difficulty validation.** On the Eval Platform this task passed
> Run I 16/16, Run II 16/16, Run III 15/16, i.e. it is trivially solvable *without* the
> paper (the zCDP/Gaussian composition machinery is standard knowledge for the model).
> It violates the passrate requirement (Run I must be ≤ 12.5%). The replacement task is
> `task-02-water-wheel-spanning-trees.md`, which hinges on a specialized, freshly published
> closed-form result that cannot be derived or recalled without the source paper.

# Paper-Assisted STEM Task — CS Domain

A single, ready-to-submit task built according to the *Paper-Assisted STEM Problems — Trainer Guidelines* (Part 2: Task Creation), using the **Traditional Workflow** (identify a paper with a non-trivial result, then formulate a problem that requires that result without merely reproducing it).

---

## 1. Domain and Subdomain (CS)

- **Domain:** Computer Science
- **Subdomain:** Differential Privacy / Privacy-Preserving Machine Learning
  - arXiv primary category of the source paper: `cs.LG` (Machine Learning); the underlying privacy machinery is also `cs.CR` (Cryptography and Security).
  - ACM CCS taxonomy alignment: *Security and privacy → Formal methods and theory of security → Privacy-preserving protocols* and *Theory of computation → Machine learning theory*.

---

## 2. Source Paper

- **Title:** Faster Differentially Private Convex Optimization via Second-Order Methods
- **Authors:** Arun Ganesh, Mahdi Haghifam, Thomas Steinke, Abhradeep Thakurta
- **arXiv:** 2305.13209
- **PDF URL:** https://arxiv.org/pdf/2305.13209
- **Abstract URL:** https://arxiv.org/abs/2305.13209
- **License:** Creative Commons Attribution 4.0 International (**CC BY 4.0**) — `https://creativecommons.org/licenses/by/4.0/` (qualifies under the allowed licenses list).

**Non-trivial results used (the paper "assists" the solver by stating these explicitly):**
- **Lemma A.2** ([BS16, Lem. 2.5]): the Gaussian mechanism that releases a query of `ℓ2`-sensitivity `Δ` by adding isotropic noise `N(·, (Δ²/2ρ) I_d)` satisfies `ρ`-zCDP — equivalently, per-coordinate noise standard deviation `σ` gives `ρ = Δ²/(2σ²)`, **independent of the output dimension `d`**.
- **Composition** (zCDP constant adds linearly across rounds): composing mechanisms that are `ρ_i`-zCDP yields `(Σ ρ_i)`-zCDP.
- **Lemma A.1** ([BS16, Prop. 1.3]): if a mechanism is `ρ`-zCDP then, for every `δ > 0`, it is `(ρ + 2√(ρ ln(1/δ)), δ)`-differentially private.

---

## 3. Prompt (raw LaTeX)

```latex
A data curator runs an iterative, fully adaptive analysis on a single fixed private
dataset. The analysis is divided into two phases, and in every round a vector-valued
statistic is released through the Gaussian mechanism: the true vector is published after
adding independent, isotropic Gaussian noise to each of its $d = 512$ coordinates.

\textbf{Phase 1.} For $k_1 = 100$ consecutive rounds, the released statistic has
$\ell_2$-sensitivity $\Delta_1 = 1$, and the noise added to each coordinate has standard
deviation $\sigma_1 = 10$.

\textbf{Phase 2.} For $k_2 = 25$ consecutive rounds, the released statistic has
$\ell_2$-sensitivity $\Delta_2 = 2$, and the noise added to each coordinate has standard
deviation $\sigma_2 = 10$.

All $k_1 + k_2 = 125$ releases use independent noise and may be chosen adaptively based on
the previously published outputs. Account for the cumulative privacy loss using
zero-concentrated differential privacy (zCDP) and then apply the standard zCDP-to-%
$(\varepsilon,\delta)$ conversion. Determine the smallest value of $\varepsilon$ for which
the entire procedure is guaranteed to be $(\varepsilon,\delta)$-differentially private with
$\delta = 10^{-5}$. Use natural logarithms and round $\varepsilon$ to three significant
figures.
```

---

## 4. Golden Answer

**Final answer:** `ε ≈ 7.79`

### Step-by-step solution (raw LaTeX)

```latex
\textbf{Step 1 — Per-round zCDP cost of the Gaussian mechanism.}
A Gaussian mechanism that releases a query of $\ell_2$-sensitivity $\Delta$ by adding
isotropic Gaussian noise with per-coordinate standard deviation $\sigma$ satisfies
$\rho$-zCDP with
\[
  \rho \;=\; \frac{\Delta^2}{2\sigma^2},
\]
and this value is \emph{independent of the output dimension} $d$ (the noise is isotropic
and $\Delta$ is the $\ell_2$-sensitivity). Hence $d = 512$ is irrelevant.

For the two phases:
\[
  \rho_1 = \frac{\Delta_1^2}{2\sigma_1^2} = \frac{1^2}{2\cdot 10^2} = 0.005,
  \qquad
  \rho_2 = \frac{\Delta_2^2}{2\sigma_2^2} = \frac{2^2}{2\cdot 10^2} = 0.02 .
\]

\textbf{Step 2 — Composition.}
Under adaptive composition the zCDP parameters add. With $k_1 = 100$ and $k_2 = 25$ rounds,
\[
  \rho_{\mathrm{tot}}
  = k_1\rho_1 + k_2\rho_2
  = 100(0.005) + 25(0.02)
  = 0.5 + 0.5
  = 1.0 .
\]

\textbf{Step 3 — Conversion to $(\varepsilon,\delta)$-DP.}
The standard conversion states that a $\rho$-zCDP mechanism is
$(\varepsilon,\delta)$-DP with
\[
  \varepsilon \;=\; \rho_{\mathrm{tot}} + 2\sqrt{\rho_{\mathrm{tot}}\,\ln(1/\delta)} .
\]
With $\delta = 10^{-5}$ we have $\ln(1/\delta) = \ln(10^{5}) = 5\ln 10 = 11.512925\ldots$, so
\[
  \varepsilon
  = 1.0 + 2\sqrt{1.0 \times 11.512925}
  = 1.0 + 2(3.393070)
  = 1.0 + 6.786140
  = 7.786140 .
\]

\textbf{Step 4 — Round.}
\[
  \boxed{\varepsilon \approx 7.79.}
\]

\textbf{Cross-check.} Treating each Gaussian release via Rényi DP (order $\alpha$ gives
$\alpha\rho$ per the Gaussian mechanism) and minimizing
$\rho_{\mathrm{tot}}\,\alpha + \ln(1/\delta)/(\alpha-1)$ over $\alpha > 1$ yields the same
optimum $\rho_{\mathrm{tot}} + 2\sqrt{\rho_{\mathrm{tot}}\ln(1/\delta)} = 7.786\ldots$,
confirming $\varepsilon \approx 7.79$. By contrast, naively applying the advanced
composition theorem to per-round $(\varepsilon,\delta)$ guarantees yields a strictly larger
(looser) value, and using $\log_{10}$ instead of the natural logarithm gives an incorrect
number.
```

---

## 5. Task-Quality Self-Check (against the guidelines)

- **Single, unambiguous answer:** Yes — `ε ≈ 7.79`. Two independent standard accounting routes (zCDP conversion and order-optimized Rényi DP) give the identical value, so the canonical answer is robust.
- **Numerical precision specified:** Yes — "round to three significant figures"; "use natural logarithms."
- **Self-contained / not paper-dependent:** Yes — an expert can solve it from the named standard framework (zCDP + standard conversion); no phrase such as "in the paper"/"in the reference" is used. All boundary conditions (sensitivities, noise scales, round counts, adaptivity, `δ`) are explicit.
- **Requires reasoning beyond lookup:** Yes — combine heterogeneous per-round costs via composition, recognize that the dimension `d = 512` does **not** enter (a common failure mode), avoid the advanced-composition trap, and apply the conversion with the correct (natural) log base.
- **Answer constraints:** Not in `{-1, 0, 1, Yes, No}`; ≤ 60 characters; not multiple-choice; not fill-in-the-blank; single question.
- **LaTeX:** All mathematics is in LaTeX and renders.
- **Paper makes it easier (Run III intent):** With the source paper in context, Lemma A.2 (Gaussian → `Δ²/(2σ²)`, dimension-independent), the additive composition statement, and Lemma A.1 (`ρ + 2√(ρ ln(1/δ))`) are stated directly, so the solver applies them mechanically rather than recalling/deriving them.

### Items the trainer must complete on the Eval Platform (cannot be done here)
- **Passrate runs** (Run I: no paper/no web; Run II: no paper/web; Run III: paper/no web) on Opus 4.8 to confirm the difficulty bands (Full Difficulty: Run I ≤ 12.5%, Run III ≤ 50% and > Run I). If Run I is too easy, raising difficulty levers are available (add a third heterogeneous phase, or invert the formula to ask for the maximum number of additional rounds within a fixed budget).
- **Novelty check** (A2): run the Perplexity novelty check and record the results URL.
- **Consistency check** across run1/run2/run3 on Taiga before submission.
