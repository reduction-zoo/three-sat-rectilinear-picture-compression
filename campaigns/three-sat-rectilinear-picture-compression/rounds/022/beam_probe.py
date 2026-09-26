"""Exact finite interface of the Figure 7 open beam machine."""
from pathlib import Path
import sys
import z3

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "005"))
from tile_probe import maximal_rectangles

# Coordinates read from the vector boundary of Figure 7(a), unit 10.8 pt.
# The open endpoints (5,7),(7,5) are completed around the optional quadrant.
boundary = [(5,7),(5,6),(4,6),(4,7),(3,7),(3,8),(0,8),(0,6),
            (1,6),(1,5),(2,5),(2,4),(4,4),(4,2),(5,2),(5,1),
            (6,1),(6,0),(8,0),(8,3),(7,3),(7,4),(6,4),(6,5),
            (7,5),(7,7)]


def inside(x,y):
    crossings = sum(a==c and min(b,d)<y<max(b,d) and a>x
                    for (a,b),(c,d) in zip(boundary,boundary[1:]+boundary[:1]))
    return crossings % 2 == 1


cells = {(r,c) for r in range(9) for c in range(9)
         if inside(c+.5,r+.5) or (r>=5 and c>=5)}
demand = {cell for cell in cells if cell[0]<5 or cell[1]<5} | {(5,5)}
matrix = [[int((r,c) in cells) for c in range(9)] for r in range(9)]
rects = [rect for rect, _ in maximal_rectangles(cells, 9, 9)]


def solve(required, k):
    solver = z3.Solver()
    chosen = [z3.Bool(f"b{i}") for i in range(len(rects))]
    for r,c in required:
        solver.add(z3.Or([chosen[i] for i,(a,b,d,e) in enumerate(rects)
                          if a<=r<=b and d<=c<=e]))
    solver.add(z3.PbLe([(v,1) for v in chosen], k))
    result = solver.check()
    assert result != z3.unknown
    if result == z3.unsat:
        return None
    model = solver.model()
    return [rect for rect,v in zip(rects,chosen) if z3.is_true(model.eval(v))]


if __name__ == "__main__":
    for row in matrix:
        print("".join(map(str,row)))
    for label, extras in [("base",set()),("horizontal",{(5,8)}),
                           ("vertical",{(8,5)}),("both",{(5,8),(8,5)})]:
        required=demand | extras
        for k in range(1,10):
            witness=solve(required,k)
            if witness is not None:
                print({"state":label,"optimum":k,"witness":witness})
                break
