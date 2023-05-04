# In Python, a tuple is an ordered, immutable collection of elements.
# Once a tuple is created, its contents cannot be modified.
# Tuples are defined by enclosing a comma-separated sequence of elements in parentheses.

my_tuple = (1, "hello", True)

# Accessing tuple elements
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

# Packing and unpacking
my_tuple = ("Suvesh", "Moza", 21)
first_name, last_name, age = my_tuple
print(first_name)
print(last_name)
print(age)

# Returning multiple values from function


def get_name_and_age():
    name = "John"
    age = 25
    return name, age


name, age = get_name_and_age()
print(name)
print(age)

# Since tuples are immutable,
# they can be used as keys in a dictionary

my_dict = {("John", "Doe"): 25, ("Jane", "Doe"): 30}
print(my_dict[("John", "Doe")])  # prints 25

# As elements in a list
my_list = [(1, 2), ("hello", "world")]
print(my_list[0])  # prints (1, 2)
