from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import valid_source_witness,NO
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'025'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'022'))
from kissat_cover import solve_cnf
from graph import source_graph,recover_graph
cases=json.loads((Path(__file__).resolve().parents[2]/'work/cases.json').read_text())
outputs=0
for index,case in enumerate(cases):
    g=source_graph(case['source']);cnf=[[a+1,b+1] for a,b in g['edges']]
    first=solve_cnf(g['n'],cnf,g['budget'])
    print({'case':index,'vertices':g['n'],'answer':'unsat' if first is None else 'sat'},flush=True)
    assert (first is None)==(case['expected']==NO)
    for _ in range(2):
        chosen=first if _==0 else solve_cnf(g['n'],cnf,g['budget'])
        if chosen is None:break
        C={i-1 for i in chosen}
        assignment=recover_graph(case['source'],g,C)
        assert valid_source_witness(case['source'],assignment)
        outputs+=1;cnf.append([-i if i in chosen else i for i in range(1,g['n']+1)])
print({'source_cases':len(cases),'decoded_graph_covers':outputs})
