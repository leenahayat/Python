#positional arguments
def add(a, b):
    print(a + b)
add(5, 10) 


#Keyword Arguments
def student_info(age, name):
    print(f"Name: {name}, Age: {age}")
student_info(age=20, name="Leena")


#Default Arguments
def greet(name, greeting="Hello"): 
    print(f"{greeting}, {name}!")
greet("Alice") 
greet("Bob", "Hi") 

