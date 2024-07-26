everything = ["orange", "apple", 5.67, 6, "rohan"]
print(everything)   # output: ['orange', 'apple', 5.67, 6, 'rohan']
print(everything[0])   # output: orange

everything[0] = "green"
print(everything)   # output: ['green', 'apple', 5.67, 6, 'rohan']
print(everything[0])   # output: green
# unlike strings, lists are mutable


# LIST INDEXING
# list indexing is same as string
print(everything[1:4:2])   # output: ['apple', 6]
