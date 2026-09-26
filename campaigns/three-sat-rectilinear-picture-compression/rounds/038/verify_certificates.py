from padded_source import padded_source
from pathlib import Path
from itertools import combinations
import json
for entry in json.loads(Path(__file__).with_name('certificates.json').read_text()):
    cells,outputs=padded_source(entry['degree'])
    forced=[tuple(r) for r,on in zip(outputs,entry['state']) if on]
    cover=[tuple(r) for r in entry['cover']];points=[tuple(p) for p in entry['lower_points']]
    k=9*entry['degree']+8+int(any(entry['state']))
    assert len(cover)==k and all(r in cover for r in forced)
    covered={(r,c) for a,b,d,e in cover for r in range(a,b+1) for c in range(d,e+1)}
    assert covered==cells and len(points)+len(forced)==k and set(points)<=cells
    assert all(not(a<=r<=b and d<=c<=e) for r,c in points for a,b,d,e in forced)
    for (r,c),(s,t) in combinations(points,2):
        assert any((y,x) not in cells for y in range(min(r,s),max(r,s)+1) for x in range(min(c,t),max(c,t)+1))
print('All 14 source-state upper/lower certificates pass direct cell and bounding-box checks; no solver used.')
