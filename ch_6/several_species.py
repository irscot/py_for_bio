""" 
Printing out the gene names for all genes belonging to
 D. melanogaster or D. simulans
"""

# reading the data from the csv file
data = open("data.csv")

# writing for loop
for gene in data:
    if 