# Round 013 — alternative direct matrix hardness proofs

## Plan

Gap: the small local clause constructions have not yielded an OR, and the Masek source cited for the exact matrix problem is unavailable. Investigate a different literature route: later primary proofs for covering ones in a binary matrix by contiguous all-one rectangles, especially formulations under image compression, array tiling, or geometric set cover that state an explicit reduction.

First discriminating check: locate accessible full primary text with a theorem whose target exactly matches the fixed matrix/budget semantics, then inspect whether its construction gives polynomial matrix dimensions, a computable budget and assignment recovery from every cover. A hardness citation or optimization variant alone does not meet the check. Search scope is later direct matrix proofs, distinct from round 004's Culberson–Reckhow polygon route and round 001's named Masek/Garey–Johnson citation chain.

Prior evidence: [round 001](../001/round.md) found only a catalog statement for the exact matrix target; [round 004](../004/round.md) found an inaccessible polygon construction. No board experience entries were present in the local checkout.

## Evidence and diagnosis

Searched on 2026-09-25 under `binary matrix minimum number all ones rectangles contiguous`, `covering ones in binary matrix NP-complete proof`, `rectilinear picture rectangle cover reduction 3SAT`, `new proof`, and image-compression/array-cover aliases. Inspected the following accessible primary full texts and their theorem/proof directions:

- [Baier's thesis](https://laboratorio2b.github.io/data-compression/papers/baier_thesis.pdf), Problem 3.13 and pp. 71–72, states the exact binary-picture problem, then explicitly traces hardness to Masek and Culberson–Reckhow; it supplies no new direct matrix construction.
- [Koch–Marenco's subarray-polytope preprint](https://repositorio.utdt.edu/server/api/core/bitstreams/543c88e2-8229-4f4f-8153-507a4d4fe9c2/content), introduction, defines contiguous all-one matrix rectangles and treats RPC as the application, but cites Masek for hardness rather than proving it.
- [Reordering the Reorderable Matrix](https://www.mat.ucsb.edu/g.legrady/academic/courses/15w259/d/re_orderableMatrix.pdf), Theorem 2, embeds RPC as a subproblem of a different matrix problem. This reduction points **out of** RPC and cannot provide the required 3SAT-to-RPC rule.
- [Compressing Rectilinear Pictures and Minimizing Access Control Lists](https://citeseerx.ist.psu.edu/document?doi=063940b038565a3d460da837f19383e677d5f92f&repid=rep1&type=pdf), §5 and Appendix A.3, gives a detailed reduction from RPC to rule-list minimization, again in the wrong direction for this campaign.
- The [Berkeley rectangle-covering thesis](https://digicoll.lib.berkeley.edu/record/136227/files/ERL-89-49.pdf), §3.4, initially resembles the exact target, but its stated `2^(2n)` rectangle count on an all-one `n×n` matrix implies arbitrary row/column subsets rather than the at-most `O(n^4)` contiguous submatrices in the fixed question. This mismatch is an inference from its count; no construction was imported from it.

No inspected later primary full text supplied an explicit exact-target matrix construction, polynomial dimensions/budget and all-cover decoder. This bounded search supports an access/route gap, not nonexistence of such a proof. Actual target/source/recovery solves in this literature round: 0/0/0. Open obligations are unchanged. Experience extraction: [rectangle-alias caution](../../../../research/experience/rectangle-alias-caution.md).

## Next action

Return to an original construction strategy. Before using any rectangle-covering result, verify whether its rows and columns must each be consecutive and whether the reduction points toward the fixed target.
