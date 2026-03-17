class Empoyee:
    companey = "TFC"  # This is a class attribute
    lang = "python"
    salary = "120000"

debo = Empoyee()
debo.name = "Debojyoti Tantra"  # This is a class attribute or instance attribute
print(debo.name, debo.companey, debo.lang, debo.salary)

rohon = Empoyee()
rohon.name = "Rohon Das"
print(rohon.name, rohon.companey, rohon.lang, rohon.salary)

# here name is object is object attribute and salary and language are class attributes as they directly belong to class

# instance vs class: Instance attributes, takes peference over class attributes during assignment & retrieval
class Companey:
    lang = "Java"
    salary = "200000"

comp = Companey()
comp.name = "TCS"
comp.lang = "Java Script"

print(comp.name, comp.lang, comp.salary)
# output language is must be "Java Script"

# Self Parameter
class Companey2:
    lang = "Java"
    salary = "200000"

    def getInfo(self):
        print(f"The language is {self.lang}. The salary is {self.salary}")
    
    @staticmethod  # to mark we don't need object
    def greed():
        print("Good Morning")

comp2 = Companey2()
comp2.name = "TCS"
comp2.lang = "Java Script"
comp2.getInfo()  # is equivalent to Companey2.getInfo(comp2)
comp2.greed()
# print(comp2.name, comp2.lang, comp2.salary)

# Constractor
class Student:
    studied = "6th sem"
    deperement = "physics"

    def __init__(self):
        print("I am creating a object")  # special method(dunder method) which is automatically called

    def __init__(self, name, studied, deperement):
        self.name = name
        self.deperement = deperement
        self.studied = studied
debo1 = Student("debo", "6th sem", "physics")
# debo1.name = "debo"
print(debo1.name, debo1.studied, debo1.deperement)
# output:
# I am creating a object
# debo 6th sem physics
ayushi = Student("Ayushi", "3rd sem", "chemistry")
print(ayushi.name, ayushi.studied, ayushi.deperement)