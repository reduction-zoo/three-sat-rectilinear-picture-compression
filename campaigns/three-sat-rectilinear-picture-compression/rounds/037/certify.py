from padded import terminal,solve
from itertools import combinations
import json
from pathlib import Path
cells,ports=terminal(3)
results=[]
for bits in [(False,False),(False,True),(True,False),(True,True)]:
    need=cells-(ports[0] if bits[0] else set())-(ports[1] if bits[1] else set())
    k=5 if any(bits) else 6
    def incompatible(a,b):
        return any((r,c) not in cells for r in range(min(a[0],b[0]),max(a[0],b[0])+1) for c in range(min(a[1],b[1]),max(a[1],b[1])+1))
    pack=next((p for p in combinations(sorted(need),k) if all(incompatible(a,b) for a,b in combinations(p,2))),None)
    witness=solve(cells,need,k)
    assert pack is not None and witness is not None
    results.append({'inputs':bits,'lower_bound':pack,'cover':witness})
Path(__file__).with_name('certificates.json').write_text(json.dumps(results,indent=2)+'\n')
print('All four terminal states have directly checkable antirectangle and cover certificates.')
