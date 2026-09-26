from pathlib import Path
import sys
from itertools import combinations
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'022'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'025'))
from geometry import maximal_rectangles
from kissat_cover import solve

def optimum(cells,need):
    return next(k for k in range(10) if solve(cells,need,k) is not None)

found=[];tested=0
for mask in range(1,512):
    cells={(i//3,i%3) for i in range(9) if mask>>i&1}
    ports=[]
    for c in range(3):
        end=next((r for r in range(3) if (r,c) not in cells),3)
        ports.append({(r,c) for r in range(end)})
    for a,b in combinations(range(3),2):
        if not ports[a] or not ports[b]:continue
        tested+=1
        costs=[optimum(cells,cells-s) for s in [set(),ports[a],ports[b],ports[a]|ports[b]]]
        if costs[0]==costs[1]+1 and costs[1]==costs[2]==costs[3]:
            found.append({'mask':mask,'columns':[a,b],'costs':costs,'cells':sorted(cells),'ports':[sorted(ports[a]),sorted(ports[b])]})
print({'tested':tested,'found':len(found),'examples':found[:10]},flush=True)
