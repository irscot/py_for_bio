apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
chimp_index = apes.index("Pan troglodytes")
# chimp_index is now 1

print(apes.index("Pan troglodytes"))
print(chimp_index)
print(apes)

apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
apes.append("Pan paniscus")
print(apes)

apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
monkeys = ["Papio ursinus", "Macaca mulatta"]
primates = apes + monkeys
print(str(len(apes)) + " apes")
print(str(len(monkeys)) + " monkeys")
print(str(len(primates)) + " primates")

for ape in apes:
    print(f"{ape} is an ape.")
    name_length = len(ape) - 1
    first_letter = ape[0]
    print(ape + " is an ape. Its name starts with " + first_letter)
    print("Its name has " + str(name_length) + " letters")