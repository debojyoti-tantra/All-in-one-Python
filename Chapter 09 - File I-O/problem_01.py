# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

f = open("problem_01.txt")

content =  f.read()
if ("twinkle" in content):
    print("The word twinkel is present in the txt file")
else:
    print("The word twinkel is not present in the txt file")

f.close()

# output: The word twinkel is present in the txt file