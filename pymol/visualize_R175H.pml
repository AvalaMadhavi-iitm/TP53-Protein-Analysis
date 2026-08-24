# PyMOL script for the TP53 DNA-binding domain structure 2XWR.
# Download 2XWR from RCSB PDB and place it at data/2XWR.pdb before running.
#
# In PyMOL:
#   cd /path/to/TP53-Protein-Analysis
#   @pymol/visualize_R175H.pml

load data/2XWR.pdb, tp53
hide everything, tp53
show cartoon, tp53
color gray80, tp53

# Highlight residue 175 (R175 in the reference structure).
select R175, chain A and resi 175
show sticks, R175
color red, R175
zoom R175, 8

# Optional: save an image after positioning the structure.
# ray 1200,900
# png images/TP53_R175H_location.png, dpi=200
