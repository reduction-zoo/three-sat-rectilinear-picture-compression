# Round 018 — two-input edge checker for Vertex Cover

## Plan

Gap: three-input SAT clauses were not obtained from local thick cores. Berman–DasGupta's graph route needs an edge checker with a two-input OR: a cost penalty only when neither endpoint vertex is selected. New construction attempt: use two independently controlled thick cores and a one-cell marker, testing the four state rows instead of a three-input clause.

First discriminating check: enumerate dihedral placements of two local state-selective taps at a shared marker cell, with disjoint cores and clear distinct state ports. At additive budget six, require the all-inactive marker picture to be infeasible and all three patterns with an active input to be feasible. This tests only an isolated two-core edge checker, not graph fanout, routing, global layout or source recovery.

Prior evidence: [round 014](../014/round.md) identifies an edge OR in a published polygon reduction; [rounds 010–012](../010/round.md) exclude several small three-input local junctions. The board experience collection remains absent.

## Evidence and diagnosis

`edge_checker_probe.py` enumerated 276 pairs of the 24 local tap/dihedral placements. It found 180 with disjoint cores and 120 with four clear, distinct state ports. All 120 core unions require the additive budget six. Of 112 with additive all-inactive ports, 88 made the marker costly in the false row. Eighty passed the threshold OR test (`K=6` feasible exactly when at least one input is active). A stronger exact-cost check found **24** placements whose true rows require exactly six rectangles and false row exactly seven. The first threshold-only placement `(0,2)` allowed a five-rectangle cover when both inputs were active; this real counterexample motivated the stronger check and is retained in `edge_checker_output.txt`.

The first exact-cost placement `(0,15)` is proved as a finite gadget in [edge-gadget.md](../../work/edge-gadget.md). `edge_example.py` independently reconstructs its four pictures, verifies 7/6/6/6 by explicit antirectangle lower bounds and validated covers, and solves two alternative target outputs per positive row. The exact target oracle agrees. These are four local state pictures, not four source injections. Actual injected source/recovery instances: 0/0. No variable gadget, arbitrary-degree fanout, global geometry, budget or all-cover assignment decoder exists. Experience extraction: [exact-cost edge checker](../../../../research/experience/exact-cost-edge-checker.md).

## Next action

Test whether two exact-cost edge checkers can share a variable-state core without a budget discount or phase conflict. A graph reduction also needs arbitrary-degree fanout and isolation.
