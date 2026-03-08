#old way of formatting string in python
letter = "Hey my name is {} and I am from {}"
name = "Leena"
country = "Pakistan"
print(letter.format(name, country))

# string formatting using fstring
print(f"Hey my name is {name} and I am from {country}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

print(f"{2 * 30}")
print(type(f"{2 * 30}"))