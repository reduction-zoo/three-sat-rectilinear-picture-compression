# Round 015 — antirectangle induction for a thick wire

## Plan

Gap: round 008 verified a repeated thick wire through five cores but has no proof for arbitrary length. New proof strategy: use a repeating set of pairwise incompatible one-cells (an antirectangle) to certify a `2t` lower bound for `t` cores, and a `2t+1` antirectangle when both endpoints are required. If the certificates and matching endpoint covers have a fixed local recurrence, the wire property could follow by induction without characterizing every optimal cover.

First discriminating check: construct the explicit repeated wire for three through at least six cores, solve the maximum-antirectangle problem independently for its base and both-end pictures, and compare the coordinate patterns after subtracting each new core's translation. A failure at six refutes the recurrence; successful finite counts alone leave the induction and all-output phase decoding open.

Prior evidence: [round 008](../008/round.md) gives finite base and endpoint target statuses through five cores; [round 002](../002/round.md) proves pairwise incompatibility bounds rectangle covers.

## Evidence and diagnosis

`antirectangle_induction_probe.py` constructed the round-008 wire for 3–6 cores and solved eight independent maximum-antirectangle problems (base and both-end picture for each length). The maxima were `2t` and `2t+1` respectively: `6/7`, `8/9`, `10/11`, `12/13`. The output gives actual cell sets. A nested closed-form certificate, inferred from these examples, was then checked directly for every length `3≤t≤20` (36 base/both pictures) without calling the target-cover oracle. The displayed repeated core is a transpose translated by `(3,-2)` at each step. The same script used the independent prepared witness validator on 54 explicit `2t` covers for the base, left-end and right-end pictures through 20 cores.

The finite pattern yields a **general proof**, written in [wire-lemma.md](../../work/wire-lemma.md): two local rectangles per core cover the base picture or either one endpoint; explicit monotone antirectangles of sizes `2t` and `2t+1` prove the matching lower bounds for every `t≥3`. The proof lists the occupied rows of each repeated core and a zero witness between every consecutive antirectangle pair. This establishes exact cover sizes `2t` for the base or one-end picture and `2t+1` with both endpoints, independent of finite solver checks. There is no arbitrary-cover phase decoder, occurrence-fanout theorem, clause gadget, polynomial global layout or 3SAT F/G. Source/recovery instances: 0/0. The partial proof has not been independently reviewed; the registered reviewer is reserved for a complete candidate. Experience extraction: updated [thick exclusive ports](../../../../research/experience/thick-exclusive-ports.md).

## Next action

Investigate a construction that uses this certified wire while solving clause composition and all-cover recovery, or switch to a different global encoding. The wire lemma alone does not reduce 3SAT.
