from flat_swap import flat_swap,solve,maximal_rectangles,product
cells,ins,outs=flat_swap()
combined=cells|{(r+65,c+39) for r,c in cells}
move=lambda r:(r[0]+65,r[1]+65,r[2]+39,r[3]+39)
outputs=[move(outs[1]),move(outs[0])]
assert all(r in maximal_rectangles(frozenset(combined)) for r in outputs)
lo,hi=0,105
while lo<hi:
    mid=(lo+hi)//2
    if solve(combined,combined,mid) is None:lo=mid+1
    else:hi=mid
base=lo
print({'baseline':base,'rectangles':len(maximal_rectangles(frozenset(combined)))},flush=True)
for a,b in product(product((False,True),repeat=2),repeat=2):
    need=combined-set().union(*(s for s,on in zip(ins,a) if on))
    forced=tuple(r for r,on in zip(outputs,b) if on)
    k=base+sum(y and not x for x,y in zip(a,b))
    low=solve(combined,need,k-1,forced=forced);high=solve(combined,need,k,forced=forced)
    print({'in':a,'out':b,'expected':k,'below':low is not None,'at':high is not None},flush=True)
    if low is not None or high is None:
        print({'witness':low},flush=True)
        raise SystemExit(1)
