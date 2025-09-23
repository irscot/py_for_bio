"""
Print out the gene names for all genes between 90 and 110 bases long.
"""

# first index[0] = species name, second index[1] = sequence, 
# third index[2] = gene name, fourth index[3] = expression level

# rehashing the for loop from several_species.py
data = open(r"C:\Users\irsco\repos\py_for_bio\ch_6\data.csv")

for section in data:
    # getting rid of new line (\n) showing up in output by stripping the right
    # and using split method to seperate each part of the data by their commas
    # which brings each line into a list
    section = section.rstrip().split(",")
    gene_name = section[2]

    # getting length of sequence
    sequence = len(section[1])

    # using conditional for sequences with bases between 90 and 110
    # and printing those gene names with their number of bases
    # if they meet those conditions
    if sequence >= 90 and sequence <= 110:
        print(f"{gene_name}: {sequence} bases")