# Round 027 — Paired beam translation with two forced backgrounds

## Plan

Replace the leaking single-machine permutation strip by an isolated pair of opposed beam machines, following the translation-stage idea. A shared horizontal rectangle covers both mouths when inactive; an incoming vertical beam should enable an outgoing vertical beam at the same incremental cost. Two opposite staircase/background anchors should cover the auxiliary mouth squares. First check: all four input/output partial-cover states for one pair, with actual full-length output rectangle forced. Geometry is generated explicitly, not inferred from a favorable cover. The existing beam-route experience and Figure 11 motivate the interface but do not prove this regularization.

## Evidence and diagnosis

The first background fill erased structural zeros and collapsed both cores: all four costs were nine (`output.txt`). That diagnostic version used `box(5,0,span-4,11)|box(5,-2,span-8,0)|box(9,11,span-4,13)` in `pair`. The repaired fill preserves the core boundaries and has exact costs 14,15,14,14 for spans 18 and 24 (`repaired_output.txt`, eight state instances).

Chaining pairs at offsets (row,column)=(14i,8i) preserves the intended endpoint table for lengths 1,2,3,4: baseline 14n, one extra rectangle precisely for a forced output without supplied input. `chain_output.txt` records all 16 state instances with SAT at the expected budget and UNSAT one below; covers directly checked by the previously cross-checked Kissat backend. No timeouts. The interface is an actual full output rectangle, not just an endpoint cell. This is finite evidence, not a general chain proof or crossing gadget.

Reproduce `uv run python campaigns/three-sat-rectilinear-picture-compression/rounds/027/probe.py` and `.../chain.py`. Source F/G injections and recovery: 0/0. Experience extraction: update the beam-route entry to retain this positive finite composition result; global routing and arbitrary-cover decoding remain open.

## Next action

Only compose if the exact local implication table holds.
