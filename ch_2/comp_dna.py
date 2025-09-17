dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"


# taking advantage of case sensitivity
# to replace these nucleotides better

replacement1 = dna.replace('A', 't')
replacement2 = replacement1.replace('T', 'a')
replacement3 = replacement2.replace('C', 'g')
comp_dna = replacement4 = replacement3.replace('G', 'c')
# printing replacement4 with upper() method to
# put the comp DNA in all upper case
print(dna)
print(comp_dna.upper())
