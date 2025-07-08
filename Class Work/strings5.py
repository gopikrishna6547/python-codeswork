# -----------------------------------------
# String Operations Demo
# -----------------------------------------

# 1. Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(" Concatenation:", result)

# 2. Repetition
print(" Repetition:", "Python! " * 3)

# 3. Indexing
text = "Python"
print(" Indexing [0]:", text[0])
print(" Indexing [-1]:", text[-1])

# 4. Slicing
print(" Slicing [0:3]:", text[0:3])
print(" Slicing [:4]:", text[:4])
print(" Slicing [2:]:", text[2:])

# 5. Membership
print(" Membership 'Pyt' in text:", 'Pyt' in text)
print(" Membership 'Java' not in text:", 'Java' not in text)

# -----------------------------------------
# Built-in String Functions
# -----------------------------------------

sample = "Hello World"

print(" len():", len(sample))
print(" max():", max("abcXYZ"))  # Based on ASCII
print(" min():", min("abcXYZ"))
print(" sorted():", sorted("python"))

# chr() and ord()
print(" ord('A'):", ord('A'))
print(" chr(97):", chr(97))

# -----------------------------------------
# String Methods
# -----------------------------------------

# Case Conversion
print(" upper():", "hello".upper())
print(" lower():", "HELLO".lower())
print(" capitalize():", "python".capitalize())
print(" title():", "hello world".title())
print(" swapcase():", "PyThOn".swapcase())
print(" casefold():", "ß".casefold())

# Alignment & Formatting
print(" center():", "python".center(10, "*"))
print(" ljust():", "py".ljust(5, "-"))
print(" rjust():", "py".rjust(5, "-"))
print(" zfill():", "42".zfill(5))
print(" format():", "Name: {}, Age: {}".format("Tom", 25))
print(" format_map():", "{name} is {age}".format_map({'name': 'Tom', 'age': 25}))

# Search & Find Methods
print(" find():", "hello".find("l"))
print(" rfind():", "hello".rfind("l"))
print(" index():", "hello".index("e"))
print(" rindex():", "hello".rindex("l"))
print(" count():", "banana".count("a"))

# String Testing (Boolean)
print(" startswith():", "python".startswith("py"))
print(" endswith():", "python".endswith("on"))
print(" isalpha():", "Hello".isalpha())
print(" isalnum():", "abc123".isalnum())
print(" islower():", "hello".islower())
print(" isupper():", "HELLO".isupper())
print(" isspace():", " ".isspace())
print(" istitle():", "Hello World".istitle())
print(" isidentifier():", "my_var".isidentifier())
