"""Check compressed covers against the original geometric union."""
from itertools import product
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions
from rank_grid import compress, lift


def inside(rects, x, y):
    return any(a <= x < b and c <= y < d for a, b, c, d in rects)


xs, ys = [0, 1, 2**80, 2**160], [-2**90, -1, 2, 2**100]
checked = 0
for bits in product((0, 1), repeat=9):
    original = [[bits[3*r+c] for c in range(3)] for r in range(3)]
    rects = [(xs[c], xs[c+1], ys[r], ys[r+1])
             for r in range(3) for c in range(3) if original[r][c]]
    matrix, cx, cy = compress(rects)
    expected = next(k for k in range(10) if target_solutions({"matrix": original, "K": k}, 1) != [NO])
    covers = target_solutions({"matrix": matrix, "K": expected}, 2)
    assert covers != [NO]
    if expected:
        assert target_solutions({"matrix": matrix, "K": expected-1}, 1) == [NO]
    for cover in covers:
        lifted = lift(cover, cx, cy)
        assert len(lifted) == len(cover)
        for r in range(3):
            for c in range(3):
                # Use exact doubled midpoints, avoiding floating-point loss.
                x, y = xs[c]+xs[c+1], ys[r]+ys[r+1]
                scaled = [(2*a, 2*b, 2*d, 2*e) for a,b,d,e in lifted]
                assert inside(scaled, x, y) == bool(original[r][c])
    checked += 1
assert compress([(0, 2**1000, 0, 1)])[0] == [[1]]
print({"binary_patterns": checked, "huge_coordinate_rectangle": "passed"})
