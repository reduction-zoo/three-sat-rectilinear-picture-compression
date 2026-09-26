from turn import solve
cells={(0,0),(0,1),(1,0)}
h=(0,0,0,1); v=(0,1,0,0)
assert solve(cells,cells,2,forbidden=(h,)) is None
assert solve(cells,cells,2,forced=(h,v)) is not None
assert solve(cells,cells,2,forced=(h,),forbidden=(h,)) is None
print('Forced/forbidden exact-rectangle constraints pass real L-picture checks.')
