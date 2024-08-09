# Write a program to mine a log file and find out whether it contains ‘python’.

with open("problem_06.txt") as f:
    content = f.read()

if ("python" in content):
    print("The word python is present in this txt file")
else:
    print("The word python is not present in this txt file")

# output: The word python is present in this txt file