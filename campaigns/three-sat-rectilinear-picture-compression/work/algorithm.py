"""Unverified integrated candidate. Read proof.md and verification.md before use."""
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'rounds/040'))
from graph import source_graph,recover_graph
from picture import graph_picture,graph_layout,compress,recover_cover


def forward(source):
    target,_=graph_picture(source_graph(source))
    return target


def extract(source,witness):
    graph=source_graph(source)
    if witness=='NO-SOLUTION':return 'NO-SOLUTION'
    layout,origins=graph_layout(graph)
    if not layout.modules:
        if witness!=[]:raise ValueError('empty picture requires empty cover')
        return [False]*source['n']
    chosen=recover_cover(graph,layout,origins,compress(layout),witness)
    return recover_graph(source,graph,chosen)


if __name__=='__main__':
    item=json.load(sys.stdin)
    answer=extract(item['source'],item['target_solution']) if sys.argv[1:]==['--extract'] else forward(item)
    json.dump(answer,sys.stdout,separators=(',',':'))
    print()
