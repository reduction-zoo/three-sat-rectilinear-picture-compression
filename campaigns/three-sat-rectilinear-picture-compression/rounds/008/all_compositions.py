"""Check every exclusive 3x3 core pair under two-copy dihedral joins."""

from functools import lru_cache
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from port_probe import search_candidates
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions


def transform(p, reflect, turns):
    r, c = p
    if reflect:
        c = 4 - c
    for _ in range(turns):
        r, c = c, 4 - r
    return r, c


def matrix_key(cells):
    r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
    h = max(r for r, _ in cells) - r0 + 1
    w = max(c for _, c in cells) - c0 + 1
    return tuple(tuple(int((r + r0, c + c0) in cells) for c in range(w)) for r in range(h))


@lru_cache(None)
def optimum(matrix):
    target = {"matrix": [list(row) for row in matrix]}
    for k in range(1, sum(sum(row) for row in matrix) + 1):
        if target_solutions({**target, "K": k}, 1) != [NO]:
            return k
    raise AssertionError("every picture has a singleton-cell cover")


@lru_cache(None)
def feasible_at(matrix, budget):
    return target_solutions({"matrix": [list(row) for row in matrix], "K": budget}, 1) != [NO]


candidates, _, _, _ = search_candidates()
tested = successes = disjoint_successes = third_tested = additive_third_successes = 0
first = None
first_triple = None
for bits, core_k, p, q in candidates:
    core = {(r + 1, c + 1) for r in range(3) for c in range(3) if bits[r * 3 + c]}
    for reflect in (False, True):
        for turns in range(4):
            moved_core = {transform(cell, reflect, turns) for cell in core}
            for input_port, output_port, outer_a in ((p, q, q), (q, p, p)):
                anchor = transform(input_port, reflect, turns)
                dr, dc = input_port[0] - anchor[0], input_port[1] - anchor[1]
                moved = {(r + dr, c + dc) for r, c in moved_core}
                other = transform(output_port, reflect, turns)
                outer_b = (other[0] + dr, other[1] + dc)
                joined = core | moved | {input_port}
                if outer_a in joined or outer_b in joined or outer_a == outer_b:
                    continue
                tested += 1
                base = optimum(matrix_key(joined))
                a = optimum(matrix_key(joined | {outer_a}))
                b = optimum(matrix_key(joined | {outer_b}))
                both = optimum(matrix_key(joined | {outer_a, outer_b}))
                if a == b == base and both > base:
                    successes += 1
                    disjoint_successes += not bool(core & moved)
                    if first is None:
                        first = {"core": [bits[r * 3:(r + 1) * 3] for r in range(3)],
                                 "core_budget": core_k, "ports": [p, q],
                                 "reflect": reflect, "turns": turns, "input_port": input_port,
                                 "outer_ports": [outer_a, outer_b],
                                 "core_overlap": len(core & moved),
                                 "joined_picture": matrix_key(joined),
                                 "costs": [base, a, b, both]}
                    if core & moved or base != 2 * core_k:
                        continue
                    for endpoint, far_port in ((outer_a, outer_b), (outer_b, outer_a)):
                        for third_input, third_output in ((p, q), (q, p)):
                            for third_reflect in (False, True):
                                for third_turns in range(4):
                                    third_anchor = transform(third_input, third_reflect, third_turns)
                                    er, ec = endpoint[0] - third_anchor[0], endpoint[1] - third_anchor[1]
                                    third_core = {(r + er, c + ec) for r, c in
                                                  (transform(cell, third_reflect, third_turns) for cell in core)}
                                    third_other = transform(third_output, third_reflect, third_turns)
                                    new_port = (third_other[0] + er, third_other[1] + ec)
                                    extended = joined | third_core | {endpoint}
                                    if joined & third_core or new_port in extended or far_port in extended or new_port == far_port:
                                        continue
                                    third_tested += 1
                                    expected = base + core_k
                                    if feasible_at(matrix_key(extended), expected - 1):
                                        continue
                                    if (feasible_at(matrix_key(extended), expected)
                                            and feasible_at(matrix_key(extended | {far_port}), expected)
                                            and feasible_at(matrix_key(extended | {new_port}), expected)
                                            and not feasible_at(matrix_key(extended | {far_port, new_port}), expected)):
                                        additive_third_successes += 1
                                        if first_triple is None:
                                            first_triple = {"core": [bits[r * 3:(r + 1) * 3] for r in range(3)],
                                                            "core_budget": core_k, "ports": [p, q],
                                                            "first_join": [reflect, turns, input_port],
                                                            "third_join": [third_reflect, third_turns, third_input],
                                                            "outer_ports": [far_port, new_port],
                                                            "picture": matrix_key(extended),
                                                            "budgets": [base, expected]}
print({"exclusive_core_port_pairs": len(candidates), "nondegenerate_joins": tested,
       "exclusive_outer_port_joins": successes, "disjoint_core_successes": disjoint_successes,
       "third_disjoint_joins_tested": third_tested,
       "additive_three_core_successes": additive_third_successes,
       "first_success": first, "first_triple": first_triple})
