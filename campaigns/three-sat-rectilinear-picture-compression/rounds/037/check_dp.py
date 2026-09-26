from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'022'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'025'))
from geometry import maximal_rectangles
from kissat_cover import solve
from residual import oracle
for mask in range(1,512):
    cells={(i//3,i%3) for i in range(9) if mask>>i&1}
    opt=oracle(cells)
    for need in [cells,{p for p in cells if p[1]!=0}]:
        k=opt(need)
        assert solve(cells,need,k) is not None
        assert k==0 or solve(cells,need,k-1) is None
print('Residual DP: 1022 full/partial cases agree with independently encoded Kissat bounds.')
