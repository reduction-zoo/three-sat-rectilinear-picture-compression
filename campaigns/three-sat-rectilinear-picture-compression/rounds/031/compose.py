from crossing import crossing,solve,maximal_rectangles,product
cells,ins,outs=crossing()
shift=lambda p:(p[0]+14,p[1]+30)
combined=cells|{shift(p) for p in cells}
inputs=[ins[0],ins[1],{shift(p) for p in ins[1]}]
move=lambda r:(r[0]+14,r[1]+14,r[2]+30,r[3]+30)
outputs=[move(outs[0]),outs[1],move(outs[1])]
for r in outputs:
    assert r in maximal_rectangles(frozenset(combined)),r
for a,b in product(product((False,True),repeat=3),repeat=2):
    need=combined-set().union(*(s for s,on in zip(inputs,a) if on))
    forced=tuple(r for r,on in zip(outputs,b) if on)
    k=56+sum(y and not x for x,y in zip(a,b))
    low=solve(combined,need,k-1,forced=forced)
    high=solve(combined,need,k,forced=forced)
    print({'in':a,'out':b,'expected':k,'below':low is not None,'at':high is not None},flush=True)
    if low is not None or high is None:
        print({'witness':low},flush=True)
        raise SystemExit(1)
