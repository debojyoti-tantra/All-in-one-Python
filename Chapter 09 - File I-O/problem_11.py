# Write a python program to rename a file to “renamed_by_ python.txt.

import os

with open("11.txt") as f:
    content = f.read()

with open("problem_11.txt", "w") as f:
    f.write(content)

os.remove("11.txt")