# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter any no: "))

table = [n*i for i in range(1,11)]
print(table)
with open("./Chapter 12 - Advance Python/table.txt", "a") as f:
    f.write(f"Table of {n} is:" + "\n" + str(table) + "\n")