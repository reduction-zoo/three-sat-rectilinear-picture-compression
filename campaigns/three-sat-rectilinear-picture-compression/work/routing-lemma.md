# Monotone permutation routing

## Local contracts

Round 039's capped swap has baseline 46 and cost `46+|O\I|` (outputs labelled by their originating inputs). Each translator, with either left or right output wing, has baseline 16 and cost `16+[out and not in]`. All 24 constant-template states have explicit covers and forced-output antirectangle certificates in `rounds/039/certificates.json`, checked directly without a solver by `verify_certificates.py`.

A translator moves a vertical beam right by any integer D≥8. Its D=8 template is stretched by duplicating column 9, which is not a beam column. This preserves legal rectangles and the supplied/forced port sets. Every incoming cap has width two, to the right of its beam. Ordinary outgoing tails lie to the left. The alternative translator tail lies to the right for a terminal requiring a left input wing.

A top cap may be extended vertically upward by duplicating its boundary-row interval. If several cap intervals are disjoint, extend them independently. Every cover rectangle touching that interval can be extended upward; no such rectangle spans two cap intervals because their separating cells are zero. Conversely restriction to the original module gives a local cover. Supplied input beams are extended too. Thus all local state bounds and upper covers survive the operation.

## Construction invariant

Let n tracks start at strictly increasing positions with consecutive gaps at least P=100(n+1)^2. Sources are already complete above all active routing bodies. Route the desired final order by selection from right to left. For a desired last remaining track, repeatedly:

1. Translate it right to eleven columns left of its next neighbor.
2. Apply the capped swap. The selected track emerges 39 columns right of the neighbor's old position; the displaced neighbor emerges 28 columns right of its own old position.

After the selected track reaches the end of the remaining order, translate it to its reserved final position. Reserved positions are P apart, begin at least 3P to the right of the largest initial position, and are filled from right to left. Every module body occupies a fresh row band. Its incoming cap extends upward to the row just below its producer's output tail. Existing channels occupy only their two-column incoming cap strips outside active bodies.

At the start of each selection pass, every unselected track still corresponds to a distinct original slot, with a rightward displacement at most 28n. During a pass the selected track can be eleven columns right of its immediately displaced neighbor; all tracks ahead retain gaps at least P−28n−39. A translator protrudes only five columns left of its input and five right of its output. A compact swap occupies columns five left of its left input through five right of its right output. The two-column caps therefore leave zeros between every active body and every idle channel, even at the eleven-column temporary gap. The originally wider swap input cap violated this invariant; its counterexample is retained at commit fc01887.

Parking crosses no remaining track, because the selected track is the rightmost remaining one. It crosses no parked track, because its destination is left of all prior parked positions by at least P. The invariant is restored for the next pass. At a linked port, the predecessor's left output wing and successor's right input wing have only the beam column in common. A maximal rectangle meeting both modules is consequently that single-column beam, extended from its producer core through the successor's supplied input run. Input and output columns inside a routing module differ, so a beam cannot traverse three modules.

These facts establish the hypotheses of the conditional cut-composition lemma for this routing architecture, provided its sources supply separated left-wing outputs above the routing bands. No source or terminal attachment is established by this routing statement alone. For n=0 there is no routing; for n=1 there is only the parking translator.

## Size and evidence

There are at most n(n−1)/2 swaps, at most that many preparatory translations, and n parking translations. Thus there are O(n²) constant-complexity modules. Coordinate magnitudes are polynomial in n and the initial span. The sparse polygon uses O(n²) rectangles and boundary coordinates; rank compression produces at most O(n⁴) explicit cells. This is a worst-case polynomial bound, not a practical-size claim.

The exact code is `rounds/039/routing.py`. All six three-track permutations and two four-track permutations have no module overlap and exactly the intended inter-module maximal rectangles. Four endpoint tests on three-track reversal match the summed baseline plus unsupported outputs. These checks supplement the geometric invariant; they do not verify a complete 3SAT reduction.
