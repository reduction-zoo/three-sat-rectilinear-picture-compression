"""Small exact cover probe over a cell mask and a required subset."""
from functools import lru_cache
import z3


@lru_cache(None)
def maximal_rectangles(cells):
    cells=frozenset(cells)
    if not cells:
        return ()
    rmin,rmax=min(r for r,c in cells),max(r for r,c in cells)
    cmin,cmax=min(c for r,c in cells),max(c for r,c in cells)
    rows={r:sum(1<<(c-cmin) for rr,c in cells if rr==r) for r in range(rmin,rmax+1)}
    result=[]
    for top in range(rmin,rmax+1):
        common=(1<<(cmax-cmin+1))-1
        for bottom in range(top,rmax+1):
            common &= rows[bottom]
            if not common:
                break
            c=0
            while c<=cmax-cmin:
                if not (common>>c)&1:
                    c+=1
                    continue
                left=c
                while (common>>c)&1:
                    c+=1
                mask=((1<<(c-left))-1)<<left
                if (rows.get(top-1,0)&mask)!=mask and (rows.get(bottom+1,0)&mask)!=mask:
                    result.append((top,bottom,left+cmin,c-1+cmin))
    return tuple(result)


def cover(cells,required,budget,timeout=30000,forced=()):
    assert required<=cells
    rects=maximal_rectangles(frozenset(cells))
    solver=z3.SolverFor("QF_FD")
    solver.set(timeout=timeout)
    chosen=[z3.Bool(f"rect{i}") for i in range(len(rects))]
    for rect in forced:
        solver.add(chosen[rects.index(rect)])
    solver.add(z3.PbLe([(v,1) for v in chosen],budget))
    clauses={frozenset(i for i,(a,b,d,e) in enumerate(rects) if a<=r<=b and d<=c<=e)
             for r,c in required}
    minimal=[]
    for clause in sorted(clauses,key=len):
        if not any(other<=clause for other in minimal):
            minimal.append(clause)
            solver.add(z3.Or([chosen[i] for i in clause]))
    answer=solver.check()
    if answer==z3.unknown:
        raise RuntimeError(f"unknown: {solver.reason_unknown()}")
    if answer==z3.unsat:
        return None
    model=solver.model()
    witness=[rect for v,rect in zip(chosen,rects) if z3.is_true(model.eval(v))]
    covered={(r,c) for a,b,d,e in witness for r in range(a,b+1) for c in range(d,e+1)}
    assert required<=covered<=cells and len(witness)<=budget
    return witness


def box(x0,y0,x1,y1):
    return {(r,c) for r in range(y0,y1) for c in range(x0,x1)}
