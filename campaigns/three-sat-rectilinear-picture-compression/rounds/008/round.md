# Round 008 — thick exclusive-port core

## Plan

Gap: thin pictures are polynomial by round 007. Seek a core containing an all-one 2×2 block that supports a genuine Boolean choice at two outside ports. Proposed interface: a variable core has base cover cost `k`; either exterior port can be covered at cost `k` by extending a chosen rectangle, but covering both costs at least `k+1`. A wire would join opposite ports of neighboring cores, and a clause cell would be reachable from one true literal port. Composition still needs proof of phase propagation, crossing, isolation, global budget and decoding from every witness.

First discriminating check: exhaust 3×3 cores containing a 2×2 all-one block, put each of two port cells at distinct positions along the four sides of a surrounding 5×5 grid, and use the independent exact target oracle to test `opt(core)=opt(core+P)=opt(core+Q)<opt(core+P+Q)`. A positive local core needs a composition test; a negative result excludes only this bounded one-cell-port family.

Prior evidence: rounds 005–006 produced thin ambiguous tiles; round 007 proves the entire thin class tractable. The thin-picture experience entry applies because the new search must leave that class.

## Evidence and diagnosis

`port_probe.py` exhausted all 95 binary 3×3 cores containing a 2×2 all-one block. The oracle found 380 singly free exterior ports and tested 912 pairs of them; 224 pairs were exclusive at the core's minimum budget. No exclusive pair used opposite sides. The first core (zero-based 3×3 rows `000/011/111`) has budget 2 in a 5×5 frame, with free ports `(4,1)` and `(3,0)` individually, but both require budget 3. The first execution incorrectly searched only budgets 1–3 and raised `StopIteration` on a thicker core needing more than three rectangles; this was an experiment-code bound error, not a target answer. The bound was repaired to the number of one-cells and the full finite family rerun.

Composition is not automatic. For that first core, a same-orientation two-core join at one port collapsed to cover size 2 instead of the expected 4; each outer port then cost an extra rectangle. Seven nondegenerate rotations/reflections of that particular join had no exclusive outer-port pair. The local port predicate alone does not prove a wire.

`all_compositions.py` then checked all 224 exclusive core/port pairs under two-copy dihedral joins: 2,624 nondegenerate joins, 432 with exclusive outer ports, of which 304 had disjoint cores. It tested 3,968 disjoint third-core extensions of additive two-core joins; 896 kept an additive exact budget and exclusive outer ports. These are counts of geometries; exact Z3 calls were not separately instrumented. All target statuses came from the prepared exact rectangle oracle; no candidate F/G was involved.

One explicit core with ports `(4,1)` and `(2,4)` forms a thick diagonal wire. `repeat_probe.py` reconstructs a three-core additive join, checks 20 four-core orientations, and finds four additive exclusive joins. Repeating the first such orientation gives four- and five-core pictures of sizes 10×10 and 13×12. In both, the oracle found minimum budget `2t`, each endpoint individually coverable at `2t`, and the two endpoints together infeasible at `2t`. An independent incompatibility-graph optimization found antirectangles of sizes 8 and 10 in the base pictures, and 9 and 11 after adding both endpoints; these certify the corresponding lower bounds. Finite cases are not a general proof. Exact geometry and commands remain in the scripts, with no random choices.

No full 3SAT reduction exists yet. Open obligations: prove the port property for every wire length; create fanout for repeated variable occurrences; place three literal wires at a clause cell without cross-gadget rectangles; specify a polynomial layout and exact budget; and recover an assignment from every legal target cover, including `NO-SOLUTION`. Actual injected source/recovery instances: 0/0. Literature novelty and significance of any eventual theorem are unassessed. Experience extraction: [thick exclusive-port candidate](../../../../research/experience/thick-exclusive-ports.md).

## Next action

Investigate free side ports as possible occurrence taps and a clause interface in a new construction round; preserve this finite wire as a partial candidate, not a complete F/G rule.
