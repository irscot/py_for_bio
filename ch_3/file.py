file = open(r"c:/Users/irsco/repos/py_for_bio/ch_3/examples/dna.txt")
file_contents = file.read()

dna_length = (len(file_contents))


print(f"Sequence: {file_contents}")
print("Sequence Length: " + str(dna_length) + " bases")
