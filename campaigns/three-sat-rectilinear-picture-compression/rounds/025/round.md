# Round 025 — Span-blocking holes for stage isolation

## Plan

Round 022/023 counterexamples use rectangles from an earlier right staircase to supply a later input notch. The previous regularization put its right hole strictly to the right of the first staircase corner, so that corner's rectangle escaped the intended blocker. New geometric isolation strategy: place the hole across the horizontal span of ALL earlier staircase corners, as required by the published stage-isolation lemma. Retain the local machine interface, then check two composed stages before scaling.

First check: one-stage implication table and the two-stage all-input-absent/second-output-present counterexample. A passing local table alone is insufficient. Experience used: vertex-cover-beam-route; round 023 distinguishes left-boundary and right-background leaks.

## Evidence and diagnosis

The one-stage table is exact (16,17,16,16), but two stages still leak. With right-hole span extension only, baseline is 31 and the second output can be present at 31 with both inputs absent (`kissat_output.txt`). Combining the previous left-boundary reset gives baseline 32 and the same leak at 32 (`combined_output.txt`). Both logs retain full validated covers. The isolated blocking conditions do not make the backgrounds independent: a middle background rectangle can supply a later notch, or a previous left background can cover a later staircase.

The initial Z3 run timed out on the two-stage baseline (`output.txt`), an execution failure. Added an installed-Kissat backend with explicit sequential cardinality CNF; its self-test compares minima and all lower budgets for all 511 nonempty 3×3 pictures to Z3. Self-test passed. All SAT witnesses are directly validated for exact legal coverage, cardinality and forced output rectangles. `blocked(inputs, reset=False)` reproduces the first geometry; default enables both barriers. Reproduce: `uv run python campaigns/three-sat-rectilinear-picture-compression/rounds/025/check.py --kissat`. Two two-stage counterexamples, four one-stage state rows checked per variant; source F/G and recovery counts remain 0/0. Tests were written before the new modules and failed on missing imports.

Experience extraction: none; this is a precise additional composition counterexample to the existing beam-route entry, not a general impossibility theorem.

## Next action

If isolation holds, test all two-stage port states and derive a general certificate. Otherwise retain the exact failing cover.
