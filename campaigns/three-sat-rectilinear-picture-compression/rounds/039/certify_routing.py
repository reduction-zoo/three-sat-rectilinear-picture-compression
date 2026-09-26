from pathlib import Path
import sys,json
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'038'))
from certify import packing
from capped_swap import capped_swap,solve
from translator import translator
results=[]
for kind,cells,inputs,outputs,base in [('swap',*capped_swap(),46)]+[(wing,*((lambda a:(a[0],[a[1]],[a[2]]))(translator(8,wing))),16) for wing in ['left','right']]:
    for a,b in product(product((False,True),repeat=len(inputs)),repeat=2):
        need=cells-set().union(*(s for s,on in zip(inputs,a) if on))
        forced=tuple(r for r,on in zip(outputs,b) if on)
        k=base+sum(y and not x for x,y in zip(a,b))
        pack=packing(cells,forced,k-len(forced),required=need)
        print({'kind':kind,'in':a,'out':b,'packing':pack if isinstance(pack,str) else len(pack)},flush=True)
        if isinstance(pack,str):raise SystemExit(1)
        witness=solve(cells,need,k,forced=forced)
        assert witness is not None
        results.append({'kind':kind,'inputs':a,'outputs':b,'points':pack,'forced':forced,'cover':witness})
Path(__file__).with_name('certificates.json').write_text(json.dumps(results,indent=2)+'\n')
