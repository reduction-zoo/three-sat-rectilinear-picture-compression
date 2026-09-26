from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'027'))
from probe import pair,solve,maximal_rectangles
from geometry import box

def translator(distance=8,wing='left'):
    cells,_,out=pair(distance+10)
    end=distance+5
    cells|=box(5,-5,7,-2)
    cells|=box(end-1 if wing=='left' else end,13,end+1 if wing=='left' else end+2,16)
    return cells,box(5,-5,6,10),(1,15,end,end)

if __name__=='__main__':
    for distance in [8,31]:
        for wing in ['left','right']:
            cells,inp,out=translator(distance,wing)
            assert out in maximal_rectangles(frozenset(cells))
            costs=[]
            for a,b in [(False,False),(False,True),(True,False),(True,True)]:
                need=cells-inp if a else cells
                costs.append(next(k for k in range(12,20) if solve(cells,need,k,forced=(out,) if b else ()) is not None))
            print({'distance':distance,'wing':wing,'costs':costs},flush=True)
