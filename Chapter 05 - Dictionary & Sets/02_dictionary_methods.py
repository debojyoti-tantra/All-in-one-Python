games = {
#    "keys": "values"
     "rohon": "pubg",
     "ankit": "cod",
     "jasmin": "ludo",
     "khanzadi": "free-fire"
}

print(games.items())
# output: dict_items([('rohon', 'pubg'), ('ankit', 'cod'), ('jasmin', 'ludo'), ('khanzadi', 'free-fire')])

print(games.keys())
# output: dict_keys(['rohon', 'ankit', 'jasmin', 'khanzadi'])

print(games.values())
# output: dict_values(['pubg', 'cod', 'ludo', 'free-fire'])

games.update({"rohon": "null", "dekisugi": "books"})   # if same key is present then it's only update the values but if same key is not present then it add the new key and values
print(games)
# output: {'rohon': 'null', 'ankit': 'cod', 'jasmin': 'ludo', 'khanzadi': 'free-fire', 'dekisugi': 'books'}

print(games.get("ankit"))   # output: cod
print(games["ankit"])   # output: cod
# bot both are same then what is the difference (interview question)
# print(games.get("ankit2"))   # output: None
# print(games["ankit2"])   # returns a KeyError

my_dict = {
     'a': 1,
     'b': 2
}
value = my_dict.pop('a')   # remove a
print(value)  # Output: 1
print(my_dict)  # Output: {'b': 2}

my_dict = {
     'a': 1,
     'b': 2
}
item = my_dict.popitem()   # Removes and returns the last key-value
print(item)  # Output: ('b', 2)
print(my_dict)  # Output: {'a': 1}

my_dict = {'a': 1, 'b': 2}
my_dict.clear()
print(my_dict)  # Output: {}

my_dict = {'a': 1, 'b': 2}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2}

my_dict = {'a': 1, 'b': 2}
value = my_dict.setdefault('c', 3)  # returns the entered value and add the key-value pair
print(value)  # Output: 3
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}