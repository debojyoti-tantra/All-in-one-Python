f = open("04_readline().txt")

lines = f.readlines()

print(lines, type(lines))

f.close()

# output: ["It's frist line\n", "It's second line\n", "It's third line"] <class 'list'>

f = open("04_readline().txt")

line1 = f.readline()
print(line1)
# output: It's frist line

line2 = f.readline()
print(line2)
# output: It's second line

line3 = f.readline()
print(line3)
# output: It's third line

line4 = f.readline()
print(line4)
# output: {Empty String}

f.close()

# By While Loop

f = open("04_readline().txt")

line = f.readline()
while(line!=""):
    print(line)
    line = f.readline()

f.close()
'''
output:
It's frist line

It's second line

It's third line
'''