#!/usr/bin/env python3
import random
number = random.randint(-10, 10)

# Check if the number is positive, zero, or negative
if number > 0:
    print(f"{number} is positive")  # Positive number case
elif number == 0:
    print(f"{number} is zero")      # Zero case
else:
    print(f"{number} is negative")  # Negative number case

