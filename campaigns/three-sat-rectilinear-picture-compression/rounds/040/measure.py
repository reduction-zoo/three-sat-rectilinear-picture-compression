from pathlib import Path
import json
from graph import source_graph
from picture import graph_layout,dimensions
cases=json.loads((Path(__file__).resolve().parents[2]/'work/cases.json').read_text())
for index in [2,16,40,70,110]:
    source=cases[index]['source'];g=source_graph(source);L,_=graph_layout(g);h,w=dimensions(L)
    print({'case':index,'variables':source['n'],'clauses':len(source['clauses']),'tracks':2*len(g['edges']),'modules':len(L.modules),'shape':[h,w],'cells':h*w},flush=True)
