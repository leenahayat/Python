# tuples are immutable, if we want to add,remove or edit tuples then we first convert tuple to list then perform operations on that ist and convert it back to tuple

countries = ("Spain", "Italy", "India", "England","Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)                           #add item
temp[2] = "Finland"                   #remove item
countries = tuple(temp)               #change item
print(countries)