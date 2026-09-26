from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'027'))
from probe import pair,solve
from geometry import box,maximal_rectangles
for width in [1,2,3]:
    local,supplied,_=pair(18)
    shift=18
    cells=local|{(r+shift,c+8) for r,c in local}|box(13,12,13+width,shift-1)
    out=(shift+1,shift+12,21,21)
    assert out in maximal_rectangles(frozenset(cells))
    costs=[]
    for inp,on in [(False,False),(False,True),(True,False),(True,True)]:
        need=cells-supplied if inp else cells
        lo,hi=0,35
        while lo<hi:
            mid=(lo+hi)//2
            if solve(cells,need,mid,forced=(out,) if on else ()) is None:lo=mid+1
            else:hi=mid
        costs.append(lo)
    print({'width':width,'costs':costs},flush=True)
