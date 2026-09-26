"""Regularized single permutation stage with its two notched holes."""
from itertools import product
from beam_probe import demand as core
from geometry import box,cover,maximal_rectangles


def stage():
    cells=set()
    for r in range(50):
        left=0 if r<10 else 1 if r<11 else 2 if r<12 else 3
        right=40 if r<5 else 42 if r<7 else 44 if r<9 else 46 if r<11 else 48 if r<13 else 50 if r<30 else 61
        cells|=box(left,r,right,r+1)
    cells|={(r+25,65-c) for r,c in core}
    holes=box(18,22,20,28)|box(20,24,21,28)|box(21,26,22,28)
    holes|=box(41,30,45,33)|box(45,31,46,33)
    cells-=holes
    incoming=box(20,0,21,24)
    output=(49,60)
    required=cells-box(60,33,61,50)
    return cells,required,incoming,output


if __name__=="__main__":
    cells,required,incoming,output=stage()
    print({"cells":len(cells),"rectangles":len(maximal_rectangles(frozenset(cells)))},flush=True)
    for active,out in product((False,True),repeat=2):
        need=(required-incoming if active else required)|({output} if out else set())
        for k in range(12,18):
            witness=cover(cells,need,k)
            if witness is not None:
                print({"input":active,"output_required":out,"optimum":k,"witness":witness},flush=True)
                break
