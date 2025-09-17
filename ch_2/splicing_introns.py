"""
Here's a short section of genomic DNA:
ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGA
TCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACT
ACTAT

It comprises two exons and an intron. The first exon runs from the start of the
sequence to the sixty-third character, and the second exon runs from the ninetyfirst
character to the end of the sequence. Write a program that will print just the
coding regions of the DNA sequence.
"""

genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

# seeing the genomic dna and its length
print(genomic_dna)
print(len(genomic_dna))

# 123 characters in the genomic dna

first_exon = genomic_dna[0:62]
print(first_exon)

# making sure first exon goes up to 63rd character
print(len(first_exon))

# second exon runs from 91st to end of sequence 123rd
second_exon = genomic_dna[90:123]
print(second_exon)
print(len(second_exon))

# printing just the coding regions
# by concatenating the exons together
coding_regions = first_exon + second_exon
print(coding_regions)