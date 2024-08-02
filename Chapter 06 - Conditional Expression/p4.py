# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your UserName: ")

if (len(username)>10):
    print("Username has more then 10 characters")
elif (len(username==10)):
    print("username has 10 characters")
else:
    print("Username has less then 10 characters")
