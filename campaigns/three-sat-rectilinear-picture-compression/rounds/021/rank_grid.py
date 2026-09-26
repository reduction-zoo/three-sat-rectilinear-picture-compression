"""Compress a finite union of nondegenerate rational-coordinate rectangles."""


def compress(rectangles):
    if not rectangles:
        return [], [], []
    if any(a >= b or c >= d for a, b, c, d in rectangles):
        raise ValueError("nondegenerate rectangles required")
    xs = sorted({x for a, b, _, _ in rectangles for x in (a, b)})
    ys = sorted({y for _, _, c, d in rectangles for y in (c, d)})
    matrix = [[int(any(a <= x0 and x1 <= b and c <= y0 and y1 <= d
                       for a, b, c, d in rectangles))
               for x0, x1 in zip(xs, xs[1:])]
              for y0, y1 in zip(ys, ys[1:])]
    return matrix, xs, ys


def lift(cover, xs, ys):
    return [(xs[c0], xs[c1 + 1], ys[r0], ys[r1 + 1])
            for r0, r1, c0, c1 in cover]
