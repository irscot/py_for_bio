protein = "vlspadktnv"

# replace valine with tyrosine
print(protein.replace("v", "y"))

# we can replace more than one character
print(protein.replace("vls", "ymt"))

# the original variable is not affected
print(protein)



# indexing:0123456789
protein = "vlspadktnv"

# taking a substring of the protein by slicing


# print positions three to five
# inclusive at start but exclusive at stop
# includes 3 up and stops before getting to 5
print(protein[3:5])

# positions start at zero, not one
print(protein[0:6])

# if we use a stop position beyond the end, it's the same as using the end
print(protein[0:60])

# indexing to only print valine (v)
print(protein[0])

protein = "vlspadktnv"

# count amino acid residues
valine_count = protein.count('v')
lsp_count = protein.count('lsp')
tryptophan_count = protein.count('w')

# now print the counts
print("valines: " + str(valine_count))
print("lsp: " + str(lsp_count))
print("tryptophans: " + str(tryptophan_count))


"""
transferring the protein.find() into a str in unecessary
'from page 33' in Python for Biologists

protein = "vlspadktnv"
print(str(protein.find('p')))
print(str(protein.find('kt')))
print(str(protein.find('w')))
"""

# finding the index of an amino acid within the protein
protein = "vlspadktnv"
print(protein.find('p'))
print(protein.find('kt'))
print(protein.find('w'))