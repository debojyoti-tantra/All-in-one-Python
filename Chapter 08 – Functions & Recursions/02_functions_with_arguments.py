# A function can accept some value it can work with. We can put these values in the parentheses.

print("average of two numbers")
def mean(a, b):
    print((a+b)/2)

mean(78,68)
# output:
# average of two numbers
# 73.0


# if we want function returan a value
# A function can also return value
def summ(a, b):
    print(a + b)
    return "done"

p = summ(1,5)
print(p)
# output:
# 6
# done