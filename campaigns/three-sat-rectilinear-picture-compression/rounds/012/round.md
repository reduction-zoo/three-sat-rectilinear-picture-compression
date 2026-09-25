# Round 012 — reserved 2×2 clause checker

## Plan

Gap: the shared-cell junction leaks, and its additive placements leave no room for a guard. New construction: reserve a 2×2 clause checker before placing variable cores. Align three state-selective local taps to three distinct cells of the checker. A checker picture may force an extra rectangle when all inputs are inactive while allowing an active core rectangle to absorb it.

First discriminating check: enumerate dihedral copies of the `001/111/011` core with each tap aligned to a distinct checker cell, rejecting overlap of cores, checker and state ports. For each geometric candidate, solve its all-inactive baseline and checker picture at budget nine. A costly false row warrants checking the seven positive rows; a lack of placements or false-row failures bounds this specific checker mechanism.

Prior evidence: [rounds 010–011](../010/round.md) expose leakage and packing for a one-cell interface; the reserved region changes the construction. No local board experience entries were present.

## Evidence and diagnosis

`checker_probe.py` placed three core taps at three distinct cells of a fixed 2×2 checker. Up to checker symmetries and input order, the fixed slots cover the possible three-corner attachment patterns. Each slot had ten dihedral/tap options after excluding overlap with the checker. Of 1,000 triples, 562 had pairwise disjoint cores, 324 had state ports outside every core, and 256 had six distinct state ports. The prepared exact target oracle found 188 with additive core budget nine, 146 also with additive all-inactive state ports. Of those 146, 74 made the checker costly for the all-inactive state. Every one of the 74 failed at least one of the seven positive rows, so **zero** satisfied the exact OR condition at budget nine. These are finite target statuses, not source injections; source/recovery instances: 0/0.

`checker_output.txt` retains a leaked 8×7 all-inactive target with a valid nine-rectangle cover. Its first false-costly example is placement 63: activating input 1 leaves the baseline at cost nine, but the checker picture is still infeasible at nine (matrix retained), so the active rectangle cannot absorb this checker. The failure modes are distinct: some placements leak the false row, while the others overcharge an active row. The evidence excludes only this `001/111/011` core, the three enumerated local taps, one 2×2 checker, disjoint/clear ports and budget nine. It does not exclude larger checkers or different cores. Experience extraction: updated [shared-cell clause leak](../../../../research/experience/shared-clause-cell-leak.md).

## Next action

Change proof route: look for a source-level construction that provides clause geometry and isolation, since these small local junctions have not supplied an OR.
