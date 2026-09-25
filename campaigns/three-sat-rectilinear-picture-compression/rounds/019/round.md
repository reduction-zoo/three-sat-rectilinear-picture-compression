# Round 019 — share a variable core between two edge checkers

## Plan

Gap: round 018's exact-cost OR table concerns an isolated pair of cores. A graph Vertex Cover reduction needs one vertex choice to feed every incident edge. New construction: attach two exact-cost edge checkers at distinct state-selective taps of one shared core, with one central state port and separate leaf state ports.

First discriminating check: enumerate locally exact-cost pair attachments to the fixed central `001/111/011` core, then form disjoint two-leaf compositions. For each, solve all eight central/leaf state assignments with both checker cells present. At budget nine, require no discount below nine when both edges are covered and a penalty whenever any edge has both endpoints inactive. A failure records which state row or cross-gadget rectangle breaks composition.

Prior evidence: [edge-gadget.md](../../work/edge-gadget.md) has a finite 7/6/6/6 table; [round 009](../009/round.md) shows local taps can lose selectivity after joining. This attempt tests one fixed three-core fanout, not arbitrary degree or a full source reduction.

## Evidence and diagnosis

`shared_core_probe.py` tested 30 nonoverlapping attachments of a leaf core to one of the central core's state-selective taps. Six passed the isolated exact-cost 7/6/6/6 edge table. Three pairs of these attachments used two distinct, same-polarity central taps with disjoint leaves, clear checker cells and six distinct state ports. For each pair, the prepared exact target oracle computed the minimum cover for all eight central/leaf state assignments by budget binary search: 24 combined pictures total.

All three compositions had the same cost table. If the central input is active, cost is 9 regardless of the two leaves. If it is inactive, cost is 9 only when both leaves are active; otherwise cost is 10. Thus the **Vertex Cover threshold at nine survives** for a two-edge path. The tempting additive formula `9 + number of uncovered edges` is false: the all-inactive row has two uncovered edges but costs 10, not 11. `shared_core_output.txt` retains each placement, all eight minima and a concrete matrix for this discount. The discount appears to share one extra rectangle between the two local penalties; that causal explanation is plausible from the geometry but is not proved. No full fixed target, source injections or recovery outputs exist (0/0).

This is a finite degree-two fanout example. It does not prove composition for arbitrary graph degree, multiple checkers, routing across a planar or nonplanar layout, a global budget lower bound, or an assignment decoder from every cover. Experience extraction: updated [exact-cost edge checker](../../../../research/experience/exact-cost-edge-checker.md).

## Next action

Test whether a third incident edge can be attached with one central state and threshold preservation, or whether degree-two geometry is the limit of this local core. The final round should also assess remaining global obligations honestly.
