# Campaign state

Status: `stopped_without_discovery` after 40 numbered attempts.
Board source: 834a23a845589826383af2fdf2f1425e02e88864.

Capability probe (2026-09-25): Python 3.12.14 at `/Users/xiweipan/.local/bin/python3`; uv 0.12.17 at `/Users/xiweipan/.local/bin/uv`; Z3 executable 5.1.0 at `/opt/homebrew/bin/z3`; Kissat 4.0.4 at `/opt/homebrew/bin/kissat`; Typst 0.15.1 at `/opt/homebrew/bin/typst`; Lean 4.34.1 at `/opt/homebrew/bin/lean`; Lake 5.0.0 at `/opt/homebrew/bin/lake`. Python Z3 binding selected for Prepare; locked version recorded in `uv.lock`. Mathlib status: not probed because formalization is not requested. Writing skill is available in the session catalogue. No capability blocker for Prepare.
Prepare: 120 fixed source cases, independent Z3 and exhaustive source checks, exact target rectangle-cover oracle and direct validators; see [preparation](work/preparation.md). Self-test passed 2026-09-25. No construction claim follows from Prepare.
Current claim: an unverified integrated F/G candidate now composes a degree-three graph reduction, certified source/translator/swap/terminal templates, monotone routing and a charging decoder. The graph step passes all 120 prepared sources and 212 cover recoveries. Three small graph-to-picture instances pass (two recovered covers, one UNSAT). Two empty-clause source commands pass. No nonempty formula has completed end-to-end candidate verification; global attachment and source bit-length obligations remain. See [candidate argument](work/proof.md) and [verification scope](work/verification.md).
Next action: address feasible explicit-matrix size, a complete attachment proof, and the fixed source encoding's unused-variable bit-length obligation. Known hardness is not disputed.

Resumption assessment: the known hardness result stands. Current prospects are unknown (uncalibrated); published constructions are the primary route. Preserve the first closeout below as history.

Closeout assessment (2026-09-25): **Correctness:** the wire and diagonal-band partial lemmas have explicit proofs and computational checks, but no source reduction exists and no independent review was triggered. The 120-case Prepare oracle is checked independently; candidate F/G checks are 0/0. **Novelty:** unestablished for the partial lemmas and gadgets; the campaign did not establish priority over literature. **Significance:** a usable 3-SAT reduction was not obtained. The strongest obstruction is coordinating one fixed global picture with variable fanout, clause costs, isolation from unintended rectangles, polynomial layout and a decoder for every valid cover. Eight mechanism families were explored across 20 attempts: literature reconstruction, compatibility-graph formulation, one-anchor embedding, small phase tiles, tractable-picture boundaries, thick wire and ports, clause junctions, and Vertex Cover edge checkers. Twelve local experience entries were created, six later updated; board promotion is pending separate authorization, and the board was not edited. No entry remains pending extraction from a completed round.

Closeout checks (2026-09-25): reran the Prepare self-test (120 source cases), round 015 certificate/witness probe (through 20 cores), round 017 band DP comparison (21 pictures), round 018 four-row edge witness check, round 019 shared-core search (output byte-identical to retained evidence), and round 020 exhaustive tap count. All completed successfully. The README gives the exact commands. No candidate verification, independent review, paper or formalization applies without F/G and a general reduction proof.


## Second closeout (2026-09-25)

Rounds 021–040 are complete: **40 numbered attempt records**.
Status `stopped_without_discovery` means no accepted complete rule, not no useful
partial result. The full prepared candidate run ended at an execution limit and
has no full-suite verdict. The known hardness theorem is not contradicted.

**Correctness:** executable candidate F/G and a conditional argument are retained;
120 independently labelled graph cases, 212 graph recoveries, three small actual
picture instances and two empty-source command cases pass. The local source and
routing certificates and 511-picture backend regression pass. General attachment
correctness, nonempty-source full-loop verification and a source bit-length issue
remain unresolved. No independent review, paper or formalization was eligible.
**Novelty:** not established; this is reconstruction of a known hardness rule,
with locally derived gadget repairs and certificates, not a claim of a new
complexity classification. **Significance:** the campaign now has a concrete
integrated candidate and reusable routing components, but has not delivered the
accepted reduction. The measured 16-clause target has 15,514,487,415 cells, a serious
explicit-size obstacle. This does not reject the known hardness result.

For navigation, the additional 20 attempts cover 11 broad mechanism/scope
families: rank compression; published beam reconstruction and isolation;
alternative primary literature/code investigations; translators and corridors;
perpendicular crossings; inverting turns; vertical swaps and ownership cuts;
terminal synthesis; closed vertex sources; monotone global routing; full
source/graph/picture integration. This grouping does not merge or discount any
numbered attempt. Prepare and all same-strategy tests/repairs stay outside the
attempt count or within their existing attempt, respectively.

