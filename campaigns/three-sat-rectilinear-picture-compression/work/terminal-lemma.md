# A two-input terminal with separated ports

For integer g≥2, take rows 0..3 with intervals `[0,g]`, `[1,g+1]`, `[0,g]`, `[0,g−1]`, and add two top stems: rows −2..−1, columns −1..0 and g..g+1. Supply input A as column 0, rows −2..0, and input B as column g, rows −2..2. All remaining one-cells must be covered; every covering rectangle must stay inside the full picture.

The minimum cost is six when neither input is supplied and five otherwise. For g=3, round 037 stores a cover of that size and a pairwise rectangle-incompatible set of that size in each of the four states (`certificates.json`). Each lower-bound point remains required, and each pair's bounding box contains a zero. Thus these are independently checkable finite proofs, not merely SAT answers. `certify.py` checks both bounds. For every g≥2, the columns strictly between the ports are identical non-input columns. Duplicating or contracting these columns preserves legal rectangle covers and both supplied input sets, by the coordinate-rank argument of round 021. Hence the four exact costs hold for all g≥2.

Input A has its background wing on the left and input B on the right. Upstream output wings must be on the opposite sides to obtain beam-only cuts. No complete source layout or decoder is asserted here.
