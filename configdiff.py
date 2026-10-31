import argparse,difflib
from pathlib import Path
def compare(a,b):
 left=Path(a).read_text(encoding="utf-8",errors="replace").splitlines()
 right=Path(b).read_text(encoding="utf-8",errors="replace").splitlines()
 return "\n".join(difflib.unified_diff(left,right,fromfile=str(a),tofile=str(b),lineterm=""))
def main():
 p=argparse.ArgumentParser();p.add_argument("before");p.add_argument("after");x=p.parse_args();print(compare(x.before,x.after))
if __name__=="__main__":main()
