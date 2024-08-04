for i in range(5):
    print(i)
'''
[Running] python -u "/storage/emulated/0/python/chapter 07 – Loops In Python/03_for_loops.py"
0
1
2
3
4

[Done] exited with code=0 in 0.4 seconds
'''

# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

# for loops iterate

# for loops with list
l = ["Doremon", "Nobita", "Sizuka", "Suniyo", "Dekisugi"]
for i in range(len(l)):
    print(l[i])

# for loops with Tuples
t = (1, 3, 6, 9, 8)
for i in range(len(t)):
    print(t[i])

# For Loop with Strings
s = "Debo"
for i in s:
    print(i)
