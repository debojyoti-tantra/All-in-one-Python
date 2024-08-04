# Write a python program using function to convert Fahrenheit to Celsius.

# c/5 = (f-32)/9
# c = 5 X (f-32)/9

def f_to_c(f):
    c = 5 * (f-32)/9
    return c

f = int(input("Enter the temprature in Fahrenheit: "))

c_round = round(f_to_c(f), 2)

print(f"{f}°F = {c_round}°C")