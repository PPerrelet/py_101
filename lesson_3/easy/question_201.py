# Write two distinct ways of reversing the list without mutating the original list.
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

reversed_list = list(reversed(numbers))
reversed_list_v2 = numbers[::-1]

print(numbers)
print(reversed_list)
print(reversed_list_v2)