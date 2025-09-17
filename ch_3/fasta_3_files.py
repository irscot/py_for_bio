# taking data from fasta.py and putting the sequences into 3 seperate files

# sequence 1
fasta_file_1 = open(r"c:/Users/irsco/repos/py_for_bio/ch_3/seq_1.fasta", "w")
sequence_header_1 = ">ABC123"
dna_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
fasta_file_1.write(sequence_header_1 + "\n" + dna_1)
fasta_file_1.close()


# sequence 2
fasta_file_2 = open(r"c:/Users/irsco/repos/py_for_bio/ch_3/seq_2.fasta", "w")
sequence_header_2 = ">DEF456"
dna_seq_2 = "actgatcgacgatcgatcgatcacgact"
dna_2 = dna_seq_2.upper()
fasta_file_2.write(sequence_header_2 + "\n" + dna_2)
fasta_file_2.close()


# sequence 3
fasta_file_3 = open(r"c:/Users/irsco/repos/py_for_bio/ch_3/seq_3.fasta", "w")
sequence_header_3 = ">HIJ789"
dna_seq_3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
dna_3 = dna_seq_3.replace("-", "")
fasta_file_3.write(sequence_header_3 + "\n" + dna_3)

fasta_file_3.close()