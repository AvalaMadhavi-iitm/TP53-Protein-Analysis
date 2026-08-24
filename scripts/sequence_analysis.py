#!/usr/bin/env python3
"""
Basic TP53 protein sequence analysis.

Usage:
    python scripts/sequence_analysis.py
"""

from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
FASTA = ROOT / "data" / "tp53.fasta"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

VALID_AA = set("ACDEFGHIKLMNPQRSTVWY")

def read_fasta(path):
    lines = path.read_text().splitlines()
    header = lines[0]
    sequence = "".join(line.strip() for line in lines[1:] if line.strip())
    return header, sequence

def main():
    header, sequence = read_fasta(FASTA)
    invalid = sorted(set(sequence) - VALID_AA)

    if invalid:
        raise ValueError(f"Unexpected characters in sequence: {invalid}")

    counts = Counter(sequence)
    length = len(sequence)

    # Average residue masses in Da; approximate calculation.
    masses = {
        "A": 89.09, "R": 174.20, "N": 132.12, "D": 133.10, "C": 121.15,
        "E": 147.13, "Q": 146.15, "G": 75.07, "H": 155.16, "I": 131.17,
        "L": 131.17, "K": 146.19, "M": 149.21, "F": 165.19, "P": 115.13,
        "S": 105.09, "T": 119.12, "W": 204.23, "Y": 181.19, "V": 117.15
    }
    molecular_weight = sum(masses[a] for a in sequence) - 18.01528 * (length - 1)

    print(f"Protein: {header}")
    print(f"Length: {length} aa")
    print(f"Approx. molecular mass: {molecular_weight/1000:.2f} kDa")
    print("\nAmino-acid composition:")
    for aa in "ACDEFGHIKLMNPQRSTVWY":
        pct = 100 * counts[aa] / length
        print(f"{aa}: {counts[aa]:3d} ({pct:6.2f}%)")

if __name__ == "__main__":
    main()
