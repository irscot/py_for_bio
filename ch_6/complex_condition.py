"""
Print out the gene names for all genes whose name begins with 
"k" or "h" except those belonging to Drosophila melanogaster.
"""


# first index[0] = species name, second index[1] = sequence, 
# third index[2] = gene name, fourth index[3] = expression level

data = open(r"C:\Users\irsco\repos\py_for_bio\ch_6\data.csv")

for section in data:
    # getting rid of new line (\n) showing up in output by stripping the right
    # and using split method to seperate each part of the data by their commas
    # which brings each line into a list
    section = section.rstrip().split(",")
    species_name = section[0]
    gene_name = section[2]


    # My Understanding of the program needed:
        # make a condition where the gene name 
        # startswith "k" or startswith "h"
        # and not equals Drosophila melanogaster

        # NOTE: Need to put the and first in order for this to work
        # otherwise it will bring in the D. melanogaster that starts with a k for the gene_name

    if species_name != "Drosophila melanogaster" and gene_name.startswith('k') or gene_name.startswith('h'):
        print(f"{species_name}: {gene_name}\n")