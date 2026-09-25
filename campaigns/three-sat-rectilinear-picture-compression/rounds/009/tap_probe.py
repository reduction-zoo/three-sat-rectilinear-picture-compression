"""Find exterior ports that follow one of two exclusive core states."""

from functools import lru_cache
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "008"))
from port_probe import ports, picture, search_candidates
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import NO, target_solutions


@lru_cache(None)
def feasible(bits, budget, extras):
    return target_solutions({"matrix": picture(bits, extras), "K": budget}, 1) != [NO]


candidates, _, _, _ = search_candidates()
selected_bits = (0, 0, 0, 0, 1, 1, 1, 1, 1)
selected_pair = ((4, 1), (2, 4))
tap_count = 0
selected_taps = []
examples = []
both_polarity_pairs = 0
first_both_polarity = None
orbit_reps = {}


def transform(point, reflect, turns):
    r, c = point
    if reflect:
        c = 4 - c
    for _ in range(turns):
        r, c = c, 4 - r
    return r, c


for bits, k, p, q in candidates:
    polarities = set()
    for tap in ports:
        if tap in (p, q) or not feasible(bits, k, (tap,)):
            continue
        with_p = feasible(bits, k, tuple(sorted((p, tap))))
        with_q = feasible(bits, k, tuple(sorted((q, tap))))
        if with_p == with_q:
            continue
        tap_count += 1
        polarities.add("P" if with_p else "Q")
        item = {"core": [bits[r * 3:(r + 1) * 3] for r in range(3)],
                "budget": k, "state_ports": [p, q], "tap": tap,
                "compatible_state": "P" if with_p else "Q"}
        if bits == selected_bits and (p, q) == selected_pair:
            selected_taps.append(item)
        if len(examples) < 5:
            examples.append(item)
    if len(polarities) == 2:
        both_polarity_pairs += 1
        cells = {(r + 1, c + 1) for r in range(3) for c in range(3) if bits[r * 3 + c]}
        key = min((tuple(sorted(transform(cell, reflect, turns) for cell in cells)),
                   tuple(sorted((transform(p, reflect, turns), transform(q, reflect, turns)))))
                  for reflect in (False, True) for turns in range(4))
        orbit_reps.setdefault(key, {"core": [bits[r * 3:(r + 1) * 3] for r in range(3)],
                                     "budget": k, "ports": [p, q]})
        if first_both_polarity is None:
            first_both_polarity = {"core": [bits[r * 3:(r + 1) * 3] for r in range(3)],
                                   "budget": k, "ports": [p, q]}
print({"exclusive_pairs": len(candidates), "state_selective_taps": tap_count,
       "both_polarity_pairs": both_polarity_pairs, "first_both_polarity": first_both_polarity,
       "both_polarity_orbits": len(orbit_reps), "orbit_representatives": list(orbit_reps.values()),
       "selected_wire_core_taps": selected_taps, "examples": examples})
