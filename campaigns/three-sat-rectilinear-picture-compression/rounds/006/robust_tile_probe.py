"""Search connected 4x4 pictures for two genuinely different minimum covers."""

from itertools import combinations, product
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "005"))
from tile_probe import connected, maximal_rectangles
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

h = w = 4
checked = connected_count = two_cover_count = robust_count = oracle_checks = 0
examples = []
for bits in product((0, 1), repeat=h * w):
    checked += 1
    ones = {(r, c) for r in range(h) for c in range(w) if bits[r * w + c]}
    if not connected(ones, h, w) or any(not any(r == row for r, _ in ones) for row in range(h)) or any(not any(c == col for _, c in ones) for col in range(w)):
        continue
    connected_count += 1
    rects = maximal_rectangles(ones, h, w)
    for k in range(1, len(rects) + 1):
        covers = [tuple(rects[i][0] for i in ids) for ids in combinations(range(len(rects)), k)
                  if set().union(*(rects[i][1] for i in ids)) == ones]
        if covers:
            break
    if connected_count % 397 == 0:
        matrix = [list(bits[r * w:(r + 1) * w]) for r in range(h)]
        assert target_solutions({"matrix": matrix, "K": k - 1}, 1) == [NO]
        assert target_solutions({"matrix": matrix, "K": k}, 1) != [NO]
        oracle_checks += 1
    two_cover_count += len(covers) == 2
    if len(covers) == 2 and len(set(covers[0]) ^ set(covers[1])) >= 4:
        robust_count += 1
        if len(examples) < 5:
            examples.append({"matrix": [list(bits[r * w:(r + 1) * w]) for r in range(h)],
                             "minimum": k, "covers": covers})
print({"shape": [h, w], "checked": checked, "connected_full_span": connected_count,
       "two_cover_tiles": two_cover_count, "robust_two_cover_tiles": robust_count,
       "independent_oracle_samples": oracle_checks, "examples": examples})
