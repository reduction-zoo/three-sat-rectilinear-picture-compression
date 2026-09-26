from pathlib import Path
import sys
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'031'))
from crossing import crossing,pair,solve,maximal_rectangles

def swap():
    local,supplied,out=pair(60)
    transform=lambda p:(p[1]-25,p[0]+25)
    cells=local|{transform(p) for p in local}
    inputs=[supplied,{transform(p) for p in supplied}]
    outputs=[out,(out[2]-25,out[3]-25,out[0]+25,out[1]+25)]
    local,supplied,_=pair(24)
    local={p for p in local if p[1]<=12}
    before=lambda p:(p[0]-25,p[1]+11)
    after=lambda p:(p[1]+25,p[0]+39)
    cells|={before(p) for p in local}|{after(p) for p in local}
    inputs=[inputs[0],{before(p) for p in supplied if p in local}]
    outputs=[outputs[0],(26,37,44,44)]
    return cells,inputs,outputs

if __name__=='__main__':
    cells,inputs,outputs=swap()
    rects=maximal_rectangles(frozenset(cells))
    normalized=[]
    for a,b,c,d in outputs:
        candidates=[r for r in rects if r[0]<=a and r[1]>=b and r[2]<=c and r[3]>=d]
        assert len(candidates)==1,candidates
        normalized.append(candidates[0])
    outputs=normalized
    lo,hi=0,50
    while lo<hi:
        mid=(lo+hi)//2
        if solve(cells,cells,mid) is None:lo=mid+1
        else:hi=mid
    base=lo
    print({'baseline':base,'outputs':outputs,'rectangles':len(rects)},flush=True)
    for ins,outs in product(product((False,True),repeat=2),repeat=2):
        need=cells-set().union(*(s for s,on in zip(inputs,ins) if on))
        force=tuple(r for r,on in zip(outputs,outs) if on)
        expected=base+sum(out and not inp for inp,out in zip(ins,outs))
        low=solve(cells,need,expected-1,forced=force);high=solve(cells,need,expected,forced=force)
        print({'in':ins,'out':outs,'expected':expected,'below':low is not None,'at':high is not None},flush=True)
        if low is not None or high is None:
            print({'witness':low},flush=True)
            raise SystemExit(1)
