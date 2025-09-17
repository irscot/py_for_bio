"""
Modify the function from part one so that it accepts a list of amino acid residues
rather than a single one. If no list is given, the function should return the
percentage of hydrophobic amino acid residues (A, I, L, M, F, W, Y and V). Your
function should pass the following assertions:
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65
"""

def get_aa_percentage(protein, aa_list=['A','I','L','M','F','W','Y','V']):
    protein = protein.upper()
    protein_length = len(protein)
    total = 0
    for aa in aa_list:
        aa = aa.upper()
        aa_count = protein.count(aa)
        total = total + aa_count
    percentage = total * 100 / protein_length
    return percentage

assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65

print(len("MSRSLLLRFLLFLLLLPPLP"))
percentage = 1/20
print(percentage * 100, end="%\n")

print(get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "M"), end="%")