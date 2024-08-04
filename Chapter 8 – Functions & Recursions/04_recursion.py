# Recursion is a function which calls itself.
# It is used to directly use a mathematical formula as function. 
# Example:
# factorial(n) = n x factorial (n-1)

def fact (n):
    if (n==0 or n==1):
        return 1
    elif (n<0):
        return "not possible"
    return n * fact(n-1)

n = int(input("Enter the number: "))
print("Fcatorial of this number is", fact(n))