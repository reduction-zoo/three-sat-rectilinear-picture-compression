"""Try a thicker core with both-polarity taps in a three-core wire."""

from functools import lru_cache
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "008"))
from port_probe import ports
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

representatives = [
    ([[0, 0, 1], [0, 1, 1], [1, 1, 1]], 3, (4, 1), (2, 4)),
    ([[0, 0, 1], [0, 1, 1], [1, 1, 1]], 3, (4, 2), (2, 4)),
    ([[0, 0, 1], [1, 1, 1], [0, 1, 1]], 3, (4, 2), (1, 4)),
    ([[1, 0, 1], [0, 1, 1], [1, 1, 1]], 4, (4, 1), (2, 4)),
    ([[1, 0, 1], [0, 1, 1], [1, 1, 1]], 4, (4, 2), (2, 4)),
    ([[1, 0, 1], [1, 1, 1], [1, 1, 1]], 3, (4, 2), (1, 0)),
]
index = int(sys.argv[1]) if len(sys.argv) > 1 else 0
rows, k, p, q = representatives[index]
core = {(r + 1, c + 1) for r in range(3) for c in range(3) if rows[r][c]}


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
    other = q if input_port == p else p
    return {move(cell) for cell in core}, move(other)


def matrix_key(cells):
    r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
    return tuple(tuple(int((r, c) in cells) for c in range(c0, max(c for _, c in cells) + 1))
                 for r in range(r0, max(r for r, _ in cells) + 1))


@lru_cache(None)
def feasible(matrix, budget):
    return target_solutions({"matrix": [list(row) for row in matrix], "K": budget}, 1) != [NO]


local_taps = []
for tap in ports:
    if tap in (p, q) or not feasible(matrix_key(core | {tap}), k):
        continue
    with_p = feasible(matrix_key(core | {p, tap}), k)
    with_q = feasible(matrix_key(core | {q, tap}), k)
    if with_p != with_q:
        local_taps.append((tap, "P" if with_p else "Q"))
assert {state for _, state in local_taps} == {"P", "Q"}

two_joins = triples = surviving_taps = 0
first = None
for input_two in (p, q):
    for ref_two in (False, True):
        for turn_two in range(4):
            second, end_two = placed(p, input_two, ref_two, turn_two)
            if core & second:
                continue
            pair = core | second | {p}
            if q in pair or end_two in pair or q == end_two:
                continue
            if (feasible(matrix_key(pair), 2 * k - 1)
                    or not all(feasible(matrix_key(pair | {end}), 2 * k) for end in (q, end_two))
                    or feasible(matrix_key(pair | {q, end_two}), 2 * k)):
                continue
            two_joins += 1
            for input_three in (p, q):
                for ref_three in (False, True):
                    for turn_three in range(4):
                        third, end_three = placed(q, input_three, ref_three, turn_three)
                        if pair & third:
                            continue
                        wire = pair | third | {q}
                        ends = (end_two, end_three)
                        if (end_two in wire or end_three in wire or end_two == end_three
                                or feasible(matrix_key(wire), 3 * k - 1)
                                or not all(feasible(matrix_key(wire | {end}), 3 * k) for end in ends)
                                or feasible(matrix_key(wire | set(ends)), 3 * k)):
                            continue
                        triples += 1
                        for tap, polarity in local_taps:
                            if tap in wire or tap in ends or not feasible(matrix_key(wire | {tap}), 3 * k):
                                continue
                            with_ends = [feasible(matrix_key(wire | {tap, end}), 3 * k) for end in ends]
                            if with_ends[0] != with_ends[1]:
                                surviving_taps += 1
                                if first is None:
                                    first = {"local_tap": tap, "polarity": polarity,
                                             "two_join": [input_two, ref_two, turn_two],
                                             "third_join": [input_three, ref_three, turn_three],
                                             "wire_endpoints": ends, "compatibility": with_ends,
                                             "picture": matrix_key(wire)}
print({"orbit": index, "core": rows, "ports": [p, q], "local_taps": local_taps, "additive_two_joins": two_joins,
       "additive_three_core_wires": triples, "surviving_selective_taps": surviving_taps,
       "first": first})
