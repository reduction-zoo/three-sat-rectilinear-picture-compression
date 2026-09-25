"""Check the row/column-run matching formula on every thin 3x3 picture."""

from itertools import product
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions


def run_graph(matrix):
    rows, cols = len(matrix), len(matrix[0]) if matrix else 0
    horizontal = {}
    vertical = {}
    h_count = v_count = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c]:
                if c == 0 or not matrix[r][c - 1]:
                    h_count += 1
                horizontal[r, c] = h_count - 1
    for c in range(cols):
        for r in range(rows):
            if matrix[r][c]:
                if r == 0 or not matrix[r - 1][c]:
                    v_count += 1
                vertical[r, c] = v_count - 1
    adjacency = [set() for _ in range(h_count)]
    for cell, h in horizontal.items():
        adjacency[h].add(vertical[cell])
    return adjacency, v_count


def max_matching(adjacency, v_count):
    mate = [-1] * v_count

    def augment(h, seen):
        for v in adjacency[h]:
            if v in seen:
                continue
            seen.add(v)
            if mate[v] == -1 or augment(mate[v], seen):
                mate[v] = h
                return True
        return False

    return sum(augment(h, set()) for h in range(len(adjacency)))


checked = 0
for bits in product((0, 1), repeat=9):
    matrix = [list(bits[r * 3:(r + 1) * 3]) for r in range(3)]
    if any(all(matrix[r + dr][c + dc] for dr in (0, 1) for dc in (0, 1))
           for r in range(2) for c in range(2)):
        continue
    adjacency, v_count = run_graph(matrix)
    optimum = max_matching(adjacency, v_count)
    assert target_solutions({"matrix": matrix, "K": optimum}, 1) != [NO]
    if optimum:
        assert target_solutions({"matrix": matrix, "K": optimum - 1}, 1) == [NO]
    checked += 1
print(f"matching formula agreed with exact rectangle cover on {checked} thin 3x3 pictures")
