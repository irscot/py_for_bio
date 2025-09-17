# creating FASTA file to write 3 sequences of dna to
fasta_file = open(r"c:/Users/irsco/repos/py_for_bio/ch_3/dna_sequences.FASTA", "w")

sequence_header_1 = ">ABC123"
sequence_header_2 = ">DEF456"
sequence_header_3 = ">HIJ789"

# sequence 1 is fine so keeping it in the same variable naming sense
# as are final variables for the second and third dna sequences
# in other words it is matching dna_2 and dna_3 for consistancy
dna_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"

# fixing sequence 2
# use upper() to make the bases uppercase
dna_seq_2 = "actgatcgacgatcgatcgatcacgact"
# putting it as a different variable to write to the file
dna_2 = dna_seq_2.upper()

# fixing sequence 3
# replace "-" with empty string "" to get rid of the dashes
dna_seq_3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
# putting it as a different variable to write to the file
dna_3 = dna_seq_3.replace("-", "")

# writing to the FASTA file and make a new line
# to seperate header and dna sequences
fasta_file.write(sequence_header_1 + "\n" + dna_1 + "\n")
fasta_file.write("\n" + sequence_header_2 + "\n" + dna_2 + "\n")
fasta_file.write("\n" + sequence_header_3 + "\n" + dna_3 + "\n")

fasta_file.close()



