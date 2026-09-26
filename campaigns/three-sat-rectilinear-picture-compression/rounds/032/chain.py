from turn import turn,solve,maximal_rectangles
for n in [2,4,6]:
    cells=set();local,supplied,_=turn()
    for i in range(n):
        j=i//2
        cells|={(r+14*j,c+14*j) if i%2==0 else (c+14*j,r+14*(j+1)) for r,c in local}
    out=(1+14*(n//2-1),12+14*(n//2-1),5+14*(n//2),5+14*(n//2))
    assert out in maximal_rectangles(frozenset(cells))
    costs=[]
    for inp,on in [(False,False),(False,True),(True,False),(True,True)]:
        need=cells-supplied if inp else cells
        lo,hi=0,10*n
        while lo<hi:
            mid=(lo+hi)//2
            if solve(cells,need,mid,forced=(out,) if on else ()) is None: lo=mid+1
            else: hi=mid
        costs.append(lo)
    print({'turns':n,'costs':costs,'expected_form':'B,B+1,B,B'},flush=True)
