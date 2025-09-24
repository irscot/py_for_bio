"""
Here's a list of made-up gene accession names:
xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp
Write a program that will print only the accession names that satisfy the following
criteria – treat each criterion separately:

• contain the number 5
• contain the letter d or e
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

# contain the letter d or e
print("Accession names with the letter d and/or e:")
for accession_name in accession_names:
    if re.search(r"d|e", accession_name):
        print(f"- {accession_name}")

# contain both the letters d and e in any order
print("Accession names with the letter d and e:")
for accession_name in accession_names:
    if re.search(r"d.*e|e.*d", accession_name):
        print(f"- {accession_name}")

# start with x or y
print("Accession names that start with x or y:")
for accession_name in accession_names:
    if re.search(r"^x|^y", accession_name):
        print(f"- {accession_name}")

# start with x or y and end with e
print("Accession names that start with x or y and end with e:")
for accession_name in accession_names:
    # sectioning off previous regex and adding onto it to include
    # any characters after it then end with an e
    if re.search(r"(^x|^y).*e$", accession_name):
        print(f"- {accession_name}")

# contain three or more numbers in a row
print("Accession names that have three or more numbers in a row:")
for accession_name in accession_names:
    # sectioning off numbers 0 to 9
    # with a range 3 to an unlimited amount in case of 
    # long accesion names with many numbers in a row
    if re.search(r"[0123456789]{3,}", accession_name):
        print(f"- {accession_name}")

# end with d followed by either a, r or p
print("Accession names ending with d followed by either a, r or p:")
# end point will be either an a, r or p (a|r|p)$
# needs to be followed up by a d = d(a|r|p)$
# using "5" to find any accession name that has 5
for accession_name in accession_names:
    if re.search(r"d(a|r|p)$", accession_name):
        print(f"- {accession_name}")