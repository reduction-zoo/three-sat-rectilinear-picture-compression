"""Test whether one anchor per vertex realizes each small conflict graph."""

from itertools import combinations, permutations, product
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions


def box(a, b, n):
    return sum(1 << (r * n + c) for r in range(min(a[0], b[0]), max(a[0], b[0]) + 1)
               for c in range(min(a[1], b[1]), max(a[1], b[1]) + 1))


def realizable(n, edge_mask):
    pairs = list(combinations(range(n), 2))
    for rows in permutations(range(n)):
        for cols in permutations(range(n)):
            anchors = list(zip(rows, cols))
            boxes = [box(anchors[u], anchors[v], n) for u, v in pairs]
            filled = sum(1 << (r * n + c) for r, c in anchors)
            for i, candidate in enumerate(boxes):
                if not edge_mask & (1 << i):
                    filled |= candidate
            if all(candidate & ~filled for i, candidate in enumerate(boxes)
                   if edge_mask & (1 << i)):
                return anchors
    return None


def picture(n, edge_mask, anchors):
    pairs = list(combinations(range(n), 2))
    filled = set(anchors)
    for i, (u, v) in enumerate(pairs):
        if not edge_mask & (1 << i):
            filled |= {(r, c) for r in range(min(anchors[u][0], anchors[v][0]), max(anchors[u][0], anchors[v][0]) + 1)
                       for c in range(min(anchors[u][1], anchors[v][1]), max(anchors[u][1], anchors[v][1]) + 1)}
    return [[int((r, c) in filled) for c in range(n)] for r in range(n)]


def chromatic_number(n, edge_mask):
    pairs = list(combinations(range(n), 2))
    return next(k for k in range(1, n + 1)
                if any(all(colors[u] != colors[v] for i, (u, v) in enumerate(pairs)
                           if edge_mask & (1 << i)) for colors in product(range(k), repeat=n)))


for n in (3, 4, 5):
    pair_count = n * (n - 1) // 2
    checked = 0
    for edge_mask in range(1 << pair_count):
        checked += 1
        placement = realizable(n, edge_mask)
        if placement is None:
            pairs = list(combinations(range(n), 2))
            print({"n": n, "graphs_checked": checked,
                   "conflict_edges": [edge for i, edge in enumerate(pairs) if edge_mask & (1 << i)],
                   "one_anchor_realization": None})
            break
    else:
        print({"n": n, "graphs_checked": checked, "all_realizable": True})

for n in (4, 5):
    pairs = list(combinations(range(n), 2))
    checked = 0
    for edge_mask in range(1 << len(pairs)):
        anchors = realizable(n, edge_mask)
        assert anchors is not None
        k = chromatic_number(n, edge_mask)
        matrix = picture(n, edge_mask, anchors)
        checked += 1
        if target_solutions({"matrix": matrix, "K": k}, 1) == [NO]:
            print({"n": n, "graphs_checked": checked, "conflict_edges": [edge for i, edge in enumerate(pairs) if edge_mask & (1 << i)],
                   "chromatic_number": k, "picture": matrix, "anchor_positions": anchors,
                   "cover_at_k": NO})
            break
    else:
        print({"n": n, "graphs_checked": checked, "all_anchor_pictures_coverable_at_chromatic_number": True})

pairs = list(combinations(range(4), 2))
edges = {(0, 1), (0, 3), (1, 2)}
edge_mask = sum(1 << i for i, edge in enumerate(pairs) if edge in edges)
valid = coverable = 0
for rows in permutations(range(4)):
    for cols in permutations(range(4)):
        anchors = list(zip(rows, cols))
        matrix = picture(4, edge_mask, anchors)
        if any(all(matrix[r][c] for r in range(min(anchors[u][0], anchors[v][0]), max(anchors[u][0], anchors[v][0]) + 1)
                   for c in range(min(anchors[u][1], anchors[v][1]), max(anchors[u][1], anchors[v][1]) + 1))
               for u, v in edges):
            continue
        valid += 1
        if target_solutions({"matrix": matrix, "K": 2}, 1) != [NO]:
            coverable += 1
            print({"graph": sorted(edges), "some_two_rectangle_embedding": anchors})
            break
    if coverable:
        break
print({"graph": sorted(edges), "valid_placements_checked": valid, "coverable": bool(coverable)})
