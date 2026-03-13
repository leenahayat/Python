#order doesnot matter in sets


s = {2,3,5,7,8}
s2 = {4,5,7}
print(s.union(s2))   #used for finding union of 2 sets

s.update(s2)
print(s, s2)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x.intersection(y))      #used for finding union of 2 sets


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.symmetric_difference(B))     #used to get the elements present in either of the two sets, but not common to both sets.


