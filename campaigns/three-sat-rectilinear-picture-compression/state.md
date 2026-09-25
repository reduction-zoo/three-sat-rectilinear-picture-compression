# Campaign state

Budget: 20 rounds. Used: 9 (round 009 open).
Board source: 834a23a845589826383af2fdf2f1425e02e88864.

Capability probe (2026-09-25): Python 3.12.14 at `/Users/xiweipan/.local/bin/python3`; uv 0.12.17 at `/Users/xiweipan/.local/bin/uv`; Z3 executable 5.1.0 at `/opt/homebrew/bin/z3`; Kissat 4.0.4 at `/opt/homebrew/bin/kissat`; Typst 0.15.1 at `/opt/homebrew/bin/typst`; Lean 4.34.1 at `/opt/homebrew/bin/lean`; Lake 5.0.0 at `/opt/homebrew/bin/lake`. Python Z3 binding selected for Prepare; locked version recorded in `uv.lock`. Mathlib status: not probed because formalization is not requested. Writing skill is available in the session catalogue. No capability blocker for Prepare.
Prepare: 120 fixed source cases, independent Z3 and exhaustive source checks, exact target rectangle-cover oracle and direct validators; see [preparation](work/preparation.md). Self-test passed 2026-09-25. No construction claim follows from Prepare.
Current claim: finite thick exclusive-port wires through five cores, plus one four-core wire with two simultaneously free same-state taps; no general induction or 3SAT rule.
Next action: round 010 clause-junction test.

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
