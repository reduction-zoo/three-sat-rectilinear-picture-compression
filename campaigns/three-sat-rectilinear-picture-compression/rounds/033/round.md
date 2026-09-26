# Round 033 — Adjacent swap through an inverted crossing channel

## Plan

Build a vertical-input/vertical-output swap from the successful perpendicular crossing plus compact turns on its horizontal channel. Two inversions restore the original signal; the other channel is unchanged. This is a new routing construction, not merely another chain length. Compact turns should leave the other vertical input/output columns clear. First check: legal unobstructed port rays and all 16 two-input/two-output costs. The required table is baseline plus one per unsupported output; source labels follow channels, not column order. Round 032 provides finite turn behavior but warns that baseline cannot be assumed additive.

## Evidence and diagnosis

The compact version failed: supplying the turned channel reduced the baseline, so the intended flat two-channel table did not hold (`repaired_output.txt`, implementation commit `db730f7`). Its first run also exposed an incorrect output endpoint outside the picture (`output.txt`), repaired before any cover claim.

Widening the crossing to span 60 and using full half-translator turns separates the turn cores from the other channel. The resulting swap has baseline 45 and 122 maximal rectangles. All 16 state instances have minimum exactly 45 plus the number of unsupported outputs (`wide_output.txt`), with SAT/UNSAT adjacent thresholds and directly checked witnesses. Input columns are 5 and 16; their corresponding outputs are 55 and 44, so order is reversed. The boundary ports have different heights, however, and arbitrary network composition is not established. Source/recovery counts 0/0; no unknown results.

Experience extraction: appended to the beam-route entry. The next obstruction is connecting staggered ports without a mandatory narrow corridor simulating a signal.

## Next action

If the swap works, route permutations with polynomially many swaps and prove the resulting layout/count.
