"""
Translating a DNA sequence into an amino acid
"""
dna = "ATGTTCGGT"

# splitting up sequence into codons by slicing
# making three seperate codons
codon_one, codon_two, codon_three = dna[0:3], dna[3:6], dna[6:9]

print(codon_one, codon_two, codon_three)