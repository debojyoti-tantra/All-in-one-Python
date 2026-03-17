# Write a class “calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square of {self.n} is {self.n * self.n}")
    
    def cube(self):
        print(f"The square of {self.n} is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The square of {self.n} is {self.n ** (1/2)}")

a = Calculator(4)
a.square()
a.squareroot()
Calculator(4).cube()
# output:
# The square of 4 is 16
# The square of 4 is 2.0
# The square of 4 is 64