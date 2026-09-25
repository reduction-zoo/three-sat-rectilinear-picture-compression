# Round 004 — orthogonal-polygon proof route

## Plan

Gap: the direct one-anchor scheme has uncontrolled filler cost. Investigate Culberson–Reckhow's published reduction from SAT to minimum rectangle cover of a hole-free orthogonal polygon, then assess exact digitization into the fixed binary-matrix target. First discriminating check: does an accessible primary proof specify enough beam-machine coordinates, interactions, budget and assignment extraction to define executable F/G for arbitrary 3-CNF? A theorem statement or schematic without coordinates is insufficient.

Prior evidence: round 001 found Masek's exact matrix proof unavailable; round 003's direct anchor filler budget failed. A later polygon-cover paper identifies binary-matrix RPC as an integral version of rectangle cover, but that equivalence alone does not supply a 3SAT reduction.

## Evidence and diagnosis

The [1988 Culberson–Reckhow proceedings proof](https://paperzz.com/doc/7331430/covering-polygons-is-hard---foundations-of), §3 and Theorem 3.1, gives a SAT-to-orthogonal-polygon route via beam machines, inversion/corners, variable generators, clause checkers, line switches and noise filters. It states five rectangles plus a beam per machine, six background rectangles per three-literal clause checker and a polynomial number of relay machines. The accessible OCR interleaves columns and strips geometric detail from Figures 7–17; §3 describes switching and interference qualitatively, not with integer coordinates or a precise algorithm for the total budget and extracting assignments from *every* optimal cover. The longer [1994 journal version](https://www.sciencedirect.com/science/article/abs/pii/S019667748471025X) was identified but its full text was not accessible in this search. Thus the proceedings text is evidence that a published route exists, but not enough to implement the fixed F/G contract here.

Digitization lemma (derived here): if an orthogonal polygon `P` is a union of unit cells on an integer grid, make the matrix of its cells. Any discrete rectangle cover is a continuous rectangle cover. Conversely, for each continuous rectangle contained in `P`, expand each side to the outer boundary of every grid cell it intersects with positive area. Since the original rectangle intersects the Cartesian product of its touched rows and columns, each of those cells lies in `P`, so the expanded rectangle remains inside `P` and covers at least as much. Thus the optimum counts agree. This also gives a way to map each continuous witness to a discrete one; it does not decode SAT without the polygon gadgets.

Size obstruction: an integer-coordinate polygon with corners `(0,0),(2^b,0),(2^b,1),(0,1)` has `O(b)`-bit coordinate encoding but rasterizes to `2^b` matrix entries. A polynomial-time polygon construction is insufficient by itself; the constructed bounding-box area must also be polynomial in the source size. The accessible proceedings says the number of gadgets is polynomial but does not give a usable area bound. This is a representation gap, not a contradiction of its theorem.

Actual injected source/target/recovery instances: 0/0/0; the round was a proof-route and encoding analysis. Remaining obligations: obtain explicit bounded geometry and decoder, or construct an independent matrix gadget. Experience extraction: [rasterization size constraint](../../../../research/experience/rasterization-area-bound.md).

## Next action

Synthesize a small two-state matrix gadget in round 005, then test whether its states expose clause-covering ports.
