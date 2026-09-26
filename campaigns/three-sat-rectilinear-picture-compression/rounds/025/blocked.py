from switch_composition import switches
from geometry import box

def blocked(inputs,reset=True):
    cells,supplied,outgoing=switches(inputs)
    for j,a in enumerate(inputs):
        y,r=40*j,40+21*j
        cells-=box(r-8,y+30,r+1,y+33)
    if reset:
        height=40*(len(inputs)-1)+50
        for j in range(1,len(inputs)):
            for y in range(40*j,40*(j+1) if j+1<len(inputs) else height):
                local=y-40*j
                left=0 if local<12 else 1 if local<13 else 2 if local<15 else 3
                cells|=box(left,y,3*j+left,y+1)
    return cells,supplied,outgoing
