# Vertex cover beams give a decoder, but need grid geometry

## Claim and applicability

Tags: rectangle cover, rectilinear polygon, Vertex Cover, beam gadget, rasterization. Berman–DasGupta's primary proof reduces bounded-degree Vertex Cover to interior rectangle cover of a rectilinear polygon. Its normalization lemma handles arbitrary covers before decoding a vertex cover, and its component counts give a baseline plus one rectangle per selected vertex. This supplies a potential recovery pattern for matrix RPC after a valid polynomial-size digitization.

## Evidence and status

[Round 014](../../campaigns/three-sat-rectilinear-picture-compression/rounds/014/round.md) records the full preprint, theorem and lemma locations, offset formula and missing coordinate/area obligations. The figures are schematic. No executable polygon or matrix constructor, raster-area proof, or independent review exists.

## Consequence for search

Do not infer an explicit 3SAT-to-matrix reduction from an L-reduction statement alone. The polygon must be laid out on a polynomial-area integer grid while retaining every noninteraction claimed by the gadgets; then the arbitrary-cover normalization and source decoding must be checked after rasterization.

## Use history

Created 2026-09-25 from round 014. Intended board promotion is pending; the board was not edited.
