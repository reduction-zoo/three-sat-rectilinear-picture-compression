# Round 006 — robust 4×4 phase tile

## Plan

Gap: the five-cell staircase's two maximal covers differ by one rectangle and its phase can slip under endpoint composition. Search a larger, still finite tile family for two minimum maximal covers differing by at least two rectangles, ideally with distinct extendible boundary ports. This is an expanded synthesis family and a new tile mechanism.

Proposed full interface remains a variable wire with a phase propagated between tiles and clause cells covered by a true literal port. Unresolved composition obligations are phase coupling, crossing/routing, gadget isolation and all-output decoding.

First discriminating check: enumerate connected full-span 4×4 binary pictures, exact maximal rectangles and all optimum covers, then identify any with exactly two optimum maximal covers whose symmetric difference has at least four rectangles. A candidate must be tested with the independent oracle and with an actual two-tile join before scaling; no such tile would exclude only this bounded family.

Prior evidence: round 005's 3×3/3×4 enumeration and endpoint-coupling counterexample; its lesson applies to this search.

## Evidence and diagnosis

`robust_tile_probe.py` exhausted all 65,536 binary 4×4 matrices. Of these, 7,943 were connected and spanned every row and column. Exactly 976 had two minimum covers after restricting to inclusion-maximal rectangles, but **none** had a symmetric difference of four or more rectangles: every such pair differs by only one rectangle on each side. The script cross-checked minimum cover size for 20 spread-out connected instances using the independent Z3 target oracle at `K-1` and `K`; all matched exhaustive enumeration. The earlier 3×3/3×4 script was rerun after making its helpers importable and retained its reported counts.

Expected for the stronger tile strategy: at least one 4×4 picture with two coupled multi-rectangle phases. Actual: zero in the stated finite family. This does not rule out a larger tile, a gadget with more than two raw optimum covers but only two decoded states, or a different coupling method. The cause of the 4×4 exclusion is not established by a general theorem. No composition was tested because no candidate met the first gate. Actual source/target/recovery instances: 0/40/0 for the 20 oracle samples at two budgets; no F/G exists.

Experience extraction: [small two-cover tile bound](../../../../research/experience/small-two-cover-tiles.md), a bounded exclusion. This round used the staircase lesson from round 005 to require a stronger phase separation; no advance resulted.

## Next action

Change construction strategy rather than enlarge the same local search without a reason to expect a different phase mechanism.
