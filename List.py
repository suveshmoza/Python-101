# A list is a collection of ordered, mutable
# and indexed elements enclosed in square brackets []

# append() -> adds an element to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# extend() -> adds elements from an iterable to the end of the list.
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)

# insert() -> inserts an element at a specific position in the list.
my_list = [1, 2, 3]
my_list.insert(1, 'hello')
print(my_list)  # Output: [1, 'hello', 2, 3]

# remove() -> removes the first occurrence of an element from the list.
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]

# pop() -> removes and returns the element at the specified position.
# If no position is specified, it removes and returns the last element.
my_list = [1, 2, 3]
popped_element = my_list.pop()
print(popped_element)  # Output: 3
print(my_list)  # Output: [1, 2]

# index() -> returns the index of the first occurrence of an element in the list.
my_list = [1, 2, 3, 2]
index_of_2 = my_list.index(2)
print(index_of_2)  # Output: 1

# count() -> returns the number of times an element appears in the list.
my_list = [1, 2, 3, 2]
count_of_2 = my_list.count(2)
print(count_of_2)  # Output: 2

# sort() -> sorts the list in ascending order.
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

# reverse() -> reverses the order of elements in the list.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

# copy() -> returns a shallow copy of the list.
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]

# clear() -> removes all elements from the list.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []

# len() -> returns the number of elements in the list.
my_list = [1, 2, 3]
length_of_list = len(my_list)
print(length_of_list)  # Output: 3


# slice a list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# slice the list from the 3rd to the 7th element (inclusive)
sliced_list = list[2:7]
print(sliced_list)

# slice the list from the beginning to the 4th element (exclusive)
sliced_list = list[:4]
print(sliced_list)

# slice the list from the 6th element to the end
sliced_list = list[5:]
print(sliced_list)

# slice the list in reverse order, taking every third element
sliced_list = list[::-3]
print(sliced_list)
