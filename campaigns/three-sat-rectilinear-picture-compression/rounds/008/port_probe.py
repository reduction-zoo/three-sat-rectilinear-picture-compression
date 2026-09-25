"""Search thick 3x3 cores for two individually free but jointly costly ports."""

from itertools import combinations, product
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions

ports = [(0, c) for c in range(1, 4)] + [(4, c) for c in range(1, 4)] + [(r, 0) for r in range(1, 4)] + [(r, 4) for r in range(1, 4)]


def picture(bits, extra=()):
    matrix = [[0] * 5 for _ in range(5)]
    for r in range(3):
        for c in range(3):
            matrix[r + 1][c + 1] = bits[r * 3 + c]
    for r, c in extra:
        matrix[r][c] = 1
    return matrix


def feasible(matrix, budget):
    return target_solutions({"matrix": matrix, "K": budget}, 1) != [NO]


def search_candidates():
    candidates = []
    cores = free_singletons = tested_pairs = 0
    for bits in product((0, 1), repeat=9):
        core = [bits[r * 3:(r + 1) * 3] for r in range(3)]
        if not any(all(core[r + dr][c + dc] for dr in (0, 1) for dc in (0, 1))
                   for r in range(2) for c in range(2)):
            continue
        cores += 1
        k = next(k for k in range(1, sum(bits) + 1) if feasible(picture(bits), k))
        free = [port for port in ports if feasible(picture(bits, (port,)), k)]
        free_singletons += len(free)
        for p, q in combinations(free, 2):
            tested_pairs += 1
            if not feasible(picture(bits, (p, q)), k):
                candidates.append((bits, k, p, q))
    return candidates, cores, free_singletons, tested_pairs


if __name__ == "__main__":
    candidates, cores, free_singletons, tested_pairs = search_candidates()
    opposite = [(bits, k, p, q) for bits, k, p, q in candidates
                if (p[0], q[0]) in ((0, 4), (4, 0)) or (p[1], q[1]) in ((0, 4), (4, 0))]
    examples = [{"core": [bits[r * 3:(r + 1) * 3] for r in range(3)], "base_budget": k,
                 "ports": [p, q], "full_picture": picture(bits, (p, q))}
                for bits, k, p, q in candidates[:5]]
    print({"thick_cores": cores, "free_single_ports": free_singletons,
           "tested_free_port_pairs": tested_pairs, "exclusive_port_pairs": len(candidates),
           "opposite_side_pairs": len(opposite), "examples": examples})
