# importing regular expression module
import re

dna = "AGCTGGTACTGTGGC"

# ALTERNATIONS AND CHARACTER GROUPS
# using re.search regular expression to find restriction sites
# using pipe bar (|) in case restriction site has either of the 
# two patterns: CTG or CGG in this dna string. 
if re.search(r"C(T|G)G", dna):
    print("restriction site found!")

# ? = makes something optional - match either 0 or 1 time
# ACT or ACTG will be looked for in the dna string
# if one or both are found then it do the action
if re.search(r"ACT(G)?", dna):
    print("restriction found!")

# QUANTIFIERS
# + = mathces one or more times
# Ex: the code will match AGCT with GGT and print found to console
# but if GGT was changed to GGC it would not due to GGC not being
# next to AGCT
# this will match AGC followed by one or more Ts, and then
# followed by GGT
if re.search(r"AGCT+GGT", dna):
    print("found!")

# * = matches 0 or more times making the character or group optional
# can also be repeated
# Ex: code will match AG, followed by 0 or more Ts and 
# then followed by 0 or more Cs
if re.search(r"AGT*C", dna):
    print("Found it!")

# specifying number of repeats with {}
# Ex: Pattern TA{1}C will match TAC 
# but not anything less or greater
# like TA(have no Cs) or TACC(have 2 Cs instead of one)
if re.search(r"TA{1}C", dna):
    print("found at least one C after TA!")

# practicing group method
k = re.search(r"TA{1}C", dna)
print("Found:", k.group()) # type: ignore

# you can also do a range 
# with this example: TA{1,3}C you can have either 1,2,or 3 Cs leading
# after TA; so it can match TAC, TACC, or TACCC
if re.search(r"TA{1,3}C", dna):
    print("found at least one C after TA!")

# practicing group method
l = re.search(r"TA{1,3}C", dna)
print("Found:", l.group()) # type: ignore

# POSITIONS
# ^ = matches the start of the string
# $ = matches the end of the string
# in the example below it will not print the message
# due to the dna string not starting with T and/or ending with C
if re.search(r"^TAC$", dna):
    print("dna starts with a thyamine and/or ends with a cytosine!")


dna_two = "ATGACGTACGTACGACTG"

# store the match object in the variable m
m = re.search(r"GA[ATGC]{3}AC", dna_two)

# calling group() method shows us the macthed part of the DNA sequence
print(m.group()) # type: ignore

# USING CAPTURING 

dna_three = "ATGACGTACGTACGACTG"
# store the match object in the variable n

# searching for GA with 3 bases ([ATGC]{3}) -> captured
# followed by AC followed by 2 bases ([ATGC]{2}) -> captured
# followed by AC
n = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna_three)

# printing out the entire match
print("entire match: " + n.group()) # type: ignore

# printing out the first captured bit
# in other words, only printing what comes after GA that is in parenthesis
print("first bit: " + n.group(1)) # type: ignore

# printing out the second captured bit
# in other words, printing only what comes after the 3 bases that is in parenthesis
print("second bit: " + n.group(2)) # type: ignore

# POSTION MATCHING
dna_four = "ATGACGTACGTACGACTG"
o = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna_four)

# using start() method to print out the index position of where the search begins within dna
# C is the starting part of the search which is index 2
print("start: " + str(o.start())) # type: ignore

# using end() method to print out the index positon of where the search ends with dna
# C is the end part of the search which is index 13
print("end: " + str(o.end())) # type: ignore

# CONNECTION: it is like slicing it starts at the index you are searching for
# and ends with the index right after the one you want to look for
# Ex: the second GT are indexed at 9 and 10 so you would want the index 11 (A)
# to be the stopping point to get GT to print
print(dna[9:11])

# SPLITTING A STRING
# using split method to only read As Ts Gs and Cs in dna
dna_five = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
# using [^ATGC] as are starting point in the dna string
# to start splitting any character that isn't a A, T, G or C
runs = re.split(r"[^ATGC]", dna_five)
print(runs)

# FINDING MULTIPLE MATCHES
# finading all patterns that have a range of 4 to 100 As and Ts in the dna
# with findall method
dna_six = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.findall(r"[AT]{4,100}", dna_six)
print(runs)

# using a for loop with finditer method 
# to return the sequence of matching parts found in the dna
runs_two = re.finditer(r"[AT]{3,100}", dna_six)
for match in runs_two:
    run_start = match.start()
    run_end = match.end()
    print("AT rich region from " + str(run_start) + " to " + str(run_end))
