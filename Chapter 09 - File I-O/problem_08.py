# Write a program to make a copy of a text file “this. txt”

with open("problem_08.txt") as f:
    content = f.read()

with open("problem_08_copy.txt", "w") as f:
    f.write(content)