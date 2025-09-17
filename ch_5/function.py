# making a function to get at content of dna from a string

# passing dna as an argument to the function
# the argument dna only exists when it runs
# NOTE: any variable apart of function only exist in the 
# scope of the function and can't be accessed outside of function
# arguments can be default or be assigned and treated like a variable
# only thing is a nondefault (dna="ATGC") can't follow a default argument(sig_figs)
def get_at_content(dna, sig_figs=2):
    length = len(dna)
    # combing upper() and count() methods to catch instances
    # of lowercase dna being placed in the string
    # also acts as a safeguard due to user input
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = ((a_count + t_count) / length) * 100

    # returning AT content that is calculated in the function
    # and output it to be used outside of the function
    # using round() to round up to the nearest 2 sig figs of at_content
    return round(at_content, sig_figs)

# calling function by passing a string of dna sequence inside
# the function name as an argument

# using at_content to print the functions content to terminal

test_dna = "ATGCATGCAACTGTAGC"
print(f"{get_at_content(test_dna, 1)}%")
print(f"{get_at_content(test_dna, 2)}%")