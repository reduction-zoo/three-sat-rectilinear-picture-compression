# Round 030 — Narrow-channel routing between isolated translators

## Plan

The adjacent translator chain passes, but cannot yet route between remote components. New construction: separate consecutive pairs by an all-one one-cell channel, surrounded by zeros. This would isolate arbitrary backgrounds and permit orthogonal wire crossings. First discriminating check: a two-pair chain with a positive gap must retain the implication cost table; if the gap itself can create an output for free, the crossing extension is invalid and should not be attempted. Test gaps 1 and 4, with adjacent gap 0 as a control. Reuse round 027 pair geometry and exact oracle; no assumptions from unpublished global routing.

## Evidence and diagnosis

Exact costs in input/output order 00,01,10,11: gap 0 gives 28,29,28,28; gap 1 also gives 28,29,28,28; gap 4 gives 29,29,28,28 (`output.txt`). Thus a positive short join is valid, but an arbitrarily extendable narrow corridor is not. The gap-cover rectangle itself can simulate the downstream input, and the incoming beam instead earns a discount. All 12 partial-cover state instances solved with direct witness validation. No timeout; no source or recovery instances. The proposed long-channel crossing was not attempted because its premise fails.

Experience extraction: none; this is a scoped limitation of the round 027 translation route, not an obstruction to other crossing designs.

## Next action

Attempt a crossing only if the gap preserves a signal.
