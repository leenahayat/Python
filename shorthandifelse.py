#short hand if-else statement

a = 330000
b = 3303
print("A") if a > b else print("=") if a == b else print("B")


#same program using if-else
if a > b:
    print("A")
else:
    if a == b:
        print("=")
    else:
        print("B") 

#same program using elif
if a > b:
    print("A")
elif a == b:
    print("=")
else:
    print("B")

   
c = 9 if a>b else 0
print(c)