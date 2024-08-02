# Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter The Number 1: "))
b = int(input("Enter The Number 2: "))
c = int(input("Enter The Number 3: "))
d = int(input("Enter The Number 4: "))

if (a>b and a>c and a>d):
    print("Greatest number is Number 1:",a)
elif (b>a and b>c and b>d):
    print("Greatest number is Number 2:",b)
elif (c>b and c>a and c>d):
    print("Greatest number is Number 3:",c)
elif (d>b and d>c and d>a):
    print("Greatest number is Number 4:",d)
else:
    print("Two greatest numbers are same")
