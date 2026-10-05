def to_rna(dna_strand):
    rna_strand=""
    for nuc in dna_strand:
        if nuc=="G":
            rna_strand+="C"
        if nuc=="C":
            rna_strand+="G"
        if nuc=="T":
            rna_strand+="A"
        if nuc=="A":
            rna_strand+="U"
    return rna_strand