# Open the file in write mode
file = open("example.txt", "w")

# Write some text to the file
file.write("This is an example text.")

# Close the file
file.close()

# Open the file in read mode
file = open("example.txt", "r")

# Read the contents of the file
content = file.read()

# Print the content
print(content)

# Close the file
file.close()
