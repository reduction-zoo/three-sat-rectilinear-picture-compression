"""Compare independent color and rectangle-cover models on every 3x3 picture."""

from itertools import product
import sys
from pathlib import Path

import z3

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions


def colorable(matrix, budget):
    ones = [(r, c) for r in range(3) for c in range(3) if matrix[r][c]]
    if not ones:
        return True
    if budget == 0:
        return False
    colors = [z3.Int(f"c{i}") for i in range(len(ones))]
    solver = z3.Solver()
    for color in colors:
        solver.add(color >= 0, color < budget)
    for i, (r, c) in enumerate(ones):
        for j in range(i):
            s, d = ones[j]
            if any(matrix[a][b] == 0 for a in range(min(r, s), max(r, s) + 1)
                   for b in range(min(c, d), max(c, d) + 1)):
                solver.add(colors[i] != colors[j])
    result = solver.check()
    assert result in (z3.sat, z3.unsat)
    return result == z3.sat


count = 0
for bits in product((0, 1), repeat=9):
    matrix = [list(bits[r * 3:(r + 1) * 3]) for r in range(3)]
    for budget in range(4):
        assert colorable(matrix, budget) == (target_solutions({"matrix": matrix, "K": budget}, 1) != [NO])
        count += 1
print(f"matched {count} picture/budget pairs")
