# Creating a dictionary
my_dict = {"apple": 2, "banana": 3, "cherry": 5}

# Accessing a value using a key
print(my_dict["banana"])

# Adding a new key-value pair
my_dict["durian"] = 7
print(my_dict)

# Updating a value using a key
my_dict["banana"] = 4
print(my_dict)

# Removing a key-value pair using del
del my_dict["cherry"]
print(my_dict)

# Removing a key-value pair using pop()
value = my_dict.pop("banana")
print(my_dict)
print(value)

# Clearing the dictionary
my_dict.clear()
print(my_dict)

# Creating a dictionary from a list of keys and values
keys = ["apple", "banana", "cherry"]
values = [2, 3, 5]
my_dict = dict(zip(keys, values))
print(my_dict)

# Getting the keys of a dictionary
keys = my_dict.keys()
print(keys)

# Getting the values of a dictionary
values = my_dict.values()
print(values)

# Getting the key-value pairs of a dictionary as tuples
items = my_dict.items()
print(items)

# Checking if a key is in the dictionary
if "banana" in my_dict:
    print("Yes")

# Merging two dictionaries
dict1 = {"apple": 2, "banana": 3}
dict2 = {"cherry": 5, "durian": 7}
dict1.update(dict2)
print(dict1)

# Copying a dictionary
new_dict = my_dict.copy()
print(new_dict)
