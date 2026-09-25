# A two-input checker can have exact OR cost

## Claim and applicability

Tags: rectangle cover, thick core, Vertex Cover, OR checker, exact budget. Two dihedral copies of the `001/111/011` core form an isolated one-cell edge checker with minimum cover cost 7 when both input ports are inactive and 6 for every other input pair. Exact cost in all active rows matters: a different placement passes threshold feasibility but saves one rectangle when both inputs are active.

## Evidence and status

[Round 018](../../campaigns/three-sat-rectilinear-picture-compression/rounds/018/round.md) exhausts the stated two-core placement family. [Finite gadget proof](../../campaigns/three-sat-rectilinear-picture-compression/work/edge-gadget.md) gives cells, four antirectangles and four covers; the reproducer checks them with the independent target validator. No composition theorem or independent review exists.

## Consequence for search

Require an exact cost table, not merely a yes/no threshold table, before summing gadget budgets. The remaining hard step is to create one fixed global picture whose cover states select variable values while preserving edge costs and preventing cross-gadget discounts.

Round 019 found three clear two-edge compositions around one shared core. Each preserves the Vertex Cover threshold at budget nine for all eight state assignments, but two uncovered edges together cost only one extra rectangle. Thus even an exact isolated cost table need not have additive penalties after composition; threshold correctness needs a separate global proof.

## Use history

Created 2026-09-25 from round 018. Intended board promotion is pending; the board was not edited.
Updated 2026-09-25 from round 019.
