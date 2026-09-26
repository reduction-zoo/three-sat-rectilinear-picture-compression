from pathlib import Path
import json,sys,z3
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import valid_source_witness,NO
from graph import source_graph,recover_graph
cases=json.loads((Path(__file__).resolve().parents[2]/'work/cases.json').read_text())
outputs=0
for index,case in enumerate(cases):
    g=source_graph(case['source']);xs=[z3.Bool(f'v{i}') for i in range(g['n'])];s=z3.SolverFor('QF_FD');s.set(timeout=30000)
    for a,b in g['edges']:s.add(z3.Or(xs[a],xs[b]))
    if xs:s.add(z3.PbLe([(x,1) for x in xs],g['budget']))
    first=s.check();assert first!=z3.unknown,(index,s.reason_unknown())
    print({'case':index,'vertices':g['n'],'answer':str(first)},flush=True)
    assert (first==z3.unsat)==(case['expected']==NO)
    for _ in range(2):
        if s.check()==z3.unsat:break
        model=s.model();bits=[z3.is_true(model.eval(x,model_completion=True)) for x in xs]
        C={i for i,on in enumerate(bits) if on}
        assignment=recover_graph(case['source'],g,C)
        assert valid_source_witness(case['source'],assignment)
        outputs+=1;s.add(z3.Or([x!=on for x,on in zip(xs,bits)]))
print({'source_cases':len(cases),'decoded_graph_covers':outputs})
