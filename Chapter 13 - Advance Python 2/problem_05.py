# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

l = [32,54,7,1,35,980,432,65,57]

def greater(a, b):
    if(a > b):
        return a
    return b

greatestNo = reduce(greater, l)
print(greatestNo)