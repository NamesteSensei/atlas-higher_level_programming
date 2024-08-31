# Function to convert a string to uppercase
def uppercase(str):
    # Initialize an empty string to store the result
    result = ""

    # Loop through each character in the input string
    for char in str:
        # Check if the character is a lowercase letter
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert to uppercase by subtracting 32 from the ASCII value
            result += chr(ord(char) - 32)
        else:
            # If it's not lowercase, keep the character as is
            result += char
    
    # Print the result followed by a new line
    print("{}".format(result))
