import random

n = random.randint(1, 100)
num = -1

guses = 0
while(num != n):
    num = int(input("Guess a number: "))

    if (num > n):
        print("Guess Lower number please")
        guses += 1

    if (num < n):
        print("Guess Higher number please")
        guses += 1

print(f"You are correctly guess the number {num} in {guses} attempts.")