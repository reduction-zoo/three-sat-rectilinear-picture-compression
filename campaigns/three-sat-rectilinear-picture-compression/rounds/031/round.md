# Round 031 — Perpendicular translator crossing

## Plan

Cross the shared horizontal rectangle of one paired translator with the shared vertical rectangle of a rotated translator. Their four beam cores remain disjoint; only their background strips overlap. This avoids the long mandatory narrow corridor that loses its signal. Use span 40 and rotate/translate the second pair by (r,c)→(c−15,r+15). First check: all 16 input/output states with baseline plus one cost per unsupported output. If a mixed state leaks, preserve its cover and do not claim a crossover. Reuse paired-translation evidence, but background union changes the allowed rectangle family.

## Evidence and diagnosis

`crossing.py` gives a 40-span perpendicular-pair union with 78 maximal rectangles. All 16 input/output state instances have minimum exactly 28 plus the number of unsupported outputs (`output.txt`). Each result includes SAT at that budget and UNSAT one below. `compose.py` joins two such crossings by their vertical channel at offset (14,30); all 64 three-input/three-output states have exact minimum 56 plus unsupported outputs (`compose_output.txt`). Covers are validated directly, and the existing backend self-test covers its SAT encoding. No unknown results. Source/recovery counts remain 0/0.

This is positive finite evidence for an explicit crossover and a nontrivial composition. It does not yet supply arbitrary routing, a turn interface, a general all-cover proof, or an executable source map. Experience extraction: appended to the beam-route entry. Reproduction: `uv run python campaigns/three-sat-rectilinear-picture-compression/rounds/031/crossing.py` and `.../compose.py`.

## Next action

If the table is exact, establish all-cover isolation and connect to source/edge components.
