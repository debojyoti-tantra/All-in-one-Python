# Write a program to print third, fifth and seventh element from a list using enumerate function.

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

for i, item in enumerate(l):
    if (i == 2 or i == 4 or i == 6):
        print(item)