from capped_swap import capped_swap
from translator import translator
from pathlib import Path
from itertools import combinations
import json
for e in json.loads(Path(__file__).with_name('certificates.json').read_text()):
    if e['kind']=='swap':cells,inputs,outputs=capped_swap();base=46
    else:
        cells,inp,out=translator(8,e['kind']);inputs=[inp];outputs=[out];base=16
    need=cells-set().union(*(s for s,on in zip(inputs,e['inputs']) if on))
    forced=[tuple(r) for r,on in zip(outputs,e['outputs']) if on]
    witness=[tuple(r) for r in e['cover']];points=[tuple(p) for p in e['points']]
    k=base+sum(b and not a for a,b in zip(e['inputs'],e['outputs']))
    covered={(r,c) for a,b,d,f in witness for r in range(a,b+1) for c in range(d,f+1)}
    assert need<=covered<=cells and len(witness)==k and all(r in witness for r in forced)
    assert len(points)+len(forced)==k and set(points)<=need
    assert all(not(a<=r<=b and d<=c<=f) for r,c in points for a,b,d,f in forced)
    for (r,c),(s,t) in combinations(points,2):
        assert any((y,x) not in cells for y in range(min(r,s),max(r,s)+1) for x in range(min(c,t),max(c,t)+1))
print('All 24 routing-state cover/antirectangle certificates pass direct checks without a solver.')
