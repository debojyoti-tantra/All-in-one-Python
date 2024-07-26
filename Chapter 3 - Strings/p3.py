# Write a program to detect double space in a string.

a = "Sraddha is a good girl"
print(a.find("  "))
# output: -1

b = "Harry is a  good boy"
print(b.find("  "))
# output: 10

# conclusion:
# if string has not a singal diuble space then output will be -1
# if string has a singal diuble space then output will not equals to -1
