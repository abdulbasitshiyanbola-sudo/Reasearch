# CS Domain Task Working Draft

## Guideline takeaways from the uploaded PDF

- Each task needs a source paper with an approved open license: Apache, MIT, CC BY,
  CC BY-SA, CC0, or BSD.
- The prompt must be self-contained; the paper should help, but an expert should
  still be able to solve the problem without seeing it.
- The prompt should ask exactly one question and have one unambiguous final answer.
- If the answer is numeric, specify the exact precision or make clear that an exact
  integer is required.
- Avoid prompts that can be answered by lookup, multiple choice, fill-in-the-blank,
  yes/no, or answers equal to `-1`, `0`, or `1`.
- The final answer should be short, ideally under 60 characters.
- Use LaTeX for mathematical symbols.
- Before submission, run the required novelty check and record the Perplexity
  result URL.

## CS source-paper candidate

- **Subdomain:** Computer Science / graph algorithms / network analysis
- **Paper:** Tomaz Hocevar and Janez Demsar, "Combinatorial algorithm for counting
  small induced graphs and orbits," PLOS ONE 12(2): e0171428, 2017.
- **URL/DOI:** https://doi.org/10.1371/journal.pone.0171428
- **License evidence:** The article states that it is distributed under the
  Creative Commons Attribution License.
- **Why it fits:** The paper develops linear-equation methods for counting small
  induced graphlets and vertex orbits. A task about a particular induced graphlet
  orbit is self-contained but is easier to frame and solve after reading the paper.

## Draft task prompt

Let \(H\) be a simple undirected graph with vertex set
\[
\{x\}\cup A\cup B\cup P\cup Q,
\]
where
\[
A=\{a_1,\ldots,a_8\},\quad
B=\{b_1,\ldots,b_7\},\quad
P=\{p_1,\ldots,p_6\},\quad
Q=\{q_1,\ldots,q_5\}.
\]
The vertex \(x\) is adjacent exactly to every vertex in \(A\cup B\). There are no
edges inside any one of the sets \(A,B,P,Q\), and there are no edges between
\(P\) and \(Q\). All remaining edges are defined as follows:

- \(a_i b_j\) is an edge iff \(i+j\) is even.
- \(a_i p_k\) is an edge iff \(i\le k+2\).
- \(a_i q_\ell\) is an edge iff \(i\equiv \ell\pmod 3\).
- \(b_j p_k\) is an edge iff \(j+k\equiv 0\pmod 3\).
- \(b_j q_\ell\) is an edge iff \(j\ge \ell+2\).

An induced \(P_4\) means an induced path on four vertices. Count the induced
\(P_4\)'s in \(H\) for which \(x\) is one of the two internal vertices. Give the
exact integer.

## Golden answer

`412`

## Verification solution

If \(x\) is internal in an induced \(P_4\), the path has the form
\[
y-x-z-w,
\]
where \(y,z\in A\cup B\), \(w\in P\cup Q\), \(zw\) is an edge, and the forbidden
extra edges are \(yz\) and \(yw\). Since \(x\) is adjacent exactly to \(A\cup B\),
there is no possible extra edge \(xw\). Each valid induced path is counted once
by choosing the ordered triple \((y,z,w)\), because \(z\) is the internal vertex
adjacent to \(w\).

Sum the valid choices by the types of \(z\) and \(w\):

| type of \(z\) | type of \(w\) | subtotal |
| --- | --- | ---: |
| \(A\) | \(P\) | 141 |
| \(A\) | \(Q\) | 100 |
| \(B\) | \(P\) | 82 |
| \(B\) | \(Q\) | 89 |

The subtotals come from the following index sums:

- For \(z=a_i,w=p_k\), require \(i\le k+2\). Summing valid \(y\)'s over
  \(k=1,\ldots,6\) gives \(22+24+27+27+21+20=141\).
- For \(z=a_i,w=q_\ell\), require \(i\equiv \ell\pmod 3\). Summing over
  \(\ell=1,\ldots,5\) gives \(18+20+16+22+24=100\).
- For \(z=b_j,w=p_k\), require \(j+k\equiv 0\pmod 3\). Summing over
  \(k=1,\ldots,6\) gives \(15+18+13+12+14+10=82\).
- For \(z=b_j,w=q_\ell\), require \(j\ge \ell+2\). Summing over
  \(\ell=1,\ldots,5\) gives \(23+22+21+15+8=89\).

Therefore the required count is
\[
141+100+82+89=412.
\]

## Submission checklist status

- Single question: yes.
- Single unambiguous answer: yes, exact integer `412`.
- Answer length under 60 characters: yes.
- Not multiple choice or fill-in-the-blank: yes.
- Does not ask "in the paper" or "in the reference": yes.
- Source paper license appears compliant: yes, CC BY.
- Novelty check: still required before submission; record the Perplexity URL.
- Pass-rate testing: still required on the eval platform.

## Notes before final submission

The uploaded guidelines say not to submit questions found online or questions
created using AI/LLMs. Treat this file as a collaborative working draft: before
submission, a human trainer should either independently author/modify the final
problem or confirm the project's policy for AI-assisted drafting.
