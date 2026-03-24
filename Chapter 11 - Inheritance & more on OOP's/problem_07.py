# Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, lenght):
        self.lenght = lenght

    def __len__(self):
        return len(self.lenght)        
    
v1 = Vector([1, 2, 3])
print(len(v1))