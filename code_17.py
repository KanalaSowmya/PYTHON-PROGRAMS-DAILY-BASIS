''' QUESTION - 17'''

'''Write a Python program using the list [10, 20, 30, 40, 50]. Perform the following: print the first element, print the last element, add 60 to the list, and remove 30 from the list.'''

numbers = list(map(int, input().split()))
print("First element:", numbers[0])

print("Last element:", numbers[-1])

# Add 60 to the list
numbers.append(60)
print("After adding 60:", numbers)

# Remove 30 from the list
numbers.remove(30)
print("After removing 30:", numbers)