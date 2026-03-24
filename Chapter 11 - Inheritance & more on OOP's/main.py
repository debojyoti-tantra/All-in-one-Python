class Employee:  # base class
    companey = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Programmer:
    companey = "ITC Info Tech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")

a = Employee()
b = Programmer()
print(a.companey, b.companey)

# here we can use inheritance
class Programmer(Employee):  # derived class: allattributes in class Employee goes to class Programmer
    companey = "ITC-2"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")

a = Employee()
b = Programmer()
print(a.companey, b.companey)

# multiple inheritance: like class Programmer(Employee, {any class here}):

class aa:
    a = 1
    def __init__(self):
        print("constractor aa")
class bb(aa):
    b = 2
    def __init__(self):
        print("constractor bb")
class cc(bb):
    c = 3
    def __init__(self):
        super().__init__()
        print("constractor cc")
o = cc()
print(o.a, o.b, o.c)

# class attribute
class Tan:
    a = 1

    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")
    
tan = Tan()
tan.a = 5
tan.show()

# property decorators
class Tan2:
    b = 1

    @classmethod
    def show2(cls):
        print(f"the value of a is {cls.b}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Tan2()
e.b = 2

e.name = "Debojyoti Tantra"
print(e.name)

e.show2()

# operator overloading
class Number:
    def __init__(self, n):
        self.n = n
    
    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)
print(n+m)

# p1+p2 # p1.__add__(p2)
# p1-p2 # p1.__sub__(p2)
# p1*p2 # p1.__mul__(p2)
# p1/p2 # p1.__truediv__(p2)
# p1//p2 # p1.__floordiv__(p2