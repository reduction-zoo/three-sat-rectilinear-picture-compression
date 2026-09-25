# Round 014 — adapt MaxSNP-hardness construction

## Plan

Gap: the later RPC literature cites a MaxSNP-hardness proof by Berman and DasGupta, which may contain an explicit matrix construction independent of Masek's inaccessible manuscript. New proof route: reconstruct that reduction and compose its source problem with 3SAT, then derive deterministic budget and recovery rules for the fixed target.

First discriminating check: obtain the full primary proof, identify its source problem and exact rectangle semantics, and determine whether the constructed matrix has polynomial dimensions and a threshold equivalence with a computable witness decoder. If only an approximation statement or an inaccessible abstract is available, record the exact missing lemma rather than claiming a reduction.

Prior evidence: [round 013](../013/round.md) found Koch–Marenco's exact RPC definition and its citation to Berman–DasGupta, but did not inspect that proof. This route differs from Masek's 3SAT citation and the polygon gadgets.

## Evidence and diagnosis

Located the full [Berman–DasGupta preprint](https://citeseerx.ist.psu.edu/document?doi=c7aee40d8378b0d654e5a898d5f483412e8a5576&repid=rep1&type=pdf) (31 pages; dated 1994 in the copy) and visually inspected its Figures 6–11 and Lemmas 5.2–5.7, Theorem 5.1. It gives an L-reduction from bounded-degree Vertex Cover to *interior cover of a rectilinear polygon*. The construction uses vertex gadgets, edge gadgets, two translation stages and at most `p ≤ d|V|` permutation stages. Lemma 5.6 says an arbitrary polygon cover can be normalized without increasing its rectangle count so that each vertex gadget has a consistent beam state, each edge gadget receives a selected endpoint beam, and background regions have canonical covers. Lemma 5.7 then decodes a vertex cover of size at most `θ−C`, where `θ` is the polygon cover size and the component counts in its proof give `C=(7d+8)|V|+32|E|+14p−1` for fixed degree cap `d`. This is a more explicit witness-recovery route than the earlier catalog citation.

The available text and figures still describe geometric stages schematically. In particular, they do not give integer coordinates for the beam, vertex, edge, translation and permutation shapes, a deterministic rule for placing all stages without accidental rectangle interactions, or a polynomial bound on the area after unit-cell rasterization. The last item matters by round 004's exponential-raster counterexample. The paper's proof is for a continuous polygon, not directly for the fixed binary matrix. A bounded-degree Vertex Cover reduction from the fixed 3SAT input would also have to be specified and composed. No F/G was implemented and no source/target/recovery instance was run in this literature/proof-route round (0/0/0). These are implementation/proof gaps, not a refutation of the published theorem.

The useful change in assessment is that an all-cover decoder and linear *cover-count* offset exist in a primary proof; the missing object is explicit bounded grid geometry. Experience extraction: [vertex-cover beam route](../../../../research/experience/vertex-cover-beam-route.md).

## Next action

Try a distinct, smaller matrix construction before attempting to digitize the entire multi-stage beam system. Preserve this proof route for a future coordinate reconstruction with independently checked gadgets and area bounds.
