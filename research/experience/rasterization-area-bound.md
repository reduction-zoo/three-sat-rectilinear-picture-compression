# Rasterization needs an area bound

## Claim and applicability

Tags: polygon-to-matrix, encoding size, rectangle cover. A unit-grid orthogonal polygon and its binary cell matrix have equal minimum axis-aligned rectangle-cover size, but a polynomial-bit coordinate encoding can rasterize to exponentially many matrix entries. Applying a polygon hardness proof to explicit binary-matrix picture compression requires a polynomial bound on the constructed grid area, in addition to polynomial polygon encoding size.

## Evidence and status

General snapping argument and a `2^b × 1` counterexample to the naive size inference: [round 004](../../campaigns/three-sat-rectilinear-picture-compression/rounds/004/round.md). Agent-derived, not independently reviewed.

## Consequence for search

Before adapting a continuous rectangle-cover reduction, specify integer coordinates and bound their maximum row and column spans in the source length. The polygon gadget proof and decoder are separate obligations.

## Use history

Created 2026-09-25 in round 004. Intended board promotion remains pending; the board was not edited.
