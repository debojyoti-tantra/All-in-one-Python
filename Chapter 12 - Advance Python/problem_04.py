# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(f"The value of a/b is: {a/b}")
except ZeroDivisionError as v:
    print("Infinite")
