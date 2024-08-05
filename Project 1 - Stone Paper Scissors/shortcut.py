import random
'''
stone = 1
paper = 2
scissor = 3
'''
print("Press 'st' for Stone")
print("Press 'p' for Paper")
print("Press 'sc' for Scissor")
print(" * "*10)

computer = random.choice([1, 2, 3])

your_numb = input("Enter your choice: ")
your_dict = {
    "st": 1,
    "p": 2,
    "sc": 3
}
reverse_dict = {
    1: "Stone",
    2: "Paper",
    3: "Scissor"
}
you = your_dict[your_numb]

print(f"You chose: {reverse_dict[you]}\nComputer chose: {reverse_dict[computer]}")

if (computer==you):
    print("Match is Draw")
# else: 
#     if (computer==1 and you==2): 2-1=1 win
#         print("You Win!")
#     elif (computer==1 and you==3): 3-1=2 lose
#         print("You Lose!")
#     elif (computer==2 and you==3): 3-2=1 win
#         print("You Win!")
#     elif (computer==2 and you==1): 1-2=-1 lose
#         print("You Lose!")
#     elif (computer==3 and you==1): 1-3=-2 win
#         print("You Win!")
#     elif (computer==3 and you==2): 2-3=-1 lose
#         print("You Lose!")
#     else:
#         print("Something went Wrong!!")
#  if you - computer = 1 or -2 then I win!!
#  if you - computer = 2 or -1 then I lose!!

else:
    if (you-computer==1 or you-computer==-2):
        print("You Win!")
    elif (you-computer==2 or you-computer==-1):
        print("You Lose!")
    else:
        print("Something went Wrong!!")