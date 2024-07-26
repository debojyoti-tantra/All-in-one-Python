# once we apply method on a list then original list is changed

l1 = [56, 34, 389, 39, 74, 0, 23]
l1.sort() # sort the list in assending order
print(l1)
# output: [0, 23, 34, 39, 56, 74, 389]

l2 = [56, 34, 389, 39, 74, 0, 23]
l2.sort(reverse=True) # sort the list in decending order
print(l2)
# output: [389, 74, 56, 39, 34, 23, 0]

l3 = [84, 39, 20, 3, 64, 73, 27]
l3.reverse()   # reverse the list
print(l3)
# output: [27, 73, 64, 3, 20, 39, 84]

l4 = ["harry", "petter", "rohan", "sraddha"]
l4.append("bulbul")   # insert the element at the last
print(l4)
# output: ['harry', 'petter', 'rohan', 'sraddha', 'bulbul']

l5 = ["mango", "apple", "orange", "banana"]
# if we wnat to insert any element by it's index number
l5.insert(2, "hee")   # 1st number denotes in which index the insert element is placed, 2nd thing denotes the elements which is insert
print(l5)
# output: ['mango', 'apple', 'hee', 'orange', 'banana']

l6 = [6, 5, 9, 4, 8, 0, 1, 3, 2, 7]
# if we want to remove an element by it's index number
print(l6.pop(2))   # output: 9   # returns removed element
print(l6)   # output: [6, 5, 4, 8, 0, 1, 3, 2, 7]

l7 = ["physics", "chemistry", "math"]
# if we wnat to remove an element by element's name
print(l7.remove("chemistry"))   # output: None
print(l7)   # output: ['physics', 'math']

my_list1 = [1, 2, 3]
my_list1.extend([4, 5])   # to extand the list
print(my_list1)  # Output: [1, 2, 3, 4, 5]

my_list2 = [1, 2, 3]
my_list2.clear()   # to clear the list
print(my_list2)  # Output: []

my_list3 = [1, 2, 3, 2]
index = my_list3.index(2)   # to find any index of an element
print(index)  # Output: 1

my_list4 = [1, 2, 3, 2]
count = my_list4.count(2)   # to determine how many time a element is present
print(count)  # Output: 2

my_list5 = [1, 2, 3]
new_list = my_list5.copy()
print(new_list)  # Output: [1, 2, 3]
