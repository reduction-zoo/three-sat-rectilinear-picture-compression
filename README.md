# 3-SAT → Rectilinear picture compression

The campaign resumed with 20 additional rounds (021–040) after the first 20 rounds ended without a complete reduction. No executable source-to-target map F, every-output recovery map G, or general 3-SAT correctness proof was found. The strongest partial results are an [exact endpoint-budget lemma for one repeated thick wire](campaigns/three-sat-rectilinear-picture-compression/work/wire-lemma.md), an [exact dynamic program for fixed-width diagonal-band pictures](campaigns/three-sat-rectilinear-picture-compression/work/band-lemma.md), and [finite two-input edge gadgets](campaigns/three-sat-rectilinear-picture-compression/work/edge-gadget.md). None establishes the fixed global picture, routing, clause behavior, or decoder required by the [question](campaigns/three-sat-rectilinear-picture-compression/question.md). The partial proofs have not received independent review.

[State and attempt records](campaigns/three-sat-rectilinear-picture-compression/state.md) · [Prepared corpus and oracle evidence](campaigns/three-sat-rectilinear-picture-compression/work/preparation.md) · [Reusable findings](research/experience/README.md)

The fixed Prepare corpus has 120 distinct 3-CNF cases (100 seeded, 20 edge), with source labels checked by Z3 and exhaustive search. The target oracle independently solves small exact rectangle-cover instances and validates returned covers. There were **zero** candidate F/G source-to-target or recovery checks because no complete candidate existed. Finite gadget results are bounded to the families stated in their round records.

Reproduce the main checks from the repository root:

```sh
uv sync --locked
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/work/check.py --self-test
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/015/antirectangle_induction_probe.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/017/band_dp.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/018/edge_example.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/019/shared_core_probe.py
uv run --locked python campaigns/three-sat-rectilinear-picture-compression/rounds/020/degree_three_probe.py
```

Board source commit: 834a23a845589826383af2fdf2f1425e02e88864.
