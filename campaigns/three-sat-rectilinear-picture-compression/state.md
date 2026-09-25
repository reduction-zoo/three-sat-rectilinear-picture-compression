# Campaign state

Budget: 20 rounds. Used: 18 (round 018 open).
Board source: 834a23a845589826383af2fdf2f1425e02e88864.

Capability probe (2026-09-25): Python 3.12.14 at `/Users/xiweipan/.local/bin/python3`; uv 0.12.17 at `/Users/xiweipan/.local/bin/uv`; Z3 executable 5.1.0 at `/opt/homebrew/bin/z3`; Kissat 4.0.4 at `/opt/homebrew/bin/kissat`; Typst 0.15.1 at `/opt/homebrew/bin/typst`; Lean 4.34.1 at `/opt/homebrew/bin/lean`; Lake 5.0.0 at `/opt/homebrew/bin/lake`. Python Z3 binding selected for Prepare; locked version recorded in `uv.lock`. Mathlib status: not probed because formalization is not requested. Writing skill is available in the session catalogue. No capability blocker for Prepare.
Prepare: 120 fixed source cases, independent Z3 and exhaustive source checks, exact target rectangle-cover oracle and direct validators; see [preparation](work/preparation.md). Self-test passed 2026-09-25. No construction claim follows from Prepare.
Current claim: a general exact endpoint-budget lemma for one repeated thick wire; a fixed-width diagonal-band exact DP applies to every length of that wire. A finite two-input exact-cost OR checker exists, alongside a four-core alternate wire with two simultaneously free same-state taps. Tested three-input clause interfaces fail. No 3SAT rule or all-cover assignment decoder.
Next action: compose edge checkers with variable states and test budget additivity; long-wire three-arm junctions remain undecided.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Cited and adjacent primary proofs | Find exact rectangle-cover proof and decoder | No reconstructible proof found in bounded accessible search | [record](rounds/001/round.md) |
| 002 | Pairwise compatibility graph | Search a pairwise-compatible set with an illegal global bounding box | Exact chromatic equivalence proved; arbitrary-graph embedding remains open | [record](rounds/002/round.md) |
| 003 | One-anchor graph embedding | Enumerate anchor orders for forced nonedge boxes | Filler cells caused a 3-vs-2 cover gap in naive placement | [record](rounds/003/round.md) |
| 004 | Published orthogonal-polygon route | Locate explicit beam geometry, cover budget and extraction | Published route found; explicit geometry/decoder and raster area bound remain missing | [record](rounds/004/round.md) |
| 005 | Two-state variable tile | Enumerate small connected pictures with two minimum maximal covers | Endpoint join has four optimal modes, so proposed wire fails | [record](rounds/005/round.md) |
| 006 | Robust 4×4 phase tile | Seek two optimum covers differing by at least two rectangles | None among 7,943 connected full-span pictures | [record](rounds/006/round.md) |
| 007 | Thin-picture obstruction | Compare run-graph matching with exact cover | Polynomial matching theorem for all 2×2-free pictures | [record](rounds/007/round.md) |
| 008 | Thick exclusive-port core | Find core with either port free but both costly | Local and finite joined wires found; general proof/fanout/clause open | [record](rounds/008/round.md) |
| 009 | Occurrence tap and fanout | Find third port compatible with one state only | Local taps can fail after joining; alternate four-core wire has two jointly free same-state taps | [record](rounds/009/round.md) |
| 010 | Three-input clause junction | Enumerate three-core shared-cell placements and test eight-state OR table | All 16 additive inactive placements leak at the clause cell | [record](rounds/010/round.md) |
| 011 | Guarded two-cell clause marker | Add one neighboring cell to each additive shared-cell junction | Zero legal adjacent guard positions across all 16 eligible geometries | [record](rounds/011/round.md) |
| 012 | Reserved 2×2 clause checker | Align three state-selective taps with distinct checker cells | 74 placements reject the false row but all fail an active row | [record](rounds/012/round.md) |
| 013 | Alternative direct matrix hardness proofs | Locate a full exact-target matrix reduction with budget and decoder | No such proof in bounded accessible search; several sources use wrong direction or variant | [record](rounds/013/round.md) |
| 014 | Adapt MaxSNP-hardness construction | Inspect Berman–DasGupta's primary matrix reduction for exact threshold and decoder | Polygon decoder and count offset found; integer layout and raster-area proof missing | [record](rounds/014/round.md) |
| 015 | Antirectangle induction for thick wire | Search repeating `2t`/`2t+1` lower-bound witnesses | General exact endpoint-budget theorem proved for one explicit wire | [record](rounds/015/round.md) |
| 016 | Clause junction of certified long wires | Try three disjoint rotated endpoint wires at one clause cell | 128 clear geometries per tested length; eight false-row certificate searches returned unknown | [record](rounds/016/round.md) |
| 017 | Diagonal-band dynamic programming boundary | Prove bounded rectangle spans and test exact row-scan DP | Exact fixed-parameter DP proved; 21 independent oracle comparisons agree | [record](rounds/017/round.md) |
| 018 | Two-input edge checker for Vertex Cover | Search a shared marker with exactly the two-input OR table | 24 local placements have exact 7/6/6/6 costs; composition unproved | [record](rounds/018/round.md) |
