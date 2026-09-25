"""Rebuild the fixed Prepare corpus; no candidate code is used."""

import json
import random
from pathlib import Path

from check import NO, source_solution


def source_for_seed(seed):
    rng = random.Random(seed)
    n = rng.randint(2, 5)
    m = rng.randint(2, 16)
    return {"n": n, "clauses": [[rng.choice((-1, 1)) * rng.randint(1, n) for _ in range(3)]
                              for _ in range(m)]}


def unit(lit):
    return [lit, lit, lit]


EDGES = [
    ({"n": 0, "clauses": []}, True),
    ({"n": 1, "clauses": []}, True),
    ({"n": 1, "clauses": [unit(1)]}, True),
    ({"n": 1, "clauses": [unit(-1)]}, True),
    ({"n": 1, "clauses": [unit(1), unit(-1)]}, False),
    ({"n": 1, "clauses": [[1, -1, 1]]}, True),
    ({"n": 1, "clauses": [[-1, 1, -1]]}, True),
    ({"n": 2, "clauses": []}, True),
    ({"n": 2, "clauses": [unit(1), unit(2)]}, True),
    ({"n": 2, "clauses": [unit(1), unit(-1)]}, False),
    ({"n": 2, "clauses": [unit(1), unit(-1), unit(2)]}, False),
    ({"n": 2, "clauses": [unit(1), unit(-1), unit(-2)]}, False),
    ({"n": 2, "clauses": [[1, 2, 2], [-1, -2, -2]]}, True),
    ({"n": 2, "clauses": [unit(1), unit(-2)]}, True),
    ({"n": 3, "clauses": [unit(1), unit(2), unit(3)]}, True),
    ({"n": 3, "clauses": [unit(1), unit(-1)]}, False),
    ({"n": 3, "clauses": [[1, 2, 3]]}, True),
    ({"n": 3, "clauses": [[-1, -2, -3]]}, True),
    ({"n": 4, "clauses": [unit(4), unit(-4)]}, False),
    ({"n": 5, "clauses": []}, True),
]


def main():
    cases = []
    for source, should_satisfy in EDGES:
        expected = source_solution(source)
        assert (expected != NO) == should_satisfy
        cases.append({"source": source, "kind": "edge", "expected": expected})
    for seed in range(1000, 1100):
        source = source_for_seed(seed)
        cases.append({"source": source, "kind": "random", "seed": seed,
                      "expected": source_solution(source)})
    path = Path(__file__).with_name("cases.json")
    path.write_text(json.dumps(cases, indent=2) + "\n")
    print(f"wrote {len(cases)} cases to {path}")


if __name__ == "__main__":
    main()
