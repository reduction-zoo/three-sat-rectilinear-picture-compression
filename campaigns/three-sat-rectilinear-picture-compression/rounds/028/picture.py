"""Explicit closure of Figure 13 vector paths; no raster interpretation."""
import json
from pathlib import Path
from geometry import maximal_rectangles

def picture():
    paths=json.loads(Path(__file__).with_name('vector_paths.json').read_text())
    left=[(125,390.97),(125,438.22),(129.5,438.22),(129.5,442.72),(134,442.72),(134,447.22),(138.5,447.22),(138.5,564.22),(143,564.22),(143,568.72),(147.5,568.72),(147.5,573.22),(152,573.22),(152,663.22),(388.25,663.22),(388.25,612.82)]
    # Trace each machine backwards along its outside boundary.
    outer2=[(388.25,612.82),(393.65,612.82),(393.65,617.77),(398.6,617.77),(398.6,622.72),(413.45,622.72),(413.45,612.82),(408.5,612.82),(408.5,607.87),(403.55,607.87),(403.55,602.92),(393.65,602.92),(393.65,593.02),(388.25,593.02),(388.25,588.07),(383.3,588.07),(383.3,583.12),(373.4,583.12),(373.4,597.97),(378.35,597.97),(378.35,602.92),(383.3,602.92),(383.3,606.97),(320.75,606.97)]
    stairs2=[(320.75,570.97),(311.75,570.97),(311.75,561.97),(302.75,561.97),(302.75,552.97),(293.75,552.97),(293.75,543.97),(284.75,543.97),(284.75,534.97),(276.65,534.97),(276.65,508.87)]
    outer1=[(283.85,508.87),(283.85,514.72),(289.7,514.72),(289.7,521.02),(308.15,521.02),(308.15,508.87),(301.85,508.87),(301.85,502.57),(295.55,502.57),(295.55,497.17),(283.85,497.17),(283.85,484.57),(276.65,484.57),(276.65,478.27),(271.25,478.27),(271.25,471.97),(259.1,471.97),(259.1,490.42),(264.95,490.42),(264.95,497.17),(271.25,497.17),(271.25,502.57),(251,502.57)]
    stairs1=[(251,453.97),(239.75,453.97),(239.75,444.97),(230.75,444.97),(230.75,435.97),(221.75,435.97),(221.75,426.97),(212.75,426.97),(212.75,415.72),(203.75,415.72),(203.75,390.97)]
    boundary=left+outer2[1:]+stairs2+outer1+stairs1
    loops=[boundary]+[[tuple(a) for a,b in paths[0][i:j]] for i,j in [(0,8),(8,16),(16,22),(22,28)]]
    xs=sorted({x for loop in loops for x,y in loop});ys=sorted({y for loop in loops for x,y in loop})
    def inside(loop,x,y):
        return sum(a==c and min(b,d)<y<max(b,d) and a>x for (a,b),(c,d) in zip(loop,loop[1:]+loop[:1]))%2==1
    cells={(r,c) for r in range(len(ys)-1) for c in range(len(xs)-1) if sum(inside(loop,(xs[c]+xs[c+1])/2,(ys[r]+ys[r+1])/2) for loop in loops)%2}
    supplied=[{(r,c) for r,c in cells if xs[c]>=a and xs[c+1]<=b and ys[r+1]<=end} for a,b,end in [(174.5,176.75,483.22),(192.5,194.75,591.22)]]
    outputs=[]
    for a,b,start in [(271.25,276.65,478.27),(383.3,388.25,588.07)]:
        rect=(ys.index(start),len(ys)-2,xs.index(a),xs.index(b)-1)
        assert rect in maximal_rectangles(frozenset(cells)),rect
        outputs.append(rect)
    return cells,supplied,outputs
