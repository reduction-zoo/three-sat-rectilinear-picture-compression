# A finite exact-cost two-input OR checker

This is an isolated constant-size target gadget, not a source reduction. Coordinates are integer cell positions; translate all cells by `(2,3)` to obtain a nonnegative matrix.

Let `C={(1,3),(2,1),(2,2),(2,3),(3,2),(3,3)}` and define two disjoint copies

```
A={(r,c-3):(r,c)∈C},     B={(c-3,r-4):(r,c)∈C}.
```

The shared checker cell is `z=(0,0)`. For input 1, add either active port `P1=(4,-1)` or inactive port `Q1=(1,1)`. For input 2, add either `P2=(-1,0)` or `Q2=(1,-3)`. The target picture for an input pair is `A∪B∪{z, chosen port 1, chosen port 2}`.

**Exact local truth table:** the minimum rectangle count is 7 for `(inactive,inactive)` and 6 for each of the other three input pairs.

For lower bounds, the following are pairwise incompatible sets of one-cells in the corresponding pictures, in input order `00,10,01,11`:

```
00: [(-2,-2),(-1,-1),(0,0),(1,-3),(1,1),(2,-2),(3,-1)]
10: [(-2,-2),(-1,-1),(1,-3),(1,0),(2,-2),(3,-1)]
01: [(-2,-2),(-1,0),(0,-3),(1,1),(2,-2),(3,-1)]
11: [(-2,-2),(-1,-1),(0,-3),(1,0),(2,-2),(4,-1)]
```

For upper bounds, one cover for each row follows. Rectangles are `(first row,last row,first column,last column)` after translation by `(2,3)`:

```
00: [(0,0,1,1),(1,2,1,2),(2,3,0,0),(2,5,3,3),(3,3,3,4),(4,4,1,1),(4,5,2,2)]
10: [(0,1,1,1),(1,2,1,2),(2,3,0,0),(2,5,3,3),(4,4,1,2),(4,6,2,2)]
01: [(0,2,1,1),(1,1,1,3),(2,2,0,3),(3,3,3,4),(4,4,1,2),(4,5,2,3)]
11: [(0,2,1,1),(1,2,2,2),(1,5,3,3),(2,2,0,0),(4,4,1,2),(5,6,2,2)]
```

Each lower set is checked directly by bounding boxes and each upper cover by the independent target witness validator in [round 018's reproducer](../rounds/018/edge_example.py). The exact oracle also checked two alternative valid covers for each positive row. The broader local search found 24 exact-cost placements among 120 geometries with clear, distinct ports.

This truth table compares four *different* pictures with chosen port cells. A source-to-target reduction must build one fixed picture whose covers choose vertex states, maintain these local costs after many checkers are connected, and recover a vertex cover or 3SAT assignment from every legal cover. None of those composition properties follows from this isolated table.
