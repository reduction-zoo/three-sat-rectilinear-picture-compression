# Vertex cover beams give a decoder, but need grid geometry

## Claim and applicability

Tags: rectangle cover, rectilinear polygon, Vertex Cover, beam gadget, rasterization. Berman–DasGupta's primary proof reduces bounded-degree Vertex Cover to interior rectangle cover of a rectilinear polygon. Its normalization lemma handles arbitrary covers before decoding a vertex cover, and its component counts give a baseline plus one rectangle per selected vertex. This supplies a potential recovery pattern for matrix RPC after a valid polynomial-size digitization.

## Evidence and status

[Round 014](../../campaigns/three-sat-rectilinear-picture-compression/rounds/014/round.md) records the full preprint, theorem and lemma locations, offset formula and missing coordinate/area obligations. The figures are schematic. No executable polygon or matrix constructor, raster-area proof, or independent review exists.

## Consequence for search

Do not infer an explicit 3SAT-to-matrix reduction from an L-reduction statement alone. The polygon must be laid out on a polynomial-area integer grid while retaining every noninteraction claimed by the gadgets; then the arbitrary-cover normalization and source decoding must be checked after rasterization.

## Use history

Created 2026-09-25 from round 014. Intended board promotion is pending; the board was not edited.

Round 021 removed the area objection by rank compression. Round 022 digitized the six-rectangle beam and a degree-1/2/3 vertex family, with baseline 8d+7 and a one-rectangle penalty for any nonempty output subset. The paper's component description says 8d+7 whereas its later count says 7d+7; the previous extracted offset is therefore not trustworthy without recomputation. A regularized switch had a valid finite local implication table but failed when stacked: a previous background rectangle covered the next stage's staircase corner. See [round 022](../../campaigns/three-sat-rectilinear-picture-compression/rounds/022/round.md) and its independently validated leaking cover. This is a failure of the reconstructed geometry, not a refutation of the published hardness result.

## Paired translation, 2026-09-25

[Round 027](../../campaigns/three-sat-rectilinear-picture-compression/rounds/027/round.md) gives explicit opposed beam cores with preserved structural zeros. Two single-pair spans and chains through four pairs have the desired implication cost table. This is a finite isolated-chain result; it does not establish crossings, global independent backgrounds, or a full reduction.

## Perpendicular crossing, 2026-09-25

[Round 031](../../campaigns/three-sat-rectilinear-picture-compression/rounds/031/round.md) crosses the two shared rectangles of orthogonal translator pairs with disjoint cores. All 16 local states and 64 states of two joined crossings have exact additive unsupported-output penalties. Arbitrary network composition and routing remain unproved.

## Vertical swap, 2026-09-25

[Round 033](../../campaigns/three-sat-rectilinear-picture-compression/rounds/033/round.md) combines two turns with a perpendicular crossing. After separating the cores, its 16-state table is exact and two vertical channels exchange order. Ports are staggered in height; connecting them without corrupting costs remains open.
