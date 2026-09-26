# Round 032 — Inverting turns and telescoping port costs

## Plan

A paired translator changes position but preserves orientation. New strategy: split it into single-machine 90-degree turns, allowing complementary signal states and a port-dependent cost. If a turn costs B−input for complementary states, this equals B−1/2+(output−input)/2; differences telescope along an even-turn route. First check: an explicit isolated half-translator must have that cost table, and pairs of turns must regain an equal endpoint cost. A cost discount is usable only with this accounting proof; it is not automatically a failure. The earlier two-core and crossover evidence motivates the split but supplies no all-cover argument for it.

## Evidence and diagnosis

The half translator has costs 9,9,8,9 for input/output-required states 00,01,10,11. Explicitly forbidding the maximal output beam gives the same four costs. Complementary states therefore satisfy the potential formula `8.5+(out−in)/2`; equal states have an extra half unit, not the initially proposed full unit. This supports a possible telescoping bound but requires an ownership/decomposition theorem.

For two, four and six joined turns, exact endpoint tables are respectively 14/15/14/14, 28/29/28/28, and 41/42/41/41 (`chain_exact_output.txt`). An initial scan incorrectly started its search at 7n, so it reported 42 in every six-turn state (`chain_output.txt`). That was a checker lower-bound assumption, NOT a signal counterexample. Replaced the scan by binary search over 0..10n; all 12 exact state instances now pass the implication table. However the baseline itself ceases to be additive: six turns cost 41 rather than 42. No general network count or all-cover ownership proof follows.

Added forbidden-rectangle support to the existing Kissat oracle after a three-case real L-picture test failed on the missing keyword. All those tests now pass. Eight one-turn state queries plus twelve corrected chain instances; no unknown results, source/recovery counts 0/0. Experience extraction: none; these remain supporting finite turn observations rather than an established compositional theorem.

## Next action

Prove or refute the port-potential accounting before designing arbitrary routed networks.
