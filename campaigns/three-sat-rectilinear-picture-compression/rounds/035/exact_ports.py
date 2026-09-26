from cut import tile,solve,product
cells,inputs,outputs=tile()
for a,b in product(product((False,True),repeat=2),repeat=2):
    need=cells-set().union(*(s for s,on in zip(inputs,a) if on))
    forced=tuple(r for r,on in zip(outputs,b) if on)
    forbidden=tuple(r for r,on in zip(outputs,b) if not on)
    k=next(k for k in range(44,49) if solve(cells,need,k,forced=forced,forbidden=forbidden) is not None)
    print({'in':a,'out':b,'exact_cost':k},flush=True)
