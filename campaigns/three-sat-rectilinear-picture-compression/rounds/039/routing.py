"""Sparse monotone permutation layout; all coordinates are integer boundaries."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'035'))
from cut import tile,solve,maximal_rectangles
from translator import translator
from capped_swap import capped_swap

class Layout:
    def __init__(self,positions):
        self.positions=dict(enumerate(positions));self.outputs={};self.external={}
        self.modules=[];self.interfaces=[];self.link_info=[];self.output_owner={};self.time=0;self.baseline=0

    def add(self,cells,inputs,outputs,labels,baseline,xmap):
        top=min(r for r,c in cells);bottom=max(r for r,c in cells)
        shift=self.time-top;owner=len(self.modules)
        def move(rect):
            a,b,c,d=rect
            return (a+shift,b+shift,xmap(c),xmap(d+1)-1)
        rectangles=[move(r) for r in maximal_rectangles(frozenset(cells))]
        input_rects=[]
        for supplied,label in zip(inputs,labels):
            c=next(iter(supplied))[1];end=max(r for r,cc in supplied)
            assert all(cc==c for r,cc in supplied)
            left=right=c
            while (top,left-1) in cells:left-=1
            while (top,right+1) in cells:right+=1
            previous=self.outputs.get(label)
            start=previous[1]+1 if previous else 0
            assert start<=self.time
            if start<self.time:rectangles.append((start,self.time-1,xmap(left),xmap(right+1)-1))
            incoming=(start,end+shift,xmap(c),xmap(c+1)-1)
            assert incoming[2]==incoming[3]
            input_rects.append(incoming)
            if previous:
                assert previous[2]==incoming[2]
                self.interfaces.append((previous[0],incoming[1],incoming[2],incoming[3]))
                self.link_info.append({"producer":self.output_owner[label],"consumer":owner,"label":label})
            else:self.external[label]=incoming
        moved=[move(r) for r in outputs]
        self.modules.append({'rectangles':rectangles,'inputs':input_rects,'outputs':moved,'labels':list(labels),'baseline':baseline,'kind':'route'})
        for label,out in zip(labels,moved):self.outputs[label]=out;self.positions[label]=out[2];self.output_owner[label]=owner
        self.baseline+=baseline;self.time=bottom+shift+4

    def translate(self,label,distance,wing='left'):
        assert distance>=8
        cells,inp,out=translator(8,wing)
        origin=self.positions[label]-5
        self.add(cells,[inp],[out],[label],16,lambda x:origin+x+(distance-8 if x>=10 else 0))

    def swap(self,left,right):
        assert self.positions[right]-self.positions[left]==11
        cells,inputs,outputs=capped_swap();origin=self.positions[left]-5
        self.add(cells,inputs,outputs,[left,right],46,lambda x:origin+x)


def permute(layout,target,pitch):
    n=len(target)
    remaining=sorted(target,key=lambda label:layout.positions[label])
    parking=max((layout.positions[label] for label in target),default=0)+3*pitch
    for wanted in reversed(target):
        at=remaining.index(wanted)
        while at+1<len(remaining):
            right=remaining[at+1]
            distance=layout.positions[right]-layout.positions[wanted]-11
            if distance:layout.translate(wanted,distance)
            layout.swap(wanted,right)
            remaining[at],remaining[at+1]=right,wanted
            at+=1
        remaining.pop()
        layout.translate(wanted,parking+pitch*target.index(wanted)-layout.positions[wanted])
    return layout


def route(target):
    n=len(target);assert sorted(target)==list(range(n))
    pitch=100*(n+1)**2
    return permute(Layout([pitch*i for i in range(n)]),target,pitch)


def compress(layout):
    rectangles=[r for m in layout.modules for r in m['rectangles']]
    extra=list(layout.external.values())+list(layout.outputs.values())+layout.interfaces
    ys=sorted({v for a,b,c,d in rectangles+extra for v in (a,b+1)})
    xs=sorted({v for a,b,c,d in rectangles+extra for v in (c,d+1)})
    ri={v:i for i,v in enumerate(ys)};ci={v:i for i,v in enumerate(xs)}
    def rank(rect):
        a,b,c,d=rect;return ri[a],ri[b+1]-1,ci[c],ci[d+1]-1
    owners={}
    for owner,module in enumerate(layout.modules):
        for rect in module['rectangles']:
            a,b,c,d=rank(rect)
            for r in range(a,b+1):
                for col in range(c,d+1):
                    assert owners.get((r,col),owner)==owner,('overlap',owner,owners[(r,col)],r,col)
                    owners[r,col]=owner
    cells=set(owners)
    supplies={name:{(r,c) for r in range(a,b+1) for c in range(d,e+1)} for name,rect in layout.external.items() for a,b,d,e in [rank(rect)]}
    outputs={name:rank(rect) for name,rect in layout.outputs.items()}
    interfaces={rank(rect) for rect in layout.interfaces}
    return cells,supplies,outputs,owners,interfaces,xs,ys

if __name__=='__main__':
    import json
    target=[2,1,0]
    layout=route(target)
    cells,inputs,outputs,owners,interfaces,xs,ys=compress(layout)
    rects=maximal_rectangles(frozenset(cells))
    crossing={rect for rect in rects if len({owners[r,c] for r in range(rect[0],rect[1]+1) for c in range(rect[2],rect[3]+1)})>1}
    print({'modules':len(layout.modules),'baseline':layout.baseline,'shape':[len(ys)-1,len(xs)-1],'cells':len(cells),'maximal_rectangles':len(rects),'interface_count':len(interfaces),'crossing_count':len(crossing)},flush=True)
    assert crossing==interfaces,{'extra':sorted(crossing-interfaces),'missing':sorted(interfaces-crossing)}
    assert all(r in rects for r in outputs.values())
    assert [name for name in sorted(outputs,key=lambda name:outputs[name][2])]==target
    for ins,outs in [((False,False,False),(False,False,False)),((False,False,False),(True,True,True)),((True,False,True),(True,False,True)),((False,True,False),(True,True,False))]:
        need=cells-set().union(*(inputs[i] for i,on in enumerate(ins) if on))
        forced=tuple(outputs[i] for i,on in enumerate(outs) if on)
        k=layout.baseline+sum(b and not a for a,b in zip(ins,outs))
        lo=solve(cells,need,k-1,forced=forced);hi=solve(cells,need,k,forced=forced)
        print({'in':ins,'out':outs,'expected':k,'below':lo is not None,'at':hi is not None},flush=True)
        assert lo is None and hi is not None
