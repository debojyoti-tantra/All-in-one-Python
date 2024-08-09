# Write a program to find out the line number where python is present from ques 6.

with open("problem_07.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"The word pyhton is present in this file.\nLine No: {lineno}")
        break
    lineno += 1

else:
    print(f"The word pyhton is not present in this file.")
'''
output:
The word pyhton is present in this file.
Line No: 15
'''