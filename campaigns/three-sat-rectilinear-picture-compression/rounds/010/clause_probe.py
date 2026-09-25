"""Search a three-core, shared-cell clause junction."""

from itertools import combinations
from functools import lru_cache
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


orientations = []
for tap, polarity in taps:
    for reflect in (False, True):
        for turns in range(4):
            tr, tc = transform(tap, reflect, turns)
            move = lambda point: tuple(x - y for x, y in zip(transform(point, reflect, turns), (tr, tc)))
            orientations.append((tap, polarity, reflect, turns,
                                 {move(cell) for cell in core}, move(p), move(q)))

geometries = []
disjoint = 0
port_clear = 0
for indices in combinations(range(len(orientations)), 3):
    triple = [orientations[index] for index in indices]
    cells = [item[4] for item in triple]
    if any(cells[i] & cells[j] for i, j in combinations(range(3), 2)):
        continue
    disjoint += 1
    union = set().union(*cells)
    ports = [point for item in triple for point in item[5:7]]
    if (0, 0) in union or any(point in union or point == (0, 0) for point in ports):
        continue
    port_clear += 1
    if len(set(ports)) != 6:
        continue
    geometries.append((indices, union, tuple((item[5], item[6]) for item in triple)))

print({"disjoint": disjoint, "port_clear": port_clear, "dihedral_placements": len(geometries),
       "orientations": [indices for indices, _, _ in geometries]})


def matrix_key(cells):
    r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
    return tuple(tuple(int((r, c) in cells) for c in range(c0, max(c for _, c in cells) + 1))
                 for r in range(r0, max(r for r, _ in cells) + 1))


@lru_cache(None)
def feasible(matrix, budget):
    return target_solutions({"matrix": [list(row) for row in matrix], "K": budget}, 1) != [NO]


counts = {"core_additive": 0, "inactive_baseline_additive": 0,
          "inactive_clause_costly": 0, "exact_or": 0}
first_leak = None
for indices, union, ports in geometries:
    if feasible(matrix_key(union), 8):
        continue
    counts["core_additive"] += 1
    triple = [orientations[index] for index in indices]
    inactive = {ports[i][int(triple[i][1] == "P")] for i in range(3)}
    if feasible(matrix_key(union | inactive), 8) or not feasible(matrix_key(union | inactive), 9):
        continue
    counts["inactive_baseline_additive"] += 1
    if feasible(matrix_key(union | inactive | {(0, 0)}), 9):
        if first_leak is None:
            matrix = matrix_key(union | inactive | {(0, 0)})
            first_leak = indices
            print({"inactive_clause_leak": indices, "matrix": matrix,
                   "witness": target_solutions({"matrix": [list(row) for row in matrix], "K": 9}, 1)[0]},
                  flush=True)
        continue
    counts["inactive_clause_costly"] += 1
    all_patterns = True
    for mask in range(1, 8):
        selected = {ports[i][int(bool(mask & (1 << i)) != (triple[i][1] == "P"))]
                    for i in range(3)}
        if (feasible(matrix_key(union | selected), 8)
                or not feasible(matrix_key(union | selected | {(0, 0)}), 9)):
            all_patterns = False
            print({"failed_positive": indices, "mask": mask}, flush=True)
            break
    if all_patterns:
        counts["exact_or"] += 1
        print({"exact_or": indices, "matrix": matrix_key(union | inactive)}, flush=True)
    print({"checked": indices, "counts": counts}, flush=True)
print({"final_counts": counts})
