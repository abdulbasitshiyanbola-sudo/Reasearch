# Research — Paper-Assisted STEM Problems

Authoring workspace for the *Paper-Assisted STEM Problems* project: challenging,
single-answer STEM problems each linked to an openly-licensed source paper that makes the
problem easier to solve (but is not required by an expert).

## Layout

```
tasks/
  cs/                      Computer Science domain
    README.md              workflow, submission checklist, vetted source-paper pipeline
    TEMPLATE.md            reusable per-task template
    cs-001-.../            one folder per task (task.md + verification script)
```

## Conventions

- Every task is **self-contained** (solvable by a domain expert without the paper), has a
  **single unambiguous answer** with an explicit rounding / canonical-form convention, and
  uses **LaTeX** for all math.
- Every task ships a small **verification script** that re-derives and asserts the golden
  answer with no heavy dependencies.
- Source papers must be **Apache, MIT, CC BY, CC BY-SA, CC0, or BSD** licensed; verify the
  license on the exact hosted version cited.
- Eval Platform / Taiga / Perplexity steps (pass-rate runs, novelty check, consistency
  check) are tracked per task and must be completed on the trainer account.

See [`tasks/cs/README.md`](tasks/cs/README.md) to get started in the CS domain.
