# Round 040 — Full 3SAT composition and cover charging decoder

## Plan

Compose the certified constant-degree sources, monotone routing, and separated terminals with a 3SAT-to-degree-three Vertex Cover map. This final attempt constructs both F and G. First check: source-to-graph preprocessing and recovery against all 120 prepared cases, then one complete graph-to-picture instance with all rectangle ownership conditions and arbitrary-cover charging. Implement the whole source-to-target command once this composition works. Measure dimensions before scaling the explicit matrix; polynomial size alone does not establish feasibility of the prepared end-to-end run.

Reuse the source, terminal, cut and routing lemmas, preserving their exact assumptions. No independent review is eligible until the full rule, general proof and prepared checks pass. All verification, proof repairs and writing remain in this attempt; no discovery round remains after it.

## Evidence and diagnosis

The source-to-degree-three graph map passes all 120 prepared cases with an
independent Kissat oracle, and 212 graph covers decode to valid assignments
(`graph_kissat_output.txt`). Earlier default-Z3 and native-cardinality runs were
interrupted or timed out, not interpreted as UNSAT (`graph_output.txt`,
`graph_native_output.txt`). A path-ordering error imported an old probe called
`check`; its output is retained in `graph_import_failure.txt`. The corrected
check imports the prepared validator first. Extracting the already-used unary
cardinality encoding into a reusable SAT function left all 511 small-picture
minimum/rejecting-budget comparisons with Z3 passing (`backend_regression.txt`).

The full graph-to-picture compiler and charging decoder are in `picture.py`.
Three actual matrix instances passed independent covering checks: one edge at
graph budget one is YES, the same at zero is NO, and a two-edge path at one is
YES. Both YES covers decode. Every inter-module maximal rectangle in these
pictures is an intended interface (`picture_output.txt`, repeated after the
backend refactor in `picture_final_output.txt`). This checks two positive
recoveries and one negative instance, not arbitrary source composition.

The first size measurements showed 134,247,719,259 explicit cells for prepared
case 70 (16 clauses). A bounded graph-vertex reordering, preserving the graph
isomorphism, reduces it to 15,514,487,415 cells, still beyond practical prepared
verification (`dimensions_initial.txt`, `dimensions_reordered.txt`). No additional
layout strategy was opened. The sparse layout has a polynomial O(m^4) dense-size
bound, with prohibitive constants and degree on these cases.

The integrated fresh-process F/G entry point is now `../../work/algorithm.py`.
A boundary test was written and failed before that file existed
(`command_before.txt`); it passes for two empty-clause sources after implementation
(`command_after.txt`, test now at `../../work/verify.py`). The unchanged prepared
candidate checker was invoked, then its process group terminated at a 30-second
execution limit without a full-suite verdict (`prepared_candidate_output.txt`).
No nonempty source completed the full F/target-oracle/G loop. This is an execution
failure, not a mathematical counterexample, NO-SOLUTION answer, or exhausted
search family. The 120-case Prepare self-test and 14 source/24 routing local
certificates were rechecked successfully; retained `*_regression.txt` logs give
the exact scope.

The [candidate argument](../../work/proof.md) proves the graph step and records
the conditional cover charging argument, size bound and remaining general
attachment proof. It also flags that binary n with an explicit n-bit assignment
is not covered by this implementation's polynomial-in-(n+m) source cost. The
contract and prepared cases were not weakened. Full verification, resolution of
the bit-length obligation, independent review and paper remain outstanding.

Experience extraction: update [beam-cut composition](../../../../research/experience/beam-cut-composition.md)
with small complete graph evidence and the practical rank-grid limit. Existing
rank-compression, source and terminal findings were reused. No claim of novelty
or of nonexistence of the known hardness construction follows.

## Next action

Close as `stopped_without_discovery`: 40 numbered attempts, no rounds remaining,
and an unverified integrated candidate. A further allocation should first address
the output-size bottleneck and all attachment cases, keeping exact cover and
source-output semantics fixed. No board changes or publication were made.
