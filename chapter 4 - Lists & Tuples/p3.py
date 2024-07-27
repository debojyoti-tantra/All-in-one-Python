# Check that a tuple type cannot be changed in python.

a = (5, 6.67, "harry")

a[2] = "larry"

print(a)


# output:
# File "/storage/emulated/0/python/chapter 4 - Lists & Tuples/p3.py", line 5, in <module>
#     a[2] = "larry"
#     ~^^^
# TypeError: 'tuple' object does not support item assignment