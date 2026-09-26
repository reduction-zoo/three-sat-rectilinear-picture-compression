from pathlib import Path
import sys
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'034'))
from flat_swap import flat_swap,solve,maximal_rectangles

def tile():
    cells,ins,outs=flat_swap()
    cells={p for p in cells if not(p[0]>=33 and 44<p[1]<52)}
    return cells,ins,outs

if __name__=='__main__':
    cells,ins,outs=tile()
    combined=cells|{(r+65,c+39) for r,c in cells}
    crossing=[r for r in maximal_rectangles(frozenset(combined)) if r[0]<=37<r[1]]
    print({'crossing_rectangles':crossing},flush=True)
    assert len(crossing)==2 and {r[2] for r in crossing}=={44,55} and all(r[2]==r[3] for r in crossing)
    for n,pic,inputs,outputs in [(1,cells,ins,outs),(2,combined,ins,[(outs[1][0]+65,outs[1][1]+65,outs[1][2]+39,outs[1][3]+39),(outs[0][0]+65,outs[0][1]+65,outs[0][2]+39,outs[0][3]+39)])]:
        lo,hi=0,50*n
        while lo<hi:
            mid=(lo+hi)//2
            if solve(pic,pic,mid) is None:lo=mid+1
            else:hi=mid
        base=lo; print({'tiles':n,'baseline':base},flush=True)
        for a,b in product(product((False,True),repeat=2),repeat=2):
            need=pic-set().union(*(s for s,on in zip(inputs,a) if on))
            force=tuple(r for r,on in zip(outputs,b) if on)
            k=base+sum(y and not x for x,y in zip(a,b))
            low=solve(pic,need,k-1,forced=force);high=solve(pic,need,k,forced=force)
            print({'in':a,'out':b,'expected':k,'below':low is not None,'at':high is not None},flush=True)
            if low is not None or high is None:
                print({'witness':low},flush=True)
                raise SystemExit(1)
