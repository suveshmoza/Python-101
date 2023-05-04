# In Python, a module is a file that contains Python definitions and statements.
# It allows you to logically organize your Python code and make it reusable.

# There are several ways to import modules

# 1. Importing the entire module
# import module_name

# 2. Importing specific functions or variables from a module
# from module_name import function_name, variable_name

# 3. Importing the entire module with an alias
# import module_name as alias_name

# 4. Importing specific functions or variables from a module with an alias
# from module_name import function_name as alias_name, variable_name as alias_name

# 5. Importing all functions and variables from a module
# from module_name import *


from mathModule import add, subtract

x = 10
y = 5

# Use the add() function from the math_module
result = add(x, y)
print(f"{x} + {y} = {result}")

# Use the subtract() function from the math_module
result = subtract(x, y)
print(f"{x} - {y} = {result}")
