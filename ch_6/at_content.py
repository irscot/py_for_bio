"""
Print out the gene names for all genes whose AT content is 
less than 0.5 and whose expression level is greater than 200.
"""

# first index[0] = species name, second index[1] = sequence, 
# third index[2] = gene name, fourth index[3] = expression level

# rehashing the for loop from len_range.py
data = open(r"C:\Users\irsco\repos\py_for_bio\ch_6\data.csv")

# defining a function for AT content
def get_at_content(dna):
    a_count = dna[1].upper().count('A')
    t_count = dna[1].upper().count('T')

    # getting length of sequence
    length = len(section[1])

    # calculating at_content into a percentage
    at_content = ((a_count + t_count) / length) * 100
    return round(at_content)


print("Genes with AT Content > 50 and expression level > 200:")

for section in data:
    section = section.rstrip().split(",")
    sequence = section[1]
    gene_name = section[2]

    # creating expression level variable
    # and changing it into an integer
    exp_lvl = int(section[3])

    # TESTING CODE: printing and round up at content
    # print(f"AT Content of {gene_name}: {round(at_content, 2)}%")

    # using conditional for sequences with 
    # AT content < 50 and expression level > 200
    if get_at_content(sequence) < 50 and exp_lvl > 200:
        print(gene_name)