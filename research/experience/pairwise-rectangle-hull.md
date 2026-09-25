# Pairwise rectangle-hull lemma

## Claim and applicability

Tags: rectangle cover, binary matrix, incompatibility graph. For any finite set of cells in a rectangular integer grid, its full bounding rectangle equals the union of the bounding rectangles of all pairs of cells. Therefore the minimum number of all-one axis-aligned rectangles exactly covering a binary picture equals the chromatic number of the graph on its one-cells, adjacent when their pairwise bounding rectangle contains a zero. The empty picture has both values zero. This does not imply arbitrary graphs occur as these incompatibility graphs.

## Evidence and status

General proof and finite cross-checks: [round 002](../../campaigns/three-sat-rectilinear-picture-compression/rounds/002/round.md). Agent-derived, not independently reviewed.

## Consequence for search

This supplies a local compatibility criterion and a lower-bound mechanism for rectangle covers. A graph-coloring reduction still needs a geometric embedding with controlled filler cells.

## Use history

Created 2026-09-25 in round 002. [Round 003](../../campaigns/three-sat-rectilinear-picture-compression/rounds/003/round.md) applied the lemma to anchor cells; it identified a filler-cell budget failure, without producing a reduction. Intended promotion to the board's local shared collection is pending separate access; no board edits made.
