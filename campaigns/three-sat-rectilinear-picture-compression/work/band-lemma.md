# Exact covering in a diagonal band

Fix positive integers `a,b` and a nonnegative width `w`. Suppose every one-cell `(r,c)` of a binary matrix satisfies `ℓ ≤ ar+bc ≤ ℓ+w`. Set `h=⌊w/a⌋+1` and `q=⌊w/b⌋+1`.

**Claim.** The minimum all-one rectangle cover can be found in `2^{O(hq)}·poly(mn,h,q)` time for an `m×n` matrix. In particular, the problem is polynomial for fixed `a,b,w`.

For a fixed row, at most `q` columns lie in the band. If an all-one rectangle spans rows `r0..r1` and columns `c0..c1`, both opposite corners are one-cells, so `a(r1-r0)+b(c1-c0)≤w`. Thus the rectangle spans at most `h` rows and at most `q` columns. At each top row there are at most `h·q(q+1)/2` possible rectangles, before rejecting those containing zeros.

Scan rows from top to bottom. Before row `r`, record which one-cells in rows `r..r+h-1` are already covered by rectangles selected at earlier top rows. This is a mask of at most `hq` cells. Choose any subset of valid rectangles whose top row is `r`; require that the union with the old mask covers every one-cell in row `r`. Charge one per chosen rectangle, clear row `r` from the mask, and continue. For each resulting mask retain the least cost. Any rectangle selected by a cover has one unique top row, so processing its rectangles at that row follows a DP path of the same cost. Conversely, every DP path selects only all-one rectangles and covers each row when it is cleared. This proves exactness. There are at most `2^{hq}` states and at most `2^{hq}` distinct subset-union masks at each row; computing choices and transitions takes the claimed fixed-parameter time.

The [implementation and independent checks](../rounds/017/round.md) compare this DP with the prepared exact target oracle on a full thick band picture and 20 seeded sparse/thick variants. The explicit wire in [wire-lemma.md](wire-lemma.md) satisfies `7≤2r+3c≤20` for every core and join cell, and its two endpoints satisfy `7≤2r+3c≤21`. Thus every single wire in that family lies in a fixed-width band, regardless of its length. The theorem does not cover arbitrary arrangements of many wires, crossings or clause gadgets whose band width grows.
