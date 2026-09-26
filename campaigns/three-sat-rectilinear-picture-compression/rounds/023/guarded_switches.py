from itertools import product
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"022"))
from switch_composition import switches
from geometry import box,cover,maximal_rectangles


def guarded(inputs):
    cells,supplied,outgoing=switches(inputs)
    height=40*(len(inputs)-1)+50
    for j in range(1,len(inputs)):
        for y in range(40*j,40*(j+1) if j+1<len(inputs) else height):
            local=y-40*j
            left=0 if local<12 else 1 if local<13 else 2 if local<15 else 3
            cells|=box(left,y,3*j+left,y+1)
    return cells,supplied,outgoing


if __name__=="__main__":
    cells,supplied,outgoing=guarded([20,24])
    lo,hi=0,40
    while lo<hi:
        mid=(lo+hi)//2
        if cover(cells,cells,mid) is None:
            lo=mid+1
        else:
            hi=mid
    print({"baseline":lo,"maximal_rectangles":len(maximal_rectangles(frozenset(cells)))},flush=True)
    for ins,outs in [((False,False),(False,True))]+list(product(product((False,True),repeat=2),repeat=2)):
        need=cells-set().union(*(s for s,on in zip(supplied,ins) if on))
        forced=tuple(rect for rect,on in zip(outgoing,outs) if on)
        expected=lo+sum(out and not inp for inp,out in zip(ins,outs))
        witness=cover(cells,need,expected-1,forced=forced)
        upper=cover(cells,need,expected,forced=forced)
        print({"inputs":ins,"outputs":outs,"expected":expected,
               "below_expected":witness is not None,"at_expected":upper is not None},flush=True)
        if witness is not None or upper is None:
            print({"counterexample":witness},flush=True)
            break
