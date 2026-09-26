# 3-SAT → Rectilinear picture compression

**Stopped after 40 rounds with an unverified integrated candidate.** The second
20-round allocation produced executable construction/recovery code, certified
local gadgets and a monotone routing compiler. It did not complete the general
attachment proof or nonempty-source end-to-end verification. This reconstructs
a known hardness result; the campaign's failures do not dispute that result.

- [Fixed question](campaigns/three-sat-rectilinear-picture-compression/question.md)
- [Candidate F/G](campaigns/three-sat-rectilinear-picture-compression/work/algorithm.py)
- [Argument and remaining obligations](campaigns/three-sat-rectilinear-picture-compression/work/proof.md)
- [Verification scope and reproduction](campaigns/three-sat-rectilinear-picture-compression/work/verification.md)
- [State and all 40 attempt records](campaigns/three-sat-rectilinear-picture-compression/state.md)
- [Prepare corpus](campaigns/three-sat-rectilinear-picture-compression/work/preparation.md)

## Evidence and limits

Prepare has 120 fixed source cases: 100 seeded random and 20 edge cases. All 120
pass the independent source-to-degree-three-graph checks; 212 graph covers decode
to satisfying assignments. Fourteen source states and 24 routing states have
directly checked upper/lower certificates. Three small graph-to-picture instances
pass, including one UNSAT case and two cover recoveries.

The actual F/G command passes two empty-clause source cases. **No nonempty source
has completed the full target-solver/recovery loop.** The unchanged prepared
candidate run hit its execution limit. A measured 16-clause layout has
15,514,487,415 explicit matrix entries after a bounded vertex-order improvement.
The source contract's binary unused-variable count also needs a bit-length audit.
No independent review, manuscript or formal certification is claimed. Novelty is
unestablished; the contribution here is a partial reconstruction and its evidence.

## Reproduce

From this repository, with uv and Kissat 4.0.4 installed:

```sh
uv sync --locked
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/work/check.py --self-test
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/work/verify.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/040/check_graph.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/040/check_picture.py
```

Additional certificate, backend and dimension commands are in the verification
record. The [round 040 record](campaigns/three-sat-rectilinear-picture-compression/rounds/040/round.md)
preserves failed executions and the exact stop reason. Further discovery requires
a new allocation; practical matrix size and general attachment correctness are
the next priorities.

Fourteen [local experience entries](research/experience/README.md) await separately
authorized board promotion. Nothing was published and the board was not edited.
Board source commit: `834a23a845589826383af2fdf2f1425e02e88864`.
