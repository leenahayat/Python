'''
Importing in Python is the process of loading code from a 
Python module into the current script. This allows you to use
the functions and variables defined in the module in your current script, 
as well as any additional modules that the imported module may depend on.

To import a module in Python, you use the import statement
followed by the name of the module. For example, to import 
the math module, which contains a variety of mathematical 
functions, you would use the following statement:
import math

from keyword
You can also import specific functions or variables from a 
module using the from keyword. 

importing everything
It's also possible to import all functions and variables from 
a module using the * wildcard. However, this is generally not 
recommended as it can lead to confusion and make it harder to 
understand where specific functions and variables are coming from.
from math import *

The dir function
Finally, Python has a built-in function called dir that you can
use to view the names of all the functions and variables defined
in a module. This can be helpful for exploring and understanding 
the contents of a new module.
'''


# from math import sqrt, pi
# from math import pi, sqrt as s

import math
result = math.sqrt(64) * math.pi
print(result)         #Output = 25.1327


import math as m
result = m.sqrt(9) * m.pi
print(result)         #Output = 9.424

print(dir(math))
print(math.nan , type(math.nan))

import Rb as r                #we can also import one file in another file, Rb is a file
r.welcome()
print(r.Rb)      