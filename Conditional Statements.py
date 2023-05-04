# Conditional statements in Python allow the program to execute different code
# depending on whether a condition is true or false. There are two types of
# conditional statements in Python: if statements and if-else statements.

age = 25

# Example of if
if age >= 18:
    print("You are an adult")

# Example of if-else
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

# Example of if-elif-else
if age < 18:
    print("You are not an adult")
elif age >= 18 and age < 30:
    print("You are a young adult")
elif age >= 30 and age < 60:
    print("You are a middle-aged adult")
else:
    print("You are a senior adult")
