from routing import route,compress,maximal_rectangles
from itertools import permutations
for target in list(permutations(range(3)))+[(3,2,1,0),(1,3,0,2)]:
    layout=route(target)
    cells,inputs,outputs,owners,interfaces,xs,ys=compress(layout)
    crossing={rect for rect in maximal_rectangles(frozenset(cells)) if len({owners[r,c] for r in range(rect[0],rect[1]+1) for c in range(rect[2],rect[3]+1)})>1}
    assert crossing==interfaces,('crossing',target,crossing-interfaces,interfaces-crossing)
    assert tuple(sorted(outputs,key=lambda k:outputs[k][2]))==target
    print({'target':target,'modules':len(layout.modules),'shape':[len(ys)-1,len(xs)-1],'interfaces':len(interfaces)},flush=True)
