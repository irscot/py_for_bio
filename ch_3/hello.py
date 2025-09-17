# creating a new file out.txt with the write(w) mode
file = open("out.txt", "w")

# Writing a greeting to the out.txt file
file.write("Hello World!")

# closing files in order to avoid bugs
file.close()



my_variable = "ATGCGGT"

my_file = open("overwriting_example.txt", "w")

# write "abcdef"
my_file.write("abc" + "def")

# write "8"
my_file.write(str(len('AGTGCTAG')))

# write "TTGC"
my_file.write("ATGC".replace('A', 'T'))

# write "atgc"
my_file.write("ATGC".lower())

# write contents of my_variable
my_file.write(my_variable)

# closing files in order to avoid bugs
my_file.close()

my_file = open("C:/Users/irsco/repos/py_for_bio/ch_3/out.txt")