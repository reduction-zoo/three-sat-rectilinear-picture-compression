"""Compose two exact-cost edge checkers around one central core."""

from functools import lru_cache
from itertools import combinations, product
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

core = {(1, 3), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)}
p, q = (4, 2), (1, 4)
taps = (((0, 3), "P"), ((4, 3), "P"), ((3, 4), "Q"))


def transform(point, reflect, turns):
    r, c = point
    if reflect:
        c = 4 - c
    for _ in range(turns):
        r, c = c, 4 - r
    return r, c


def matrix_key(cells):
    r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
    return tuple(tuple(int((r, c) in cells) for c in range(c0, max(c for _, c in cells) + 1))
                 for r in range(r0, max(r for r, _ in cells) + 1))


@lru_cache(None)
def feasible(matrix, budget):
    return target_solutions({"matrix": [list(row) for row in matrix], "K": budget}, 1) != [NO]


def selected_port(ports, polarity, active):
    return ports[0] if active == (polarity == "P") else ports[1]


local = []
tested = 0
for center_tap, center_polarity in taps:
    for leaf_tap, leaf_polarity in taps:
        for reflect, turns in product((False, True), range(4)):
            ar, ac = transform(leaf_tap, reflect, turns)
            dr, dc = center_tap[0] - ar, center_tap[1] - ac
            move = lambda point: tuple(x + y for x, y in zip(transform(point, reflect, turns), (dr, dc)))
            leaf = {move(cell) for cell in core}
            leaf_ports = (move(p), move(q))
            state_ports = (p, q, *leaf_ports)
            if (leaf & core or any(point in leaf | core or point == center_tap for point in state_ports)
                    or len(set(state_ports)) != 4):
                continue
            tested += 1
            union = core | leaf | {center_tap}
            passed = True
            for center_active, leaf_active in product((False, True), repeat=2):
                picture = union | {selected_port((p, q), center_polarity, center_active),
                                   selected_port(leaf_ports, leaf_polarity, leaf_active)}
                expected = 6 if center_active or leaf_active else 7
                if feasible(matrix_key(picture), expected - 1) or not feasible(matrix_key(picture), expected):
                    passed = False
                    break
            if passed:
                local.append({"center_tap": center_tap, "center_polarity": center_polarity,
                              "leaf_tap": leaf_tap, "leaf_polarity": leaf_polarity,
                              "reflect": reflect, "turns": turns, "leaf": leaf,
                              "leaf_ports": leaf_ports})

compositions = []
for left, right in combinations(local, 2):
    if left["center_tap"] == right["center_tap"] or left["center_polarity"] != right["center_polarity"]:
        continue
    if left["leaf"] & right["leaf"]:
        continue
    markers = {left["center_tap"], right["center_tap"]}
    all_cores = core | left["leaf"] | right["leaf"]
    ports = {p, q, *left["leaf_ports"], *right["leaf_ports"]}
    if (markers & all_cores or markers & ports or any(point in all_cores for point in ports)
            or len(ports) != 6):
        continue
    compositions.append((left, right))

print({"local_nonoverlap_tested": tested, "exact_local_attachments": len(local),
       "by_center_tap": {str(tap): sum(item["center_tap"] == tap for item in local)
                         for tap, _ in taps},
       "clear_two_edge_compositions": len(compositions)})


def optimum(cells):
    matrix = matrix_key(cells)
    lo, hi = 0, len(cells)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(matrix, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


for index, (left, right) in enumerate(compositions):
    rows = []
    threshold_ok = True
    for center_active, left_active, right_active in product((False, True), repeat=3):
        cells = (core | left["leaf"] | right["leaf"]
                 | {left["center_tap"], right["center_tap"],
                    selected_port((p, q), left["center_polarity"], center_active),
                    selected_port(left["leaf_ports"], left["leaf_polarity"], left_active),
                    selected_port(right["leaf_ports"], right["leaf_polarity"], right_active)})
        expected = 9 + int(not center_active and not left_active) + int(not center_active and not right_active)
        actual = optimum(cells)
        rows.append({"state": (center_active, left_active, right_active),
                     "expected_additive_cost": expected, "actual_cost": actual})
        threshold_ok &= (actual == 9) if expected == 9 else (actual > 9)
        if actual != expected:
            print({"first_composition_mismatch": index, "row": rows[-1],
                   "matrix": matrix_key(cells)}, flush=True)
    print({"composition": index,
           "attachments": [{key: item[key] for key in ("center_tap", "center_polarity", "leaf_tap",
                                                        "leaf_polarity", "reflect", "turns")}
                           for item in (left, right)],
           "rows_checked": rows, "vertex_cover_threshold_at_nine": threshold_ok}, flush=True)
