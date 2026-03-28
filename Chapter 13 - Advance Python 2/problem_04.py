# Write a program to filter a list of numbers which are divisible by 5.

def divisibleByFive(n):
    if(n%5 == 0):
        return True
    return False

a = [32,54,7,1,35,980,432,65,57]
f = list(filter(divisibleByFive, a))

print(f)