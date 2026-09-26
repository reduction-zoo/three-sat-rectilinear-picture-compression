from itertools import product
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"005"))
from tile_probe import maximal_rectangles as reference
from geometry import maximal_rectangles

for bits in product((0,1),repeat=9):
    cells={(r,c) for r in range(3) for c in range(3) if bits[3*r+c]}
    assert set(maximal_rectangles(frozenset(cells))) == {rect for rect,_ in reference(cells,3,3)}
print("all maximal rectangles agree on 512 binary 3x3 pictures")
