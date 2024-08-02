# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

comment = input("Write your comment: ")

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

if ((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("This is a spam comment")
else:
    print("This is not a spam comment")
