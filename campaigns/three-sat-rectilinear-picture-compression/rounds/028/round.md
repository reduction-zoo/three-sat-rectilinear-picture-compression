# Round 028 — Coordinate-faithful published permutation stages

## Plan

Rather than regularize the drawing by eye, recover the exact vector boundary paths of Berman–DasGupta Figure 13, close only the top/bottom interfaces, and rank-compress the resulting polygon. This tests whether earlier counterexamples came from losing geometric order constraints. First check: four-state table for each of the two selected input/output beams, then their joint 16-state table. The published figure is schematic; any open-end closure and coordinate perturbation must be explicit. Rank-compression experience applies; earlier switch regularizations are not evidence about this geometry.

## Evidence and diagnosis

Extracted vector paths from Figure 13 (PDF page 26), retained in `vector_paths.json`. `picture.py` explicitly closes the top and bottom and joins two small gaps in the right boundary; it maps the first machine's final x=276.65 to the following staircase, and connects the second mouth at x=383.3. These are interpretations of a schematic, not verified intended coordinates. Rank compression gives 1,298 cells and 147 maximal rectangles. Minimum is 34; the second output is possible at 34 with both inputs absent. `output.txt` retains a validated full cover. The five unsatisfiable/satisfiable baseline thresholds tested range from 24 through 34; no unknown results. Check stops at the first nontrivial state failure.

The drawing also revealed a previous interpretation error: the input hole has three width levels and its incoming beam touches the first side notch. `regularized.py` repairs that combinatorial feature in the earlier integer template. One stage has baseline 17 and needs 18 for unsupported output, but supplying an input lowers the unforced cost to 16 (`regularized_output.txt`); the intended flat transfer table still fails. The finite test stops there. The drawing's beam-core levels have small misalignments, so these experiments do not refute the published theorem.

The initial `check.py` failed on the absent `picture` module before implementation. Source/recovery tests remain 0/0. Experience extraction: none; retained geometry and counterexamples specify exactly what was and was not checked.

## Next action

If the exact drawing passes, identify scalable order constraints; otherwise preserve the finite interpretation and counterexample without claiming to refute the paper.
