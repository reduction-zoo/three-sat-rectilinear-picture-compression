"""Compose a bounded-degree graph into a sparse polygon and decode any cover."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'039'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'038'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'037'))
from routing import Layout,permute,compress,maximal_rectangles
from padded_source import padded_source
from padded import terminal


def graph_layout(graph):
    adjacent=[[] for _ in range(graph['n'])]
    for e,(a,b) in enumerate(graph['edges']):adjacent[a].append(e);adjacent[b].append(e)
    if any(len(a)>3 for a in adjacent):raise ValueError('maximum degree three required')
    count=2*len(graph['edges']);pitch=100*(count+1)**2+1;stretch=(pitch-1)//5
    layout=Layout([]);origins={};edge_labels=[[] for _ in graph['edges']];cursor=0;label=0
    for v,edges in enumerate(adjacent):
        if not edges:continue
        labels=list(range(label,label+len(edges)));label+=len(edges)
        for name,e in zip(labels,edges):origins[name]=v;edge_labels[e].append(name)
        cells,outputs=padded_source(len(edges));beams={r[2] for r in outputs}
        lo=min(c for r,c in cells);hi=max(c for r,c in cells)+1
        coordinates={lo:cursor}
        for c in range(lo,hi):coordinates[c+1]=coordinates[c]+(1 if c in beams else stretch)
        layout.add(cells,[],outputs,list(reversed(labels)),9*len(edges)+8,coordinates.__getitem__)
        layout.modules[-1].update(kind='source',vertex=v)
        cursor=coordinates[hi]+2*pitch
    target=[name for pair in edge_labels for name in pair]
    if target:permute(layout,target,pitch)
    for e,(first,second) in enumerate(edge_labels):
        layout.translate(first,8,wing='right')
        gap=layout.positions[second]-layout.positions[first]
        assert gap>=3
        cells,inputs=terminal(3);origin=layout.positions[first]
        layout.add(cells,inputs,[],[first,second],5,lambda x:origin+x+(gap-3 if x>=2 else 0))
        layout.modules[-1].update(kind='terminal',edge=e)
    return layout,origins


def dimensions(layout):
    rects=[r for module in layout.modules for r in module['rectangles']]+list(layout.outputs.values())+layout.interfaces
    ys={v for a,b,c,d in rects for v in (a,b+1)};xs={v for a,b,c,d in rects for v in (c,d+1)}
    return max(0,len(ys)-1),max(0,len(xs)-1)


def graph_picture(graph):
    layout,origins=graph_layout(graph)
    if not layout.modules:return {'matrix':[],'K':graph['budget']},(layout,origins,None)
    data=compress(layout);cells,_,_,_,_,xs,ys=data
    matrix=[[0]*(len(xs)-1) for _ in range(len(ys)-1)]
    for r,c in cells:matrix[r][c]=1
    return {'matrix':matrix,'K':layout.baseline+graph['budget']},(layout,origins,data)


def recover_cover(graph,layout,origins,data,witness):
    cells,_,_,owners,interfaces,xs,ys=data
    rects=maximal_rectangles(frozenset(cells))
    normalized=set()
    for item in witness:
        if not isinstance(item,list) or len(item)!=4 or any(type(v) is not int for v in item):raise ValueError('invalid rectangle')
        a,b,c,d=item
        candidates=[r for r in rects if r[0]<=a<=b<=r[1] and r[2]<=c<=d<=r[3]]
        if not candidates:raise ValueError('illegal cover rectangle')
        normalized.add(candidates[0])
    covered={(r,c) for a,b,d,e in normalized for r in range(a,b+1) for c in range(d,e+1)}
    if covered!=cells or len(witness)>layout.baseline+graph['budget']:raise ValueError('invalid cover')
    ri={v:i for i,v in enumerate(ys)};ci={v:i for i,v in enumerate(xs)}
    signal_in=[set() for _ in layout.modules];signal_out=[set() for _ in layout.modules]
    for rect,info in zip(layout.interfaces,layout.link_info):
        a,b,c,d=rect;rank=(ri[a],ri[b+1]-1,ci[c],ci[d+1]-1)
        if rank in normalized:
            signal_out[info['producer']].add(info['label']);signal_in[info['consumer']].add(info['label'])
    chosen=set()
    for i,module in enumerate(layout.modules):
        if module['kind']=='source':
            if signal_out[i]:chosen.add(module['vertex'])
        elif module['kind']=='route':
            for name in signal_out[i]-signal_in[i]:chosen.add(origins[name])
        elif not signal_in[i]:chosen.add(origins[module['labels'][0]])
    if len(chosen)>graph['budget'] or any(a not in chosen and b not in chosen for a,b in graph['edges']):raise ValueError('charging invariant failed')
    return chosen
