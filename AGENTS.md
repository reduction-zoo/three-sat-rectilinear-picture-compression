# Research instructions

Read the [fixed question](campaigns/three-sat-rectilinear-picture-compression/question.md), [prior state](campaigns/three-sat-rectilinear-picture-compression/state.md) and [preparation notes](campaigns/three-sat-rectilinear-picture-compression/work/preparation.md). The fixed [test corpus](campaigns/three-sat-rectilinear-picture-compression/work/cases.json) and [verifier](campaigns/three-sat-rectilinear-picture-compression/work/check.py) are the starting evidence; the preparation notes state their coverage and any pending checks.

Run `uv sync --locked`, then `uv run --locked python campaigns/three-sat-rectilinear-picture-compression/work/check.py --self-test` before relying on that evidence. Follow the current user's AutoResearch pipeline. Preserve prior evidence, commit new work incrementally and make only evidence-backed claims.
