enzymes = {
'EcoRI' : r'GAATTC',
'AvaII' : r'GG(A|T)CC',
'BisI' : r'GC[ATGC]GC'
}

# using the dictionary name and the key will print the value
print(enzymes['BisI'])

# adding KpnI - GGTACC
enzymes['KpnI'] = r'GGTACC'
print(enzymes)