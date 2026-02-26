str = "Ali is a good boy"
print(str.upper())

str1 = "Avoid bad things"
print(str1.lower())

str2 = "Leena!!!!!!"
print(str2.rstrip("!"))

str3 = "Leena"
print(str3.replace("Leena","Sarmad"))

str4 = "Python makes coding simple and fun."
print(str4.split())

str5= "pYtHoN is FuN"
print(str5.capitalize())

str6 = "center python"
print(str6.center(30))

str7 = "Python is fun and Python is powerful."
print(str7.count("Python"))

text = "Hello, world!"
print(text.endswith("world!")) # True
print(text.endswith("World"))  # False (case-sensitive)

sentence = "The quick brown fox jumps over the lazy dog."
position = sentence.find("fox")
print(f"'fox' was found at index: {position}") 

s1 = "Python123"
s2 = "Python 3"
s3 = "@Monica!"
s4 = ""
print(s1.isalnum()) # Output: True
print(s2.isalnum()) # Output: False (contains a space)
print(s3.isalnum()) # Output: False (contains '@' and '!')
print(s4.isalnum()) # Output: False (empty string)



str1 = "HelloWorld"
str2 = "Hello World"
str3 = "Hello123"
str4 = ""
print(f"'{str1}'.isalpha(): {str1.isalpha()}")
print(f"'{str2}'.isalpha(): {str2.isalpha()}")
print(f"'{str3}'.isalpha(): {str3.isalpha()}")
print(f"'{str4}'.isalpha(): {str4.isalpha()}")


