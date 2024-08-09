# The best way to open and close the file automatically is the with statement.

with open("06_with_statement.txt") as f:
    print(f.read())
'''
output:
wow,
you donn't have to close the file by;
'''