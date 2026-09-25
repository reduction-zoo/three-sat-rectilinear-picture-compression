"""Count same-state exterior taps of every exclusive 3x3 core."""

from collections import Counter
from functools import lru_cache
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "008"))
from port_probe import picture, ports, search_candidates
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions


@lru_cache(None)
def feasible(bits, k, extras):
    return target_solutions({"matrix": picture(bits, extras), "K": k}, 1) != [NO]


candidates, _, _, _ = search_candidates()
counts = Counter()
examples = []
for bits, k, p, q in candidates:
    taps = {"P": [], "Q": []}
    for tap in ports:
        if tap in (p, q) or not feasible(bits, k, (tap,)):
            continue
        with_p = feasible(bits, k, tuple(sorted((p, tap))))
        with_q = feasible(bits, k, tuple(sorted((q, tap))))
        if with_p != with_q:
            taps["P" if with_p else "Q"].append(tap)
    degree = max(map(len, taps.values()))
    counts[degree] += 1
    if degree >= 3 and len(examples) < 10:
        examples.append({"core": [bits[3 * r:3 * r + 3] for r in range(3)],
                         "budget": k, "ports": (p, q), "taps": taps})

print({"exclusive_pairs": len(candidates), "distinct_tap_oracle_queries": feasible.cache_info().misses,
       "maximum_same_state_taps": max(counts),
       "pairs_by_maximum_taps": dict(sorted(counts.items())), "examples": examples})
