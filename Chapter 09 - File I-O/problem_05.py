# Repeat program 4 for a list of such words to be censored.

words = ["Buy this", "I Love You", "Tap to see", "You won money"]

with open("problem_05.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("problem_05.txt", "w") as f:
    f.write(content)