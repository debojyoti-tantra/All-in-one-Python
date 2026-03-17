# Create a class with a class attribute a; create an object from it and set ‘a’ directly using object.a = 0. Does this change the class attribute?

class Demo:
    a = 4

o = Demo()
print(o.a)
o.a = 0
print(o.a)
print(Demo.a)
# otuput:
# 4
# 0
# 4

# so class attribute does not change but a instance attribute set