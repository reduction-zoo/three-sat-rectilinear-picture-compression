# Round 022 — digitize the published beam system

## Plan

Reconstruct Berman–DasGupta's vertex-cover reduction from the vector geometry of Figures 7–18. Rank compression from round 021 removes coordinate-span concerns. The construction hypothesis is that the constant-size beam, vertex and edge shapes can be translated into exact grid templates with the paper's costs, then assembled with its translation and permutation stages. Recovery will implement the normalization in Lemma 5.6.

First discriminating check: recover the Figure 7 beam boundary as ordered line segments, give its open mouth a precise finite grid interface, and verify the two six-rectangle beam states and the adjacent uncovered square. Then check the vertex/edge cost interfaces before global assembly. Prior experience: round 014 and `vertex-cover-beam-route.md`; the raster-area objection is now corrected by round 021. The primary PDF was fetched in round 014 and remains locally available; retain extraction commands and explicit templates for reproducibility.

## Evidence and diagnosis

The exact Figure 7 core has six-rectangle horizontal and vertical states, while simultaneous extension costs seven (`beam_probe.py`). Seven maximal six-rectangle core covers exist, including five that send neither beam; they can be normalized to one of the two extending covers in this finite interface. The regularized Figure 8/9 vertex shape has baseline costs 15, 23, 31 for degrees 1, 2, 3, and every nonempty subset of requested outgoing ports costs exactly one extra (`vertex_probe.py`, 11 nonempty subsets). This agrees with the component description's 8d+7 baseline. The later printed count 7d+7 on PDF page 17 conflicts with PDF page 12; the earlier round-014 offset must not be used without recomputing it.

The first regularized permutation stage fails the intended interface (`permutation_output.txt`): costs are 17 without incoming coverage and 16 with incoming coverage, and merely requiring the output endpoint does not force an actual beam from the machine. Its staircase row ordering differs from the figure, and its truncated bottom background can cover that endpoint. These are defects in this reconstruction, not a refutation of the published gadget. Preserve this initial experiment before repairing the geometry and the beam-state measurement.

The faster maximal-rectangle enumerator was tested first against the existing exhaustive enumerator on all 512 binary 3×3 pictures. Every list agrees. Its solver checks witnesses cell by cell and treats unknown as an execution failure. No full F/G exists yet. Work continues within this attempt.

## Next action

Resolve exact beam interfaces, component placement and all-cover normalization in the same reconstruction attempt.
