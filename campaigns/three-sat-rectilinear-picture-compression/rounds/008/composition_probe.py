"""Join two exclusive-port cores at a shared cell and test outer ports."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

core = {(2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
left_port = (3, 0)
down_port = (4, 1)
offset = (1, 1)
shift = lambda p: (p[0] + offset[0], p[1] + offset[1])
assert down_port == shift(left_port)
joined = core | {shift(p) for p in core} | {down_port}
outer_a = left_port
outer_b = shift(down_port)


def target(cells, budget):
    r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
    h = max(r for r, _ in cells) - r0 + 1
    w = max(c for _, c in cells) - c0 + 1
    return {"matrix": [[int((r + r0, c + c0) in cells) for c in range(w)] for r in range(h)], "K": budget}


def optimum(cells):
    return next(k for k in range(1, len(cells) + 1) if target_solutions(target(cells, k), 1) != [NO])


values = {"joined": optimum(joined), "outer_a": optimum(joined | {outer_a}),
          "outer_b": optimum(joined | {outer_b}),
          "both_outer": optimum(joined | {outer_a, outer_b})}
print({"joined_picture": target(joined, 0)["matrix"], "outer_ports": [outer_a, outer_b],
       "minimum_covers": values,
       "baseline_witness": target_solutions(target(joined, values["joined"]), 1)[0]})


def transform(p, reflect, turns):
    r, c = p
    if reflect:
        c = 4 - c
    for _ in range(turns):
        r, c = c, 4 - r
    return r, c


tested = successes = 0
first_success = None
for reflect in (False, True):
    for turns in range(4):
        transformed = {transform(p, reflect, turns) for p in core}
        for input_port, output_port in ((left_port, down_port), (down_port, left_port)):
            anchor = transform(input_port, reflect, turns)
            dr, dc = down_port[0] - anchor[0], down_port[1] - anchor[1]
            moved = {(r + dr, c + dc) for r, c in transformed}
            other = transform(output_port, reflect, turns)
            outer_b = (other[0] + dr, other[1] + dc)
            joined = core | moved | {down_port}
            if left_port in joined or outer_b in joined or left_port == outer_b:
                continue
            tested += 1
            k = optimum(joined)
            a = optimum(joined | {left_port})
            b = optimum(joined | {outer_b})
            both = optimum(joined | {left_port, outer_b})
            if a == b == k and both > k:
                successes += 1
                if first_success is None:
                    first_success = {"reflect": reflect, "turns": turns, "input_port": input_port,
                                     "overlap_cells": len(core & moved), "joined": target(joined, k)["matrix"],
                                     "outer_ports": [left_port, outer_b], "costs": [k, a, b, both]}
print({"oriented_joins_tested": tested, "exclusive_outer_port_joins": successes,
       "first_success": first_success})
