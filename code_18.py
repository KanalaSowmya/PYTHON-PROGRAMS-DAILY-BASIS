'''QUESTION - 18'''

'''Write a Python program using the tuple (100, 200, 300, 400). Print the second element and count how many elements are present. Try modifying one value and observe the behavior.'''

numbers = tuple(map(int, input().split()))
print("Second element:", numbers[1])

# Count total elements
print(len(numbers))

# Try modifying a value
numbers[1] = 250   # This will cause an error
