# A function is a block of organized and reusable code that
# performs a specific task. It takes input, processes it and returns output.


# Function without parameters
def greet():
    print("Hello, world!")


greet()

# Function with single parameter


def greet(name):
    print("Hello, " + name + ". How are you doing?")


greet("John")

# Function with parameters


def add_numbers(num1, num2):
    result = num1 + num2
    return result


sum = add_numbers(10, 20)
print(sum)

# Function with default parameter value


def greet(name="world"):
    print("Hello, " + name + "!")


greet()
greet("John")

# Function with variable-length arguments


def print_args(*args):
    for arg in args:
        print(arg)


print_args("apple", "banana", "cherry")

# Recursive function


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
