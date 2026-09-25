# Round 017 — diagonal-band dynamic programming boundary

## Plan

Gap: the certified wire grows indefinitely but stays in a narrow diagonal band. Investigate whether every binary picture in a fixed-width band `ℓ ≤ ar+bc ≤ ℓ+w` has a polynomial exact rectangle-cover algorithm. A positive theorem would show that simply lengthening or combining isolated diagonal wires cannot by itself yield a hard global construction; clause or crossing geometry must increase structural width.

First discriminating check: prove that every valid rectangle in such a picture spans at most `⌊w/a⌋+1` rows and each row contains at most `⌊w/b⌋+1` candidate columns. Build a row-scan DP over the bounded frontier and compare its minimum cover counts on seeded thick and sparse band pictures against the prepared independent target oracle. A counterexample would invalidate the DP invariant; agreement on finite cases supports, but does not replace, the proof.

Prior evidence: [wire lemma](../../work/wire-lemma.md) gives a repeated wire translated by `(3,-2)`; its coordinates satisfy a constant-width `2r+3c` band. [Round 007](../007/round.md) proves a different thin-picture polynomial class.

## Evidence and diagnosis

The [band lemma](../../work/band-lemma.md) proves an exact row-scan dynamic program with at most `2^{hq}` frontier states, where `h=⌊w/a⌋+1` bounds rectangle height and `q=⌊w/b⌋+1` bounds one-cells per row. Every all-one rectangle has a unique top row, so the recurrence covers all legal covers and only legal covers. The explicit repeated wire has `7≤2r+3c≤20`; adding either endpoint expands the upper bound only to 21. Hence a single wire of arbitrary length remains in one constant-width band.

`band_dp.py` implements the recurrence without importing a candidate construction. It was compared with the prepared exact target oracle on 21 deterministic 6×6 pictures in the band `5≤2r+3c≤12`: one full-band picture and 20 variants from seed 20260925. Five contained a 2×2 all-one block and 16 did not. All 21 minimum cover counts agreed; the script fails on a disagreement. These finite checks support the implementation, while the recurrence proof supplies the unbounded claim. Source/recovery instances: 0/0. The theorem does not apply to global pictures with growing band width, so it does not establish impossibility of a 3SAT reduction. Experience extraction: [diagonal-band tractability](../../../../research/experience/diagonal-band-tractability.md).

## Next action

Any wire-based hard construction must account for how clause, fanout or crossing geometry leaves this restricted single-band class. Continue with a genuinely different global encoding or a clause mechanism.
