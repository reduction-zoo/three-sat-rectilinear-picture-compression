from picture import graph_picture,recover_cover,maximal_rectangles
from routing import solve
for graph in [{'n':2,'edges':[(0,1)],'budget':1},{'n':2,'edges':[(0,1)],'budget':0},{'n':3,'edges':[(0,1),(1,2)],'budget':1}]:
    target,(layout,origins,data)=graph_picture(graph)
    cells,_,_,owners,interfaces,xs,ys=data
    crossing={r for r in maximal_rectangles(frozenset(cells)) if len({owners[y,x] for y in range(r[0],r[1]+1) for x in range(r[2],r[3]+1)})>1}
    assert crossing==interfaces,{'extra':crossing-interfaces,'missing':interfaces-crossing}
    print({'vertices':graph['n'],'edges':len(graph['edges']),'budget':graph['budget'],'modules':len(layout.modules),'shape':[len(ys)-1,len(xs)-1],'K':target['K']},flush=True)
    witness=solve(cells,cells,target['K'])
    if graph['budget']==0:assert witness is None
    else:
        assert witness is not None
        chosen=recover_cover(graph,layout,origins,data,[list(r) for r in witness])
        print({'decoded_vertex_cover':sorted(chosen)},flush=True)
