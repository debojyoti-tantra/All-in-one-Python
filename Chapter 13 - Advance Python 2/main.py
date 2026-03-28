# import pandas as pd
# print(pd.__version__)

# lambda function
square = lambda x: x*x
print(square(9))

# join method
a = ["debo", "rohon", "motilal"]
final = ", ".join(a)
print(final)

# FORMAT METHOD (STRINGS)
a = "{} is a good {}".format("debojyoti", "boy")
b = "{0} is a good {1}".format("debojyoti", "boy")
c = "{1} is a good {0}".format("debojyoti", "boy")
print(a, b, c)

l = [1,2,3,4,5]
# MAP
square = lambda x: x*x
sqList = map(square, l)
print(list(sqList))

# FILTER
def even(n):
    if(n%2 == 0):
        return True
    return False
onlyEven = filter(even, l)
print(list(onlyEven))

# REDUCE
from functools import reduce
def summ(a, b):
    return a+b
mul = lambda x, y: x * y
print(reduce(summ, l))
print(reduce(mul, l))