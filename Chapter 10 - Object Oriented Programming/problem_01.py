# Create a Class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address

debojyoti = Programmer("Debojyoti Tantra", 1200000, "Jalpaiguri")
print(debojyoti.name, debojyoti.company, debojyoti.salary, debojyoti.address)