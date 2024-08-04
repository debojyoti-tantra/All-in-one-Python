# We can have a value as default as default argument in a function.

def hey(name, ending="Thank you"):
    print(f"Good Morning, {name}")
    print(ending)

hey("Debojyoti")  # if ending is not present then use default ending
# output:
# Good Morning, Debojyoti
# Thank you

hey("Sizuka", "Thanks")
# output:
# Good Morning, Sizuka
# Thanks