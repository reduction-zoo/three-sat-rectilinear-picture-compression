"""Recheck one exact-cost two-input edge gadget and expose its witnesses."""

from itertools import combinations
import sys
from pathlib import Path
import z3

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions, valid_target_witness

core = {(1, 3), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)}
upper = {(r, c - 3) for r, c in core}
lower = {(c - 3, r - 4) for r, c in core}
cores = upper | lower
active_ports = ((4, -1), (-1, 0))
inactive_ports = ((1, 1), (1, -3))


def target(cells, budget):
    r0, c0 = min(r for r, _ in cells), min(c for _, c in cells)
    matrix = [[int((r, c) in cells) for c in range(c0, max(c for _, c in cells) + 1)]
              for r in range(r0, max(r for r, _ in cells) + 1)]
    return {"matrix": matrix, "K": budget}, (r0, c0)


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
    answer = [point for point, var in zip(points, chosen) if z3.is_true(model.eval(var))]
    assert all(not all((a, b) in cells for a in range(min(r, s), max(r, s) + 1)
                       for b in range(min(c, d), max(c, d) + 1))
               for (r, c), (s, d) in combinations(answer, 2))
    return answer


for mask in range(4):
    ports = {active_ports[i] if mask & (1 << i) else inactive_ports[i] for i in range(2)}
    cells = cores | ports | {(0, 0)}
    instance, offset = target(cells, 6)
    witnesses = target_solutions(instance, 2)
    feasible = witnesses != [NO]
    assert feasible == (mask != 0)
    assert target_solutions(target(cells, 5)[0], 1) == [NO]
    if feasible:
        assert len(witnesses) == 2
        assert all(valid_target_witness(instance, witness) for witness in witnesses)
    else:
        seven_witness = target_solutions(target(cells, 7)[0], 1)[0]
        assert seven_witness != NO
    print({"active_mask": mask, "offset": offset, "matrix": instance["matrix"],
           "feasible_at_six": feasible, "witnesses": witnesses,
           "seven_witness": seven_witness if not feasible else None,
           "antirectangle": antirectangle(cells)}, flush=True)
