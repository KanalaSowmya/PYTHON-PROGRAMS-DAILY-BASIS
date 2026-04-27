'''QUESTION - 19'''

''' Write a Python program using the list [1, 2, 2, 3, 4, 4, 5]. Convert it into a set and print the unique values. Then add the value 6 to the set.'''

numbers = list(map(int, input().split()))
unique_numbers = set(numbers)
print("Unique values:", unique_numbers)
unique_numbers.add(6)
print("After adding 6:", unique_numbers)

