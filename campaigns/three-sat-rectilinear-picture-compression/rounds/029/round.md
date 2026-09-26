# Round 029 — Existing executable reduction implementations

## Plan

Search for a primary public implementation or mechanically checked proof of the exact 3SAT-to-binary-picture reduction. Finite scope: repositories and code indexed under RectilinearPictureCompression and the named Masek reduction, including the source-model repository linked in search results. This differs from the paper-retrieval attempts: an executable construction could settle missing coordinates. First check: locate actual forward/recovery code rather than a target solver or a hardness citation. No cloning or writing outside this campaign, no issue comments or publication. Existing experience provides test obligations but no implementation.

## Evidence and diagnosis

The public source-model repository was inspected at commit `309ac65e193aa6744362ee2f3d4c0338d95c0819` using GitHub's recursive tree API (not truncated). The only matching production files are `src/models/misc/rectilinear_picture_compression.rs` and `src/rules/rectilinearpicturecompression_ilp.rs`, with corresponding unit tests. Raw source confirms a target model and a reduction FROM picture compression TO ILP; neither supplies the required incoming 3SAT reduction. Primary code: https://github.com/CodingThrust/problem-reductions/tree/309ac65e193aa6744362ee2f3d4c0338d95c0819 . The exact-name code searches found the same model documentation and problem catalog, not another implementation. Search date 2026-09-25; limited to accessible indexed repositories and this complete tree, not a claim about all code in existence.

No source injections, target solver calls or recovery calls. Experience extraction: none; the direction/solver distinction is already recorded in earlier literature evidence.

## Next action

Audit and execute any located rule against the prepared corpus; otherwise return to construction.
