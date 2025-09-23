"""
For each gene, print out a message giving the gene name and 
saying whether its AT content is high (greater than 0.65), 
low (less than 0.45) or medium (between 0.45 and 0.65).
"""

# Conditional
# if at_content > 0:65 print high
# if at_content < 0:45 print low
# if at_content <=0.45 or at_content == 0.65 print medium

# defining a function for AT content
def get_at_content(dna):
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')

    length = len(section[1])

    at_content = (a_count + t_count) / length * 100
    return round(at_content)

data = open(r"C:\Users\irsco\repos\py_for_bio\ch_6\data.csv")
for section in data:
    section = section.rstrip().split(",")

    # NOTE: using sequence = len(section[1]) is not needed
    # the function is already taking care of that for us
    # just use sequence = section[1]
    # NOTE: changing sequence to length in the function 
    # deter from error

    sequence = section[1]
    gene_name = section[2]

    # using if-elif-else conditional for sequences
    # at various sizes in at_content

    if get_at_content(sequence) > 65:
        print(f"High AT content: {gene_name}")
    
    elif get_at_content(sequence) < 45:
        print(f"Low AT Content: {gene_name}")

    else:
        print(f"Medium AT Content: {gene_name}")