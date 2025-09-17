"""
Basic Conditionals

• equals (represented by ==)
• greater and less than (represented by > and <)
• greater and less than or equal to (represented by >= and <=)
• not equal (represented by!=)
• is a value in a list (represented by in)
• are two objects the same1 (represented by is)
"""

print(3 == 5) # False
print(3 > 5) # False
print(3 <=5) # True
print(len("ATGC") > 5) # False
print("GAATTC".count("T") > 1) # True
print("ATGCTT".startswith("ATG")) # True
print("ATGCTT".endswith("TTT")) # False
print("ATGCTT".isupper()) # True
print("ATGCTT".islower()) # False
print("V" in ["V", "W", "L"]) # True