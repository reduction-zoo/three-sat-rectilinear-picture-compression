# Round 005 — two-state variable tile

## Plan

Gap: the polygon route does not yield executable integer gadgets. Seek a small binary matrix with exactly two structurally distinct minimum covers, to act as a Boolean variable tile. Proposed full interface: repeat such tiles along variable wires, couple neighboring tiles so all choose the same phase, and attach each literal port to a clause cell that a chosen phase can cover without an extra rectangle. Clause cells would be placed so any of three true ports suffices. Composition assumptions still unresolved: phase coupling, routing/crossings, unintended rectangles between gadgets and an exact global budget.

First discriminating check: exhaust connected 3×3 and 3×4 matrices, enumerate maximal all-one rectangles and every minimum maximal-rectangle cover, and look for a tile with exactly two covers whose differing rectangles can extend to distinct boundary ports. A negative bounded result excludes only that tile domain; a positive tile must next survive a local composition test before larger searches.

Prior evidence: round 003 shows arbitrary filler can consume budget; round 004's beam route shows two-state signal gadgets are at least a viable published design pattern, but gives no matrix coordinates.

## Evidence and diagnosis

`tile_probe.py` exhausted 512 3×3 and 4,096 3×4 pictures. Among connected pictures spanning all rows and columns, 111 and 649 respectively, it found 4 and 44 with exactly two minimum covers **after every rectangle is enlarged to an inclusion-maximal one**. The 3×3 examples are rotations/reflections of the five-cell staircase

```text
001
011
110
```

Its maximal rectangles are the first end pair, last end pair, and one of two middle pairs (horizontal or vertical). The minimum is three: the prepared independent target oracle proves `K=2` infeasible and returns legal `K=3` covers. Thus a local binary orientation exists in the maximalized representation.

Crucial limitation: the actual target accepts *all* legal rectangles, including a singleton center cell. Two end-pair rectangles plus that singleton also use three rectangles. Therefore the tile alone has a third uncommitted witness form. It can be enlarged to either middle pair without cost, but an arbitrary target cover does not explicitly encode a Boolean state until surrounding port obligations force one. A decoder cannot simply read the raw middle orientation.

Same-strategy composition check: `composition_probe.py` joined two copies at an endpoint, producing a 5×5 nine-cell staircase. The independent target oracle established minimum cover size 5 (`K=4` UNSAT, `K=5` SAT). Exhaustive enumeration of the eight maximal rectangles found **four** minimum maximal covers, printed by the script, corresponding to a freely moving phase transition along the path. In particular, sharing the endpoint does not enforce a consistent Boolean choice in the two copies. Expected: only two global phases. Actual: four covers. The unused orientations are not eliminated by a tight rectangle budget. This invalidates the proposed propagation interface, though a different coupling gadget might work.

No full F/G or composition proof was obtained. Actual target instances solved: four budget checks across the local and joined tile; source/recovery instances: 0/0. The bounded search excludes the two tested shapes and this endpoint-sharing composition, not other geometries or joins. Remaining obligations: a tile with robust ports and a coupling that has exactly the intended global states.

Experience extraction: [staircase endpoint coupling counterexample](../../../../research/experience/staircase-coupling.md).

## Next action

Move to a distinct mechanism; do not scale this endpoint-sharing staircase as a Boolean wire without a new coupling rule.
