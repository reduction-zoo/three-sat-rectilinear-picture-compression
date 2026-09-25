# Round 009 — occurrence tap and fanout

## Plan

Gap: round 008 supplies a finite two-end wire, but a source variable may occur in arbitrarily many clauses. Hypothesis: an extra exterior port on the thick core can act as a literal tap. For two exclusive state ports `P,Q` at base cost `k`, seek a third port `T` such that `{P,T}` remains coverable at `k` while `{Q,T}` costs more. It must remain valid when a core is embedded in a wire, where neighboring rectangles may create unintended coverage.

First discriminating check: enumerate all 3×3 thick cores and free exterior port triples using the prepared exact target oracle, prioritizing the core used in round 008. A local tap candidate must then be placed on an internal core of the explicit three-core wire and tested at its exact budget with both endpoint states. This is a new fanout construction attempt, not a new parameter for the wire's length.

Prior evidence: round 008's [candidate mechanism](../../../../research/experience/thick-exclusive-ports.md) gives exclusive end ports through five finite core joins. Its general induction and clause routing remain open.

## Evidence and diagnosis

`tap_probe.py` checked the 224 exclusive local core/port pairs from round 008 against free third ports. It found 408 state-selective local taps. Forty pairs have taps for both states, in six dihedral orbits. Counts refer to local geometries, not independent source instances. The original round-008 core `000/011/111` has local taps, but `wire_tap_probe.py` found that its internal taps lose selectivity in the explicit three- and five-core wires; only the ends retain selective taps. Thus local selectivity is not compositional.

`alternate_core_probe.py` tested the six both-polarity orbit representatives in a two/three-core join family. The representative `001/111/011`, budget 3, with state ports `P=(4,2)` and `Q=(1,4)`, has local P taps `(0,3),(4,3)` and a Q tap `(3,4)`. It yielded two additive two-core joins, four additive/exclusive three-core wires, and four surviving selective taps. The other five representatives yielded no additive three-core wire in this tested topology. `fanout_chain_probe.py` extended the first explicit three-core wire: 18 disjoint four-core joins were tested, four retained additive cost 12 and exclusive endpoints, and all four kept the middle tap selective.

`fanout_multi_probe.py` checks one explicit four-core wire at budget 12. The core tap `(3,4)` maps to `(3,4),(6,1),(0,6),(8,-2)` on the four cores. Each is individually free. Relative to the two endpoints `(-2,6),(8,-4)`, their compatibility patterns alternate `[true,false]`, `[false,true]`, `[true,false]`, `[false,true]`. The two same-state tap pairs (first/third and second/fourth) are jointly free **and** jointly compatible with their matching endpoint. All four mixed-state pairs are infeasible at budget 12. The full finite result is in `fanout_multi_output.txt`; the script uses the prepared exact target oracle. The initial run was interrupted during a redundant joint endpoint solve; the resumed run completed with progress output and the same geometry. The interrupted run supplied no target verdict.

This is a finite two-occurrence fanout example, not a general wire/fanout theorem. No arbitrary-length construction, clause junction, polynomial layout, global budget, or recovery rule has been proved. Actual injected source instances/recovery outputs: 0/0. Experience extraction: [finite same-state taps](../../../../research/experience/thick-wire-fanout.md).

## Next action

Try a three-input clause junction using state-selective taps. Test whether placing three independently controlled cores around one clause cell preserves their additive budgets and makes the clause cell free exactly when a literal is active.
