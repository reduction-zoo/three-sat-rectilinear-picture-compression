# Round 002 — pairwise compatibility graph

## Plan

Gap: a direct gadget must constrain which one-cells share a rectangle. Hypothesis: color the graph on one-cells where two cells conflict if their bounding rectangle contains a zero; a color class may correspond to one legal rectangle. First discriminating check: exhaust small point sets for a color class whose every pair is compatible but whose total bounding rectangle is not all ones. If one exists, pairwise coloring alone cannot encode cover; otherwise attempt a general lemma and assess whether arbitrary graph coloring can be embedded geometrically. This is a new structural proof strategy, not a parameter rerun of round 001.

Prior evidence: exact target rectangles require consecutive rows and columns; round 001 found no reusable published gadget. Board experience entries absent.

## Evidence and diagnosis

The candidate lemma holds: for any finite set of grid cells, the union of its pairwise bounding boxes is the bounding box of the whole set. For a cell `z=(r,c)` in the full box, take points `p,q` with minimum and maximum row. If their columns bracket `c`, their pair box contains `z`. Otherwise their columns lie on the same side of `c`; take a point `e` on the other side (it exists because `c` is in the full column range). Pair `e` with `p` or `q` according to which has row on the opposite side of `r`. That pair box contains `z`.

Consequently, for a binary picture, make a graph with one vertex per one-cell and join two vertices if their pairwise bounding rectangle contains a zero. Any legal rectangle cover of size `K` colors this graph with at most `K` colors by assigning each cell one of its covering rectangles. Conversely, the bounding rectangle of each color class contains only ones by the lemma, so color classes yield legal rectangles. This is an exact equivalence, including empty pictures. It does not by itself embed an arbitrary graph or solve the fixed 3SAT reduction.

`pairwise_probe.py` found no counterexample among all 502 nontrivial subsets of a 3×3 grid and 14,876 subsets of size 2–6 in a 4×4 grid. `color_check.py` independently compared graph coloring with the prepared rectangle-cover oracle on all 512 binary 3×3 matrices at budgets 0–3 (2,048 pairs), with agreement. These finite checks support the implementation of the lemma but do not prove graph realizability. Actual injected source/target/recovery counts: 0/0/0. Remaining obligation: construct a polynomial picture whose conflict-colorings encode the given formula, or use another gadget route.

Experience extraction: [pairwise rectangle-hull lemma](../../../../research/experience/pairwise-rectangle-hull.md), a general structural fact useful for later attempts.

## Next action

Try an explicit graph-to-picture embedding in round 003 and test whether filler cells create uncontrolled colors.
