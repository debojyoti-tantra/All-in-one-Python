# pass is a null statement in python.
# It instructs to “do nothing”.

for i in range(11):
    pass

# if we now left this loop without complete it and work for new loop
# it show error
# if we use "pass" then it's not showing any error
# and we can work for next loop

i = 0
while(i<6):
    print(i)
    i+=1

'''
output:
[Running] python -u "/storage/emulated/0/python/chapter 07 – Loops In Python/07_pass_statement.py"
0
1
2
3
4
5

[Done] exited with code=0 in 0.31 seconds
'''