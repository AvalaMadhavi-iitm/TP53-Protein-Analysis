# TP53 Protein Analysis

## Overview

This project presents a computational analysis of the human TP53 protein (UniProt: P04637) using sequence analysis, similarity searching, domain annotation, variant analysis, and 3D structural visualization.

The workflow combines Python-based analysis with established bioinformatics resources including UniProt, NCBI BLASTp, InterPro, ClinVar, RCSB PDB, and PyMOL.

---

## Objectives

- Analyze the primary sequence of human TP53.
- Calculate amino-acid composition and basic sequence properties.
- Identify similar proteins using BLASTp.
- Identify protein families and functional domains using InterPro.
- Analyze selected TP53 variants using ClinVar.
- Visualize the TP53 protein structure and highlight residue R175 using PyMOL.

---

## Workflow

```text
TP53 Reference Sequence
          |
          v
   Sequence Analysis
          |
          v
Amino-Acid Composition
          |
          v
      BLASTp
          |
          v
   InterPro Analysis
          |
          v
   ClinVar Variants
          |
          v
   RCSB PDB Structure
          |
          v
   PyMOL Visualization
