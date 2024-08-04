# A function is a group of statements performing a specific task.

# When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!

# A function can be reused by the programmer in a given program any number of

# Function Defination : The part containing the exact set of instructions which are executed during the function call.
def avg():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))
    av = (a+b+c)/3
    print(f"Average of {a}, {b} and {c} is {av}")

# Function Call : Whenever we want to call a function, we put the name of the function followed by parentheses as follows:
avg()
avg()
avg()

# Quick Quiz: Write a program to greet a user with “Good day” using functions.
name = input("Enter your name: ")

def goodDay():
    print("Good Day", name)

goodDay()


# TYPES OF FUNCTIONS IN PYTHON:
# There are two types of functions in python:
# • Built in functions (Already present in python)
# • User defined functions (Defined by the user)
# Examples of built in functions includes len(), print(), range() etc.
# The avg() & goodDay() function we defined is an example of user defined function.
