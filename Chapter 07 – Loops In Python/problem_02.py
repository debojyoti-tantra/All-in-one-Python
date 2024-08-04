# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Debo", "Soham", "Sachin", "Rahul"]

l = ["Debo", "Soham", "Sachin", "Rahul"]

for name in l:
    if (name.startswith("S")):
        print(f"Hellow {name}")
'''
output:
Hellow Soham
Hellow Sachin
'''