from pathlib import Path
import sys
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'027'))
from probe import pair,solve,maximal_rectangles

def crossing():
    local,supplied,output=pair(40)
    transform=lambda p:(p[1]-15,p[0]+15)
    cells=local|{transform(p) for p in local}
    supplies=[supplied,{transform(p) for p in supplied}]
    outputs=[output, (output[2]-15,output[3]-15,output[0]+15,output[1]+15)]
    return cells,supplies,outputs

if __name__=='__main__':
    cells,supplied,outputs=crossing()
    assert all(r in maximal_rectangles(frozenset(cells)) for r in outputs)
    base=next(k for k in range(24,34) if solve(cells,cells,k) is not None)
    print({'baseline':base,'maximal_rectangles':len(maximal_rectangles(frozenset(cells)))},flush=True)
    for ins,outs in product(product((False,True),repeat=2),repeat=2):
        need=cells-set().union(*(s for s,on in zip(supplied,ins) if on))
        force=tuple(r for r,on in zip(outputs,outs) if on)
        expected=base+sum(out and not inp for inp,out in zip(ins,outs))
        low=solve(cells,need,expected-1,forced=force);high=solve(cells,need,expected,forced=force)
        print({'in':ins,'out':outs,'expected':expected,'below':low is not None,'at':high is not None},flush=True)
        if low is not None or high is None:
            print({'witness':low},flush=True)
            raise SystemExit(1)
