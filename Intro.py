# Python is a high-level, interpreted programming language that is
# easy to learn and has a simple syntax. It is used for a variety
# of applications such as web development, data analysis, artificial intelligence, and more.

# simple Python program that prompts the user to enter
# their name and age, and then prints out a greeting:

name = input("What is your name? ")
age = input("How old are you? ")
print("Hello, " + name + "! You are " + age + " years old.")

# input() -> Takes input from the user and returns string
# print() -> Outputs to the console

# In Python, range() is a built-in function used to
# generate a sequence of numbers.
# It takes three arguments: start, stop, and step.

# generate a sequence of numbers from 0 to 9
for i in range(10):
    print(i)

# generate a sequence of even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)
