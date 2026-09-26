from itertools import product
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"005"))
from tile_probe import maximal_rectangles as reference
from geometry import maximal_rectangles, cover

for bits in product((0,1),repeat=9):
    cells={(r,c) for r in range(3) for c in range(3) if bits[3*r+c]}
    assert set(maximal_rectangles(frozenset(cells))) == {rect for rect,_ in reference(cells,3,3)}
print("all maximal rectangles agree on 512 binary 3x3 pictures")
ell=frozenset({(0,0),(0,1),(1,0)})
horizontal,vertical=(0,0,0,1),(0,1,0,0)
assert cover(ell,{(0,0)},1,forced=(horizontal,vertical)) is None
assert set(cover(ell,{(0,0)},2,forced=(horizontal,vertical))) == {horizontal,vertical}
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"work"))
from check import target_solutions,NO
for bits in product((0,1),repeat=9):
    cells={(r,c) for r in range(3) for c in range(3) if bits[3*r+c]}
    if not cells:
        continue
    matrix=[list(bits[3*r:3*r+3]) for r in range(3)]
    for k in range(1,6):
        expected=target_solutions({"matrix":matrix,"K":k},1)!=[NO]
        assert (cover(cells,cells,k) is not None)==expected
        if expected:
            break
print("511 nonempty patterns: reduced clauses and native solver agree with Prepare")
