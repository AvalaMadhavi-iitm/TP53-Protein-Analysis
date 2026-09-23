# PDB ID: 2XWR
# RCSB page: https://www.rcsb.org/structure/2XWR

from pathlib import Path
from urllib.request import urlretrieve

out = Path("data") / "2XWR.pdb"
url = "https://files.rcsb.org/download/2XWR.pdb"

out.parent.mkdir(parents=True, exist_ok=True)
urlretrieve(url, out)

print(f"Downloaded to: {out}")
