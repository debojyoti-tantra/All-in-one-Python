# Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the number: "))

i = 1
sum = 0

while (i<=n):
    sum = sum + i
    i = i + 1

print(f"The sum of first naturals numbers of {n} is {sum}")