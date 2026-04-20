x = 10    #Global Variable
print(x)   

def func():
    global x
    x = 5       #local variable
    y = 5

func()
print(x)   #5 because of global x
print(y)   #through an error bcz y is a local variable and is not accessible outta function 

