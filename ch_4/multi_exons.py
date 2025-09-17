"""
The file genomic_dna.txt contains a section of genomic DNA, 
and the file exons.txt contains a list of start/stop positions 
of exons. Each exon is on a separate line and the start and stop 
positions are separated by a comma. Write a program that will
extract the exon segments, concatenate them, and write them 
to a new file.
"""

gen_dna = open(r"C:\Users\irsco\repos\py_for_bio\p4b_exercises(1)\exercises and examples\lists_and_loops\exercises\genomic_dna.txt").read()

exon_positions = open(r"C:\Users\irsco\repos\py_for_bio\p4b_exercises(1)\exercises and examples\lists_and_loops\exercises\exons.txt")

# creating an empty string to add the exons to
coding_seq = ""

for seq in exon_positions:
    # using split() method to turn this into a [start:stop] position
    # essentially turning it into a list that will allow us to use
    # indexing
    positions = seq.split(',')
    # TESTING CODE: print(positions)

    # making start and stop variable to index into
    # while also turning them from strings to integers
    # for them to work as positional numbers when indexing
    start = int(positions[0])
    stop = int(positions[1])
    # TESTING CODE: print(f"Start: {start}\nStop: {stop}")

    exon = gen_dna[start:stop]
    print(f"Adding Exon...\n{exon}\n")

    # using the loop to add each exon to the empty string 
    # in the coding_seq variable above 
    coding_seq = coding_seq + exon
    print(f"Loading new coding sequence...\n{coding_seq}\n")

# creating comparisons between original and new dna sequences
print(f"Original DNA Sequence: {gen_dna}")
gen_dna_length = len(gen_dna)
print(f"Original DNA Sequence Length: {gen_dna_length}\n")

print(f"New DNA Sequence: {coding_seq}")
coding_seq_length = len(coding_seq)
print(f"New DNA Sequence Length: {coding_seq_length}\n")

# showing how many bases were removed from the original
remaining_bases = (int(gen_dna_length)) - (int(coding_seq_length))
print(f"{remaining_bases} bases were removed from the original DNA sequence")

 # writing "coding_seq" sequence to new file
new_sequence = open("coding_sequence.txt", "w")
new_sequence.write(coding_seq)

# closing file
new_sequence.close()