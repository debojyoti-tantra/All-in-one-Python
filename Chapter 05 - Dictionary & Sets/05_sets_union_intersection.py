s1 = {1, 5, 20, 4, 67}
s2 = {67, 1, 65, 9, 0}

print(s1.union(s2))  # output: {0, 1, 65, 67, 4, 5, 9, 20}
print(s1.intersection(s2))  # output: {1, 67}

print(s1-s2)  # output: {20, 4, 5}
print(s2-s1)  # output: {0, 65, 9}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1)  # Output: {2, 3}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.difference(set2)
print(set3)  # Output: {1}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1)  # Output: {1}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.symmetric_difference(set2)
print(set3)  # Output: {1, 4}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.symmetric_difference(set2)
print(set3)  # Output: {1, 4}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 4}

set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True
# Run true if set1 is a subset of set2

set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True
# Run true if set1 is superset of other

set1 = {1, 2}
set2 = {3, 4}
print(set1.isdisjoint(set2))  # Output: True
# Returns True if the set1 has no elements in common with set2
