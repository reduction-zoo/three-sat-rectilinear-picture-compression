"""Test a two-cell clause marker against all three input states."""

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


orientations = []
for tap, polarity in taps:
    for reflect in (False, True):
        for turns in range(4):
            tr, tc = transform(tap, reflect, turns)
            move = lambda point: tuple(x - y for x, y in zip(transform(point, reflect, turns), (tr, tc)))
            orientations.append((polarity, {move(cell) for cell in core}, move(p), move(q)))

eligible = guarded = false_costly = exact_or = 0
first_leak = None
for indices in combinations(range(24), 3):
    triple = [orientations[index] for index in indices]
    parts = [item[1] for item in triple]
    if any(parts[i] & parts[j] for i, j in combinations(range(3), 2)):
        continue
    union = set().union(*parts)
    ports = [(item[2], item[3]) for item in triple]
    flat_ports = [point for pair in ports for point in pair]
    if ((0, 0) in union or any(point in union or point == (0, 0) for point in flat_ports)
            or len(set(flat_ports)) != 6):
        continue
    inactive = {ports[i][int(triple[i][0] == "P")] for i in range(3)}
    if feasible(matrix_key(union | inactive), 8) or not feasible(matrix_key(union | inactive), 9):
        continue
    eligible += 1
    for guard in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        if guard in union or guard in flat_ports:
            continue
        guarded += 1
        marker = {(0, 0), guard}
        false_picture = union | inactive | marker
        if feasible(matrix_key(false_picture), 9):
            if first_leak is None:
                matrix = matrix_key(false_picture)
                first_leak = (indices, guard)
                print({"first_leak": first_leak, "matrix": matrix,
                       "witness": target_solutions({"matrix": [list(row) for row in matrix], "K": 9}, 1)[0]},
                      flush=True)
            continue
        false_costly += 1
        passed = True
        for mask in range(1, 8):
            selected = {ports[i][int(bool(mask & (1 << i)) != (triple[i][0] == "P"))]
                        for i in range(3)}
            if (feasible(matrix_key(union | selected), 8)
                    or not feasible(matrix_key(union | selected | marker), 9)):
                passed = False
                print({"false_costly_but_positive_failed": indices, "guard": guard, "mask": mask},
                      flush=True)
                break
        if passed:
            exact_or += 1
            print({"exact_or": indices, "guard": guard}, flush=True)
print({"eligible_placements": eligible, "guarded_placements": guarded,
       "false_costly": false_costly, "exact_or": exact_or})
