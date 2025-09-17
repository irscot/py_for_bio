"""
Write a program that will split the genomic DNA into coding 
and non-coding parts, and write these sequences to two separate files.
"""

dna_file = open("gen_dna.txt")
dna = dna_file.read()


# make a seperate file for exons
coding_file = open("coding_dna.txt", "w")
first_exon = dna[0:62]
second_exon = dna[90:123]
coding_file.write(first_exon + second_exon)
coding_file.close()

# make a seperate file for the intron
noncoding_file = open("noncoding_dna.txt", "w")
intron = dna[63:89]
noncoding_file.write(intron)
noncoding_file.close()