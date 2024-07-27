name = "debojyoti"

print(len(name))   # output: 9
print(name.endswith("ti"))   # output: True
print(name.startswith("De"))   # output: False
print(name.capitalize())   # output: Debojyoti
print(name.count("e"))   # output: 1
print(name.find("eb"))   # output: 1
print(name.replace("jyoti","lina"))   # output: debolina

a = "Harry is a Good Boy"
print(a.replace("Good","Bad"))   # output: Harry is a Bad Boy

print(a.upper())   # output: HARRY IS A GOOD BOY
print(a.lower())   # output: harry is a good boy
print(a.title())   # captalized every words first latter   # output: harry Is A Good Boy
print(a.strip())   # cuts extra space
print(a.split())   # makes every words in a string   # output: ['Harry', 'is', 'a', 'Good', 'Boy']

list = ["COD", "PUBG", "BattleGround"]
print(" vs ".join(list))   # join many strings into a single string   # output: COD vs PUBG vs BattleGround

# also use usenumeric , islower , isupper