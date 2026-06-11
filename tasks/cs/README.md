# CS domain — Paper-Assisted STEM Problems

This folder holds Computer Science tasks built per the *Paper-Assisted STEM Problems —
Trainer Guidelines*. Each task lives in its own folder `cs-XYZ-short-slug/` containing:

- `task.md` — the full task record (taxonomy, source paper + license, prompt, golden
  answer, full solution, pass-rate plan, DO/DON'T self-check, novelty check).
- `solve.py` (or equivalent) — a dependency-light script that re-derives and asserts the
  golden answer, so correctness is independently reproducible.

## Tasks

| ID | Subdomain | Source paper (license) | Answer | Status |
|---|---|---|---|---|
| [CS-001](./cs-001-retrieval-orientability-overhead/task.md) | Data structures (cs.DS) — hashing | *Dense Peelable Random Uniform Hypergraphs*, Walzer, ESA 2019 (CC BY 3.0) | `0.762%` | Draft — needs Eval Platform run |

## What still must be done on the trainer side (cannot be done from here)

The autonomous agent cannot access the Eval Platform, Taiga, or Perplexity. For each task:

1. **Novelty (A2):** run the prompt through Perplexity, paste the result URL into `task.md`.
2. **Pass-rate runs:** on the Eval Platform with Opus 4.8 (or latest), run the three
   conditions, 16 attempts each, and confirm the Full-Difficulty profile:
   - Run I (no paper, no web): ≤ 12.5% (0–2/16)
   - Run II (no paper, web): no restriction
   - Run III (paper, no web): ≤ 50% (1–8/16) **and** strictly more passes than Run I
   - At least one pass across Run I or Run II (else extend to ≤ 32 attempts).
3. **Consistency:** verify the prompt + answer match across run1/run2/run3 on Taiga.
4. **Uniqueness:** confirm the built-in duplicate check passes; reuse a paper ≤ 3 times.

## Reusable task template

Copy [`TEMPLATE.md`](./TEMPLATE.md) into a new `cs-XYZ-slug/` folder to start a task.

## Vetted CC-BY source-paper pipeline (for future CS tasks)

License-checked, qualifying open-access papers with clean, verifiable quantitative results:

| Paper | Venue / License | Exploitable result |
|---|---|---|
| *Dense Peelable Random Uniform Hypergraphs* (Walzer) | LIPIcs ESA 2019 — **CC BY 3.0** | Orientability `c_k*` & peelability thresholds (used in CS-001). |
| *Load Thresholds for Cuckoo Hashing with Double Hashing* (Mitzenmacher, Panagiotou, Walzer) | LIPIcs SWAT 2018 — **CC BY 3.0** | Double-hashing achieves the same `c*(k,l)` load threshold as full randomness. |
| *Balanced Allocations with the Choice of Noise* (Los, Sauerwald) | arXiv:2206.07503 — **CC BY 4.0** | Two-choice gap `log2 log n` under noisy comparisons; phase transition in `g`. |
| *Tight Bounds for Repeated Balls-into-Bins* style / two-choice batched | arXiv:2203.13902 — **CC BY 4.0** | Gap bounds `Θ(b/n + log n)` for batched two-choice. |
| *...Memory process...* (Los, Sauerwald) | arXiv:2301.09810 — **CC BY 4.0** | `O(log log n)` gap with one bit of memory (heavily loaded). |

Always re-verify the license on the exact hosted version you cite (LIPIcs/DROPS pages are
CC BY; arXiv preprints are often non-exclusive even when the published version is CC BY).
