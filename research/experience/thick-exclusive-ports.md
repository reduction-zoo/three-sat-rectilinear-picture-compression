# Thick exclusive ports are local but not automatically compositional

## Claim and applicability

Tags: rectangle cover, Boolean gadget, 2×2 block, exclusive ports, wire. The 3×3 core `000/011/111` has a 2×2 all-one block and supports two individually free exterior ports that together cost one extra rectangle. Certain dihedral joins of such cores retain an additive budget and exclusive outer ports through five cores in exact finite checks. The claim is a candidate mechanism, not a general wire theorem or SAT reduction. A different join of the same core collapses its budget, so the local predicate alone does not justify composition.

## Evidence and status

Exhaustive bounded local/dihedral search and independent exact target solves: [round 008](../../campaigns/three-sat-rectilinear-picture-compression/rounds/008/round.md), especially `port_probe.py`, `all_compositions.py`, and `repeat_probe.py`. Antirectangle certificates support lower bounds for selected four- and five-core examples. Not independently reviewed.

## Consequence for search

Test every proposed join for baseline additivity and all-output endpoint behavior before treating it as a signal wire. A complete construction needs a general induction plus occurrence fanout, clause placement and isolation from cross-gadget rectangles.

## Use history

Created 2026-09-25 in round 008. Intended board promotion is pending; the board was not edited.
