"""Inspect lower-bound certificates in a repeated thick wire."""

from itertools import combinations
import sys
from pathlib import Path
import z3

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import valid_target_witness

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
    tr, tc = transform(input_port, reflect, turns)
    dr, dc = endpoint[0] - tr, endpoint[1] - tc
    moved = {(r + dr, c + dc) for r, c in (transform(cell, reflect, turns) for cell in core)}
    assert not cells & moved
    output = q if input_port == p else p
    orow, ocol = transform(output, reflect, turns)
    return cells | moved | {endpoint}, (orow + dr, ocol + dc), (dr, dc)


def antirectangle(cells):
    points = sorted(cells)
    chosen = [z3.Bool(f"cell_{i}") for i in range(len(points))]
    solver = z3.Optimize()
    for i, j in combinations(range(len(points)), 2):
        r, c = points[i]
        s, d = points[j]
        if all((a, b) in cells for a in range(min(r, s), max(r, s) + 1)
               for b in range(min(c, d), max(c, d) + 1)):
            solver.add(z3.Not(z3.And(chosen[i], chosen[j])))
    solver.maximize(z3.Sum([z3.If(var, 1, 0) for var in chosen]))
    assert solver.check() == z3.sat
    model = solver.model()
    return [point for point, var in zip(points, chosen) if z3.is_true(model.eval(var))]


def valid_antirectangle(cells, points):
    return all(point in cells for point in points) and all(
        not all((a, b) in cells for a in range(min(r, s), max(r, s) + 1)
                for b in range(min(c, d), max(c, d) + 1))
        for (r, c), (s, d) in combinations(points, 2))


def consecutive_zero_witnesses(cells, points):
    result = []
    for (r, c), (s, d) in zip(points, points[1:]):
        assert r < s and c > d
        missing = next((a, b) for a in range(r, s + 1) for b in range(d, c + 1)
                       if (a, b) not in cells)
        result.append(missing)
    return result


def check_upper_covers(cells, left, right, t):
    local = {"p": [(2, 3, 2, 3), (3, 4, 1, 1)],
             "q": [(2, 2, 2, 4), (3, 3, 1, 3)]}
    copies = [(False, (-2, 3), "right_end"), (False, (0, 0), "middle"),
              (True, (3, -3), "tail")]
    copies += [(True, (3 * k - 6, -2 * k + 3), "tail") for k in range(4, t + 1)]
    ports_by_mode = {"base": {"right_end": "p", "middle": "q", "tail": "p"},
                     "right": {"right_end": "q", "middle": "q", "tail": "p"},
                     "left": {"right_end": "p", "middle": "p", "tail": "q"}}
    for mode, picture in (("base", cells), ("right", cells | {right}),
                          ("left", cells | {left})):
        rmin, cmin = min(r for r, _ in picture), min(c for _, c in picture)
        matrix = [[int((r, c) in picture)
                   for c in range(cmin, max(c for _, c in picture) + 1)]
                  for r in range(rmin, max(r for r, _ in picture) + 1)]
        rectangles = []
        for transpose, (dr, dc), role in copies:
            port = ports_by_mode[mode][role]
            for r0, r1, c0, c1 in local[port]:
                corners = [(r0, c0), (r0, c1), (r1, c0), (r1, c1)]
                moved = [(c + dr, r + dc) if transpose else (r + dr, c + dc)
                         for r, c in corners]
                rectangles.append([min(r for r, _ in moved) - rmin,
                                   max(r for r, _ in moved) - rmin,
                                   min(c for _, c in moved) - cmin,
                                   max(c for _, c in moved) - cmin])
        assert valid_target_witness({"matrix": matrix, "K": 2 * t}, rectangles), (t, mode)


wire, left, move_second = attach(core, p, p, True, 3)
wire, right, move_third = attach(wire, q, p, False, 0)
nested_base = [(0, 6), (1, 4), (2, 2), (3, 1), (4, 0), (5, -1)]
nested_both = [(0, 7), (1, 5), (2, 4), (3, 2), (4, 1), (6, 0), (7, -1)]
for t in range(3, 7):
    if t > 3:
        nested_base += [(3 * t - 5, -2 * t + 6), (3 * t - 4, -2 * t + 5)]
        nested_both += [(3 * t - 4, -2 * t + 6), (3 * t - 2, -2 * t + 5)]
    base = antirectangle(wire)
    both = antirectangle(wire | {left, right})
    check_upper_covers(wire, left, right, t)
    print({"cores": t, "left_endpoint": left, "right_endpoint": right,
           "base_size": len(base), "base_points": base,
           "both_size": len(both), "both_points": both,
           "nested_base_valid": valid_antirectangle(wire, nested_base),
           "nested_both_valid": valid_antirectangle(wire | {left, right}, nested_both)}, flush=True)
    if t == 6:
        print({"base_adjacent_zeros": consecutive_zero_witnesses(wire, nested_base),
               "both_adjacent_zeros": consecutive_zero_witnesses(wire | {left, right}, nested_both)}, flush=True)
    if t < 6:
        wire, left, displacement = attach(wire, left, p, True, 3)
        print({"next_core_displacement": displacement}, flush=True)

for t in range(7, 21):
    wire, left, _ = attach(wire, left, p, True, 3)
    nested_base += [(3 * t - 5, -2 * t + 6), (3 * t - 4, -2 * t + 5)]
    nested_both += [(3 * t - 4, -2 * t + 6), (3 * t - 2, -2 * t + 5)]
    assert valid_antirectangle(wire, nested_base)
    assert valid_antirectangle(wire | {left, right}, nested_both)
    check_upper_covers(wire, left, right, t)
print({"nested_certificates_checked_through": 20, "base_size": len(nested_base),
       "both_size": len(nested_both), "upper_covers_checked": 54})
