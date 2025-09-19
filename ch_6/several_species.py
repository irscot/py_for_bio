""" 
Printing out the gene names for all genes belonging to
 D. melanogaster or D. simulans
"""

# reading the data from the csv file
# each line is a row while each field in a line is a column

# first index[0] = species name, second index[1] = sequence, third index[2] = gene name, fourth index[3] = bases in sequence
data = open(r"C:\Users\irsco\repos\py_for_bio\ch_6\data.csv")

# writing for loop to loop over the data and print out gene names
# for each iteration of D. melanogaster or D. simulans
for section in data:
    # getting rid of new line (\n) showing up in output by stripping the right
    # and using split method to seperate each part of the data by their commas
    # which brings each line into a list
    section = section.rstrip().split(",")
    species_name = section[0]
    gene_name = section[2]
    print(f"Species name: {species_name}\nGene name: {gene_name}")    