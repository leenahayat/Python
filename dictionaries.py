#dictionary

'''
1. Dictionary are using key value pairs to store values
2. They are made by using s1={ "key": "value", "key": "value" } syntax
3. you can get all keys of dictionary by s1. keys( )
4. you can get all values of dictionary by using s1.values( )
5. you can get all pairs of dictionary by s1.items( )
6. you can get the value of an item by u1. Dictionary are using key value pairs to store values
using s1['key'] and it will return the value. s1.get( "key") will also return the value but it wont
throw an error in case there is no value/key available in the dictionary
'''

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 
print(info['name'])
print(info['age'])

##for accessing multiple keys,items & values
print(info.keys())
print(info.values())
print(info.items())

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")

for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 