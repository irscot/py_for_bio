"""
Translating a DNA sequence into an amino acid
"""
dna = "ATGTTCGGT"

# splitting up sequence into codons by slicing
# making three seperate codons
codon_one, codon_two, codon_three = dna[0:3], dna[3:6], dna[6:9]

print(codon_one, codon_two, codon_three)

# translate each codon into the corresponding amino acid residue

# adding gencode dictionary
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# printing codon one two and three
print(f"codon_one ({codon_one}) amino acid is {gencode[codon_one]}.")
print(f"codon_two ({codon_two}) amino acid is {gencode[codon_two]}.")
print(f"codon_three ({codon_three}) amino acid is {gencode[codon_three]}.")

print(f"Orginal DNA: {dna}")
print(f"Original DNA codons: {codon_one}, {codon_two} and {codon_three}")
print(f"codon amino acids: {gencode[codon_one]}, {gencode[codon_two]} and {gencode[codon_three]}")