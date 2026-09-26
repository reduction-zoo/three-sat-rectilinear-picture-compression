# Round 039 — Isolated monotone routing architecture

## Plan

Compile a permutation into adjacent swaps while moving all tracks monotonically right. Before swapping neighboring tracks, translate every track to their right from rightmost to leftmost; after the swap translate tracks to their left in the same order. The vacated intervals make each active module disjoint from idle vertical input stems. Use wide input stems, opposite-sided output tails and the round 035 cut lemma. First check: a translator with separated stems retains its table for either output-wing direction, then a nontrivial three-track permutation has only designated inter-module rectangles and the exact boundary table. The new object is an arbitrary routing layout and count, not another isolated gadget.

## Evidence and diagnosis

Pending.

## Next action

If the routing compiler satisfies its geometry/ownership invariants, compose certified vertex sources, routing and terminals in the final allocated attempt.
