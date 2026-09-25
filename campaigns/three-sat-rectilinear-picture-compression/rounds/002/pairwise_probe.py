"""Find point sets whose pairwise rectangle hull misses their full hull."""

from itertools import combinations


def box(a, b):
    return {(r, c) for r in range(min(a[0], b[0]), max(a[0], b[0]) + 1)
            for c in range(min(a[1], b[1]), max(a[1], b[1]) + 1)}


for height, width, max_size in [(3, 3, 9), (4, 4, 6)]:
    cells = [(r, c) for r in range(height) for c in range(width)]
    count = 0
    for size in range(2, min(max_size, len(cells)) + 1):
        for points in combinations(cells, size):
            count += 1
            pairwise = set(points)
            for a, b in combinations(points, 2):
                pairwise |= box(a, b)
            full = box((min(r for r, _ in points), min(c for _, c in points)),
                       (max(r for r, _ in points), max(c for _, c in points)))
            if pairwise != full:
                print({"grid": [height, width], "points": points,
                       "missing": sorted(full - pairwise), "tested": count})
                raise SystemExit
    print({"grid": [height, width], "tested": count, "counterexample": None})
