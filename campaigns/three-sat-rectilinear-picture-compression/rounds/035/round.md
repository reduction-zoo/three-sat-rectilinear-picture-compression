# Round 035 — Cut decomposition for arbitrary covers

## Plan

Prove composability by making every rectangle crossing a horizontal tile boundary a designated one-column beam. Put input background strips to the right of each beam and output background strips to its left. Then all other rectangles belong to exactly one tile; a crossing rectangle can be extended to the upstream output and downstream input. First check: trim the flat swap's lower right background and enumerate every maximal rectangle in a two-tile union that crosses the cut. It must be one of the two designated beams. If this holds and local tables survive, derive the exact global cost lower bound from local tables. This proof strategy directly addresses the nonadditive baseline, not another size experiment.

## Evidence and diagnosis

Trimming the lower output background yields a swap with baseline 44 and the same exact required-output table. In a two-tile union, ALL maximal rectangles crossing the cut are the two one-column beams `(1,49,55,55)` and `(26,74,44,44)`. The two-tile baseline is exactly 88; all 32 single/composed state instances pass (`output.txt`). Also checked all 16 exact maximal-output states by forbidding unselected outputs (`exact_ports_output.txt`): signals can be dropped without penalty, which forbids treating this as an equality gate under a complemented interpretation.

The [conditional cut-composition lemma](../../work/cut-composition.md) proves arbitrary-cover ownership and a Vertex Cover charging decoder under explicit local-table and layout hypotheses. It is a general conditional proof, not a claim that a full source layout exists. The two-tile cut satisfies its rectangle-ownership hypothesis; arbitrary routing and source/edge interfaces remain to be constructed. No unknown results, source/recovery 0/0. Experience extraction: new cut-composition entry.

## Next action

Establish a reusable decomposition lemma, then supply source/edge tiles and a routing layout.
