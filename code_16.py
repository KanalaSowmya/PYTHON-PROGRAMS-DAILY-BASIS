''' QUESTION - 16 '''

''' Write a Python program that asks the user to enter an initial value. Then ask how many times Operation A (add 20) and Operation B (multiply by 2) should be applied. Perform the operations and display the final value(s).'''

initial_value = float(input())
a_times = int(input())
b_times = int(input())

# Case 1: Add first, then multiply
result1 = (initial_value + a_times) *  b_times

# Case 2: Multiply first, then add
result2 = (initial_value * b_times) + a_times

print("Add then Multiply:", result1)
print("Multiply then Add:", result2)