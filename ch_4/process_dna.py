# removing the same 14 base pair sequencing adapter from
# each sequence in input.txt

# open the file
file = open(r"C:\Users\irsco\repos\py_for_bio\p4b_exercises(1)\exercises and examples\lists_and_loops\exercises\input.txt")
for dna in file:
    print(dna)

# practice run to remove the first 14 bases from the first sequence
dna = "ATTCGATTATAAGCACTGATCGATCGATCGATCGATCGATGCTATCGTCGT"

# making sure that the first 14 bases are being taken up
# by printing the first 14 bases
# print(dna[0:15])

# making a list with all 4 sequences included
dna_seqs = ["ATTCGATTATAAGCACTGATCGATCGATCGATCGATCGATGCTATCGTCGT", 
            "ATTCGATTATAAGCATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC", 
            "ATTCGATTATAAGCACTATCGATGATCTAGCTACGATCGTAGCTGTA", 
            "ATTCGATTATAAGCACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTATGCA"]

# creating a sequence adapter variable that inludes the same 
# first 14 bases from the dna sequences
seq_adapter = dna[0:15]

# making a for loop to remove the sequence adapter
for dna_seq in dna_seqs:
    print(f"Original: {dna_seq}")
    print("Trimmed:  " + dna_seq.replace(seq_adapter, ""),"\n")