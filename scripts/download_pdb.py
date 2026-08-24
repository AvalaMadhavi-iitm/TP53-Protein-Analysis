#!/usr/bin/env python3
# Download the selected experimental TP53 structure used by this project.
# Requires internet access.
#
# PDB ID: 2XWR
# RCSB page: https://www.rcsb.org/structure/2XWR

from pathlib import Path
from urllib.request import urlretrieve

out = Path(__file__).resolve().parents[1] / "data" / "2XWR.pdb"
url = "https://files.rcsb.org/download/2XWR.pdb"

print("Downloading:", url)
urlretrieve(url, out)
print("Saved to:", out)
