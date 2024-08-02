s = {1,5,6,9,12,8,"debo"}
print(s, type(s))
# output: {1, 5, 6, 8, 9, 'debo', 12} <class 'set'>

s.add("tantra")
print(s, type(s))
# output: {1, 5, 6, 'tantra', 8, 9, 12, 'debo'} <class 'set'>

# PROPERTIES OF SETS
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

print(s.remove(12))  # output: None
print(s)  #output: {1, 5, 6, 'debo', 8, 9, 'tantra'}

print(s.pop())  # remove a random element from set
# output: 1 (so 1 is remove)
print(s)  # output: {'tantra', 5, 6, 8, 9, 'debo'}

print(s.clear())  # output: None
print(s)  # output: set()

my_set = {1, 2, 3}
my_set.discard(2)  # Removes the element elem from the set if it is present. Does nothing if the element is not found.
print(my_set)  # Output: {1, 3}
my_set.discard(4)  # Does nothing

my_set = {1, 2, 3}
new_set = my_set.copy()
print(new_set)  # Output: {1, 2, 3}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}
