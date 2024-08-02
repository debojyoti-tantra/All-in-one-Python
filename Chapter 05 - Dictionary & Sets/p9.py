# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}

print(s)
# output:
'''
[Running] python -u "/storage/emulated/0/python/chapter 05 - Dictionary & Sets/p9.py"
Traceback (most recent call last):
  File "/storage/emulated/0/python/chapter 05 - Dictionary & Sets/p9.py", line 4, in <module>
    s = {8, 7, 12, "Harry", [1,2]}
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
'''
# we cann't put list inside a set
# if it's possible then also we cann't change values of sets by indexing