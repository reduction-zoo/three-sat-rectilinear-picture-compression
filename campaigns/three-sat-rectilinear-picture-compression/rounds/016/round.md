# Round 016 — clause junction of certified long wires

## Plan

Gap: the short-core clause junctions in rounds 010–012 allow cross-gadget rearrangements. New construction: bring three copies of the proved `t=3` or `t=4` endpoint wire to one shared clause cell, with their other endpoints kept separate. Longer wires may supply antirectangle lower bounds that isolate input states from the junction.

First discriminating check: enumerate dihedral placements of three copies with one endpoint at a common cell, disjoint wire interiors, and distinct clear far endpoints. If any geometry survives, compare the all-far-endpoints picture with and without the clause cell at the additive budget `6t`; then test active patterns only if the false row is costly. No geometric placement would exclude this direct three-arm construction, not all possible clause gadgets.

Prior evidence: [wire lemma](../../work/wire-lemma.md) proves each isolated wire's exact endpoint budget; [round 010](../010/round.md) shows local tap truth tables do not compose automatically.

## Evidence and diagnosis

`long_wire_junction_probe.py` enumerated the 16 endpoint/dihedral placements of the proved wire for each of `t=3` and `t=4`. Among 560 triples at each length, 128 had pairwise disjoint interiors, a clear shared near-end cell and three distinct far endpoints. The first three-core-arm placement occupies a 15×15 bounding box. Thus the compact clause failure in rounds 010–011 does not imply a geometric packing obstruction for longer arms.

For `t=3`, the first eight valid placements were tested for a size-19 antirectangle in the picture with all far endpoints and the shared clause cell. Each Z3 query returned `unknown` under a 5,000 ms per-instance computation limit; **none is an UNSAT or SAT result**. An earlier unrestricted run on the same first geometry was interrupted after several minutes and also supplied no verdict. The retained output records all eight `unknown` statuses. A separate exact target-oracle call for the first placement `(0,2,4)` with far endpoints `(-7,8),(7,8),(8,-7)` and clause cell `(0,0)` produced a 16×16 matrix but returned `unknown` at budget 18 under a 60,000 ms solver limit. Its input is reconstructed by the retained geometry script. No exact false-row or positive-row verdict was obtained. This is an execution limitation of the chosen searches, not evidence that the junction works or fails. Actual source/recovery instances: 0/0; completed exact target solves: 0. Experience extraction: none, because the round established geometric availability but no reusable cover or obstruction rule.

Remaining obligations for this route: solve an all-inactive false row independently, check all seven active patterns, prove isolation for arbitrary global composition and derive an all-cover source decoder. The additive baseline of three separated arms follows from the wire lemma only before the shared cell is included.

## Next action

Try a different mechanism or a sharper decomposed certificate search if this junction is resumed; retain solver `unknown` as undecided.
