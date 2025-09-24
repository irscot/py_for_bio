"""
Here's a list of made-up gene accession names:
xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp
Write a program that will print only the accession names that satisfy the following
criteria – treat each criterion separately:

• contain the number 5
• contain the letter d or e
• contain the letters d and e in that order
• contain the letters d and e in that order with a single letter between them
• contain both the letters d and e in any order
• start with x or y
• start with x or y and end with e
• contain three or more numbers in a row
• end with d followed by either a, r or p
"""
import re


# creating list of accession names
accession_names = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

# contain number 5
print("Accession names with a 5:")
for accession_name in accession_names:
    if re.search(r"5", accession_name):
        print(f"- {accession_name}")



