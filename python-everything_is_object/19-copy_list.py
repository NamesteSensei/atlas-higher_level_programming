#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)          # Prints the original list
print(new_list)         # Prints the copied list

print(new_list == my_list)  # True, because their contents are equal
print(new_list is my_list)  # False, because they are different objects
