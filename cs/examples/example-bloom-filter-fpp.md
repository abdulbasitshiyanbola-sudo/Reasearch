# Example (FORMAT DEMO ONLY — DO NOT SUBMIT)

> [!WARNING]
> This file exists **only** to show how the template is filled in and how a single,
> verifiable answer is derived. It is a well-known textbook result, so a model would
> almost certainly pass **Run I** — meaning it **fails the Full-Difficulty Run I gate**
> (≤ 12.5%). It is therefore **not a valid submission**. Use it for format reference only.
> Per §1.6.3, your real submission must be authored by you (not AI-generated).

## Metadata

- **Subdomain (A1 taxonomy):** Randomized & Streaming Algorithms
- **Difficulty tranche:** N/A (demo)
- **Author:** demo
- **Date:** 2026-06-11

## Source paper (§1.3)

- **Title:** *(placeholder)* — for a real task, link a qualifying-licensed paper whose
  analysis of Bloom-filter false-positive rates supports the derivation.
- **License:** must be one of Apache / MIT / CC BY / CC BY-SA / CC0 / BSD.
- **Which result/lemma helps?** The closed-form optimal number of hash functions and the
  resulting false-positive expression.

## Problem prompt (what the model sees)

A Bloom filter uses a bit array of \(m\) bits and \(k\) independent hash functions, each
assumed to map every element independently and uniformly at random to one of the \(m\)
positions. After inserting \(n\) distinct elements, a membership query for an element not
in the set is reported as a (false) positive when all \(k\) of its hashed positions are
set. Assume \(m = 8n\) and treat the bit-set events as independent, so the false-positive
probability is modeled as \(\left(1 - e^{-kn/m}\right)^{k}\). Choose the real-valued
\(k\) that minimizes this probability. Under that optimal \(k\), what is the resulting
false-positive probability? Round your answer to 3 significant figures.

## Golden answer

- **Answer:** `0.0214`
- **Form:** numeric, rounded to 3 significant figures
- **Length check:** ≤ 60 chars ✅ — **Not in {-1,0,1,Yes,No}** ✅

## Full solution (verifiable)

Let \(p\) be the false-positive probability:
\[
p(k) = \left(1 - e^{-kn/m}\right)^{k}.
\]
Minimizing \(\ln p(k) = k \ln\!\left(1 - e^{-kn/m}\right)\) over \(k\) gives the classic
optimum
\[
k^\* = \frac{m}{n}\ln 2 .
\]
Substituting \(k^\*\) yields \(e^{-k^\* n/m} = e^{-\ln 2} = \tfrac12\), so
\[
p(k^\*) = \left(\tfrac12\right)^{k^\*} = \left(\tfrac12\right)^{(m/n)\ln 2}
        = e^{-(m/n)(\ln 2)^2}.
\]
With \(m/n = 8\):
\[
p = e^{-8(\ln 2)^2} = e^{-8(0.4804530)} = e^{-3.843624} = 0.021416\ldots
\]
Rounded to 3 significant figures: **0.0214**. The minimizer is unique because
\(\ln p(k)\) is strictly convex in \(k\) over the relevant range, so the answer is
unambiguous.

## Why this is only a demo

The closed form \(k^\* = (m/n)\ln 2\) and \(p = e^{-(m/n)(\ln 2)^2}\) are standard, so the
model solves it without any paper — there is no Run III > Run I gap. A real CS task needs a
genuine reasoning gap that the paper's specific result helps close.
