# Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter the number: "))
fact = 1

for i in range(1,n+1):
    fact = fact*i

print(f"The factorial of {n} is {fact}")