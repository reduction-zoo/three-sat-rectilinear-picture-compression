"""Regularized Figure 8/9 geometry with an optional output channel."""
from itertools import combinations
from beam_probe import demand as core
from geometry import box,cover,maximal_rectangles


def vertex(d):
    right=20
    base=12*d+2
    shape=set()
    for i in range(d):
        x,y=-6*i,12*i
        shape|={(r+y,c+x) for r,c in core}
        shape|=box(x+1,y+5,right,y+6)  # horizontal beam
        shape|=box(x+5,y+5,16-i,base+3+i)  # vertical background
        shape|=box(x+5,y+6,right+3,12*(i+1)+5 if i+1<d else base)
    shape|=box(14,4,17,base+1)  # top bump and its forced column
    shape|={(base+5-r,right+5-c) for r,c in core}  # reversed bottom machine
    shape|=box(-6*(d-1)-5,base,right+5,base+1)  # forcing notch
    depth=base+d+6
    channel=box(-6*(d-1)+5,base+1,16-d,depth)
    ports=[(depth-1,-6*i+5) for i in range(d)]
    return shape|channel,shape,ports


if __name__=="__main__":
    for d in (1,2,3):
        cells,required,ports=vertex(d)
        lo,hi=0,8*d+10
        while lo<hi:
            mid=(lo+hi)//2
            if cover(cells,required,mid) is None:
                lo=mid+1
            else:
                hi=mid
        print({"degree":d,"cells":len(cells),"maximal_rectangles":len(maximal_rectangles(frozenset(cells))),
               "base_optimum":lo,"paper_prediction":8*d+7},flush=True)
        for count in range(1,d+1):
            for selected in combinations(ports,count):
                forced=required|set(selected)
                print({"degree":d,"selected":selected,"at_base":cover(cells,forced,lo) is not None,
                       "at_base_plus_one":cover(cells,forced,lo+1) is not None},flush=True)
