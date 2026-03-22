import sys
from pathlib import Path

path_to_src = Path(__file__).resolve().parent.parent / "src"
sys.path.append(str(path_to_src))
