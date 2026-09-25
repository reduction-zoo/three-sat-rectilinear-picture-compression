# Finite same-state taps in a thick wire

## Claim and applicability

Tags: rectangle cover, Boolean gadget, fanout, occurrence tap, thick wire. The 3×3 core `001/111/011` has two exclusive state ports and local taps for both states. In one explicit four-core wire, all four transformed copies of one Q tap remain selective relative to the wire endpoints. Two taps on alternating cores can be included simultaneously at the base cover budget, together with their matching endpoint. Mixed-state tap pairs cost more. This is a finite example, not a general fanout theorem.

## Evidence and status

[Round 009](../../campaigns/three-sat-rectilinear-picture-compression/rounds/009/round.md) records the local search, alternate core and join tests, exact four-core target solves, and the failed internal-tap behavior of the earlier core. The reproducible script is `fanout_multi_probe.py`; its compact output is `fanout_multi_output.txt`. No source-to-target reduction or independent review exists.

## Consequence for search

Local tap selectivity alone is insufficient: it can disappear after joining cores. The alternate core justifies investigating a clause junction and a general composition invariant, but finite fanout does not establish arbitrary occurrence count or global geometric isolation.

[Round 020](../../campaigns/three-sat-rectilinear-picture-compression/rounds/020/round.md) exhausted the thick 3×3 core family with individually free but jointly costly exterior state ports. Among 224 such port pairs, no pair has more than two one-cell exterior taps selective for the same state (24 have zero, 32 have one, 168 have two). This bounds the direct degree-three same-state attachment route in that finite family, not larger or nonlocal fanout mechanisms.

## Use history

Created 2026-09-25 from round 009. Intended board promotion is pending; the board was not edited.
Updated 2026-09-25 from round 020.
