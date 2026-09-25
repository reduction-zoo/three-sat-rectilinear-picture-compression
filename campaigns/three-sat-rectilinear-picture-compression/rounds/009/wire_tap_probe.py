"""Check whether local literal taps remain selective inside a three-core wire."""

from functools import lru_cache
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

core = {(2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
p, q = (4, 1), (2, 4)
taps = ((3, 0), (3, 4))


def transform(point, reflect, turns):
    r, c = point
    if reflect:
        c = 4 - c
    for _ in range(turns):
        r, c = c, 4 - r
    return r, c


def moved_core(endpoint, input_port, reflect, turns):
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


second, move_second = moved_core(p, p, True, 3)
third, move_third = moved_core(q, p, False, 0)
wire = core | second | third | {p, q}
ends = (move_second(q), move_third(q))
assert not feasible(matrix_key(wire), 5)
assert all(feasible(matrix_key(wire | {end}), 6) for end in ends)
assert not feasible(matrix_key(wire | set(ends)), 6)

tested = free = selective = 0
results = []
for position, move in (("middle", lambda x: x), ("end_one", move_second), ("end_two", move_third)):
    for local in taps:
        tap = move(local)
        if tap in wire or tap in ends:
            continue
        tested += 1
        if not feasible(matrix_key(wire | {tap}), 6):
            continue
        free += 1
        with_ends = [feasible(matrix_key(wire | {tap, end}), 6) for end in ends]
        if with_ends[0] != with_ends[1]:
            selective += 1
        results.append({"core": position, "local_tap": local, "tap": tap,
                        "endpoint_compatibility": with_ends})
print({"wire_endpoints": ends, "candidate_taps": tested, "free_taps": free,
       "state_selective_taps": selective, "results": results})

long_wire = wire
far_left, far_right = ends
placements = [("middle", lambda x: x), ("end_one", move_second), ("end_two", move_third)]
for count in (4, 5):
    moved, move = moved_core(far_left, p, True, 3)
    assert not long_wire & moved
    long_wire |= moved | {far_left}
    far_left = move(q)
    placements.append((f"extension_{count}", move))
long_ends = (far_left, far_right)
assert not feasible(matrix_key(long_wire), 9)
assert all(feasible(matrix_key(long_wire | {end}), 10) for end in long_ends)
assert not feasible(matrix_key(long_wire | set(long_ends)), 10)

long_results = []
for position, move in placements:
    for local in taps:
        tap = move(local)
        if tap in long_wire or tap in long_ends:
            continue
        if not feasible(matrix_key(long_wire | {tap}), 10):
            continue
        with_ends = [feasible(matrix_key(long_wire | {tap, end}), 10) for end in long_ends]
        long_results.append({"core": position, "local_tap": local,
                             "endpoint_compatibility": with_ends})
print({"five_core_endpoints": long_ends, "free_taps": len(long_results),
       "state_selective_taps": sum(x["endpoint_compatibility"][0] != x["endpoint_compatibility"][1]
                                   for x in long_results), "results": long_results})
