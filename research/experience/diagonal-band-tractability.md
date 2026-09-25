# Fixed-width diagonal bands admit exact covering DP

## Claim and applicability

Tags: rectangle cover, diagonal band, dynamic programming, wire. If all one-cells satisfy `ℓ≤ar+bc≤ℓ+w` for positive fixed `a,b` and fixed `w`, then every legal rectangle has bounded row span and each row has bounded one-cells. A row-scan frontier DP finds the exact minimum cover in polynomial time. The explicit thick wire of round 015 stays in such a band for every length.

## Evidence and status

[Proof and recurrence](../../campaigns/three-sat-rectilinear-picture-compression/work/band-lemma.md); [round 017](../../campaigns/three-sat-rectilinear-picture-compression/rounds/017/round.md) has 21 independent target-oracle comparisons including five thick examples. The result concerns one band; it has not been independently reviewed.

## Consequence for search

Lengthening a single diagonal wire does not create unbounded cover complexity. A reduction based on these wires needs interactions whose width or incidence structure can represent source clauses and assignments; the band theorem does not rule out such global arrangements.

## Use history

Created 2026-09-25 from round 017. Intended board promotion is pending; the board was not edited.
