#!/usr/bin/python3

# Loop through ASCII values for lowercase letters 'a' to 'z'
for i in range(97, 123):
    # Check if the current character is not 'e' (ASCII 101) and not 'q' (ASCII 113)
    if chr(i) not in "eq":
        # Print the character corresponding to the current ASCII value without a newline
        print("{}".format(chr(i)), end="")

