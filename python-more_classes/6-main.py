#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

# Create two Rectangle instances
my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)

# Print the number of instances after creation
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

# Delete the first rectangle and check the number of instances
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

# Delete the second rectangle and check the number of instances
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
