# Rectangle-covering aliases can change the problem

## Claim and applicability

Tags: rectangle cover, binary matrix, literature, consecutive rows, reduction direction. Papers using “rectangle covering” can mean either contiguous submatrices or Cartesian products of arbitrary row and column subsets. For an `n×n` matrix, the former has at most `O(n^4)` candidate rectangles, while the latter has up to `2^(2n)`; the count provides a quick diagnostic. A proof that reduces *from* rectilinear picture compression establishes hardness of another problem, not a construction into RPC.

## Evidence and status

[Round 013](../../campaigns/three-sat-rectilinear-picture-compression/rounds/013/round.md) compares accessible matrix and compression papers. The combinatorial rectangle-count distinction follows directly from the two definitions; the Berkeley-source mismatch is inferred from its stated count. This is a literature-screening rule, not a hardness theorem.

## Consequence for search

Before transferring a gadget or theorem, check contiguity, all-one containment, overlap semantics, input representation, budget and the direction of witness extraction.

## Use history

Created 2026-09-25 from round 013. Intended board promotion is pending; the board was not edited.
