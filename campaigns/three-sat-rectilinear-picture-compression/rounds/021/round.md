# Round 021 — coordinate rank compression

## Plan

The previous polygon route treated polynomial geometric area as necessary for a polynomial explicit matrix. Test a different proof strategy: map every distinct horizontal and vertical polygon coordinate to its sorted rank. A separable increasing homeomorphism maps every axis-aligned rectangle to an axis-aligned rectangle, so it should preserve all rectangle covers while producing only quadratically many cells in the number of coordinates.

First discriminating check: prove witness preservation in both directions, including arbitrary rectangle boundaries not at polygon coordinates, and run an explicit huge-gap polygon through rank compression and target cover recovery. This directly reassesses the counterexample in round 004 and the experience entry `rasterization-area-bound.md`. The shared board remains read-only.

## Evidence and diagnosis

The [rank-compression proof](../../work/rank-compression.md) establishes the proposed equivalence for arbitrary regular closed orthogonal regions, including holes and disconnected components. Separable increasing maps preserve every rectangle; snapping after compression and lifting by coordinate lookup preserve cover count. With n polygon vertices the matrix has at most (n−1)² entries, independent of coordinate magnitude. This corrects the earlier assertion that polynomial geometric area is required.

The test was written first and initially failed because the compression implementation did not exist. After implementation, `check_rank_grid.py` checked all 512 binary 3×3 pictures with coordinates stretched to gaps of up to 160 bits, comparing minimum counts with the uncompressed 3×3 oracle and validating up to two lifted covers per picture directly against the original geometric cells. A 2^1000×1 rectangle compresses to a single cell. All completed successfully; `output.txt` retains the result. No 3SAT F/G exists yet; source/recovery checks remain 0/0.

Experience extraction: corrected [rasterization area bound](../../../../research/experience/rasterization-area-bound.md), retaining the earlier mistake explicitly. The published beam construction now needs a finite coordinate/order specification, not a separate bound on geometric area.

## Next action

If rank compression succeeds, remove the unnecessary area obligation and concentrate on the finite combinatorial layout of the published gadgets.
