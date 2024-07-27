# properties:
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.

marks = {
     "harry": 100,
     "rohan": 75,
     "nobita": 26,
     "list": [100, 75, 26]
}

print(marks)  # output: {'harry': 100, 'rohan': 75, 'nobita': 26, 'list': [100, 75, 26]}
print(type(marks))  # output: <class 'dict'>
print(marks["harry"])  # output: 100
print(marks["list"])  # output: [100, 75, 26]

c = {} # called empty dictionary
