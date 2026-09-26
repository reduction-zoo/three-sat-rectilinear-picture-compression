from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'022'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'025'))
from beam_probe import demand as core
from geometry import box,maximal_rectangles
from kissat_cover import solve

def pair(span):
    cells={(10-r,c) for r,c in core}|{(r,span-c) for r,c in core}
    cells|=box(5,-2,span-8,6)|box(9,5,span-4,13)|box(8,0,span-7,11)
    supplied=box(5,-2,6,10)
    outgoing=(1,12,span-5,span-5)
    return cells,supplied,outgoing

if __name__=='__main__':
    for span in [18,24]:
        cells,supplied,out=pair(span)
        # The beam can broaden; choose a maximal extension containing the whole signal.
        options=[r for r in maximal_rectangles(frozenset(cells)) if r[0]<=out[0] and r[1]>=out[1] and r[2]<=out[2]<=r[3]]
        assert len(options)==1,options
        out=options[0]
        costs=[]
        for inp,on in [(False,False),(False,True),(True,False),(True,True)]:
            need=cells-supplied if inp else cells
            costs.append(next(k for k in range(8,18) if solve(cells,need,k,forced=(out,) if on else ()) is not None))
        print({'span':span,'costs':costs,'expected_form':'B,B+1,B,B','beam':out},flush=True)
