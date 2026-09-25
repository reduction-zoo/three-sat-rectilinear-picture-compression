# Round 001 — primary-source construction search

## Plan

Gap: no concrete rectangle gadget or recovery rule is known. Investigate the cited Garey–Johnson A4.2 attribution and directly related primary proofs for a reduction whose matrix, budget and decoding can be reconstructed. First discriminating check: locate an actual theorem/proof for the exact all-one axis-aligned rectangle cover formulation, and compare its source problem and witness decoding to the fixed question. A matching full proof could anchor the construction; a catalog citation or theorem statement alone cannot.

Prior evidence: the fixed question contains only an upstream issue and an unverified A4.2 page reference. The board's local experience-entry directory is absent.

## Evidence and diagnosis

Checked [Garey–Johnson, SR25, p. 232](https://perso.limos.fr/~palafour/PAPERS/PDF/Garey-Johnson79.pdf): the catalog states the binary-matrix exact rectangle-cover problem and says “Transformation from 3SAT,” but gives no construction or decoder. The cited Masek, *Some NP-complete set covering problems* (1978/1979), remains an unpublished manuscript; no accessible primary copy was located in title/author searches. The primary [Chaiken–Kleitman–Saks–Shearer paper](https://www.researchgate.net/publication/239486876_Covering_Regions_by_Rectangles) explicitly attributes general nonconvex hardness to Masek while proving a positive result for convex boards; it does not reproduce the hardness gadgets. The [Applegate et al. paper](https://citeseerx.ist.psu.edu/document?doi=063940b038565a3d460da837f19383e677d5f92f&repid=rep1&type=pdf) uses RPC as a hardness source for a different compression problem, without a 3SAT-to-RPC rule. A later [rectangle-cover study](https://eprints.cs.univie.ac.at/7923/1/Covering_Rectilinear_Polygons.pdf), §2, confirms the exact matrix formulation and its polygon relation, but cites rather than proves Masek's theorem. Search covered the named manuscript, GJ citation, these primary follow-ons and accessible direct-proof leads; inaccessible archives were not audited.

Outcome: no full proof suitable for F/G reconstruction found in this finite search. This is an access/coverage result, not a claim the proof does not exist. Actual solver/recovery instances: 0/0; literature scope only. Supported cause: the named source is unpublished and the accessible adjacent papers defer the reduction. Remaining obligation: construct or find a proof with concrete matrix, budget and recovery.

Experience extraction: none; source unavailability is campaign-specific and no transferable construction constraint was established.

## Next action

Try a new structural construction strategy in round 002, beginning with the geometry of cell compatibility.
