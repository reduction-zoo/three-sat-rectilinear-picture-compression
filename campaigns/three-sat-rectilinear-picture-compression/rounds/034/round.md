# Round 034 — Wide corridors with mandatory side coverage

## Plan

A one-cell long corridor creates a signal because its mandatory rectangle can enter the next machine. Add a parallel mandatory side strip, so a background rectangle must cover width greater than the signal and cannot extend through the core's narrow notch. First check: the previously failing gap-four translator connection, widths two and three, then flatten the staggered ports of the round 033 swap using side strips placed outside all cores. Need exact input/output costs; the width increase alone is no guarantee. This is a new isolation mechanism addressing the retained round 030 counterexample.

## Evidence and diagnosis

Adding a mandatory side strip repairs the gap-four connection: widths two and three both have exact costs 29,30,29,29, while the retained width-one control has 29,29,28,28 (`output.txt`, 12 state instances). The side strip forces background coverage that cannot act as the full narrow beam.

`flat_swap.py` adds disjoint side strips to the staggered swap. Its common top/bottom boundaries are rows −27 and 37. Baseline is 46 and all 16 states have exact additive unsupported-output penalties (`flat_output.txt`). Two such swaps stacked at offset (65,39) have baseline 91, and all 16 two-channel endpoint states are exact (`compose_output.txt`). The baseline is one below the sum 92, due to background sharing; hence a general additive theorem still needs an interface restriction. All 44 state instances solved, all covers directly validated, no unknown results. Source/recovery 0/0.

Experience extraction: appended to the beam-route entry; the width-one counterexample remains a regression. The next proof attempt will restrict cross-interface rectangles rather than assume count additivity.

## Next action

If long corridors preserve signal costs, derive an isolated routing layout and additive background count.
