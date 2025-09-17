# removing the same 14 base pair sequencing adapter from
# each sequence in input.txt

# open the file
file = open(r"C:\Users\irsco\repos\py_for_bio\p4b_exercises(1)\exercises and examples\lists_and_loops\exercises\input.txt")

# making a new writable file with trimmed dna sequence
trimmed = open("trimmed.txt", "w")

# making a for loop to iterate over the original input.txt file
for dna in file:
    # creating a sequence adapter variable that inludes the same 
    # first 14 bases from the dna sequences
    seq_adapter = dna[0:14]
    trimmed_dna = dna.replace(seq_adapter, "")
    trimmed.write(trimmed_dna)

    # printing length of each trimmed dna to the screen
    length = len(trimmed_dna)
    print(f"Length of Trimmed DNA: {length}")