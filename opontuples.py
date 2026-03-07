# tuples are immutable, if we want to add,remove or edit tuples then we first convert tuple to list then perform operations on that ist and convert it back to tuple

countries = ("Spain", "Italy", "India", "England","Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)                           #add item
temp[2] = "Finland"                   #remove item
countries = tuple(temp)               #change item
print(countries)

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
res = tuple1.index(3)
# res = tuple1.index(311)
res = tuple1.index(3, 4, 8)
print(tuple1)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)
