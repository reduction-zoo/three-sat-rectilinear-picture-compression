# Verification scope at round 040 closeout

The integrated `algorithm.py` is an **unverified candidate**. Its proof status is
documented in [proof.md](proof.md). No independent review or paper is claimed.

| Layer | Actual evidence |
|---|---|
| Prepare | 120 source cases (100 fixed seeds, 20 edge cases); independent source labels and small target oracle self-tests pass |
| Source to graph | All 120 labels agree with Kissat; 212 graph covers decode and pass direct formula validation |
| Local certificates | 14 source states and 24 routing states pass direct upper/lower certificate checks without a solver |
| SAT backend | All 511 nonempty 3×3 pictures agree with the independently implemented Z3 oracle on minima and smaller rejecting budgets |
| Graph to picture | Three instances: single edge at budgets 1 and 0, and two-edge path at budget 1; two actual picture covers decode, one is UNSAT; all crossing maximal rectangles have designated ownership |
| Source command F/G | Two empty-clause sources (n=0 and n=3), independently known empty target cover, fresh-process recovery; no nonempty formula has completed the full loop |
| Full Prepare candidate run | Invoked unchanged `check.py --candidate algorithm.py`; terminated after 30 seconds as an execution/resource failure, without a full-suite verdict |
| Size measurement | Five retained source cases; a 16-clause target has 15,514,487,415 matrix entries after the bounded ordering improvement |

Raw evidence is under `rounds/040/`. Previous Z3 graph runs were interrupted or
timed out; they were not counted as NO-SOLUTION. The replacement backend run
also initially imported an old probe named `check` because of path ordering;
that failing log is retained, and the corrected run checks the intended prepared
validator. The command test failed before `algorithm.py` existed; it now lives
at `verify.py` and passes. No expected source labels were changed.

Reproduce from the repository root, using the locked uv environment and installed
Kissat 4.0.4:

```sh
uv sync --locked
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/work/check.py --self-test
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/work/verify.py --candidate campaigns/three-sat-rectilinear-picture-compression/work/algorithm.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/040/check_graph.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/040/check_picture.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/025/check_kissat.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/038/verify_certificates.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/039/verify_certificates.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/040/measure.py
```

The unchanged full gate is `work/check.py --candidate work/algorithm.py`, with
both paths prefixed by the campaign directory. It is not expected to finish at
current target sizes. The run in `prepared_candidate_output.txt` wrapped that
command in a subprocess group and terminated the group at 30 seconds. This
resource ceiling is not an exhaustive search bound or a mathematical verdict.
Neither arbitrary nonmaximal covers nor NO-SOLUTION on a nonempty source have
been exercised through the full F/G command. Empty-clause command success and
the separate graph/picture tests must not be added together as full coverage.
