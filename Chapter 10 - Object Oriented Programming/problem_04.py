# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square of {self.n} is {self.n * self.n}")
    
    def cube(self):
        print(f"The square of {self.n} is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The square of {self.n} is {self.n ** (1/2)}")
    
    @staticmethod
    def hellow():
        print("Your ans is here")

a = Calculator(4)
a.hellow()
a.square()
a.squareroot()
Calculator(4).cube()
# output:
# Your ans is here
# The square of 4 is 16
# The square of 4 is 2.0
# The square of 4 is 64