# Thick exclusive ports are local but not automatically compositional

## Claim and applicability

Tags: rectangle cover, Boolean gadget, 2×2 block, exclusive ports, wire. The 3×3 core `000/011/111` has a 2×2 all-one block and supports two individually free exterior ports that together cost one extra rectangle. A specific diagonal repeated join now has a general endpoint-budget theorem: `t` cores require exactly `2t` rectangles with zero or one outer endpoint, and `2t+1` with both, for every `t≥3`. Other joins can collapse the budget, so the theorem applies only to the explicit placement in the proof. No SAT reduction or all-cover phase decoder follows from it.

## Evidence and status

Exhaustive bounded local/dihedral search and independent exact target solves: [round 008](../../campaigns/three-sat-rectilinear-picture-compression/rounds/008/round.md), especially `port_probe.py`, `all_compositions.py`, and `repeat_probe.py`. The [general wire proof](../../campaigns/three-sat-rectilinear-picture-compression/work/wire-lemma.md) and [round 015](../../campaigns/three-sat-rectilinear-picture-compression/rounds/015/round.md) give explicit constructive upper covers and antirectangle lower bounds; direct certificates were checked through 20 cores. Not independently reviewed.

## Consequence for search

Use only the explicitly proved repeated placement when relying on the endpoint budget. A complete construction still needs arbitrary occurrence fanout, clause placement, isolation from cross-gadget rectangles and assignment recovery from every valid cover.

## Use history

Created 2026-09-25 in round 008. Intended board promotion is pending; the board was not edited.
Updated 2026-09-25 with the round-015 general wire lemma.
