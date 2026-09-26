from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'022'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'025'))
from geometry import box,maximal_rectangles
from kissat_cover import solve

def terminal(gap=11):
    base={(0,0),(0,1),(0,2),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(3,0),(3,1)}
    cells=set()
    for r,c in base:
        for x in (range(1,gap) if c==1 else [0 if c==0 else c+gap-2]):cells.add((r,x))
    cells|=box(-1,-2,1,0)|box(gap,-2,gap+2,0)
    inputs=[box(0,-2,1,1),box(gap,-2,gap+1,3)]
    return cells,inputs

if __name__=='__main__':
    for gap in [3,11,30]:
        cells,inputs=terminal(gap)
        costs=[]
        for a,b in [(False,False),(False,True),(True,False),(True,True)]:
            need=cells-(inputs[0] if a else set())-(inputs[1] if b else set())
            costs.append(next(k for k in range(10) if solve(cells,need,k) is not None))
        print({'gap':gap,'costs':costs},flush=True)
