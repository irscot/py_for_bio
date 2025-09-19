"""
Basic Conditionals

• equals (represented by ==)
• greater and less than (represented by > and <)
• greater and less than or equal to (represented by >= and <=)
• not equal (represented by!=)
• is a value in a list (represented by in)
• are two objects the same (represented by is)
"""

# 3 does not equal 5 so saying 3 equals 5 will come back false
print(3 == 5) # False

# 3 is not greater than 5
print(3 > 5) # False

# 3 is less than 5 so it meets the less than or equal to conditon
print(3 <=5) # True

# ATGC only has 4 characters in its string so it cannot be greater than 5
print(len("ATGC") > 5) # False

# There are two T's in this DNA seq
# 2 is greater than 1 so this is True
print("GAATTC".count("T") > 1) # True

# This DNA seq starts with ATG so this is True
print("ATGCTT".startswith("ATG")) # True

# This DNA seq ends with CTT not TTT so this comes back as false
print("ATGCTT".endswith("TTT")) # False

# The whole DNA seq are uppercase so this will come back true
print("ATGCTT".isupper()) # True

# The whole DNA seq are uppercase so using the islower method here would
# return false
print("ATGCTT".islower()) # False

# V is within the list so this will return True
print("V" in ["V", "W", "L"]) # True