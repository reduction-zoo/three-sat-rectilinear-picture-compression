"""Test whether a successful two-core exclusive-port join extends to three cores."""

from functools import lru_cache
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

core = {(2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
ports = ((4, 1), (3, 0))


def transform(p, reflect, turns):
    r, c = p
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
def optimum(matrix):
    for k in range(1, sum(map(sum, matrix)) + 1):
        if target_solutions({"matrix": [list(row) for row in matrix], "K": k}, 1) != [NO]:
            return k
    raise AssertionError


def attachment(cells, endpoint, input_port, reflect, turns):
    anchor = transform(input_port, reflect, turns)
    dr, dc = endpoint[0] - anchor[0], endpoint[1] - anchor[1]
    moved = {(r + dr, c + dc) for r, c in (transform(p, reflect, turns) for p in core)}
    other = transform(ports[1] if input_port == ports[0] else ports[0], reflect, turns)
    new_port = (other[0] + dr, other[1] + dc)
    return moved, new_port, cells | moved | {endpoint}


first_moved, first_outer, joined = attachment(core, ports[1], ports[1], True, 1)
assert not core & first_moved
outer = (ports[0], first_outer)
assert [optimum(matrix_key(joined | {p})) for p in outer] == [4, 4]
assert optimum(matrix_key(joined | set(outer))) == 5

tested = exclusive = additive_exclusive = 0
examples = []
for side in (0, 1):
    endpoint, far_port = outer[side], outer[1 - side]
    for input_port in ports:
        for reflect in (False, True):
            for turns in range(4):
                moved, new_port, extended = attachment(joined, endpoint, input_port, reflect, turns)
                if joined & moved or new_port in extended or far_port in extended or new_port == far_port:
                    continue
                tested += 1
                base = optimum(matrix_key(extended))
                a = optimum(matrix_key(extended | {far_port}))
                b = optimum(matrix_key(extended | {new_port}))
                both = optimum(matrix_key(extended | {far_port, new_port}))
                if a == b == base and both > base:
                    exclusive += 1
                    if len(examples) < 5:
                        examples.append({"attach_side": side, "input_port": input_port,
                                         "reflect": reflect, "turns": turns,
                                         "outer_ports": [far_port, new_port], "costs": [base, a, b, both],
                                         "picture": matrix_key(extended)})
                if [base, a, b, both] == [6, 6, 6, 7]:
                    additive_exclusive += 1
print({"two_core_cost": optimum(matrix_key(joined)), "disjoint_three_core_joins": tested,
       "exclusive_joins": exclusive, "additive_exclusive_joins": additive_exclusive, "examples": examples})
