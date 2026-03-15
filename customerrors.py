# we can raise custom errors by using raise keyword

a = int( input("Enter your marks between 80 and 90: "))

if(a<80 or a>90):
    raise ValueError("Value should be between 80 and 90")
else:
    print("Good Grades!")
        