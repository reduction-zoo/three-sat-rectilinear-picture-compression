# Coordinate compression removes naive rasterization blowup

## Claim and applicability

Tags: polygon-to-matrix, encoding size, rectangle cover. Naive unit rasterization can be exponentially large, but sorting distinct x and y boundary coordinates and replacing them by ranks preserves all axis-aligned rectangle covers. A polygon with n vertices becomes a matrix with at most (n−1)² cells. Polynomial geometric area is not required.

## Evidence and status

The original [round 004](../../campaigns/three-sat-rectilinear-picture-compression/rounds/004/round.md) correctly identified naive raster blowup but incorrectly treated an area bound as necessary. [Round 021](../../campaigns/three-sat-rectilinear-picture-compression/rounds/021/round.md) corrects this with a general rank-compression proof and 512 exhaustive small-pattern checks under enormous nonuniform coordinate stretching. Agent-derived, not independently reviewed.

## Consequence for search

Specify a polynomial number of rational polygon vertices with polynomial-bit coordinates, or an equivalent executable coordinate ordering. Rank compression then gives the matrix and a count-preserving lift of every matrix witness. The polygon gadget proof and decoder remain separate obligations.

## Use history

Created 2026-09-25 in round 004. Intended board promotion remains pending; the board was not edited.
Corrected on resumption in round 021; the earlier overstrong area requirement is retained in the historical round record.
