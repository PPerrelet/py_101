# Programmatically determine whether 42 lies between 10 and 100, inclusive. Do the same for the values 100 and 101.

number = 42
print(10 <= number <= 100)  
number = 100
print(10 <= number <= 100) 

number = 101
print(10 <= number <= 100)  


42 in range(10, 101)          # True
100 in range(10, 101)         # True
101 in range(10, 101)         # False