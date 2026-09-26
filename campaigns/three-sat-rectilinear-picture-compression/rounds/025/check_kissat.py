from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'022'))
from geometry import cover
from kissat_cover import solve
for bits in range(1,512):
    cells={(i//3,i%3) for i in range(9) if bits>>i&1}
    for budget in range(5):
        actual=solve(cells,cells,budget)
        expected=cover(cells,cells,budget)
        assert (actual is None)==(expected is None),(bits,budget)
        if actual is not None: break
print('All 511 nonempty 3x3 pictures: minimum and rejecting budgets agree with Z3.')
