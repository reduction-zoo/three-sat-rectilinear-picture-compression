from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'027'))
from probe import pair,solve,maximal_rectangles

def turn():
    cells,supplied,_=pair(24)
    cells={p for p in cells if p[1]<=12}
    supplied &=cells
    # Whole horizontal beam includes the five-cell-wide core interval.
    output=(5,5,1,12)
    return cells,supplied,output

if __name__=='__main__':
    cells,supplied,out=turn()
    assert out in maximal_rectangles(frozenset(cells))
    for inp,on in [(False,False),(False,True),(True,False),(True,True)]:
        need=cells-supplied if inp else cells
        k=next(k for k in range(5,12) if solve(cells,need,k,forced=(out,) if on else ()) is not None)
        print({'input':inp,'output_required':on,'cost':k},flush=True)
