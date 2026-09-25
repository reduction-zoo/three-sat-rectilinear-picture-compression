# A shared clause cell leaks across three thick cores

## Claim and applicability

Tags: rectangle cover, clause gadget, three-way junction, state-selective tap. Three local taps that are individually state selective need not implement an OR when identified as one cell. For the `001/111/011` core, no tested disjoint three-core dihedral placement with clear, distinct state ports maintained a false all-inactive clause row at additive budget nine.

## Evidence and status

[Round 010](../../campaigns/three-sat-rectilinear-picture-compression/rounds/010/round.md) gives the finite search definition and counts: 56 fully valid geometric placements, 16 with an additive inactive baseline, and 16/16 clause leaks. `clause_probe.py` reproduces the search with the independent exact target oracle. `clause_output.txt` contains a concrete 7×6 matrix and nine-rectangle witness. No general impossibility theorem or independent review is claimed.

## Consequence for search

Budget additivity before adding a clause cell is insufficient. A clause construction must prove isolation after the cell is added and under all input states; local tap truth tables cannot simply be composed.

Round 011 found a related packing constraint: every one of the 16 additive three-core placements has all four orthogonal neighbors of the shared cell occupied by a core or state port. An adjacent disjoint guard cannot be added to those placements.

Round 012 reserved a 2×2 checker and placed three taps on different checker cells. Among 256 clear geometries, 74 had an additive inactive baseline and a costly false checker row, but every one of those 74 rejected at least one active input at the same budget. A checker must balance both sides of the truth table; merely making the false row costly is insufficient.

## Use history

Created 2026-09-25 from round 010. Intended board promotion is pending; the board was not edited.
Updated 2026-09-25 from round 011.
Updated 2026-09-25 from round 012.
