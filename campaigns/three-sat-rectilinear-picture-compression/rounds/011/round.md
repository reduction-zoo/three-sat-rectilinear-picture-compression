# Round 011 — guarded two-cell clause marker

## Plan

Gap: round 010's one-cell clause junction leaks under all inactive inputs despite additive core budgets. New construction: add one neighboring guard cell to the clause marker, so an inactive cover must pay for the pair while an active input can absorb it. Use the same independently controlled thick cores; the guard changes the clause interface rather than a seed or core parameter.

First discriminating check: for every round-010 placement with additive all-inactive baseline, put the guard at each vacant orthogonally adjacent cell. Keep the marker cells outside cores and state ports. Solve the all-inactive row first at budget nine; only if it costs more, check all seven active rows and their baseline budgets. A success is a finite two-cell OR; failure excludes this bounded guard family only.

Prior evidence: [round 010](../010/round.md) records 16 eligible one-cell placements and an explicit leak. The local board experience collection has no entries.

## Evidence and diagnosis

`guard_probe.py` reconstructed the round-010 placements with six distinct clear state ports and used the prepared target oracle to retain the 16 with an additive all-inactive budget of nine. In every one of those 16 geometries, all four cells orthogonally adjacent to the clause cell are already occupied by a core or a state port. Therefore there are **zero legal adjacent guard placements** under the plan's disjoint-interface condition; no two-cell target solve was needed. `guard_output.txt` records 16 eligible geometries, zero guarded geometries, zero false-costly tests and zero exact ORs. Source/recovery instances: 0/0.

This is a geometric obstruction for this specific one-neighbor guard construction, not a proof that larger or differently routed clause checkers cannot work. The failed assumption was that one neighboring cell remained available around an additive three-way junction. Experience extraction: updated [shared-cell clause leak](../../../../research/experience/shared-clause-cell-leak.md).

## Next action

Try a clause mechanism that reserves its marker region before routing the three inputs; the compact shared-cell geometry leaves no adjacent free cell for this repair.
