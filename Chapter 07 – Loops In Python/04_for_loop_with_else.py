# An optional else can be used with a for loop if the code is to be executed when the loops exhausts.

l = [1,3,6,7,0]

for item in l:
    print(item)
else:
    print("done")  # this is printed when loop is exhausts!
'''
output:
[Running] python -u "/storage/emulated/0/python/chapter 07 – Loops In Python/04_for_loop_with_else.py"
1
3
6
7
0
done

[Done] exited with code=0 in 0.471 seconds
'''