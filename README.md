# TP53 Protein Analysis

## Project title

**Computational Analysis of Human TP53 Protein and Disease-Associated Mutations**

## Overview

This beginner-friendly bioinformatics project analyzes the human TP53 protein using public biological databases and simple Python analysis.

TP53 encodes the cellular tumor antigen p53, a multifunctional transcription factor involved in cell-cycle arrest, DNA repair, and apoptosis.

## Objectives

1. Retrieve and document the human TP53 protein sequence.
2. Calculate basic sequence properties using Python.
3. Compare TP53 with related protein sequences using NCBI BLASTp.
4. Identify functional domains using InterPro.
5. Compile a small set of disease-associated/hotspot variants and verify them using authoritative databases.
6. Examine a TP53 DNA-binding-domain structure using RCSB PDB.
7. Visualize a selected residue such as R175 in PyMOL.

## Project workflow

```text
UniProt P04637
      |
      v
TP53 FASTA sequence
      |
      v
Python sequence analysis
      |
      +----> NCBI BLASTp
      |
      +----> InterPro domain analysis
      |
      +----> Variant analysis
      |
      v
RCSB PDB structure 2XWR
      |
      v
PyMOL visualization
```

## Repository structure

```text
TP53-Protein-Analysis/
├── README.md
├── requirements.txt
├── data/
│   ├── tp53.fasta
│   └── mutations.csv
├── scripts/
│   ├── sequence_analysis.py
│   └── download_pdb.py
├── results/
│   ├── sequence_analysis.txt
│   └── amino_acid_composition.csv
├── pymol/
│   └── visualize_R175H.pml
└── images/
```

## Data sources

- UniProt P04637: https://www.uniprot.org/uniprotkb/P04637
- UniProt FASTA service: https://rest.uniprot.org/uniprotkb/P04637.fasta
- NCBI BLAST: https://blast.ncbi.nlm.nih.gov/
- InterPro: https://www.ebi.ac.uk/interpro/
- ClinVar: https://www.ncbi.nlm.nih.gov/clinvar/
- RCSB PDB 2XWR: https://www.rcsb.org/structure/2XWR

## Step 1 — Run the basic Python analysis

From the repository root:

```bash
python scripts/sequence_analysis.py
```

This reads `data/tp53.fasta` and reports sequence length, approximate molecular mass, and amino-acid composition.

## Step 2 — BLASTp

1. Open NCBI BLAST.
2. Select Protein BLAST (blastp).
3. Paste the TP53 amino-acid sequence from `data/tp53.fasta`.
4. Run the search.
5. Record a small number of relevant hits.
6. Save the observations in a results file or table.

Important metrics:
- Percent identity
- Query coverage
- E-value
- Bit score

## Step 3 — Domain analysis

Search for TP53/P04637 in InterPro and record important functional domains and their sequence positions.

Do not copy large database descriptions into the project. Summarize the findings in your own words.

## Step 4 — Variant analysis

`data/mutations.csv` contains a small starting set of commonly studied TP53 variants.

Before making biological or clinical claims, verify each variant using current authoritative database records such as ClinVar and UniProt, and record the evidence/source used.

## Step 5 — Structure analysis

The project uses **PDB entry 2XWR**, a crystal structure of the human p53 DNA-binding domain with an extended N-terminus. RCSB reports a 1.68 Å resolution for this structure.

Download the structure:

```bash
python scripts/download_pdb.py
```

This creates:

```text
data/2XWR.pdb
```

Then open the file in PyMOL and run:

```text
@pymol/visualize_R175H.pml
```

The script highlights residue 175.

## Interpretation

The project should distinguish between:
- what was directly calculated from the sequence,
- what was retrieved from databases,
- and what is an interpretation based on published/database evidence.

Do not claim that a mutation causes a specific structural effect solely from visualization.

## Current basic result

The UniProt P04637 reference sequence contains **393 amino acids**. The calculated approximate molecular mass from the sequence is included in `results/sequence_analysis.txt`.

## Future improvements

- Add BLAST result tables.
- Add InterPro domain annotations.
- Add verified ClinVar/UniProt variant annotations.
- Add multiple sequence alignment.
- Add a TP53 structure image.
- Compare selected wild-type and mutant structures if suitable experimental structures are available.

## Note

This repository is designed as a learning project. Database records can change, so current database pages should be checked when the final report is prepared.
