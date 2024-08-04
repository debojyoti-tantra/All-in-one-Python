# ‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.

for i in range(0,11):
    if(i==6):
        continue  # Skip the iteration
    print(i)

# in output 6 is missing

'''
output:
[Running] python -u "/storage/emulated/0/python/chapter 07 – Loops In Python/06_continue_statement.py"
0
1
2
3
4
5
7
8
9
10

[Done] exited with code=0 in 0.377 seconds
'''