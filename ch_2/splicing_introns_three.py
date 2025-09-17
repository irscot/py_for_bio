"""
Using the data from part one, write a program that will print out the original
genomic DNA sequence with coding bases in uppercase and non-coding bases (intron) in
lowercase.
"""

genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

# seeing the genomic dna and its length
print(genomic_dna)
print(len(genomic_dna))

# first exon has the first 63 characters so
# it will get the [0:62] as the index
first_exon = genomic_dna[0:62]
print("\n")
print(first_exon)

# the intron will be between the two exons
# intron will start where the first exon stopped(62)
# and stop before where the second exon started(89) 
intron = genomic_dna[62:89]
print("\n")
print(intron)

# second exon runs from 90 to end of the sequence 123
second_exon = genomic_dna[90:123]
print("\n")
print(second_exon)

# intron(non-coding bases) need to be lowercase
new_genomic_dna = first_exon + intron.lower() + second_exon