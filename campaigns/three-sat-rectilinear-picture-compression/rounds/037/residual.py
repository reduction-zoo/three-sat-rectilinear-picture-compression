from functools import lru_cache
from geometry import maximal_rectangles

def oracle(cells):
    points=sorted(cells);index={p:i for i,p in enumerate(points)}
    masks=[sum(1<<i for i,(r,c) in enumerate(points) if a<=r<=b and d<=c<=e) for a,b,d,e in maximal_rectangles(frozenset(cells))]
    containing=[[m for m in masks if m>>i&1] for i in range(len(points))]
    @lru_cache(None)
    def cost(remaining):
        if not remaining:return 0
        i=min((i for i in range(len(points)) if remaining>>i&1),key=lambda i:len(containing[i]))
        return 1+min(cost(remaining&~m) for m in containing[i])
    return lambda need:cost(sum(1<<index[p] for p in need))
