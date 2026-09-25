"""Try a reserved 2x2 checker with three independently phased cores."""

from itertools import product, combinations
from functools import lru_cache
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

core = {(1, 3), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)}
p, q = (4, 2), (1, 4)
taps = (((0, 3), "P"), ((4, 3), "P"), ((3, 4), "Q"))
checker = {(0, 0), (0, 1), (1, 0), (1, 1)}
slots = ((0, 0), (0, 1), (1, 0))


def transform(point, reflect, turns):
    r, c = point
    if reflect:
        c = 4 - c
    for _ in range(turns):
        r, c = c, 4 - r
    return r, c


options = []
for slot in slots:
    placed = []
    for tap, polarity in taps:
        for reflect in (False, True):
            for turns in range(4):
                tr, tc = transform(tap, reflect, turns)
                move = lambda point: tuple(x + y - z for x, y, z in zip(transform(point, reflect, turns), slot, (tr, tc)))
                cells = {move(cell) for cell in core}
                if cells & checker:
                    continue
                state_ports = (move(p), move(q))
                if any(port in checker for port in state_ports):
                    continue
                placed.append((tap, polarity, reflect, turns, cells, state_ports))
    options.append(placed)

geometries = []
disjoint = clear_ports = 0
for triple in product(*options):
    parts = [item[4] for item in triple]
    if any(parts[i] & parts[j] for i, j in combinations(range(3), 2)):
        continue
    disjoint += 1
    union = set().union(*parts)
    ports = [port for item in triple for port in item[5]]
    if any(port in union for port in ports):
        continue
    clear_ports += 1
    if len(set(ports)) != 6:
        continue
    geometries.append((triple, union))

print({"per_slot_options": [len(item) for item in options], "disjoint": disjoint,
       "clear_ports": clear_ports, "distinct_port_geometries": len(geometries)})


def matrix_key(cells):
    r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
    return tuple(tuple(int((r, c) in cells) for c in range(c0, max(c for _, c in cells) + 1))
                 for r in range(r0, max(r for r, _ in cells) + 1))


@lru_cache(None)
def feasible(matrix, budget):
    return target_solutions({"matrix": [list(row) for row in matrix], "K": budget}, 1) != [NO]


counts = {"additive_core": 0, "additive_inactive": 0,
          "false_costly": 0, "exact_or": 0}
first_leak = None
first_positive_failure = None
for number, (triple, union) in enumerate(geometries, 1):
    if feasible(matrix_key(union), 8):
        continue
    counts["additive_core"] += 1
    inactive = {item[5][int(item[1] == "P")] for item in triple}
    if feasible(matrix_key(union | inactive), 8) or not feasible(matrix_key(union | inactive), 9):
        continue
    counts["additive_inactive"] += 1
    false_picture = union | inactive | checker
    if feasible(matrix_key(false_picture), 9):
        if first_leak is None:
            matrix = matrix_key(false_picture)
            first_leak = number
            print({"first_leak": number, "placement": [item[:4] for item in triple],
                   "matrix": matrix,
                   "witness": target_solutions({"matrix": [list(row) for row in matrix], "K": 9}, 1)[0]},
                  flush=True)
        continue
    counts["false_costly"] += 1
    passed = True
    for mask in range(1, 8):
        selected = {item[5][int(bool(mask & (1 << i)) != (item[1] == "P"))]
                    for i, item in enumerate(triple)}
        base_eight = feasible(matrix_key(union | selected), 8)
        checker_nine = feasible(matrix_key(union | selected | checker), 9)
        if base_eight or not checker_nine:
            if first_positive_failure is None:
                first_positive_failure = (number, mask)
                print({"first_positive_failure": first_positive_failure,
                       "placement": [item[:4] for item in triple],
                       "base_feasible_at_eight": base_eight,
                       "checker_feasible_at_nine": checker_nine,
                       "matrix": matrix_key(union | selected | checker)}, flush=True)
            print({"positive_failed": number, "mask": mask}, flush=True)
            passed = False
            break
    if passed:
        counts["exact_or"] += 1
        print({"exact_or": number, "placement": [item[:4] for item in triple]}, flush=True)
    if number % 64 == 0:
        print({"processed": number, "counts": counts}, flush=True)
print({"final_counts": counts})
