# Round 023 — reset staircase boundaries between switches

## Plan

Round 022's modified switch works locally but its predecessor's background covers a later left-staircase corner for free. New isolation strategy: reset the left boundary outward between successive stages. The intervening missing cells should block any rectangle joining earlier background to the new staircase teeth. Keep the holes, beam cores and right boundary unchanged.

First discriminating check: solve the two-stage baseline and require its second output with both inputs absent. A free output refutes the proposed guard. If it charges an extra rectangle, test all 16 input/output states and then identify an antirectangle invariant for arbitrary stage count. The concrete prior leaking witness in round 022 is the regression; the scope is explicitly the two-stage family before any general claim.

## Evidence and diagnosis

The boundary reset raises the two-stage baseline from 31 to 32, but the second outgoing beam is still possible at baseline with both incoming beams absent. `output.txt` gives the exact 32-rectangle witness; Prepare's direct full-target validator accepts it. The first discriminating check therefore refutes this guard, so the remaining truth-table rows were not needed. The original corner-sharing route is blocked, but a rectangle in the previous background now reaches the next stage's input notch (for example the displayed rectangle spanning rows 5–63 and columns 22–40). This supplies the notch without an originating source beam.

Actual checks: one exact baseline search, two threshold solves for the first discriminating state, and one independent witness validation; source/recovery checks 0/0. Experience extraction: none as a separate entry; the retained explicit counterexample further limits the round-022 beam route. A usable filter must block all background rectangles from simulating input beams, not only sharing staircase corners.

## Next action

Investigate an alternative primary proof with a simpler global layout before adding more local guards. The known hardness result remains the target of reconstruction.
