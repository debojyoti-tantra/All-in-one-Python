# Write a python function to remove a given word from a list add strip it at the same time.

# first we try to remove only the word
def rem(l, word):
    for item in l:
        l.remove(word)
        return l

l = ["Debo", "Rohan", "Subham", "an"]

print(rem(l, "an"))   # output: ['Debo', 'Rohan', 'Subham']

# now we want to add strip
def rem(l, word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l = ["Debo", "Rohan", "Subham", "an"]

print(rem(l, "an"))   # output: ['Debo', 'Roh', 'Subham']