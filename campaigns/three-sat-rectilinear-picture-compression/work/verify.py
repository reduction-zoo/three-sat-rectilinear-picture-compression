"""Fresh-process command check for the legal empty-clause boundary."""
from pathlib import Path
import argparse,json,subprocess,sys
parser=argparse.ArgumentParser()
parser.add_argument('--candidate',type=Path,default=Path(__file__).with_name('algorithm.py'))
candidate=parser.parse_args().candidate.resolve()
for n in [0,3]:
    source={'n':n,'clauses':[]}
    result=subprocess.run([sys.executable,str(candidate)],input=json.dumps(source),text=True,capture_output=True,check=True)
    target=json.loads(result.stdout)
    assert target=={'matrix':[],'K':0}
    result=subprocess.run([sys.executable,str(candidate),'--extract'],input=json.dumps({'source':source,'target_solution':[]}),text=True,capture_output=True,check=True)
    answer=json.loads(result.stdout)
    assert len(answer)==n and all(type(v) is bool for v in answer)
print('Two empty-clause sources: actual target, empty cover, and fresh-process recovery passed.')
