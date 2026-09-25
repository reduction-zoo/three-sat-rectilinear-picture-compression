# Round 020 — degree-three same-state fanout

## Plan

Gap: round 019 shares one central state across two edge checkers. A bounded-degree Vertex Cover route needs degree three, and the tested central `001/111/011` core has only two locally P-selective taps. New construction: search all thick 3×3 exclusive-port cores for three same-polarity taps, then seek three disjoint exact-cost edge-checker attachments around one center. This tests whether a local degree-three vertex gadget exists in the prepared core family.

First discriminating check: enumerate local state-selective taps for every exclusive core/port pair from round 008, count same-polarity triples, and test geometric placement of three leaf attachments. If an exact local star exists, compare all 16 center/leaf state assignments at the predicted Vertex Cover threshold. Failure at any stage bounds only this 3×3 one-cell-port construction family.

Prior evidence: [round 019](../019/round.md) gives degree-two threshold behavior; [round 009](../009/round.md) found local tap selectivity but warned that joins may erase it. The board experience collection remains absent.

## Evidence and diagnosis

`degree_three_probe.py` exhaustively enumerated the round 008 family: all 224 pairs of individually free but jointly costly exterior state ports on thick 3×3 cores. For each pair it queried every other one-cell exterior port against both state ports, retaining a tap only if it was individually free and compatible with exactly one state. The tap phase made 1,548 distinct exact-target oracle queries. The maximum number of taps for either one state was **two**. Counts by maximum were 24 pairs with zero, 32 with one, and 168 with two; see `degree_three_output.txt`.

Thus the first discriminating check failed: no core in this family has three same-state one-cell exterior taps. The planned three-leaf attachment and 16-row threshold test were not run because they require those three taps. This excludes only this 3×3 exclusive-port, one-cell exterior-tap construction; a larger core, multi-cell tap, mixed-polarity encoding or nonlocal fanout remains possible. There is no new fixed target F, recovery G, source injection, or general proof (0/0 source-to-target tests and recovery checks). The prepared target oracle supplies the finite verdict, and no solver query returned unknown.

Experience extraction: updated [finite same-state taps](../../../../research/experience/thick-wire-fanout.md). This ends discovery at the authorized 20-round budget; no reviewer stage is applicable without F, G and a proof.

## Next action

Close the campaign with the exact partial lemmas and failed gadgets intact. Any resumed campaign needs a new round allocation and a construction that solves global variable fanout, routing, isolation, budget accounting and all-output decoding.
