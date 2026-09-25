"""Search a two-input OR edge checker from two thick cores."""

from functools import lru_cache
from itertools import combinations
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


options = []
for tap, polarity in taps:
    for reflect in (False, True):
        for turns in range(4):
            tr, tc = transform(tap, reflect, turns)
            move = lambda point: tuple(x - y for x, y in zip(transform(point, reflect, turns), (tr, tc)))
            options.append((tap, polarity, reflect, turns,
                            {move(cell) for cell in core}, (move(p), move(q))))

counts = {"disjoint": 0, "clear_ports": 0, "additive_core": 0,
          "additive_inactive": 0, "false_costly": 0,
          "threshold_or": 0, "exact_cost_or": 0}
first_leak = first_positive_failure = first_or = first_discount = None
for indices in combinations(range(24), 2):
    pair = [options[index] for index in indices]
    if pair[0][4] & pair[1][4]:
        continue
    counts["disjoint"] += 1
    union = pair[0][4] | pair[1][4]
    ports = [point for item in pair for point in item[5]]
    if any(point in union or point == (0, 0) for point in ports) or len(set(ports)) != 4:
        continue
    counts["clear_ports"] += 1
    if feasible(matrix_key(union), 5):
        continue
    counts["additive_core"] += 1
    inactive = {item[5][int(item[1] == "P")] for item in pair}
    if feasible(matrix_key(union | inactive), 5) or not feasible(matrix_key(union | inactive), 6):
        continue
    counts["additive_inactive"] += 1
    false_picture = union | inactive | {(0, 0)}
    if feasible(matrix_key(false_picture), 6):
        if first_leak is None:
            first_leak = indices
            matrix = matrix_key(false_picture)
            print({"first_false_leak": indices, "matrix": matrix,
                   "witness": target_solutions({"matrix": [list(row) for row in matrix], "K": 6}, 1)[0]},
                  flush=True)
        continue
    counts["false_costly"] += 1
    threshold_passed = True
    exact_cost = True
    for mask in range(1, 4):
        selected = {item[5][int(bool(mask & (1 << i)) != (item[1] == "P"))]
                    for i, item in enumerate(pair)}
        base_five = feasible(matrix_key(union | selected), 5)
        marker = matrix_key(union | selected | {(0, 0)})
        checker_six = feasible(marker, 6)
        if base_five or not checker_six:
            if first_positive_failure is None:
                first_positive_failure = (indices, mask, base_five, checker_six)
                print({"first_positive_failure": first_positive_failure,
                       "matrix": marker}, flush=True)
            threshold_passed = False
            break
        if feasible(marker, 5):
            exact_cost = False
            if first_discount is None:
                first_discount = (indices, mask)
                print({"first_active_discount": first_discount, "matrix": marker}, flush=True)
    if threshold_passed:
        counts["threshold_or"] += 1
    if threshold_passed and exact_cost:
        counts["exact_cost_or"] += 1
        if first_or is None:
            first_or = indices
            print({"first_exact_cost_or": indices, "placements": [item[:4] for item in pair],
                   "core_matrix": matrix_key(union)}, flush=True)
print({"final_counts": counts})
