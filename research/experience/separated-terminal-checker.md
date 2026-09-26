# A fixed two-input rectangle-cover terminal

Tags: rectangle cover, Vertex Cover, OR terminal, fixed picture, antirectangle certificate.

## Claim and applicability

A fixed staircase mask with two opposed input stems has minimum cost six without supplied beams and five with either or both. Its input columns can be separated arbitrarily by duplicating a non-input column. This uses a fixed allowed picture and varying externally supplied cells.

## Evidence and status

[Round 037](../../campaigns/three-sat-rectilinear-picture-compression/rounds/037/round.md) retains exact covers and antirectangle certificates for all four base states. The [general terminal lemma](../../campaigns/three-sat-rectilinear-picture-compression/work/terminal-lemma.md) proves invariance under middle-column duplication. Independent review is pending; no full reduction follows.

## Consequence for search

Use input backgrounds on the left of the first beam and right of the second. Upstream wings must be opposite for a beam-only cut. Do not stretch an input column itself while assuming its supplied cells remain a unit-width beam.

## Use history

Created 2026-09-25; no later application yet. Board promotion pending separate authorization.
