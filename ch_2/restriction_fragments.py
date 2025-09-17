"""
The sequence contains a recognition site for the EcoRI restriction enzyme, which
cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk).
Write a program which will calculate the size of the two fragments that will be
produced when the DNA sequence is digested with EcoRI.
"""


my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
print(len(my_dna))

# EcoRI will cut the DNA after the G in "GAATTCT"

# using find() method to find GAATTC
# adding 1 to account for index position starts at 0
frag1_length = my_dna.find("GAATTC") + 1

# subtracting the full length of DNA with the
# first fragament to get the length of the 
# second fragment of DNA
frag2_length = len(my_dna) - frag1_length

print("length of fragment one is " + str(frag1_length))
print("length of fragment two is " + str(frag2_length))