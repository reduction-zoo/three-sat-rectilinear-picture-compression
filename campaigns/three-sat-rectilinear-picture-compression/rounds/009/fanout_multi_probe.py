"""Check simultaneous literal taps on one explicit four-core wire."""

from functools import lru_cache
from itertools import combinations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

core = {(1, 3), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)}
p, q, local_tap = (4, 2), (1, 4), (3, 4)


def transform(point, reflect, turns):
    r, c = point
    if reflect:
        c = 4 - c
    for _ in range(turns):
        r, c = c, 4 - r
    return r, c


def placed(endpoint, input_port, reflect, turns):
    anchor = transform(input_port, reflect, turns)
    dr, dc = endpoint[0] - anchor[0], endpoint[1] - anchor[1]
    move = lambda point: (transform(point, reflect, turns)[0] + dr,
                          transform(point, reflect, turns)[1] + dc)
    return {move(cell) for cell in core}, move


def matrix_key(cells):
    r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
    return tuple(tuple(int((r, c) in cells) for c in range(c0, max(c for _, c in cells) + 1))
                 for r in range(r0, max(r for r, _ in cells) + 1))


@lru_cache(None)
def feasible(matrix, budget):
    return target_solutions({"matrix": [list(row) for row in matrix], "K": budget}, 1) != [NO]


second, move_second = placed(p, p, True, 3)
third, move_third = placed(q, p, False, 0)
end_second = move_second(q)
fourth, move_fourth = placed(end_second, p, True, 3)
wire = core | second | third | fourth | {p, q, end_second}
ends = (move_third(q), move_fourth(q))
assert not feasible(matrix_key(wire), 11)
assert feasible(matrix_key(wire), 12)
assert all(feasible(matrix_key(wire | {end}), 12) for end in ends)
assert not feasible(matrix_key(wire | set(ends)), 12)

tap_results = []
for name, move in (("first", lambda x: x), ("second", move_second),
                   ("third", move_third), ("fourth", move_fourth)):
    tap = move(local_tap)
    if tap in wire or tap in ends:
        continue
    free = feasible(matrix_key(wire | {tap}), 12)
    compatible = [feasible(matrix_key(wire | {tap, end}), 12) for end in ends] if free else [False, False]
    tap_results.append({"core": name, "tap": tap, "free": free,
                        "endpoint_compatibility": compatible})
    print(tap_results[-1], flush=True)

joint_results = []
for left, right in combinations(tap_results, 2):
    if not left["free"] or not right["free"]:
        continue
    cells = wire | {left["tap"], right["tap"]}
    both_free = feasible(matrix_key(cells), 12)
    compatible_end = next((end for i, end in enumerate(ends)
                           if left["endpoint_compatibility"][i]
                           and right["endpoint_compatibility"][i]), None)
    joint_results.append({"cores": [left["core"], right["core"]],
                          "both_taps_free": both_free,
                          "with_compatible_endpoint":
                          feasible(matrix_key(cells | {compatible_end}), 12)
                          if both_free and compatible_end is not None else None})
    print(joint_results[-1], flush=True)
print({"endpoints": ends, "tap_results": tap_results, "joint_results": joint_results})
