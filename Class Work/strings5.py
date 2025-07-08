# -----------------------------------------
# Basic String Operations
# -----------------------------------------

# 1. Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World

# 2. Repetition
print("Python! " * 3)  # Output: Python! Python! Python!

# 3. Indexing
text = "Python"
print(text[0])    # Output: P (1st character)
print(text[-1])   # Output: n (last character)

# 4. Slicing
print(text[0:3])  # Output: Pyt (from index 0 to 2)
print(text[:4])   # Output: Pyth (default start is 0)
print(text[2:])   # Output: thon (from index 2 to end)

# 5. Membership
print('Pyt' in text)       # Output: True
print('Java' not in text)  # Output: True

# -----------------------------------------
# Built-in String Functions
# -----------------------------------------

text = "Hello World"

# 1. len()
print(len(text))  # Output: 11

# 2. max() and min()
print(max("abcXYZ"))  # Output: 'c' (highest ASCII)
print(min("abcXYZ"))  # Output: 'X' (lowest ASCII)

# 3. sorted()
print(sorted("python"))  # Output: ['h', 'n', 'o', 'p', 't', 'y']

# 4. chr() and ord()
print(ord('A'))   # Output: 65
print(chr(97))    # Output: 'a'

# -----------------------------------------
# String Methods - Case Conversion
# -----------------------------------------

print("hello".upper())         # HELLO
print("HELLO".lower())         # hello
print("python".capitalize())   # Python
print("hello world".title())   # Hello World
print("PyThOn".swapcase())     # pYtHoN
print("ß".casefold())          # ss

# -----------------------------------------
# Alignment & Formatting Methods
# -----------------------------------------

print("python".center(10, "*"))                     # *python**
print("py".ljust(5, "-"))                           # py---
print("py".rjust(5, "-"))                           # ---py
print("42".zfill(5))                                # 00042
print("Name: {}, Age: {}".format("Tom", 25))        # Name: Tom, Age: 25
print("{name} is {age}".format_map({'name': 'Tom', 'age': 25}))  # Tom is 25

# -----------------------------------------
# Search & Find Methods
# -----------------------------------------

print("hello".find("l"))       # 2
print("hello".rfind("l"))      # 3
print("hello".index("e"))      # 1
print("hello".rindex("l"))     # 3
print("banana".count("a"))     # 3

# -----------------------------------------
# String Testing Methods (Boolean)
# -----------------------------------------

print("python".startswith("py"))   # True
print("python".endswith("on"))     # True
print("Hello".isalpha())           # True
print("abc123".isalnum())          # True
print("hello".islower())           # True
print("HELLO".isupper())           # True
print(" ".isspace())               # True
print("Hello World".istitle())     # True
print("my_var".isidentifier())     # True
