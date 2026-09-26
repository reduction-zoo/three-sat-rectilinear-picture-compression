from pathlib import Path
import sys
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'033'))
from swap import swap,solve,maximal_rectangles
from geometry import box

def flat_swap():
    cells,inputs,outputs=swap()
    cells|=box(5,-27,11,0)|box(52,11,56,38)
    inputs[0]=box(5,-27,6,10)
    outputs[0]=(1,37,55,55)
    return cells,inputs,outputs

if __name__=='__main__':
    cells,inputs,outputs=flat_swap()
    assert all(r in maximal_rectangles(frozenset(cells)) for r in outputs)
    lo,hi=0,55
    while lo<hi:
        mid=(lo+hi)//2
        if solve(cells,cells,mid) is None:lo=mid+1
        else:hi=mid
    base=lo
    print({'baseline':base,'rectangles':len(maximal_rectangles(frozenset(cells)))},flush=True)
    for ins,outs in product(product((False,True),repeat=2),repeat=2):
        need=cells-set().union(*(s for s,on in zip(inputs,ins) if on))
        force=tuple(r for r,on in zip(outputs,outs) if on)
        k=base+sum(out and not inp for inp,out in zip(ins,outs))
        low=solve(cells,need,k-1,forced=force);high=solve(cells,need,k,forced=force)
        print({'in':ins,'out':outs,'expected':k,'below':low is not None,'at':high is not None},flush=True)
        if low is not None or high is None:
            print({'witness':low},flush=True)
            raise SystemExit(1)
