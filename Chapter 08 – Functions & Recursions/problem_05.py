# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def tara(n):
    if (n==0):
        return
    print("*"*n)
    tara(n-1)

n = int(input("Enter the number: "))

tara(n)