# Write a program to find out whether a file is identical & matches the content of another file.

# i use previous problems files to do this problem

with open("problem_08.txt") as f:
    content1 = f.read()
with open("problem_08_copy.txt") as f:
    content2 = f.read()
if (content1 == content2):
    print("These files are identical")
else:
    print("These files are not identical")
# output: These files are identical


# try this with another files
with open("problem_04.txt") as f:
    content1 = f.read()
with open("problem_05.txt") as f:
    content2 = f.read()
if (content1 == content2):
    print("These files are identical")
else:
    print("These files are not identical")
# output: These files are not identical