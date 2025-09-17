# calculating at content in a DNA sequence
# and printing the AT content of the DNA

dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"


# need to do a count of adenine and thymine in dna
# AT content = A+T/dna length

a_content = dna.count("A")
t_content = dna.count("T")
dna_length = len(dna)

at_content = (a_content+t_content)/dna_length

print("AT content:", at_content)