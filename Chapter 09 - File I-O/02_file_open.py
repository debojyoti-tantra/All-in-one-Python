f = open("02_file_open.txt")  # or open("02_file_open.txt", "r") because default it's "r"

data = f.read()

print(data)

f.close()

# output: It's amazing you know