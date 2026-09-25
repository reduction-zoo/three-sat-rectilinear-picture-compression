"""Enumerate small connected pictures with exactly two minimum maximal covers."""

from itertools import combinations, product


def connected(ones, h, w):
    if not ones:
        return False
    seen = {next(iter(ones))}
    stack = list(seen)
    while stack:
        r, c = stack.pop()
        for p in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if p in ones and p not in seen:
                seen.add(p)
                stack.append(p)
    return seen == ones


def maximal_rectangles(ones, h, w):
    rectangles = []
    for r0 in range(h):
        for r1 in range(r0, h):
            for c0 in range(w):
                for c1 in range(c0, w):
                    cells = frozenset(product(range(r0, r1 + 1), range(c0, c1 + 1)))
                    if cells <= ones:
                        rectangles.append(((r0, r1, c0, c1), cells))
    return [(rect, cells) for rect, cells in rectangles
            if not any(cells < other for _, other in rectangles)]


for h, w in ((3, 3), (3, 4)):
    checked = connected_count = two_state_count = 0
    examples = []
    for bits in product((0, 1), repeat=h * w):
        checked += 1
        ones = {(r, c) for r in range(h) for c in range(w) if bits[r * w + c]}
        if not connected(ones, h, w) or any(not any(r == row for r, _ in ones) for row in range(h)) or any(not any(c == col for _, c in ones) for col in range(w)):
            continue
        connected_count += 1
        rects = maximal_rectangles(ones, h, w)
        for k in range(1, len(rects) + 1):
            covers = [tuple(rects[i][0] for i in ids) for ids in combinations(range(len(rects)), k)
                      if set().union(*(rects[i][1] for i in ids)) == ones]
            if covers:
                break
        if len(covers) == 2:
            two_state_count += 1
            if len(examples) < 5:
                examples.append({"matrix": [list(bits[r * w:(r + 1) * w]) for r in range(h)],
                                 "minimum": k, "covers": covers})
    print({"shape": [h, w], "checked": checked, "connected_full_span": connected_count,
           "two_state_tiles": two_state_count, "examples": examples})
