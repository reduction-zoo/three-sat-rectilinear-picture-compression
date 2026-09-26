# Round 039 — Isolated monotone routing architecture

## Plan

Compile a permutation into adjacent swaps while moving all tracks monotonically right. Before swapping neighboring tracks, translate every track to their right from rightmost to leftmost; after the swap translate tracks to their left in the same order. The vacated intervals make each active module disjoint from idle vertical input stems. Use wide input stems, opposite-sided output tails and the round 035 cut lemma. First check: a translator with separated stems retains its table for either output-wing direction, then a nontrivial three-track permutation has only designated inter-module rectangles and the exact boundary table. The new object is an arbitrary routing layout and count, not another isolated gadget.

## Evidence and diagnosis

Both translator output-wing directions have exact costs 16/17/16/16 at distances 8 and 31 (`translator_output.txt`). A first selection-and-parking layout overlapped a later wide swap input stem with the parked channel's translator (`routing_output.txt`, preserved in commit fc01887). Narrowing the swap's external caps to width two fixes this overlap; the capped swap's 16 states have baseline 46 (`cap_output.txt`).

The routing implementation uses selection from right to left and parking rather than translating every unrelated track at each swap. Three-track reversal has nine modules, compressed shape 221×187, 6,463 one-cells and exactly nine inter-module maximal rectangles, all designated beams. Four boundary tests match baseline 234 plus unsupported outputs (`capped_routing_output.txt`). All six three-track permutations and two four-track permutations pass full ownership enumeration and ordering checks (`layout_output.txt`).

All 24 capped-swap/translator local states now have explicit covers and forced-output antirectangle certificates; `verify_certificates.py` checks them directly without a solver (`verified_output.txt`). The [routing lemma](../../work/routing-lemma.md) states the monotone spacing invariant, independent cap extension, and polynomial sparse/explicit size bounds. The rectangle enumerator was optimized without changing its order or output; all 512 exhaustive small-picture comparisons and 511 target-oracle minima still pass (`rectangle_regression.txt`). No unknown results. Source F/G injections and recovery remain 0/0.

Experience extraction: update the beam-cut entry. The remaining allocated attempt will compose sources, routing, terminals, and the source-to-bounded-degree-graph map; a complete executable rule and its 120-case verification are still outstanding.

## Next action

If the routing compiler satisfies its geometry/ownership invariants, compose certified vertex sources, routing and terminals in the final allocated attempt.
