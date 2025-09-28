"""
Write a program which creates nine new folders – one for sequences between 100
and 199 bases long, one for sequences between 200 and 299 bases long, etc. Write
out each DNA sequence in the input files to a separate file in the appropriate folder.
"""
import os

# need a for loop and maybe an if conditional

for file in os.listdir("."):
    if file.endswith(".dna"):
        print(f"reading sequences from {file}")
        