Experience from these attempts: **2 distinct entries created** (beam-cut
composition and separated terminal), **2 pre-existing entries updated**
(rank-grid area and vertex-cover route); the new beam-cut entry also received
follow-up updates. There are **14 total local entries pending authorized board
promotion**, zero pending extraction from completed rounds. The board and remotes
were untouched; nothing was published. Earlier closeout evidence above is
retained as history. README and verification.md give reproduction commands.

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
| 019 | Shared variable core for two edges | Combine two exact-cost checkers around one core and test eight states | Three compositions preserve threshold nine but double-uncovered penalties merge | [record](rounds/019/round.md) |
| 020 | Degree-three same-state fanout | Search three selective taps and three clear edge-checker attachments | All 224 eligible 3×3 port pairs have at most two same-state taps; attachment stage unavailable in this family | [record](rounds/020/round.md) |
| 021 | Coordinate rank compression of polygon covers | Prove separable monotone maps preserve rectangles and test huge coordinate gaps | General count-preserving compression proved; all 512 stretched 3×3 cases pass | [record](rounds/021/round.md) |
| 022 | Digitize published beam system | Recover exact beam geometry and verify its port interface | Beam and vertex templates recovered; modified switch leaks under composition | [record](rounds/022/round.md) |
| 023 | Reset staircase boundaries | Test the first leaking two-stage state after an outward boundary reset | Refuted: previous background still supplies a later input notch at baseline 32 | [record](rounds/023/round.md) |
| 024 | Lubiw and early matrix-cover sources | Obtain a full primary construction from the cited source chain | No accessible full alternative construction; thesis metadata corrected | [record](rounds/024/round.md) |
| 025 | Span-blocking holes | Local implication and two-stage leak regression | Both barrier variants leak; exact covers retained, second SAT backend cross-checked | [record](rounds/025/round.md) |
| 026 | Full journal construction and filters | Obtain detailed primary proof | Closed publisher copy; former author page unavailable | [record](rounds/026/round.md) |
| 027 | Opposed beam translation pair | Exact four-state signal table | Exact local table and chains through four pairs pass; global routing open | [record](rounds/027/round.md) |
| 028 | Vector-faithful permutation geometry | Recover boundary and exact signal table | Schematic closure leaks; corrected notch regularization has unwanted discount | [record](rounds/028/round.md) |
| 029 | Executable published reduction search | Locate F/G code, not target solver | Found target model and outgoing ILP rule only | [record](rounds/029/round.md) |
| 030 | Narrow-channel routing | Positive-gap signal table | One-row join works; longer mandatory corridor creates signals freely | [record](rounds/030/round.md) |
| 031 | Perpendicular paired-translator crossing | Joint 16-state table | All 16 local and 64 joined states have exact additive costs | [record](rounds/031/round.md) |
| 032 | Inverting turns with port potentials | Half-translator exact cost table | Turn potentials fit; endpoint tables pass through six turns, baseline nonadditive | [record](rounds/032/round.md) |
| 033 | Two-turn adjacent swap | Port clearance and exact two-channel table | Widened swap passes all 16 states; staggered port connections remain | [record](rounds/033/round.md) |
| 034 | Mandatory side strips for long corridors | Gap-four implication table | Wide corridors and flat swaps pass; two-swap baseline is nonadditive | [record](rounds/034/round.md) |
| 035 | Rectangle ownership across tile cuts | All crossing rectangles must be designated beams | Exact beam-only cut; additive two-tile count and conditional decoder lemma | [record](rounds/035/round.md) |
| 036 | Direct terminal OR synthesis | All 3×3 masks with top-entering inputs | No terminal in 384 eligible 3×3 input-pair geometries | [record](rounds/036/round.md) |
| 037 | Four-row terminal synthesis | Residual-cover DP and independent SAT check | Found and certified separated terminal with general 6/5/5/5 lemma | [record](rounds/037/round.md) |
| 038 | Full vertex source with beam outputs | Closed-picture common activation cost | All constant-degree source states certified with one common activation charge | [record](rounds/038/round.md) |
| 039 | Monotone routing with vacated intervals | Separated translator table and three-track permutation | Certified routing templates and monotone compiler; eight layouts pass ownership checks | [record](rounds/039/round.md) |
| 040 | Full source composition and charging decoder | Prepared source/graph checks and complete picture test | Integrated unverified candidate; graph checks pass, full picture verification blocked by size | [record](rounds/040/round.md) |
