#!/usr/bin/python3

# Loop through ASCII values for lowercase letters 'a' to 'z'
for i in range(97, 123):
    # Skip the letters 'e' (ASCII 101) and 'q' (ASCII 113)
    if i != 101 and i != 113:
        # Print the character corresponding to the current ASCII value without a newline
        print("{}".format(chr(i)), end="")
