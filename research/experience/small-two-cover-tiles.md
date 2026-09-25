# Small two-cover tiles differ by one rectangle

## Claim and applicability

Tags: rectangle cover, variable gadget, finite synthesis. Among all connected full-span binary 4×4 pictures, each picture with exactly two minimum covers by inclusion-maximal all-one rectangles has the two covers differing by a single rectangle swap. The claim is only for 4×4 and this maximalized-cover model; arbitrary legal target outputs include nonmaximal rectangles.

## Evidence and status

Exhaustive enumeration of 65,536 pictures, 7,943 admissible shapes, 976 two-cover shapes, no stronger pair; 20 independent minimum-size oracle cross-checks: [round 006](../../campaigns/three-sat-rectilinear-picture-compression/rounds/006/round.md), `robust_tile_probe.py`. Finite-family evidence, not independently reviewed.

## Consequence for search

Within this small family, a two-state tile cannot obtain robustness merely by making both optimum covers change two or more rectangles. A later attempt needs a larger geometry, more legal covers with a decoder, or a different propagation mechanism.

## Use history

Created 2026-09-25 in round 006. Intended board promotion is pending; the board was not edited.
