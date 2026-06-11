# Paper-Assisted STEM Problems — Computer Science (CS) Domain

This repository holds CS-domain tasks built for the **Paper-Assisted STEM Problems**
project, following the Trainer Guidelines (Part 2: Task Creation).

Each task is a single, self-contained question with one unambiguous answer. A task
is "paper-assisted": it must be **hard without** a designated source paper, yet
**easier with** it, while remaining solvable in principle by a domain expert who
does not have the paper.

## Repository layout

```
templates/TASK_TEMPLATE.md     Reusable template capturing every required field.
tasks/                         One markdown file per task (problem + full solution).
verify/verify_answers.py       Independent code verification of every golden answer.
docs/CHECKLIST.md              The DO/DON'T + pass-rate gating checklist.
```

## The hard requirements (distilled from the guidelines)

A task is only valid if **all** of the following hold:

- **Single answer.** One unambiguous value (numeric, string, or symbolic), and it
  must be **≤ 60 characters**.
- **Answer is not** one of `-1, 0, 1, Yes, No`, and the prompt is **not**
  multiple-choice and **not** fill-in-the-blank.
- **Single question** in the prompt (no multi-part questions).
- **Rounding / canonical form specified** when relevant (e.g. "round to 4
  significant figures").
- **Self-contained.** All boundary conditions, assumptions, initial conditions and
  constants are stated in the prompt. An expert could solve it **without** the
  paper. The words "in the paper" / "in the reference" never appear.
- **Requires reasoning**, not lookup. It should fail a strong model through a
  *reasoning* error, not a trivia gap.
- **LaTeX** for every mathematical symbol, and the LaTeX must render.
- **Licensed source.** The source paper/monograph is under one of:
  Apache, MIT, CC BY, CC BY-SA, CC0, or BSD. (Note: arXiv's *default* license does
  **not** qualify — the paper must be explicitly CC BY / CC BY-SA / etc.)
- **Pass-rate profile** (Full difficulty), measured on the Eval Platform with the
  latest model over 3 runs × 16 attempts:

  | Run | Source paper? | Web search? | Target passes / 16 | Pass rate |
  |-----|---------------|-------------|--------------------|-----------|
  | I   | No            | No          | 0–2                | ≤ 12.5%   |
  | II  | No            | Yes         | 0–16               | none      |
  | III | Yes           | No          | 1–8                | ≤ 50%     |

  Plus: Run I **or** Run II has ≥ 1 pass, and Run III passes **>** Run I passes.

## Sources used here (licenses confirmed)

- **Jeff Erickson, *Algorithms*** — Creative Commons **CC BY 4.0**.
  <http://jeffe.cs.illinois.edu/teaching/algorithms/>
- **E. Lehman, F. T. Leighton, A. R. Meyer, *Mathematics for Computer Science***
  — Creative Commons **CC BY-SA 3.0**. <https://people.csail.mit.edu/meyer/mcs.pdf>

## Verifying the golden answers

```bash
pip install sympy
python3 verify/verify_answers.py
```

Every golden answer is computed **two independent ways** — the closed form a solver
would use, and a brute-force / exact-linear-algebra computation that does not assume
the closed form is correct. The script asserts they agree.

## Important note on pass-rate gating

The pass-rate targets (Run I/II/III) can only be measured on the Eval Platform with
the production model; they cannot be measured in this repo. The tasks here are
constructed to *maximize* the chance of hitting the profile (genuine reasoning
crux + verified single answer), and each task file lists **difficulty knobs** to
tune if a run comes back outside its target band.
