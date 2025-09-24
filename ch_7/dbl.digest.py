"""
In the chapter_7 file inside the exercises download, 
there's a file called dna.txt which contains a made-up DNA sequence. 

Predict the fragment lengths that we will
get if we digest the sequence with two made-up 
restriction enzymes – AbcI, whose
recognition site is ANT*AAT, and AbcII, whose recognition site 
is GCRW*TG (asterisks indicate the position of the cut site)
"""
import re

# opening dna.txt as dna to read in python file
dna = open(r"ch_7\dna.txt").read()

# making list with starting point 0 for all restriciton enzyme cuts
restriction_cuts = [0]

# need a search for restriction enzyme AbcI 
# that will look for A then any A|T|G|C and then TAAT
print("AbcI cut location:")
for match in re.finditer(r"A(A|T|G|C)TAAT", dna):
    # ATG is the starting codon so we need to start 3 bases in with +3
    print(match.start() + 3)