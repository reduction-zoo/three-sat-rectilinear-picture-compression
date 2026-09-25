"""Exact rectangle-cover DP for pictures in a fixed-width diagonal band."""

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions


def min_cover(matrix, a, b, low, width):
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    assert a > 0 and b > 0 and width >= 0
    assert all(low <= a * r + b * c <= low + width
               for r in range(rows) for c in range(cols) if matrix[r][c])
    height = width // a + 1
    states = {0: 0}
    for top in range(rows):
        top_cols = [c for c in range(cols) if matrix[top][c]]
        rectangles = []
        for bottom in range(top, min(rows, top + height)):
            for i, left in enumerate(top_cols):
                for right in top_cols[i:]:
                    if all(matrix[r][c] for r in range(top, bottom + 1)
                           for c in range(left, right + 1)):
                        rectangles.append(sum(1 << (r * cols + c)
                                              for r in range(top, bottom + 1)
                                              for c in range(left, right + 1)))
        choices = {0: 0}
        for rect in rectangles:
            for mask, cost in list(choices.items()):
                joined = mask | rect
                choices[joined] = min(choices.get(joined, cost + 1), cost + 1)
        rowmask = sum(1 << (top * cols + c) for c in top_cols)
        next_states = {}
        for state, cost in states.items():
            for choice, extra in choices.items():
                combined = state | choice
                if combined & rowmask != rowmask:
                    continue
                future = combined & ~rowmask
                next_states[future] = min(next_states.get(future, cost + extra), cost + extra)
        states = next_states
    return states[0]


def oracle_min(matrix):
    ones = sum(sum(row) for row in matrix)
    lo, hi = 0, ones
    while lo < hi:
        mid = (lo + hi) // 2
        if target_solutions({"matrix": matrix, "K": mid}, 1) == [NO]:
            lo = mid + 1
        else:
            hi = mid
    return lo


def self_check():
    a, b, low, width = 2, 3, 5, 7
    rng = random.Random(20260925)
    allowed = [[low <= a * r + b * c <= low + width for c in range(6)] for r in range(6)]
    cases = [[[int(cell) for cell in row] for row in allowed]]
    cases += [[[int(cell and rng.random() < 0.5) for cell in row] for row in allowed]
              for _ in range(20)]
    thick = sparse = 0
    for matrix in cases:
        assert min_cover(matrix, a, b, low, width) == oracle_min(matrix), matrix
        has_block = any(all(matrix[r + dr][c + dc] for dr in (0, 1) for dc in (0, 1))
                        for r in range(5) for c in range(5))
        thick += has_block
        sparse += not has_block
    print({"seed": 20260925, "cases": len(cases), "thick": thick, "thin": sparse,
           "band": [a, b, low, width]})


if __name__ == "__main__":
    self_check()
