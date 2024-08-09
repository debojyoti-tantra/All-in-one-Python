# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

with open("problem_04.txt") as f:
    content = f.read()

new_content = content.replace("Donkey", "######")

with open("problem_04.txt", "w") as f:
    f.write(new_content)
