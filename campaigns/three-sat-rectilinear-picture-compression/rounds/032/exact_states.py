from turn import turn,solve
cells,supplied,out=turn()
for inp in [False,True]:
    for on in [False,True]:
        need=cells-supplied if inp else cells
        k=next(k for k in range(5,12) if solve(cells,need,k,forced=(out,) if on else (),forbidden=() if on else (out,)) is not None)
        expected=9-int(inp)+int(inp==on)
        print({'input':inp,'output':on,'cost':k,'potential_prediction':expected},flush=True)
