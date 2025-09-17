"""
Using the data from part one, write a program 
that will calculate what percentage
of the DNA sequence is coding.
"""

genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

# seeing the genomic dna
print(genomic_dna)

first_exon = genomic_dna[0:62]
print(first_exon)

# second exon runs from 91 to 
# end of sequence 123
second_exon = genomic_dna[90:123]


# printing just the coding regions
# by concatenating the exons together
coding_regions = first_exon + second_exon
print(coding_regions)

# find lengths of the dna and the exons
dna = len(genomic_dna)
exons = len(coding_regions)

# dividing exons by dna to get percentage
print(round(exons/dna*100, 2), end="%")


"""
# we know the length of both exons and the dna itself
# we only need to know the length of the intron
introns = dna - exons
print(introns)
"""
