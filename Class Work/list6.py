# Creating Lists

my_list = []
my_list2 = list()

numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [10, "Python", 3.14, True]

nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]

list_from_tuple = list((1, 2, 3))
string_to_list = list("Python")
print(string_to_list)  # ['P', 'y', 't', 'h', 'o', 'n']

# Accessing Elements in a List

my_list = ["Python", "Java", "C++"]
print(my_list[0])   # Python
print(my_list[1])   # Java
print(my_list[-1])  # C++

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])       # [20, 30, 40]
print(numbers[:3])        # [10, 20, 30]
print(numbers[2:])        # [30, 40, 50]
print(numbers[-3:-1])     # [30, 40]
print(numbers[::-1])      # [50, 40, 30, 20, 10]

# Modifying Lists

numbers = [10, 20, 30, 40]
numbers[2] = 100
print(numbers)  # [10, 20, 100, 40]

numbers.append(50)
numbers.insert(1, 15)
numbers.extend([60, 70, 80])
print(numbers)  # [10, 15, 20, 100, 40, 50, 60, 70, 80]

numbers.remove(100)
numbers.pop(2)
numbers.pop()
del numbers[1]
numbers.clear()
print(numbers)  # []

# List Methods

numbers = [3, 1, 4, 1, 5, 9]
print(numbers.count(1))   # 2
print(numbers.index(4))   # 2
numbers.sort()
print(numbers)            # [1, 1, 3, 4, 5, 9]
numbers.reverse()
print(numbers)            # [9, 5, 4, 3, 1, 1]

# Looping Through a List

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Copying a List

list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)

# Sorting and Reversing

numbers = [5, 3, 8, 2]
numbers.sort()
print(numbers)  # [2, 3, 5, 8]
numbers.sort(reverse=True)
print(numbers)  # [8, 5, 3, 2]
numbers.reverse()
print(numbers)  # [2, 3, 5, 8]

# More List Methods Examples

lst = [10, 20, 30, 10, 40, 50]
lst.append(60)
lst.extend([70, 80])
lst.insert(2, 25)
lst.remove(10)
lst.pop()
lst.clear()
lst = [3, 1, 4, 1, 5, 9]
print(lst.index(4))
print(lst.count(1))
lst.sort()
print(lst)
lst.reverse()
print(lst)
copy_lst = lst.copy()
print(copy_lst)
print(sorted(lst))
print(max(lst))
print(min(lst))
print(sum(lst))
print(len(lst))
print(any([0, False, 1]))
print(all([1, 2, 3]))
