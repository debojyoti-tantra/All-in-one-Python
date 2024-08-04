# Write a program using functions to find greatest of three numbers.

def gre(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>b and c>a):
        return c

print(gre(45, 67, 55))  # output: 67