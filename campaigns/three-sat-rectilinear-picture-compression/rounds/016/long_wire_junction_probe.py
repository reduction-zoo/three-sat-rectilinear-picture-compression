"""Enumerate three long-wire arms meeting at one clause cell."""

from itertools import combinations, product
import z3

core = {(2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
p, q = (4, 1), (2, 4)
transposed = {(c, r) for r, c in core}


def wire(t):
    cells = core | {(r - 2, c + 3) for r, c in core} | {(r + 3, c - 3) for r, c in transposed} | {p, q}
    for k in range(4, t + 1):
        cells |= {(r + 3 * k - 6, c - 2 * k + 3) for r, c in transposed}
        cells.add((3 * k - 5, -2 * k + 7))
    return cells, ((3 * t - 2, -2 * t + 5), (0, 7))


def transform(point, swap, sr, sc):
    r, c = point
    return (sr * c, sc * r) if swap else (sr * r, sc * c)


def antirectangle_at_least(cells, bound):
    points = sorted(cells)
    chosen = [z3.Bool(f"cell_{i}") for i in range(len(points))]
    solver = z3.Solver()
    solver.set(timeout=5000)
    solver.add(z3.PbGe([(var, 1) for var in chosen], bound))
    for i, j in combinations(range(len(points)), 2):
        r, c = points[i]
        s, d = points[j]
        if all((a, b) in cells for a in range(min(r, s), max(r, s) + 1)
               for b in range(min(c, d), max(c, d) + 1)):
            solver.add(z3.Not(z3.And(chosen[i], chosen[j])))
    result = solver.check()
    if result == z3.unsat:
        return "unsat", None
    if result == z3.unknown:
        return "unknown", None
    model = solver.model()
    return "sat", [point for point, var in zip(points, chosen) if z3.is_true(model.eval(var))]


for t in (3, 4):
    cells, ends = wire(t)
    options = []
    for near in range(2):
        for swap, sr, sc in product((False, True), (1, -1), (1, -1)):
            ar, ac = transform(ends[near], swap, sr, sc)
            move = lambda point: tuple(x - y for x, y in zip(transform(point, swap, sr, sc), (ar, ac)))
            options.append((near, swap, sr, sc, {move(cell) for cell in cells}, move(ends[1 - near])))
    disjoint = far_clear = 0
    examples = []
    first_false_certificate = None
    checked = []
    for indices in combinations(range(len(options)), 3):
        triple = [options[index] for index in indices]
        parts = [item[4] for item in triple]
        if any(parts[i] & parts[j] for i, j in combinations(range(3), 2)):
            continue
        disjoint += 1
        union = set().union(*parts)
        fars = [item[5] for item in triple]
        if any(far in union or far == (0, 0) for far in fars) or len(set(fars)) != 3:
            continue
        far_clear += 1
        if t == 3 and len(checked) < 8:
            status, certificate = antirectangle_at_least(union | set(fars) | {(0, 0)}, 6 * t + 1)
            checked.append((indices, status))
            print({"antirectangle_query": indices, "status": status}, flush=True)
            if certificate is not None and first_false_certificate is None:
                first_false_certificate = {"options": indices, "certificate": certificate}
        if len(examples) < 8:
            examples.append({"options": indices, "far_endpoints": fars,
                             "shape": [max(r for r, _ in union) - min(r for r, _ in union) + 1,
                                       max(c for _, c in union) - min(c for _, c in union) + 1]})
    print({"cores_per_arm": t, "orientation_options": len(options),
           "disjoint": disjoint, "far_clear": far_clear, "examples": examples,
           "first_false_certificate": first_false_certificate,
           "bounded_antirectangle_queries": checked})
