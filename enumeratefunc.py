marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1


#same program using enumerate function
for index, mark in enumerate(marks, start=1):
  print(index , ":", mark)
  if(index == 3):
    print("Harry, awesome!")


fruits = ['apple', 'orange', 'mango']
for index, fruit in enumerate(fruits):
  print(f'{index+1}: {fruit}')