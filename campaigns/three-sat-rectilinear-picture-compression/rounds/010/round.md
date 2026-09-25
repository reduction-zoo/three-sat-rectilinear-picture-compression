# Round 010 — three-input clause junction

## Plan

Gap: round 009 has finite state-selective taps but no clause OR. Hypothesis: three rotated copies of the thick `001/111/011` core can approach one shared outside cell through their Q taps. Give each copy one exterior state port, with `P` inactive and `Q` active. At additive budget 9, the shared clause cell should be coverable for exactly the seven state patterns with an active input.

First discriminating check: enumerate dihedral placements with all three taps at one cell, rejecting overlapping cores and occupied state ports. For each surviving geometry, independently solve the eight state-port pictures with and without the clause cell at budget 9, checking baseline additivity and the exact OR truth table. The negative outcome would exclude only this one-cell, three-local-core junction family, not larger clause gadgets.

Prior evidence: [round 009](../009/round.md) found the core and finite same-state fanout; [round 007](../007/round.md) rules out thin-only gadgets. The board experience collection had no entries in the local checkout.

## Evidence and diagnosis

`clause_probe.py` enumerated 2,024 triples of the 24 dihedral placements of the core's three state-selective local taps (two P taps, one Q tap), all aligned to one clause cell. It found 432 triples with pairwise disjoint cores, 96 with no state port inside a core or at the clause cell, and 56 with six distinct state ports. The original Q-only version had six disjoint placements and zero with all state ports clear; expanding to both polarities was necessary to test a nonempty family.

The prepared exact target oracle found that all 56 core unions require nine rectangles. With all three input state ports set inactive, 16 placements still require exactly nine rectangles before the clause cell is added. In **all 16**, adding the clause cell remains feasible at budget nine, violating the required false row of the OR table. Thus none of the 56 placements is an exact OR junction under the stated additive-budget design. The first leak uses orientation indices `(0,1,12)`; `clause_output.txt` records its 7×6 target matrix and one valid nine-rectangle cover. These are target solves; source/recovery instances remain 0/0.

The supported diagnosis is that local state-selective tap predicates do not survive this three-way identification: a cover can reorganize across the joined picture and include the shared cell at no added cost. The check excludes only three copies of this particular 3×3 core, these three tap locations, dihedral placement, one shared cell, and budget nine. It says nothing about a larger junction, isolation spacers, or a different core. Experience extraction: [shared-cell clause leak](../../../../research/experience/shared-clause-cell-leak.md).

## Next action

Investigate a clause interface with geometric isolation or a different encoding; keep the leak matrix as a regression for any proposed shared-cell rule.
