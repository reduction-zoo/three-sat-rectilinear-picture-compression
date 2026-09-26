"""Stack two regularized switches and check their interaction."""
from itertools import product
from beam_probe import demand as core
from geometry import box,cover,maximal_rectangles


def switches(inputs):
    height=40*(len(inputs)-1)+50
    left_events={0:0}
    right_events={0:40}
    holes=set()
    machines=set()
    supplied=[]
    outgoing=[]
    for j,a in enumerate(inputs):
        y,r=40*j,40+21*j
        left_events.update({y+12:3*j+1,y+13:3*j+2,y+15:3*j+3})
        right_events.update({y+5:r+2,y+8:r+4,y+11:r+6,y+14:r+8,y+17:r+10,y+30:r+21})
        machines|={(rr+y+25,r+25-c) for rr,c in core}
        holes|=box(a,y+24,a+1,y+28)|box(a+1,y+26,a+2,y+28)
        holes|=box(r+1,y+30,r+5,y+33)|box(r+5,y+31,r+6,y+33)
        supplied.append(box(a,0,a+1,y+24))
        outgoing.append((y+26,height-1,r+20,r+20))
    cells=set()
    left,right=0,40
    for y in range(height):
        left=left_events.get(y,left)
        right=right_events.get(y,right)
        cells|=box(left,y,right,y+1)
    cells=(cells|machines)-holes
    return cells,supplied,outgoing


if __name__=="__main__":
    cells,supplied,outgoing=switches([20,24])
    lo,hi=0,40
    while lo<hi:
        mid=(lo+hi)//2
        if cover(cells,cells,mid) is None:
            lo=mid+1
        else:
            hi=mid
    print({"cells":len(cells),"maximal_rectangles":len(maximal_rectangles(frozenset(cells))),
           "baseline":lo},flush=True)
    for ins in product((False,True),repeat=2):
        need=cells-set().union(*(s for s,active in zip(supplied,ins) if active))
        for outs in product((False,True),repeat=2):
            forced=tuple(rect for rect,active in zip(outgoing,outs) if active)
            actual=next(k for k in range(lo-2,lo+3) if cover(cells,need,k,forced=forced) is not None)
            print({"inputs":ins,"outputs":outs,"actual":actual,
                   "expected":lo+sum(out and not inp for inp,out in zip(ins,outs))},flush=True)
