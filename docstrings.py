# Python docstrings are the string literals that appear right after the definition of a function,method,class ,or module
#doctstrings are written right below the name of function
def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)      

# doctstrings are not ingnored like comments we can print docstrings by using __doc__

