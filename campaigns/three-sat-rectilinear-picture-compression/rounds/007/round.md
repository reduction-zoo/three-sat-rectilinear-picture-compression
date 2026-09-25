# Round 007 — tractability of thin pictures

## Plan

Gap: rounds 005–006 searched staircase pictures without 2×2 all-one blocks. Hypothesis: every rectangle in a 2×2-free picture is a horizontal or vertical run, so minimum rectangle cover is bipartite vertex cover and is polynomial-time solvable. If true, this explains why thin-wire phase gadgets leak and rules out an NP-hardness proof whose entire output remains in this class (unless P=NP).

First discriminating check: derive the row-run/column-run incidence graph, compute maximum matching on all 3×3 2×2-free pictures, and compare its size with an independent exact rectangle-cover oracle. Then prove the equivalence and polynomial bound. This is a general obstruction proof strategy, distinct from the local tile searches.

Prior evidence: staircase and endpoint-composition patterns in round 005 are 2×2-free; round 006 found no stronger small two-cover phase tile. The finite small-tile experience entry is applicable only as motivation, not as proof.

## Evidence and diagnosis

The hypothesis holds. If a picture has no all-one 2×2 submatrix, every legal rectangle has height one or width one: any rectangle with both dimensions at least two contains a 2×2 block. Enlarge each selected horizontal/vertical rectangle to its unique maximal contiguous run, without raising cover size. Make a bipartite graph with one vertex per maximal horizontal run, one per maximal vertical run, and an edge for each one-cell where its two runs intersect. A set of runs covers every one-cell exactly when its vertices cover every graph edge. Thus minimum rectangle-cover size equals minimum vertex-cover size, which equals maximum matching size by Kőnig's theorem. The graph has at most `RC` edges and `2RC` vertices for an `R×C` explicit matrix; textbook augmenting-path matching is polynomial. Empty pictures have value zero.

`thin_cover.py` checked all 417 2×2-free binary 3×3 pictures. For each, it computed maximum matching and asked the independent rectangle-cover oracle at that budget and one less; all agreed. This is a finite implementation check supporting, not replacing, the proof. Actual target solves: 833 (417 at `K=optimum`, 416 nonempty at `K=optimum-1`); source/recovery instances: 0/0. The theorem applies only to pictures without an all-one 2×2 block. It does not rule out a hard reduction with thicker gadget regions. If a polynomial F/G from general 3SAT always produced thin pictures, the matching algorithm would yield a polynomial 3SAT solver; that implication is conditional on `P≠NP` for a hardness obstruction.

This explains the staircase strategy's limited expressive power: all its tested pictures were thin, so they live inside this tractable target class. It does not prove every local phase gadget in the class leaks; the broader point is polynomial solvability of the entire thin class. Remaining obligation: use 2D blocks or a different structure to encode general SAT. Experience extraction: [thin-picture matching theorem](../../../../research/experience/thin-picture-matching.md).

## Next action

Try a thick variable/clause gadget with a 2×2 all-one block and an explicit first composition check, or stop with the partial theorem and remaining obligations clearly stated.
