#!/usr/bin/python3
copy_list = lambda lst: lst[:]
my_list = [1, 2, 3]; new_list = copy_list(my_list); print(my_list, new_list, new_list == my_list, new_list is my_list)
