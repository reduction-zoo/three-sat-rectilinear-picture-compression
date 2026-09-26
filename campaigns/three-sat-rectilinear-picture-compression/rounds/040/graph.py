"""Deterministic occurrence-cycle reduction to degree-three Vertex Cover."""
def source_graph(source):
    n=source['n'];clauses=source['clauses']
    if type(n) is not int or n<0 or not isinstance(clauses,list):raise ValueError('invalid source')
    occurrences=[[] for _ in range(n)]
    for j,clause in enumerate(clauses):
        if not isinstance(clause,list) or len(clause)!=3:raise ValueError('three literals required')
        for k,lit in enumerate(clause):
            if type(lit) is not int or not 1<=abs(lit)<=n:raise ValueError('invalid literal')
            occurrences[abs(lit)-1].append((j,k,lit))
    edges=set();variables=[];ports={};size=0
    for occurrences_of_variable in occurrences:
        t=len(occurrences_of_variable);vertices=list(range(size,size+2*t));size+=2*t;variables.append(vertices)
        for k in range(2*t):
            a,b=vertices[k],vertices[(k+1)%(2*t)]
            edges.add(tuple(sorted((a,b))))
        for k,(j,pos,lit) in enumerate(occurrences_of_variable):ports[j,pos]=vertices[2*k+int(lit<0)]
    clause_vertices=[]
    for j in range(len(clauses)):
        vertices=list(range(size,size+3));size+=3;clause_vertices.append(vertices)
        for k in range(3):
            edges.add(tuple(sorted((vertices[k],vertices[(k+1)%3]))))
            edges.add(tuple(sorted((vertices[k],ports[j,k]))))
    return {'n':size,'edges':sorted(edges),'variables':variables,'clauses':clause_vertices,'budget':sum(len(v)//2 for v in variables)+2*len(clauses)}


def recover_graph(source,graph,chosen):
    if len(chosen)>graph['budget'] or any(a not in chosen and b not in chosen for a,b in graph['edges']):raise ValueError('invalid graph cover')
    assignment=[bool(v and v[0] in chosen) for v in graph['variables']]
    if not all(any(assignment[abs(l)-1]==(l>0) for l in c) for c in source['clauses']):raise ValueError('graph decoder invariant failed')
    return assignment
