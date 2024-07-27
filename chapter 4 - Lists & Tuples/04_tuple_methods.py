my_tuple1 = (1, 2, 3, 2, 2)
count = my_tuple1.count(2)  # to count the element of tupple
print(count)  # Output: 3

my_tuple2 = (1, 2, 3, 2, 2)
index = my_tuple2.index(3)  # find the index of an element
print(index)  # Output: 2

my_tuple3 = (1, 2, 3)
length = len(my_tuple3)  # to find length of tuple
print(length)  # Output: 3

my_tuple4 = (1, 2, 3)
maximum = max(my_tuple4)  # maximum number of tupple
print(maximum)  # Output: 3

my_tuple5 = (1, 2, 3)
minimum = min(my_tuple5)
print(minimum)  # Output: 1

my_tuple6 = (1, 2, 3)
total = sum(my_tuple6)
print(total)  # Output: 6

my_tuple7 = (3, 1, 2)
sorted_list = sorted(my_tuple7)
print(sorted_list)  # Output: [1, 2, 3]  # return a list

# convert list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)