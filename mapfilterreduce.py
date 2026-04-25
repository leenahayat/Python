#MAP
def cube(x):
    return x*x*x

l= [1, 2, 5, 8, 9, 44]
newl = list(map((cube), l))
print(newl)


#FILTER
def filter_function(a):
    return a>4

newnewl = list(filter(filter_function,l))
print(newnewl)


#REDUCE
from functools import reduce
numbers = [1, 2 , 3, 4, 5]
#calculate the sum of the numbers using reduce function
sum = reduce(lambda x,y: x+y , numbers)
print(sum)