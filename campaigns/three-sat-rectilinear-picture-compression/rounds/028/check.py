from pathlib import Path
import sys
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'022'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'025'))
from kissat_cover import solve
from geometry import maximal_rectangles
from picture import picture
cells,supplied,outputs=picture()
print({'cells':len(cells),'rectangles':len(maximal_rectangles(frozenset(cells)))},flush=True)
baseline=next(k for k in range(24,36) if solve(cells,cells,k) is not None)
print({'baseline':baseline},flush=True)
for ins,outs in product(product((False,True),repeat=2),repeat=2):
    need=cells-set().union(*(s for s,on in zip(supplied,ins) if on))
    force=tuple(rect for rect,on in zip(outputs,outs) if on)
    expected=baseline+sum(out and not inp for inp,out in zip(ins,outs))
    low=solve(cells,need,expected-1,forced=force)
    high=solve(cells,need,expected,forced=force)
    print({'in':ins,'out':outs,'expected':expected,'below':low is not None,'at':high is not None},flush=True)
    if low is not None or high is None:
        print({'witness':low},flush=True)
        raise SystemExit(1)
