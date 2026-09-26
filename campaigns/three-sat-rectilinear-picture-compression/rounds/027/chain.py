from probe import pair,solve,maximal_rectangles

def chain(n):
    cells=set()
    for i in range(n):
        local,_,_=pair(18)
        cells|={(r+14*i,c+8*i) for r,c in local}
    supplied=pair(18)[1]
    output=(1+14*(n-1),12+14*(n-1),13+8*(n-1),13+8*(n-1))
    return cells,supplied,output

for n in [1,2,3,4]:
    cells,supplied,out=chain(n)
    assert out in maximal_rectangles(frozenset(cells))
    for inp,on in [(False,False),(False,True),(True,False),(True,True)]:
        expected=14*n+int(on and not inp)
        need=cells-supplied if inp else cells
        low=solve(cells,need,expected-1,forced=(out,) if on else ())
        upper=solve(cells,need,expected,forced=(out,) if on else ())
        print({'pairs':n,'input':inp,'output':on,'expected':expected,'below':low is not None,'at':upper is not None},flush=True)
        if low is not None or upper is None:
            print({'witness':low},flush=True)
            raise SystemExit(1)
