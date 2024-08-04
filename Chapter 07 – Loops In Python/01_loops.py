# Sometimes we want to repeat a set of statements in our program. For instance: Print 1 to 1000.
# Loops make it easy for a programmer to tell the computer which set of instructions to repeat and how!

for i in range(1,11):
    print(i)
'''
output:
[Running] python -u "/storage/emulated/0/python/chapter 07 – Loops In Python/01_loops.py"
1
2
3
4
5
6
7
8
9
10

[Done] exited with code=0 in 0.377 seconds
'''

# range(x, y): means
# initial value x or start with x
# finanal value y-1 or ends with y-1

# if range (x, y, p): means
# initial value x or start with x
# finanal value y-1 or ends with y-1
# and p means go initial to final with jump p or p = step size

# range(y): === range(0, y, 0):

# Primarily there are two types of loops in python.
# • while loops
# • for loops
