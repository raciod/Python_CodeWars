def dna_to_rna(dna):
    rna = dna.replace("T","U")
    return rna


dna ="GCAT"
print(dna_to_rna(dna))
