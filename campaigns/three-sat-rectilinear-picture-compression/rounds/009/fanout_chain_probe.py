"""Extend a three-core wire while retaining an internal literal tap."""

from functools import lru_cache
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

core = {(1, 3), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)}
p, q = (4, 2), (1, 4)
middle_tap = (3, 4)
k = 3


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
    return {move(cell) for cell in core}, move(q if input_port == p else p), move


def matrix_key(cells):
    r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
    return tuple(tuple(int((r, c) in cells) for c in range(c0, max(c for _, c in cells) + 1))
                 for r in range(r0, max(r for r, _ in cells) + 1))


@lru_cache(None)
def feasible(matrix, budget):
    return target_solutions({"matrix": [list(row) for row in matrix], "K": budget}, 1) != [NO]


second, end_second, move_second = placed(p, p, True, 3)
third, end_third, move_third = placed(q, p, False, 0)
wire = core | second | third | {p, q}
ends = (end_second, end_third)
assert not feasible(matrix_key(wire), 8)
assert feasible(matrix_key(wire), 9)
assert all(feasible(matrix_key(wire | {end}), 9) for end in ends)
assert not feasible(matrix_key(wire | set(ends)), 9)
assert feasible(matrix_key(wire | {middle_tap}), 9)
initial_tap_ends = [feasible(matrix_key(wire | {middle_tap, end}), 9) for end in ends]
assert initial_tap_ends == [False, True]

tested = additive_wires = taps_surviving = 0
first = None
for side in (0, 1):
    endpoint, far_end = ends[side], ends[1 - side]
    for input_port in (p, q):
        for reflect in (False, True):
            for turns in range(4):
                moved, new_end, move = placed(endpoint, input_port, reflect, turns)
                extended = wire | moved | {endpoint}
                if wire & moved or new_end in extended or far_end in extended or new_end == far_end:
                    continue
                tested += 1
                if (feasible(matrix_key(extended), 11)
                        or not feasible(matrix_key(extended), 12)
                        or not all(feasible(matrix_key(extended | {end}), 12) for end in (far_end, new_end))
                        or feasible(matrix_key(extended | {far_end, new_end}), 12)):
                    continue
                additive_wires += 1
                if not feasible(matrix_key(extended | {middle_tap}), 12):
                    continue
                with_ends = [feasible(matrix_key(extended | {middle_tap, end}), 12)
                             for end in (far_end, new_end)]
                if with_ends[0] != with_ends[1]:
                    taps_surviving += 1
                    if first is None:
                        first = {"side": side, "input_port": input_port,
                                 "reflect": reflect, "turns": turns,
                                 "endpoints": [far_end, new_end],
                                 "tap_compatibility": with_ends,
                                 "picture": matrix_key(extended)}
print({"three_core_tap_compatibility": initial_tap_ends,
       "disjoint_four_core_joins": tested, "additive_exclusive_wires": additive_wires,
       "middle_taps_surviving": taps_surviving, "first": first})
