from pathlib import Path
import sys
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'022'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'025'))
from vertex_probe import vertex
from geometry import box,maximal_rectangles
from kissat_cover import solve

def source(d):
    cells,_,ports=vertex(d)
    rects=maximal_rectangles(frozenset(cells));outputs=[]
    for i,(end,c) in enumerate(ports):
        candidates=[r for r in rects if r[0]<=12*i+1 and r[1]>=end and r[2]<=c<=r[3]]
        assert len(candidates)==1,candidates
        outputs.append(candidates[0])
    return cells,outputs

if __name__=='__main__':
    for d in [1,2,3]:
        cells,outputs=source(d)
        lo,hi=0,8*d+12
        while lo<hi:
            mid=(lo+hi)//2
            if solve(cells,cells,mid) is None:lo=mid+1
            else:hi=mid
        base=lo
        print({'degree':d,'baseline':base,'outputs':outputs},flush=True)
        for state in product((False,True),repeat=d):
            forced=tuple(r for r,on in zip(outputs,state) if on)
            k=base+int(any(state))
            low=solve(cells,cells,k-1,forced=forced);high=solve(cells,cells,k,forced=forced)
            print({'state':state,'expected':k,'below':low is not None,'at':high is not None},flush=True)
            if low is not None or high is None:
                print({'witness':low},flush=True)
                raise SystemExit(1)
