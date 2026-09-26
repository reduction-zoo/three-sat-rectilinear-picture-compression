from padded_source import padded_source,solve,maximal_rectangles,product
from pathlib import Path
import z3,json

def packing(cells,forced,k,required=None):
    rectangles=maximal_rectangles(frozenset(cells))
    excluded={(r,c) for a,b,d,e in forced for r in range(a,b+1) for c in range(d,e+1)}
    required=cells if required is None else required
    profiles={frozenset(i for i,(a,b,d,e) in enumerate(rectangles) if a<=r<=b and d<=c<=e):(r,c) for r,c in sorted(required-excluded)}
    keep=[]
    for profile in sorted(profiles,key=len):
        if not any(p<=profile for p in keep):keep.append(profile)
    xs=[z3.Bool(f'p{i}') for i in range(len(keep))]
    s=z3.Solver();s.set(timeout=30000)
    s.add(z3.PbGe([(x,1) for x in xs],k))
    for i in range(len(rectangles)):
        terms=[(x,1) for x,p in zip(xs,keep) if i in p]
        if terms:s.add(z3.PbLe(terms,1))
    answer=s.check()
    if answer!=z3.sat:return str(answer)
    model=s.model();points=[profiles[p] for x,p in zip(xs,keep) if z3.is_true(model.eval(x))][:k]
    assert len(points)==k and all(not(a<=r<=b and d<=c<=e) for r,c in points for a,b,d,e in forced)
    assert all(sum(a<=r<=b and d<=c<=e for r,c in points)<=1 for a,b,d,e in rectangles)
    return points

if __name__=='__main__':
    results=[]
    for d in [1,2,3]:
        cells,outputs=padded_source(d)
        base=next(k for k in range(8*d+8,8*d+15) if solve(cells,cells,k) is not None)
        for state in product((False,True),repeat=d):
            forced=tuple(r for r,on in zip(outputs,state) if on)
            k=base+int(any(state))
            pack=packing(cells,forced,k-len(forced))
            print({'degree':d,'state':state,'packing':pack if isinstance(pack,str) else len(pack)},flush=True)
            if isinstance(pack,str):raise SystemExit(1)
            results.append({'degree':d,'state':state,'lower_points':pack,'forced':forced,'cover':solve(cells,cells,k,forced=forced)})
    Path(__file__).with_name('certificates.json').write_text(json.dumps(results,indent=2)+'\n')
