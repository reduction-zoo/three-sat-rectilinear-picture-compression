# Round 003 — one-anchor-per-vertex graph embedding

## Plan

Gap: round 002's exact graph-coloring equivalence is useful only if source constraints can be realized by a binary picture. Hypothesis: give each graph vertex one distinguished one-cell at a unique row and column, and fill the bounding box of each nonedge to make those anchors compatible. First discriminating check: for a small graph, enumerate anchor row/column orders and see whether required filler ones inevitably erase a requested conflict edge. If so, a one-anchor scheme needs a different mechanism (copies or consistency gadgets).

Prior evidence: [round 002](../002/round.md) proves pairwise compatibility is enough for rectangle classes. Its experience entry applies to one-cells, and its premise is met here.

## Evidence and diagnosis

`anchor_probe.py` enumerated all 8 labeled 3-vertex, 64 labeled 4-vertex and 1,024 labeled 5-vertex graphs. Each had *some* row/column permutation for which filling the bounding boxes of all nonedges realized the desired conflict relation among anchors. This finite observation is not a general embedding theorem; choosing a placement by permutation search is itself exponential and cannot be used as F.

The same experiment then tested cover cost. The first viable placement for the 4-vertex conflict graph with edges `{01,03,12}` produced [this 4×4 picture](filler_counterexample.json). Its graph is 2-colorable, but the independently solved picture has no 2-rectangle cover; a 3-rectangle cover is listed in the reproducer. Expected if the naive construction worked: target YES at `K=2`. Actual: `NO-SOLUTION`. A different placement of the same anchors *does* admit two rectangles, so this is an obstruction to the naive placement rule and to inferring total cover cost from anchor conflicts, not an impossibility result for all embeddings. The extra one-cells needed to fill nonedge boxes create new cover obligations.

Actual tested graph instances: 1,096 for anchor-relation realizability, plus 14 four-vertex and 22 five-vertex first-placement cover tests before a mismatch. Target solves for the retained reproducer: two budgets (`K=2,3`); source and recovery instances: 0. Supported cause: filler-cell cover cost was omitted from the budget. Remaining obligation: a placement/gadget rule computable in polynomial time with proved filler cost, or a different construction.

Experience extraction: update to the [pairwise rectangle-hull lemma](../../../../research/experience/pairwise-rectangle-hull.md) use history; its compatibility statement remains valid and exposed the missing filler budget.

## Next action

Explore a gadget with a fixed baseline cover that pays for filler cells, or switch to a published polygon reduction.
