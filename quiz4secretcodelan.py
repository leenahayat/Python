
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string
start = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(3))
end = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(3))


a = input("Do you want to coding or decoding: ")
if a== 'coding':
    c = input("Enter the message you want to encode: ")
    if len(c) < 3:
        print(c[::-1])
    else:
        new_word = c[1:] + c[0]
        result = start + new_word + end
        print(result)
elif a =='decoding': 
    z = input("Enter the message you want to decode: ")
    if len(z) < 3:
        print(z[::-1]) 
    else:
       word = z[3:-3]
       decoded = word[-1] + word[:-1]
       print(decoded)






    

