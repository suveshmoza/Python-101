# In Python, a set is an unordered collection of unique elements.
# It is defined using curly braces {} or using the built-in set() function

# Creating a set
fruits = {'apple', 'banana', 'cherry', 'durian'}

# Common methods used in set

# 1. add()
fruits.add('orange')
print(fruits)

# 2. clear()
fruits.clear()
print(fruits)

# 3. copy()
fruits = {'apple', 'banana', 'cherry', 'durian'}
new_fruits = fruits.copy()
print(new_fruits)

# 4. difference()
more_fruits = {'apple', 'banana', 'cherry', 'durian', 'elderberry'}
diff_fruits = more_fruits.difference(fruits)
print(diff_fruits)

# 5. difference_update()
more_fruits.difference_update(fruits)
print(more_fruits)

# 6. discard()
fruits.discard('durian')
print(fruits)

# 7. intersection()
other_fruits = {'banana', 'kiwi', 'orange'}
common_fruits = fruits.intersection(other_fruits)
print(common_fruits)

# 8. intersection_update()
fruits.intersection_update(other_fruits)
print(fruits)

# 9. isdisjoint()
veggies = {'carrot', 'celery', 'spinach'}
disjoint = fruits.isdisjoint(veggies)
print(disjoint)

# 10. issubset()
subset = {'banana', 'cherry'}
issub = subset.issubset(fruits)
print(issub)

# 11. issuperset()
superset = {'banana', 'cherry', 'orange', 'kiwi'}
issuper = superset.issuperset(fruits)
print(issuper)

# 12. symmetric_difference()
set1 = {'apple', 'banana', 'cherry'}
set2 = {'durian', 'elderberry'}
symm_diff = set1.symmetric_difference(set2)
print(symm_diff)
