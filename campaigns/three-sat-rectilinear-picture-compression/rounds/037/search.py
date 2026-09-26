from pathlib import Path
import sys,json
from itertools import combinations
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'022'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'025'))
from geometry import maximal_rectangles
from kissat_cover import solve
from residual import oracle
count=0
for mask in range(1,65536):
    cells={(i//4,i%4) for i in range(16) if mask>>i&1}
    ports=[]
    for c in range(4):
        end=next((r for r in range(4) if (r,c) not in cells),4)
        ports.append({(r,c) for r in range(end)})
    opt=oracle(cells);base=opt(cells)
    for a,b in combinations(range(4),2):
        if not ports[a] or not ports[b] or ("--separated" in sys.argv and b-a<int(sys.argv[sys.argv.index("--separated")+1])):continue
        count+=1
        if opt(cells-ports[a])!=base-1 or opt(cells-ports[b])!=base-1:continue
        if opt(cells-ports[a]-ports[b])!=base-1:continue
        result={'mask':mask,'columns':[a,b],'cells':sorted(cells),'ports':[sorted(ports[a]),sorted(ports[b])],'costs':[base,base-1,base-1,base-1],'tested':count}
        for supplied,k in zip([set(),ports[a],ports[b],ports[a]|ports[b]],result['costs']):
            assert solve(cells,cells-supplied,k) is not None
            assert solve(cells,cells-supplied,k-1) is None
        print(result,flush=True)
        Path(__file__).with_name('terminal_separated.json' if '--separated' in sys.argv else 'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
        break
    else:
        maximal_rectangles.cache_clear()
        continue
    break
else:print({'tested':count,'found':0},flush=True)
