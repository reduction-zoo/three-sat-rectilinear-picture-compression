"""Extend one additive three-core wire and check the exact port budget."""

from functools import lru_cache
from itertools import combinations
import sys
from pathlib import Path
import z3

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

core = {(2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
p, q = (4, 1), (2, 4)


def transform(point, reflect, turns):
    r, c = point
    if reflect:
        c = 4 - c
    for _ in range(turns):
        r, c = c, 4 - r
    return r, c


def attach(cells, endpoint, input_port, reflect, turns):
    anchor = transform(input_port, reflect, turns)
    dr, dc = endpoint[0] - anchor[0], endpoint[1] - anchor[1]
    moved = {(r + dr, c + dc) for r, c in (transform(point, reflect, turns) for point in core)}
    output = q if input_port == p else p
    other = transform(output, reflect, turns)
    return cells | moved | {endpoint}, moved, (other[0] + dr, other[1] + dc)


def matrix_key(cells):
    r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
    return tuple(tuple(int((r, c) in cells) for c in range(c0, max(c for _, c in cells) + 1))
                 for r in range(r0, max(r for r, _ in cells) + 1))


def antirectangle(matrix):
    cells = [(r, c) for r in range(len(matrix)) for c in range(len(matrix[0])) if matrix[r][c]]
    chosen = [z3.Bool(f"cell_{i}") for i in range(len(cells))]
    solver = z3.Optimize()
    for i, j in combinations(range(len(cells)), 2):
        r, c = cells[i]
        s, d = cells[j]
        if all(matrix[a][b] for a in range(min(r, s), max(r, s) + 1)
               for b in range(min(c, d), max(c, d) + 1)):
            solver.add(z3.Not(z3.And(chosen[i], chosen[j])))
    solver.maximize(z3.Sum([z3.If(v, 1, 0) for v in chosen]))
    assert solver.check() == z3.sat
    model = solver.model()
    return [cell for cell, var in zip(cells, chosen) if z3.is_true(model.eval(var))]


@lru_cache(None)
def feasible(matrix, budget):
    return target_solutions({"matrix": [list(row) for row in matrix], "K": budget}, 1) != [NO]


wire, second, outer_second = attach(core, p, p, True, 3)
assert not core & second
wire, third, outer_third = attach(wire, q, p, False, 0)
assert not (core | second) & third
ends = (outer_second, outer_third)
assert not feasible(matrix_key(wire), 5)
assert all(feasible(matrix_key(wire | {end}), 6) for end in ends)
assert not feasible(matrix_key(wire | set(ends)), 6)

tested = successes = 0
examples = []
for side in (0, 1):
    endpoint, far_end = ends[side], ends[1 - side]
    for input_port in (p, q):
        for reflect in (False, True):
            for turns in range(4):
                extended, moved, new_end = attach(wire, endpoint, input_port, reflect, turns)
                if wire & moved or new_end in extended or far_end in extended or new_end == far_end:
                    continue
                tested += 1
                matrix = matrix_key(extended)
                if (not feasible(matrix, 7) and feasible(matrix, 8)
                        and feasible(matrix_key(extended | {far_end}), 8)
                        and feasible(matrix_key(extended | {new_end}), 8)
                        and not feasible(matrix_key(extended | {far_end, new_end}), 8)):
                    successes += 1
                    if len(examples) < 3:
                        examples.append({"attach_side": side, "input_port": input_port,
                                         "reflect": reflect, "turns": turns,
                                         "endpoints": [far_end, new_end], "picture": matrix})
print({"three_core_endpoints": ends, "four_core_joins_tested": tested,
       "additive_exclusive_four_core_joins": successes, "examples": examples})

repeat_cells = wire
repeat_ends = ends
for count in (4, 5):
    previous = repeat_cells
    repeat_cells, moved, new_end = attach(previous, repeat_ends[0], p, True, 3)
    assert not previous & moved
    repeat_ends = (new_end, repeat_ends[1])
    budget = 2 * count
    result = {"cores": count, "matrix_shape": [len(matrix_key(repeat_cells)), len(matrix_key(repeat_cells)[0])],
              "budget_minus_one_feasible": feasible(matrix_key(repeat_cells), budget - 1),
              "budget_feasible": feasible(matrix_key(repeat_cells), budget),
              "end_a_feasible": feasible(matrix_key(repeat_cells | {repeat_ends[0]}), budget),
              "end_b_feasible": feasible(matrix_key(repeat_cells | {repeat_ends[1]}), budget),
              "both_ends_feasible": feasible(matrix_key(repeat_cells | set(repeat_ends)), budget)}
    print(result)
    print({"cores": count, "antirectangle": antirectangle(matrix_key(repeat_cells))})
    print({"cores": count, "both_end_antirectangle": antirectangle(matrix_key(repeat_cells | set(repeat_ends)))})
