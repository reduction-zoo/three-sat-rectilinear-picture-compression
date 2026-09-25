"""Check whether two shared-end staircase tiles propagate a Boolean phase."""

from itertools import combinations, product
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

height = width = 5
ones = {(0, 4), (1, 4), (1, 3), (2, 3), (2, 2),
        (3, 2), (3, 1), (4, 1), (4, 0)}
matrix = [[int((r, c) in ones) for c in range(width)] for r in range(height)]
rectangles = []
for r0 in range(height):
    for r1 in range(r0, height):
        for c0 in range(width):
            for c1 in range(c0, width):
                cells = frozenset(product(range(r0, r1 + 1), range(c0, c1 + 1)))
                if cells <= ones:
                    rectangles.append(((r0, r1, c0, c1), cells))
maximal = [(rect, cells) for rect, cells in rectangles
           if not any(cells < other for _, other in rectangles)]
for budget in range(1, len(maximal) + 1):
    covers = [tuple(maximal[i][0] for i in ids) for ids in combinations(range(len(maximal)), budget)
              if set().union(*(maximal[i][1] for i in ids)) == ones]
    if covers:
        break
assert target_solutions({"matrix": matrix, "K": budget - 1}, 1) == [NO]
assert target_solutions({"matrix": matrix, "K": budget}, 1) != [NO]
print({"matrix": matrix, "minimum": budget, "maximal_rectangles": len(maximal),
       "minimum_maximal_covers": len(covers), "covers": covers})
