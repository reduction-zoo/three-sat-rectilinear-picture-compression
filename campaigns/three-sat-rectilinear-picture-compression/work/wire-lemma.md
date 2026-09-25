# A repeated thick wire has an exact endpoint budget

This is a partial result for the fixed target. It does not construct a 3SAT instance or decode a source assignment.

Let `C={(2,2),(2,3),(3,1),(3,2),(3,3)}`, `p=(4,1)`, `q=(2,4)`, and `T(r,c)=(c,r)`. Write `X+(a,b)` for translating every cell of `X`. Define

```
W3 = C ∪ (T(C)+(3,-3)) ∪ (C+(-2,3)) ∪ {p,q},
R = (0,7),
L_t = (3t-2,-2t+5),
W_t = W3 ∪ ⋃_{k=4}^t [(T(C)+(3k-6,-2k+3)) ∪ {L_{k-1}}]  (t≥4).
```

The three base copies and each later copy are disjoint. The singleton cells are their shared ports. Matrix translation to nonnegative coordinates preserves all cover counts.

**Claim.** For every integer `t≥3`, `W_t`, `W_t∪{L_t}` and `W_t∪{R}` each have minimum all-one rectangle cover size `2t`; `W_t∪{L_t,R}` has minimum size `2t+1`.

**Upper bounds.** The core plus either one port has a two-rectangle cover. For `C∪{p}`, use row interval `2..3`, column interval `2..3`, and row interval `3..4`, column `1`. For `C∪{q}`, use row `2`, columns `2..4`, and row `3`, columns `1..3`. Apply the same covers after each copy's translation or transposition. The cores and shared ports form a path: from `R` through the translated core, `C`, the transposed core, then the repeated transposed cores to `L_t`. To include one endpoint, direct every core's local two-rectangle cover toward that endpoint. Every join is then covered by one of its adjacent cores, giving `2t` rectangles. For `W_t` without endpoints, direct the rightmost core toward its join with `C`, direct `C` toward that same join, and direct every remaining core toward `R`; this covers all joins without including either endpoint. Adding the other endpoint as a singleton to a one-end cover gives `2t+1` rectangles.

**Lower bound without both endpoints.** A set of cells whose pairwise bounding boxes are not all one needs one rectangle per cell. Start with

```
B3 = [(0,6),(1,4),(2,2),(3,1),(4,0),(5,-1)].
```

For each `k=4..t`, append `(3k-5,-2k+6)` and `(3k-4,-2k+5)` to obtain `B_t` of size `2t`. All points lie in `W_t`, with rows strictly increasing and columns strictly decreasing. For such a chain, it suffices to show consecutive points incompatible: the bounding box of any nonconsecutive pair contains that of a consecutive pair. For the fixed five adjacent pairs in `B3`, missing cells in their bounding boxes are `(0,4),(1,2),(2,1),(3,0),(4,-1)`. The transition to `k=4` has missing cell `(5,-2)`. For each `k≥4`, the two new points have missing cell `(3k-5,-2k+5)` in their box; between the second point of copy `k` and the first point of copy `k+1`, use `(3k-4,-2k+4)`. None of these cells belongs to `W_t`.

**Lower bound with both endpoints.** Start with

```
D3 = [(0,7),(1,5),(2,4),(3,2),(4,1),(6,0),(7,-1)].
```

For each `k=4..t`, append `(3k-4,-2k+6)` and `L_k`. This gives `D_t` of size `2t+1` inside `W_t∪{R,L_t}`, again with strictly increasing rows and decreasing columns. The six fixed consecutive pairs have missing cells `(1,7),(2,5),(3,4),(4,2),(5,1),(7,0)`. Between `L_{k-1}` and the next appended point, use the missing cell `(3k-4,-2k+7)`. Between that point and `L_k`, use `(3k-2,-2k+6)`. These remain zero even when later cores are added.

For completeness, the repeated copy's occupied tail rows are explicit. Set `a_k=-2k+6`. In `W_t`, row `3k-5` has exactly columns `a_k,a_k+1`; rows `3k-4` and `3k-3` have exactly `a_k-1,a_k`, for `4≤k≤t`. The final added endpoint `L_t` is one row below the last block. These row intervals directly verify every repeating missing-cell formula above. The fixed missing cells are outside the base `W3`; the only later row they meet is row 7, where the repeated block occupies columns `-2,-1`, so `(7,0)` stays zero.

The generator and direct pairwise-certificate checks through `t=20` are in [round 015](../rounds/015/round.md). The proof above uses the explicit row formula and is independent of that finite bound. It does not establish occurrence taps, clause composition, or recovery of a 3SAT assignment from arbitrary target covers.
