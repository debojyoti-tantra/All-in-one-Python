# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)


# TYPES DEFINITIONS IN PYTHON
n : int = 5
name: str = "Debojyoti"
def summ(a:int, b:int) -> int:
    return a+b


# Advance types
from typing import List, Tuple, Dict, Union
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid


# MATCH CASE
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
# Usage
print(http_status(200)) # Output: OK
print(http_status(404)) # Output: Not Found
print(http_status(500)) # Output: Internal Server Error
print(http_status(403)) # Output: Unknown status


# DICTIONARY MERGE & UPDATE OPERATORS
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}


# EXCEPTION HANDLING IN PYTHON
try:
    a = int(input("Enter any number: "))
    print(a)
except Exception as e:
    print(e)
print("Thank You!!")


# RAISING EXCEPTIONS
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
if (b == 0):
    raise ZeroDivisionError("Our programe is not ment to divide numbers by zero.5")
else:
    print(f"The value of a/b is: {a/b}")


# try:
#     # Somecode
# except:
#     # Somecode
# else:
#     # Code # This is executed only if the try was successful


# enumerate
l = [2,3,4,5,6,8]
index = 0
for item in l:
    print(f"The item no {index} is {item}")
    index += 1
# this can be simplyfied by enumerate function
for index, item in enumerate(l):
    print(f"The item no {index} is {item}")


# LIST COMPREHENSIONS
myList = [1, 2, 9, 5, 3, 5]
squareList = []
for item in myList:
    squareList.append(item * item)
print(squareList)
# using list comprehensions
squareList = [i*i for i in myList]
print(squareList)