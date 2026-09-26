# Round 036 — Terminal OR checker with two incoming beams

## Plan

Replace the geometric edge gadget by a directly synthesized terminal picture. Enumerate all 3×3 masks and two vertical input column runs entering from the top; seek minimum cover costs B+1,B,B,B after those run cells are supplied. This is a fixed target picture with optional supplied cells, unlike earlier state-dependent edge pictures. First check: exact minima for every input row, retaining a constant gap even when both inputs are supplied. If no 3×3 mask works, this family is exhausted; larger masks would be another attempt. The cut-composition lemma explains the needed interface but does not establish this terminal.

## Evidence and diagnosis

Exhausted all 511 nonempty 3×3 masks and their eligible pairs of top-entering maximal column runs: 384 input-pair geometries, four input states each (1,536 state instances). None has costs B+1,B,B,B. `search.py`/`output.txt` give the reproducible family and count. Each optimum was found by exact budget queries with direct validation of returned covers; no unknown results. This excludes only that tiny mask/input family, not a terminal edge gadget in general. Source/recovery 0/0.

Experience extraction: none; a small-family exclusion remains in the round record. The next construction needs more area or a different input orientation.

## Next action

Pad a found terminal's input boundaries to beam-only cuts and check its table.
