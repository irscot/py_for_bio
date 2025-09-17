"""
Write a function that takes two arguments – a protein sequence and an amino acid
residue code – and returns the percentage of the protein that the amino acid makes
up. Use the following assertions to test your function:

assert get_percent_aa("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert get_percent_aa("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert get_percent_aa("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert get_percent_aa("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
"""

# making a function called get_percent_aa that has 
# and passing protein and aa_residue as arguments
def get_percent_aa(protein, aa_residue):

    # using upper() to account for lower case in assertion testing
    protein = protein.upper()
    aa_residue = aa_residue.upper()

    # getting count of protein in accordance to amino acid residue
    aa_count = protein.count(aa_residue)

    # getting length of protein's amino acids
    protein_length = len(protein)

    # getting amino acid percentage
    percentage = (aa_count/protein_length) * 100

    # returning % of protein that the amino acide makes up
    return(percentage)

# testing function
assert get_percent_aa("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert get_percent_aa("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert get_percent_aa("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert get_percent_aa("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

print(len("MSRSLLLRFLLFLLLLPPLP"))
percentage = 1/20
print(percentage * 100, end="%\n")

print(get_percent_aa("MSRSLLLRFLLFLLLLPPLP", "M"), end="%")