#5. Replace & Modify Methods

print(text1.replace("h","i"))

print(text1.translate(str.maketrans("e","@")))

print(text1.maketrans("hello","@&%*"))


#6. Splitting & Joining Methods

print(text1.split(" "))#Splits the string into a list by sep

print(text1.rsplit(" "))# Splits from the right side.


print(text1.splitlines(" "))#Splits at line breaks ( ).


result=' '.join(text1)# Joins elements with a separator.
print(result)

text2="hello-world"#Splits into a 3-part tuple at first sep.
print(text2.partition("-"))

print(text2.rpartition("-"))# Splits into a3-part tuple at last sep.

#7. Whitespace & Trimming Methods

print("  hello ".strip()) #Removes leading and trailing characters (default: spaces).

print("----hello".lstrip("-"))#Removes leading characters.

print("hello----".rstrip("-")) #Removes trailing characters.