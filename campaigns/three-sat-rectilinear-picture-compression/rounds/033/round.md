# Round 033 — Adjacent swap through an inverted crossing channel

## Plan

Build a vertical-input/vertical-output swap from the successful perpendicular crossing plus compact turns on its horizontal channel. Two inversions restore the original signal; the other channel is unchanged. This is a new routing construction, not merely another chain length. Compact turns should leave the other vertical input/output columns clear. First check: legal unobstructed port rays and all 16 two-input/two-output costs. The required table is baseline plus one per unsupported output; source labels follow channels, not column order. Round 032 provides finite turn behavior but warns that baseline cannot be assumed additive.

## Evidence and diagnosis

Pending.

## Next action

If the swap works, route permutations with polynomially many swaps and prove the resulting layout/count.
