# Round 037 — Four-row terminal synthesis by exact residual-cover search

## Plan

Expand to four-row/four-column terminal masks, which allow two independent background obligations below top-entering beams. Enumerate at most 65,535 nonempty masks and six top-column input pairs; stop at the first exact B+1,B,B,B terminal. Use an exact residual-set dynamic program over maximal rectangles, first cross-checked against the existing SAT oracle on every nonempty 3×3 picture and nontrivial supplied subsets. This is an expanded construction family, not evidence that the 3×3 exclusion extends. First discriminating check: find and independently SAT-verify one four-row terminal; otherwise record the full finite exclusion.

## Evidence and diagnosis

The residual DP passed 1,022 full/partial 3×3 comparisons against independently encoded SAT bounds (`dp_selftest.txt`); its test failed on the missing module before implementation. The first 4×4 terminal, mask 894, has adjacent ports and costs 3/2/2/2 after 1,338 eligible input-pair tests. Requiring outermost columns excludes all 16,384 eligible masks (`separated_output.txt`; reproduce with `search.py --separated 3`). Requiring distance at least two finds mask 14311 with columns 0 and 2 and costs 4/3/3/3 after 10,730 tests (`distance_two_output.txt`; `--separated 2`). Both found tables were independently SAT checked.

`padded.py` duplicates a NON-input middle column to separate the ports arbitrarily, then adds opposite-sided two-cell-wide input stems. Costs are exactly 6/5/5/5 at gaps 3,11,30 (12 state instances). `certificates.json` retains explicit matching covers and antirectangle lower bounds for all four gap-three states, directly verified by `certify.py`. The [terminal lemma](../../work/terminal-lemma.md) extends these finite certificates to every gap g≥2 by duplication of identical non-input columns. No unknown results; source/recovery 0/0.

Experience extraction: new separated-terminal entry. A complete reduction still needs source modules and an isolated global layout.

## Next action

Give explicit covers/lower bounds and attach beam-compatible port padding if a terminal is found.
