# Write a python function which converts inches to cms.

# 1 inch = 2.54 cm
# 1 cm = 0.394 inch

def inch_to_cm(i):
    cm = 2.54*i
    return cm

i = int(input("Enter the lenght in inch: "))

print(f"{i} inch = {inch_to_cm(i)} cm")