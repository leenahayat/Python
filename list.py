list1 = [1,2,3,4,5,6]
list2 = ["Red", "Yellow", "Purple"]    

print(list1)
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])

if 5 in list1:
    print("Yes")
else:
    print("No")    

print(list2)
print(list2[0])
print(list2[1])
print(list2[2])

if "Yellow" in list2:
    print("Yes")
else:
    print("No") 


lst = [i*i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)