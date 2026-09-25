# Thin pictures reduce to bipartite matching

## Claim and applicability

Tags: rectangle cover, binary matrix, 2×2-free, bipartite matching, tractable subclass. If a binary picture has no all-one 2×2 submatrix, its minimum all-one rectangle-cover size is the maximum matching size of the bipartite incidence graph of maximal horizontal and vertical one-runs. The claim includes empty pictures and overlapping covers. It does not extend to arbitrary pictures with 2×2 blocks.

## Evidence and status

General run-cover equivalence and Kőnig's theorem, with exact independent oracle checks on all 417 thin 3×3 pictures: [round 007](../../campaigns/three-sat-rectilinear-picture-compression/rounds/007/round.md), `thin_cover.py`. Agent-derived application; not independently reviewed.

## Consequence for search

A gadget family wholly confined to thin pictures cannot establish general 3SAT hardness unless `P=NP`. Use a 2D block or explain where the construction leaves this subclass. Local two-state behavior alone is insufficient.

## Use history

Created 2026-09-25 in round 007. Intended board promotion is pending; the board was not edited.
