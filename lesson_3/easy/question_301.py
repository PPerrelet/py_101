# Write two different ways to remove all of the elements from the following list:
numbers = [1, 2, 3, 4]
numbers2 = [1, 2, 3, 4]

print(numbers)

del numbers[:]

print(numbers)
print(numbers2)

numbers2.clear()

print(numbers2)