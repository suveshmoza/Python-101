# In Python, a string is a sequence of characters enclosed
# in either single quotes (') or double quotes (").
# Strings are immutable, which means their contents cannot be changed once they are created.

# Define a string
my_string = "Hello, World!"

# Get the length of the string
print(len(my_string))

# Convert the string to all lowercase
print(my_string.lower())

# Convert the string to all uppercase
print(my_string.upper())

# Remove leading and trailing whitespace
my_string_with_spaces = "  Hello, World!  "
print(my_string_with_spaces.strip())

# Replace a substring
print(my_string.replace("World", "Universe"))

# Split the string into a list of substrings
print(my_string.split(","))

# Join a list of strings into a single string
my_list = ["apple", "banana", "cherry"]
print("-".join(my_list))

# Slicing a string

string = "Hello, World!"

# slice the string from the 7th to the 12th character (inclusive)
sliced_string = string[7:13]
print(sliced_string)

# slice the string from the beginning to the 5th character (exclusive)
sliced_string = string[:5]
print(sliced_string)

# slice the string from the 7th character to the end
sliced_string = string[7:]
print(sliced_string)

# slice the string in reverse order, taking every second character
sliced_string = string[::-2]
print(sliced_string)
