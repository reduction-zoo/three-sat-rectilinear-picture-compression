from source import source,solve,box,maximal_rectangles,product

def padded_source(d):
    cells,outputs=source(d)
    end=max(r for r,c in cells)
    for _,_,c,_ in outputs:cells|=box(c-1,end+1,c+1,end+4)
    outputs=[(a,end+3,c,c) for a,b,c,e in outputs]
    assert all(r in maximal_rectangles(frozenset(cells)) for r in outputs)
    return cells,outputs

if __name__=='__main__':
    for d in [1,2,3]:
        cells,outputs=padded_source(d)
        base=next(k for k in range(8*d+8,8*d+15) if solve(cells,cells,k) is not None)
        print({'degree':d,'baseline':base,'outputs':outputs},flush=True)
        for state in product((False,True),repeat=d):
            force=tuple(r for r,on in zip(outputs,state) if on)
            k=base+int(any(state))
            low=solve(cells,cells,k-1,forced=force);high=solve(cells,cells,k,forced=force)
            print({'state':state,'expected':k,'below':low is not None,'at':high is not None},flush=True)
            if low is not None or high is None:
                print({'witness':low},flush=True)
                raise SystemExit(1)
