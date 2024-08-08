# Write a recursive function to calculate the sum of first n natural numbers.

def summ(n):
    if(n<0):
        return "not possible"
    elif(n == 0):
        return 0
    return n+summ(n-1)

n = int(input("Enter the number: "))

print(f"The sum of first natural numbers of {n} is {summ(n)}")