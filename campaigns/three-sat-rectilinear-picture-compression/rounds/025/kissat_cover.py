"""Exact cover via installed Kissat; independent SAT backend for hard probes."""
import subprocess
from geometry import maximal_rectangles

def solve(cells,required,budget,forced=(),timeout=30):
    assert required<=cells and budget>=0
    rects=maximal_rectangles(frozenset(cells)); n=len(rects)
    clauses={frozenset(i+1 for i,(a,b,d,e) in enumerate(rects) if a<=r<=b and d<=c<=e) for r,c in required}
    cnf=[]
    for clause in sorted(clauses,key=len):
        if not any(set(other)<=clause for other in cnf): cnf.append(list(clause))
    for rect in forced: cnf.append([rects.index(rect)+1])
    var=n; prev=[]
    for x in range(1,n+1):
        curr=list(range(var+1,var+min(x,budget+1)+1)); var+=len(curr)
        cnf.append([-x,curr[0]])
        for j,v in enumerate(prev):
            cnf.append([-v,curr[j]])
            if j+1<len(curr): cnf.append([-x,-v,curr[j+1]])
        if len(curr)>budget: cnf.append([-curr[budget]])
        prev=curr
    data=f'p cnf {var} {len(cnf)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in cnf)
    result=subprocess.run(['kissat','--quiet'],input=data,text=True,capture_output=True,timeout=timeout)
    if result.returncode==20: return None
    if result.returncode!=10: raise RuntimeError(result.stderr+result.stdout)
    chosen={int(v) for line in result.stdout.splitlines() if line.startswith('v ') for v in line.split()[1:] if int(v)>0}
    witness=[r for i,r in enumerate(rects,1) if i in chosen]
    covered={(r,c) for a,b,d,e in witness for r in range(a,b+1) for c in range(d,e+1)}
    assert required<=covered<=cells and len(witness)<=budget and all(r in witness for r in forced)
    return witness
