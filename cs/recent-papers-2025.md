# Recent CS source papers (2025) — curated for paper-assisted tasks

Papers below were verified for **CC BY 4.0** (or LIPIcs CC BY) licensing and contain
results suitable for reasoning-heavy, single-answer problems. Prefer using each paper
at most once; three uses maximum per §1.6.

| Paper | arXiv / venue | License | Used in tasks |
| --- | --- | --- | --- |
| Gehnen & Stocker, *Stealing From the Dragon's Hoard: Online Unbounded Knapsack With Removal* | [2509.19914](https://arxiv.org/abs/2509.19914) (Sep 2025) | CC BY 4.0 | `knapsack-removal-lower-bound-c3`, `knapsack-focus-truncated-bound-t3` |
| Basiak et al., *A 3.3904-Competitive Online Algorithm for List Update with Uniform Costs* | [2503.17264](https://arxiv.org/abs/2503.17264) / ESA 2025 LIPIcs | CC BY 4.0 | `list-update-uniform-competitive-ratio` |

## Other 2025 candidates (not yet used)

| Paper | arXiv | License | Notes |
| --- | --- | --- | --- |
| Jiang, Ma, Zhang — prophet inequalities (tight static thresholds) | [2205.00588](https://arxiv.org/abs/2205.00588) | CC BY 4.0 | Used on sibling branch; $k=10$ threshold $\approx 0.742$ |
| Azar et al. — weighted $k$-server on uniform metrics | [2507.12130](https://arxiv.org/abs/2507.12130) | CC BY 4.0 | Exponential competitive ratio; constants $c_\ell$ grow fast |
| Bateni et al. — online MMS chore division lower bound | [2507.12984](https://arxiv.org/abs/2507.12984) | CC BY 4.0 | Tight ratio $n$ for $n$ agents — likely too easy |
| Hash & Adjust consistent hashing | [2411.11665](https://arxiv.org/abs/2411.11665) | **CC BY-NC-ND 4.0** ❌ | Does **not** qualify |

## License check command

```bash
curl -sL "https://arxiv.org/abs/ARXIV_ID" | grep -o 'licenses/[^"]*'
```

Must match one of: `licenses/by/4.0/`, `licenses/by-sa/`, etc. — **not** `by-nc-nd`.
