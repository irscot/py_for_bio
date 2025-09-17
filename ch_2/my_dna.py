my_dna = "ATGCGTA"
print(my_dna)

my_dna = "AATT" + "GGCC"
print(my_dna)

upstream = "AAA"
downstream = "GGG"
my_dna = upstream + "ATGC" + downstream
print(my_dna)

dna_length = len(my_dna)
print("The length of the DNA sequence is " + str(dna_length))

print(my_dna.lower())
print(my_dna)