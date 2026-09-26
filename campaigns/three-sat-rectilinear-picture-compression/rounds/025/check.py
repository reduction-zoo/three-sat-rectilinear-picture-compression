from pathlib import Path
import sys
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'022'))
from geometry import cover,maximal_rectangles
from blocked import blocked
if "--kissat" in sys.argv:
    from kissat_cover import solve as cover

for inputs in ([20],[20,24],[24,20]):
    cells,supplied,outgoing=blocked(inputs)
    baseline=next(k for k in range(12*len(inputs),20*len(inputs)) if cover(cells,cells,k) is not None)
    print({'inputs':inputs,'baseline':baseline,'rectangles':len(maximal_rectangles(frozenset(cells)))},flush=True)
    states=list(product(product((False,True),repeat=len(inputs)),repeat=2))
    if len(inputs)==2: states.insert(0,((False,False),(False,True)))
    for ins,outs in states:
        need=cells-set().union(*(s for s,on in zip(supplied,ins) if on))
        forced=tuple(rect for rect,on in zip(outgoing,outs) if on)
        expected=baseline+sum(out and not inp for inp,out in zip(ins,outs))
        low=cover(cells,need,expected-1,forced=forced)
        upper=cover(cells,need,expected,forced=forced)
        print({'in':ins,'out':outs,'expected':expected,'below':low is not None,'at':upper is not None},flush=True)
        if low is not None or upper is None:
            print({'witness':low},flush=True)
            raise SystemExit(1)
