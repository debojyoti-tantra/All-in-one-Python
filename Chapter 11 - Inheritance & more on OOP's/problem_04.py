# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c):
        return Complex(self.r + c.r, self.i + c.i)
    
    def __mul__(self, c):
        real_part = self.r * c.r - self.i * c.i
        imaginary_part = self.r * c.i + self.i * c.r
        return Complex(real_part, imaginary_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 + c2)
print(c1 * c2)