from pathlib import Path
import sys
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'022'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'025'))
from switch_composition import switches
from geometry import box
from kissat_cover import solve

def stages(inputs):
    cells,_,outputs=switches(inputs)
    supplied=[]
    for j,a in enumerate(inputs):
        y=40*j
        cells-=box(a,y+28,a+3,y+30)
        supplied.append(box(a+1,0,a+2,y+26))
    return cells,supplied,outputs

for inputs in [[20],[20,24],[24,20]]:
    cells,supplied,outputs=stages(inputs)
    base=next(k for k in range(12*len(inputs),20*len(inputs)) if solve(cells,cells,k) is not None)
    print({'positions':inputs,'base':base},flush=True)
    for ins,outs in product(product((False,True),repeat=len(inputs)),repeat=2):
        need=cells-set().union(*(s for s,on in zip(supplied,ins) if on))
        force=tuple(r for r,on in zip(outputs,outs) if on)
        expected=base+sum(out and not inp for inp,out in zip(ins,outs))
        low=solve(cells,need,expected-1,forced=force);high=solve(cells,need,expected,forced=force)
        print({'in':ins,'out':outs,'expected':expected,'below':low is not None,'at':high is not None},flush=True)
        if low is not None or high is None:
            print({'witness':low},flush=True)
            raise SystemExit(1)
