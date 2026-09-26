from pathlib import Path
import sys
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'035'))
from cut import tile,solve,maximal_rectangles
from geometry import box

def capped_swap():
    cells,inputs,outputs=tile()
    for i,c in enumerate([5,16]):
        cells|=box(c,-30,c+2,-27)
        inputs[i]|=box(c,-30,c+1,-27)
    return cells,inputs,outputs

if __name__=='__main__':
    cells,inputs,outputs=capped_swap()
    base=next(k for k in range(44,50) if solve(cells,cells,k) is not None)
    print({'baseline':base},flush=True)
    for a,b in product(product((False,True),repeat=2),repeat=2):
        need=cells-set().union(*(s for s,on in zip(inputs,a) if on))
        force=tuple(r for r,on in zip(outputs,b) if on)
        k=base+sum(y and not x for x,y in zip(a,b))
        low=solve(cells,need,k-1,forced=force);high=solve(cells,need,k,forced=force)
        print({'in':a,'out':b,'expected':k,'below':low is not None,'at':high is not None},flush=True)
        assert low is None and high is not None
