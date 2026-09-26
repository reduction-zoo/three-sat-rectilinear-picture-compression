from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'027'))
from probe import pair,solve
from geometry import box,maximal_rectangles
for gap in [0,1,4]:
    local,supplied,_=pair(18)
    shift=14+gap
    cells=local|{(r+shift,c+8) for r,c in local}|box(13,12,14,shift-1)
    out=(shift+1,shift+12,21,21)
    assert out in maximal_rectangles(frozenset(cells))
    costs=[]
    for inp,on in [(False,False),(False,True),(True,False),(True,True)]:
        need=cells-supplied if inp else cells
        costs.append(next(k for k in range(26,33) if solve(cells,need,k,forced=(out,) if on else ()) is not None))
    print({'gap':gap,'costs':costs,'valid':costs==[costs[0],costs[0]+1,costs[0],costs[0]]},flush=True)
