# Round 038 — Closed vertex source with actual beam outputs

## Plan

Round 022's vertex evidence supplied an optional channel and required selected endpoint cells; that is insufficient for the cut-composition contract. Construct a fully required source picture, force whole outgoing rectangles, then attach separated tails with the output wing orientations required by consumers. First check: degrees 1,2,3 must have one common activation charge, independent of the nonempty subset of selected beams. Empty output state gives the baseline. Reuse the published variable shape, but reject endpoint-only evidence as a substitute for full-beam/full-picture counts. The cut-composition entry supplies the interface obligation.

## Evidence and diagnosis

Full pictures with actual forced beam rectangles have baselines 16,24,32 for d=1,2,3 and one extra rectangle for any nonempty output subset (`output.txt`). Adding separated three-row, width-two left tails gives baselines 17,26,35 = 9d+8, preserving the same common activation charge (`padded_output.txt`). Fourteen states were checked in each geometry; no unknown results.

For all 14 padded states, `certificates.json` contains matching covers and antirectangle lower bounds outside the forced outputs. `verify_certificates.py` independently checks the exact covered cell union, forced rectangles, certificate size, and every incompatible pair directly against zeros; it uses neither SAT nor maximal-rectangle enumeration. All pass (`verified_output.txt`). The [source lemma](../../work/source-lemma.md) states the resulting finite-degree theorem and permitted coordinate stretching. Source-to-target F/G injections and recovery remain 0/0.

Experience extraction: appended to the beam-route entry; the original optional-channel/endpoint test remains historical and is not substituted for this stronger result.

## Next action

If the closed-source table holds, certify the constant-degree gadgets and integrate with routing and terminal modules.
