def calculateGmean(a,b):
    mean = (a*b) / (a+b)
    print ("Geometeric mean for", a , "and" , b , "is",  mean)

def isGreater(a,b):
    if (a > b):
        print("First number(",a,") is greater.")
    else:  
        print("Second number(",b,") is greater.")  


f = 7
g = 8
calculateGmean(f,g)
isGreater(f,g)

u = 5
v = 6
calculateGmean(u,v)
isGreater(u,v)
