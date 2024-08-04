# In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed otherwise not!
# If the loop is entered, the process of [condition check & execution] is continued until the condition becomes False.

i = 1

while(i<=5):
    print(i)
    i += 1
'''
OUTPUT:

[Running] python -u "/storage/emulated/0/python/chapter 07 – Loops In Python/02_while_loops.py"
1
2
3
4
5

[Done] exited with code=0 in 0.261 seconds
'''

# Write a program to print 1 to 50 using a while loop.
i = 1

while (i<51):
    print(i)
    i = i + 1


# Write a program to print the content of a list using while loops.
l = ["Debo", "Rohon", "Sizuka", 23, "Dr. Jhatka"]
i = 0

while(i<len(l)):
    print(l[i])
    i = i+1
