# Beam-only cuts make cover counts compositional

Tags: rectangle cover, gadget composition, arbitrary outputs, charging decoder.

## Claim and applicability

If every maximal rectangle crossing a module interface is a designated beam meeting exactly two modules, every cover can be charged to local state-cover bounds without losing rectangles to shared backgrounds. This is a conditional general lemma. It applies only after checking all cross-interface rectangles, not just intended witness covers.

## Evidence and status

[Round 035](../../campaigns/three-sat-rectilinear-picture-compression/rounds/035/round.md) proves the [decomposition and conditional Vertex Cover decoder](../../campaigns/three-sat-rectilinear-picture-compression/work/cut-composition.md), and checks a trimmed swap plus a two-swap union. Finite local tables and the general conditional proof have not received independent review. No complete source reduction follows.

## Consequence for search

Put outgoing background on one side of a port and incoming background on the other so their adjacent boundary rows intersect only in isolated beam columns. Enumerate all cross-interface maximal rectangles. Preserve a positive-only routing interpretation: the checked swap permits dropping a signal, so complementing its channel does not preserve its implication semantics.

## Use history

Created 2026-09-25. No subsequent application yet. Intended board promotion remains pending separate authorization; no board edit made.

Applied in [round 039](../../campaigns/three-sat-rectilinear-picture-compression/rounds/039/round.md): narrower external caps removed a genuine overlap, and eight routed permutations satisfy exact rectangle ownership. A general spacing invariant and constant-template certificates were recorded; full source integration remains pending.
