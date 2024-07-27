# if you want to make string from existing string then,
# newString = oldString['starting of oldString to make newString' : 'final index of oldString to make newString (but final index not includes)']
# example newString = oldString[2 : 5]   newString is madeup by oldString index no 2 to 4

a = "debojyoti"

new_a1 = a[-9:-5] 
new_a2 = a[4:9] 
print(new_a1 , new_a2)   # output: debo  jyoti

# if new = old[ : ] written then it is mean 0 index to last(index - 1)
print(a[:])   # output: debojyoti

# skip value
# newString = oldString['starting of oldString to make newString' : 'final index of oldString to make newString (but final index not includes)' : 'after starting index skip string elements by this numbers']
print(a[0:9:2]) # skip by two
# output: dbjoi